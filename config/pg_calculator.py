"""Utility functions for calculating Pflegegrad scores."""
from typing import Dict

from config.pflegegrad_config import pflegegrad_thresholds
from config.child_development_data import child_development_data

# Mapping tables copied from app.py
weighted_score_mapping_tables = {
    1: [(0, 0), (2, 2.5), (4, 5), (6, 7.5), (10, 10)],
    2: [(0, 0), (2, 3.75), (6, 7.5), (11, 11.25), (17, 15)],
    3: [(0, 0), (1, 3.75), (3, 7.5), (5, 11.25), (7, 15)],
    4: [(0, 0), (3, 10), (8, 20), (19, 30), (37, 40)],
    5: [(0, 0), (1, 5), (2, 10), (4, 15), (6, 20)],
    6: [(0, 0), (1, 3.75), (4, 7.5), (7, 11.25), (12, 15)],
}


def map_raw_to_weighted_score(module_id: int, raw_score: float) -> float:
    """Convert raw module points to weighted points using the official tables."""
    mapping = weighted_score_mapping_tables.get(module_id, [])
    weighted = 0.0
    for limit, value in mapping:
        if raw_score >= limit:
            weighted = value
        else:
            break
    return float(weighted)


def total_weighted_score(raw_scores: Dict[int, float]) -> float:
    """Calculate the overall weighted score from raw scores."""
    m1 = map_raw_to_weighted_score(1, raw_scores.get(1, 0))
    m2 = map_raw_to_weighted_score(2, raw_scores.get(2, 0))
    m3 = map_raw_to_weighted_score(3, raw_scores.get(3, 0))
    m4 = map_raw_to_weighted_score(4, raw_scores.get(4, 0))
    m5 = map_raw_to_weighted_score(5, raw_scores.get(5, 0))
    m6 = map_raw_to_weighted_score(6, raw_scores.get(6, 0))

    score = m1
    score += max(m2, m3)
    score += m4 + m5 + m6
    return score


def determine_pflegerad(total_score: float) -> int:
    """Return the Pflegegrad based on the configured thresholds."""
    grad = 0
    for level, cfg in sorted(
        pflegegrad_thresholds.items(), key=lambda x: x[1]["min_points"]
    ):
        if total_score >= cfg["min_points"]:
            grad = level
        else:
            break
    return grad


def calculate_pflegerad(raw_scores: Dict[int, float]) -> Dict[str, float | int]:
    """Convenience helper returning score and grade."""
    score = total_weighted_score(raw_scores)
    grade = determine_pflegerad(score)
    return {
        "total_score": round(score, 2),
        "pflegegrad": grade,
    }


def calculate_and_determine_pflegegrad(
    answers: Dict[str, int],
) -> Dict[str, float | int]:
    """Calculate the total score and determine the Pflegegrad from answers."""
    raw_scores: Dict[int, float] = {}
    for question_id, score in answers.items():
        module_id = int(question_id.split(".")[0])
        raw_scores.setdefault(module_id, 0)
        raw_scores[module_id] += score

    return calculate_pflegerad(raw_scores)


def calculate_child_pflegerad(
    answers: Dict[str, int],
    age_months: int,
) -> Dict[str, float | int]:
    """Calculate the total score and determine the Pflegegrad for a child."""
    raw_scores: Dict[int, float] = {}
    for question_id, score in answers.items():
        module_id_str, _ = question_id.split(".")
        module_id = int(module_id_str)

        raw_scores.setdefault(module_id, 0)

        expected_score = 0
        if (
            f"module_{module_id}" in child_development_data
            and question_id in child_development_data[f"module_{module_id}"]
        ):
            for min_age, max_age, expected in child_development_data[
                f"module_{module_id}"
            ][question_id]:
                if min_age <= age_months < max_age:
                    expected_score = expected
                    break

        raw_scores[module_id] += max(0, score - expected_score)

    return calculate_pflegerad(raw_scores)