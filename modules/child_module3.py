# modules/child_module3.py

child_module3 = {
    'id': 3,
    'name': 'Modul 3: Verhaltensweisen und psychische Problemlagen (Kinder)',
    'weight': 15, # Placeholder weight
    'questions': [
        {
            'id': '3.1',
            'text': 'Motorisch geprägte Verhaltensauffälligkeiten',
            'explanation': '''Dieses Kriterium fasst verschiedene Verhaltensweisen zusammen. Dazu gehören
vor allem das (scheinbar) ziellose Herumlaufen in der Wohnung oder der Ein-
richtung, das wiederholte selbstgefährdende Klettern auf Möbelstücke trotz
eines Verbotes sowie der Versuch desorientierter Kinder, ohne Begleitung die
Wohnung, Einrichtung zu verlassen oder Orte aufzusuchen, die für ein Kind unzu-
gänglich sein sollten. Ebenso zu berücksichtigen ist allgemeine motorische
Unruhe in Form von ständigem Aufstehen und Hinsetzen oder Hin- und Herrut-
schen auf dem Sitzplatz.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.2',
            'text': 'Nächtliche Unruhe',
            'explanation': '''Gemeint sind hier nächtliches Umherirren, Wachphasen, in denen das Kind aktiv
Beschäftigung beziehungsweise Zuwendung einfordert oder längere Schreipha-
sen hat, die nicht durch kurzes Beruhigen zu beenden sind.
Schlafstörungen wie Einschlafschwierigkeiten am Abend oder das bis ins Schul-
alter vorkommende Aufwachen in der Nacht sind nicht zu werten, wenn nur
kurzes Beruhigen oder die Gabe von Getränken erforderlich ist.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.3',
            'text': 'Selbstschädigendes und autoaggressives Verhalten',
            'explanation': '''Selbstschädigendes und autoaggressives Verhalten kann zum Beispiel darin
bestehen, sich durch Gegenstände zu verletzen, ungenießbare Substanzen zu
essen und zu trinken, sich selbst zu schlagen und sich selbst mit den Fingernä-
geln oder Zähnen zu verletzen.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.4',
            'text': 'Beschädigen von Gegenständen',
            'explanation': '''Gemeint sind hier aggressive auf Gegenstände gerichtete Handlungen, zum Bei-
spiel Gegenstände wegstoßen, gegen Gegenstände schlagen, das Zerstören
von Dingen sowie das Treten nach Gegenständen.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.5',
            'text': 'Physisch aggressives Verhalten gegenüber anderen Personen',
            'explanation': '''Physisch aggressives Verhalten gegenüber anderen Personen kann zum Beispiel
sein: nach Personen schlagen oder treten, beißen, kratzen, stoßen oder weg-
drängen, Verletzungsversuche gegenüber anderen Personen mit Gegenständen.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.6',
            'text': 'Verbale Aggression',
            'explanation': '''Verbale Aggression kann sich zum Beispiel in verbalen Beschimpfungen oder in
der Bedrohung anderer Personen ausdrücken.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.7',
            'text': 'Andere pflegerelevante vokale Auffälligkeiten',
            'explanation': '''Andere pflegerelevante vokale Auffälligkeiten können sein: lautes Rufen,
Schreien, vor sich hin schimpfen, fluchen, seltsame Laute von sich geben, stän-
diges Wiederholen von Sätzen, Fragen. Bei Säuglingen und Kleinkindern ist
anhaltendes Weinen beziehungsweise Schreien zu berücksichtigen, bei dem
das Kind nur mit großer Mühe zu beruhigen ist.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.8',
            'text': 'Abwehr pflegerischer und anderer unterstützender Maßnahmen',
            'explanation': '''Hier ist die Abwehr von Unterstützung, zum Beispiel bei der Körperpflege, die
Verweigerung der Nahrungsaufnahme oder anderer notwendiger Verrichtungen,
wie zum Beispiel Inhalation, oder die Manipulation an Vorrichtungen, wie zum
Beispiel Katheter, Infusion, Sondenernährung, gemeint. Dazu gehört nicht die
willentliche (selbstbestimmte) Ablehnung bestimmter Maßnahmen.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.9',
            'text': 'Wahnvorstellungen',
            'explanation': '''Diese treten bei Kindern eher selten auf. Wahnvorstellungen dürfen nicht mit den spielerischen Fantasien von Kindern verwechselt werden.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.10',
            'text': 'Ängste',
            'explanation': '''Es geht hier um ausgeprägte Ängste, die wiederkehrend sind und als bedrohlich
erlebt werden. Das Kind hat keine eigene Möglichkeit/Strategie zur Bewältigung
und Überwindung der Angst.
Angst beziehungsweise Weinen in der Nacht ist nicht zu werten, weil dies auch
bei vielen gesunden Kindern auftritt.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.11',
            'text': 'Antriebslosigkeit bei depressiver Stimmungslage',
            'explanation': '''Antriebslosigkeit bei depressiver Stimmungslage zeigt sich zum Beispiel daran,
dass das Kind kaum Interesse an der Umgebung hat, kaum Eigeninitiative auf-
bringt und eine aufwendige Motivierung durch andere benötigt, um etwas zu tun.
Hiervon sind eher ältere Kinder betroffen.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.12',
            'text': 'Sozial inadäquate Verhaltensweisen',
            'explanation': '''Sozial inadäquate Verhaltensweisen sind zum Beispiel distanzloses Verhalten,
auffälliges Einfordern von Aufmerksamkeit, sich vor anderen in unpassenden
Situationen zu entkleiden, unangemessenes Greifen nach Personen, unangemes-
sene körperliche oder verbale sexuelle Annäherungsversuche.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        },
        {
            'id': '3.13',
            'text': 'Sonstige pflegerelevante inadäquate Handlungen',
            'explanation': '''Sonstige pflegerelevante inadäquate Handlungen sind zum Beispiel Nesteln an
der Kleidung, ständiges Wiederholen der gleichen Handlung (Stereotypien), plan-
lose Aktivitäten, Verstecken oder Horten von Gegenständen, Kotschmieren,
Urinieren in die Wohnung.''',
            'options': [
                {'score': 0, 'text': 'Nie oder sehr selten'},
                {'score': 1, 'text': 'Selten (ein- bis dreimal innerhalb von zwei Wochen)'},
                {'score': 3, 'text': 'Häufig (zweimal bis mehrmals wöchentlich, aber nicht täglich)'},
                {'score': 5, 'text': 'Täglich'}
            ]
        }
    ]
}
