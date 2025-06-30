# config/child_development_data.py

# Age-appropriate independence levels for children in months
# Structure: {module_id: {question_id: [(min_months, max_months, "independence_level"), ...]}}

CHILD_DEVELOPMENT_DATA = {
    1: { # Module 1: Mobilität
        "1.1": [ # Positionswechsel im Bett
            (0, 1, "unselbständig"),
            (1, 3, "überwiegend unselbständig"),
            (3, 9, "überwiegend selbständig"),
            (9, 216, "selbständig"), # Up to 18 years (216 months)
        ],
        "1.2": [ # Halten einer stabilen Sitzposition
            (0, 6, "unselbständig"),
            (6, 8, "überwiegend unselbständig"),
            (8, 9, "überwiegend selbständig"),
            (9, 216, "selbständig"),
        ],
        "1.3": [ # Umsetzen
            (0, 8, "unselbständig"),
            (8, 9, "überwiegend unselbständig"),
            (9, 11, "überwiegend selbständig"),
            (11, 216, "selbständig"),
        ],
        "1.4": [ # Fortbewegen innerhalb des Wohnbereichs
            (0, 12, "unselbständig"),
            (12, 13, "überwiegend unselbständig"),
            (13, 18, "überwiegend selbständig"),
            (18, 216, "selbständig"),
        ],
        "1.5": [ # Treppensteigen
            (0, 15, "unselbständig"),
            (15, 18, "überwiegend unselbständig"),
            (18, 30, "überwiegend selbständig"), # 2 years and 6 months = 30 months
            (30, 216, "selbständig"),
        ],
        # KF 4.1.B is age-independent, so it's not in this data structure.
    },
    2: { # Module 2: Kognitive und kommunikative Fähigkeiten
        "2.1": [ # Erkennen von Personen aus dem näheren Umfeld
            (0, 1.5, "nicht vorhanden"), # 6 weeks = 1.5 months
            (1.5, 9, "in geringem Maße vorhanden"),
            (9, 15, "größtenteils vorhanden"),
            (15, 216, "vorhanden/unbeeinträchtigt"),
        ],
        "2.2": [ # Örtliche Orientierung
            (0, 13, "nicht vorhanden"),
            (13, 18, "in geringem Maße vorhanden"),
            (18, 72, "größtenteils vorhanden"), # 6 years = 72 months
            (72, 216, "vorhanden/unbeeinträchtigt"),
        ],
        "2.3": [ # Zeitliche Orientierung
            (0, 30, "nicht erforderlich"), # Under 2 years and 6 months = 30 months
            (30, 60, "in geringem Maße vorhanden"), # 2 years 6 months to under 5 years
            (60, 84, "größtenteils vorhanden"), # 5 years to under 7 years
            (84, 216, "vorhanden/unbeeinträchtigt"), # From 7 years
        ],
        "2.4": [ # Erinnern an wesentliche Ereignisse oder Beobachtungen
            (0, 9, "nicht vorhanden"),
            (9, 36, "in geringem Maße vorhanden"), # 9 months to under 3 years
            (36, 66, "größtenteils vorhanden"), # 3 years to under 5 years 6 months
            (66, 216, "vorhanden/unbeeinträchtigt"), # From 5 years 6 months
        ],
        "2.5": [ # Steuern von mehrschrittigen Alltagshandlungen
            (0, 5, "nicht vorhanden"),
            (5, 12, "in geringem Maße vorhanden"),
            (12, 15, "größtenteils vorhanden"),
            (15, 216, "vorhanden/unbeeinträchtigt"),
        ],
        "2.6": [ # Treffen von Entscheidungen im Alltag
            (0, 18, "nicht vorhanden"),
            (18, 30, "in geringem Maße vorhanden"), # 18 months to under 2 years 6 months
            (30, 54, "größtenteils vorhanden"), # 2 years 6 months to under 4 years 6 months
            (54, 216, "vorhanden/unbeeinträchtigt"), # From 4 years 6 months
        ],
        "2.7": [ # Verstehen von Sachverhalten und Informationen
            (0, 48, "nicht erforderlich"), # Under 4 years
            (48, 60, "in geringem Maße vorhanden"), # 4 years to under 5 years
            (60, 72, "größtenteils vorhanden"), # 5 years to under 6 years
            (72, 216, "vorhanden/unbeeinträchtigt"), # From 6 years
        ],
        "2.8": [ # Erkennen von Risiken und Gefahren
            (0, 30, "nicht erforderlich"), # Under 2 years and 6 months
            (30, 78, "in geringem Maße vorhanden"), # 2 years 6 months to under 6 years 6 months
            (78, 120, "größtenteils vorhanden"), # 6 years 6 months to under 10 years
            (120, 216, "vorhanden/unbeeinträchtigt"), # From 10 years
        ],
        "2.9": [ # Mitteilen von elementaren Bedürfnissen
            (0, 3, "nicht vorhanden"),
            (3, 13, "in geringem Maße vorhanden"),
            (13, 48, "größtenteils vorhanden"), # 13 months to under 4 years
            (48, 216, "vorhanden/unbeeinträchtigt"), # From 4 years
        ],
        "2.10": [ # Verstehen von Aufforderungen
            (0, 16, "nicht vorhanden"),
            (16, 18, "in geringem Maße vorhanden"),
            (18, 30, "größtenteils vorhanden"), # 18 months to under 2 years 6 months
            (30, 216, "vorhanden/unbeeinträchtigt"), # From 2 years 6 months
        ],
        "2.11": [ # Beteiligen an einem Gespräch
            (0, 15, "nicht vorhanden"),
            (15, 24, "in geringem Maße vorhanden"), # 15 months to under 2 years
            (24, 48, "größtenteils vorhanden"), # 2 years to under 4 years
            (48, 216, "vorhanden/unbeeinträchtigt"), # From 4 years
        ],
    },
    4: { # Module 4: Selbstversorgung
        "4.1": [ # Waschen des vorderen Oberkörpers
            (0, 24, "nicht erforderlich"), # Under 2 years
            (24, 216, "selbständig"), # Default to self-sufficient for older children
        ],
        "4.2": [ # Körperpflege im Bereich des Kopfes
            (0, 216, "selbständig"), # No age-specific guidance, assume self-sufficient for older children
        ],
        "4.3": [ # Waschen des Intimbereichs
            (0, 24, "nicht erforderlich"), # Under 2 years
            (24, 216, "selbständig"),
        ],
        "4.4": [ # Duschen und Baden einschließlich Waschen der Haare
            (0, 42, "nicht erforderlich"), # Under 3 years 6 months = 42 months
            (42, 216, "selbständig"),
        ],
        "4.5": [ # An- und Auskleiden des Oberkörpers
            (0, 216, "selbständig"), # No age-specific guidance
        ],
        "4.6": [ # An- und Auskleiden des Unterkörpers
            (0, 216, "selbständig"), # No age-specific guidance
        ],
        "4.7": [ # Mundgerechtes Zubereiten der Nahrung und Eingießen von Getränken
            (0, 24, "nicht erforderlich"), # Under 2 years
            (24, 216, "selbständig"),
        ],
        "4.8": [ # Essen (KF 4.4.8) - Special case, triple weighting
            (0, 216, "selbständig"), # No age-specific guidance for baseline
        ],
        "4.9": [ # Trinken
            (0, 216, "selbständig"), # No age-specific guidance
        ],
        "4.10": [ # Benutzen einer Toilette oder eines Toilettenstuhls (KF 4.4.10) - Special case, double weighting
            (0, 216, "selbständig"), # No age-specific guidance for baseline
        ],
        "4.11": [ # Bewältigen der Folgen einer Harninkontinenz und Umgang mit Dauerkatheter und Urostoma
            (0, 60, "nicht erforderlich"), # Under 5 years = 60 months
            (60, 216, "selbständig"),
        ],
        "4.12": [ # Bewältigen der Folgen einer Stuhlinkontinenz und Umgang mit Stoma
            (0, 60, "nicht erforderlich"), # Under 5 years
            (60, 216, "selbständig"),
        ],
        "4.13": [ # Ernährung parenteral oder über Sonde
            (0, 216, "selbständig"), # No age-specific guidance
        ],
        # KF 4.4.0 is a special case for 0-18 months, not a general age-dependent question.
    },
    6: { # Module 6: Gestaltung des Alltagslebens und sozialer Kontakte
        "6.1": [ # Gestaltung des Tagesablaufs und Anpassung an Veränderungen
            (0, 30, "nicht erforderlich"), # Under 2 years 6 months
            (30, 60, "überwiegend unselbständig"), # 2 years 6 months to under 5 years
            (60, 84, "überwiegend selbständig"), # 5 years to under 7 years
            (84, 216, "selbständig"), # From 7 years
        ],
        "6.2": [ # Ruhen und Schlafen
            (0, 6, "unselbständig"),
            (6, 60, "überwiegend unselbständig"), # 6 months to under 5 years
            (60, 132, "überwiegend selbständig"), # 5 years to under 11 years
            (132, 216, "selbständig"), # From 11 years
        ],
        "6.3": [ # Sichbeschäftigen
            (0, 6, "unselbständig"),
            (6, 36, "überwiegend unselbständig"), # 6 months to under 3 years
            (36, 60, "überwiegend selbständig"), # 3 years to under 5 years
            (60, 216, "selbständig"), # From 5 years
        ],
        "6.4": [ # Vornehmen von in die Zukunft gerichteten Planungen
            (0, 30, "nicht erforderlich"), # Under 2 years 6 months
            (30, 36, "überwiegend unselbständig"), # 2 years 6 months to under 3 years
            (36, 60, "überwiegend selbständig"), # 3 years to under 5 years
            (60, 216, "selbständig"), # From 5 years
        ],
        "6.5": [ # Interaktion mit Personen im direkten Kontakt
            (0, 1.5, "unselbständig"), # Under 6 weeks
            (1.5, 9, "überwiegend unselbständig"), # 6 weeks to under 9 months
            (9, 12, "überwiegend selbständig"), # 9 months to under 12 months
            (12, 216, "selbständig"), # From 12 months
        ],
        "6.6": [ # Kontaktpflege zu Personen außerhalb des direkten Umfelds
            (0, 12, "unselbständig"),
            (12, 36, "überwiegend unselbständig"), # 12 months to under 3 years
            (36, 60, "überwiegend selbständig"), # 3 years to under 5 years
            (60, 216, "selbständig"), # From 5 years
        ],
    },
}

# Scoring matrix for children (assessed_child_level vs. age_appropriate_level)
# Points are awarded based on the deviation from the age-appropriate level.
# The keys are tuples: (assessed_child_level, age_appropriate_level)
CHILD_SCORING_MATRIX = {
    "unselbständig,selbständig": 3,
    "unselbständig,überwiegend selbständig": 2,
    "unselbständig,überwiegend unselbständig": 1,
    "unselbständig,nicht vorhanden": 0,
    "unselbständig,nicht erforderlich": 0,

    "überwiegend unselbständig,selbständig": 2,
    "überwiegend unselbständig,überwiegend selbständig": 1,
    "überwiegend unselbständig,überwiegend unselbständig": 0,
    "überwiegend unselbständig,nicht vorhanden": 0,
    "überwiegend unselbständig,nicht erforderlich": 0,

    "überwiegend selbständig,selbständig": 1,
    "überwiegend selbständig,überwiegend selbständig": 0,
    "überwiegend selbständig,überwiegend unselbständig": 0,
    "überwiegend selbständig,nicht vorhanden": 0,
    "überwiegend selbständig,nicht erforderlich": 0,

    "selbständig,selbständig": 0,
    "selbständig,überwiegend selbständig": 0,
    "selbständig,überwiegend unselbständig": 0,
    "selbständig,nicht vorhanden": 0,
    "selbständig,nicht erforderlich": 0,

    "nicht vorhanden,nicht vorhanden": 0,
    "nicht vorhanden,in geringem Maße vorhanden": 1,
    "nicht vorhanden,größtenteils vorhanden": 2,
    "nicht vorhanden,vorhanden/unbeeinträchtigt": 3,

    "in geringem Maße vorhanden,in geringem Maße vorhanden": 0,
    "in geringem Maße vorhanden,größtenteils vorhanden": 1,
    "in geringem Maße vorhanden,vorhanden/unbeeinträchtigt": 2,

    "größtenteils vorhanden,größtenteils vorhanden": 0,
    "größtenteils vorhanden,vorhanden/unbeeinträchtigt": 1,

    "vorhanden/unbeeinträchtigt,vorhanden/unbeeinträchtigt": 0,

    "nicht erforderlich,nicht erforderlich": 0,
}

# Special scoring for Module 4 (Selbstversorgung)
# These are deviations from the standard CHILD_SCORING_MATRIX
CHILD_MODULE4_SPECIAL_SCORING = {
    "4.8": { # Essen (KF 4.4.8) - Triple weighting
        "unselbständig,überwiegend selbständig": 6, # 2 * 3
        "überwiegend unselbständig,selbständig": 6, # 2 * 3
    },
    "4.10": { # Benutzen einer Toilette oder eines Toilettenstuhls (KF 4.4.10) - Double weighting
        "überwiegend unselbständig,selbständig": 4, # 2 * 2
    }
}

# Special rule for children 0-18 months (KF 4.4.0)
# If KF 4.4.0 is "Ja", add 20 points.
KF_4_4_0_POINTS = 20
