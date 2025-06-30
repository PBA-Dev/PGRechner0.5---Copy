# modules/child_module1.py

child_module1 = {
    'id': 1,
    'name': 'Modul 1: Mobilität (Kinder)',
    'weight': 10, # Weight in percent for final score calculation
    'questions': [
        {
            'id': '1.1',
            'text': 'Positionswechsel im Bett',
            'explanation': '''Die Einschätzung richtet sich ausschließlich danach, ob das Kind in der Lage
ist, ohne personelle Unterstützung eine Körperhaltung einzunehmen/zu wechseln
und sich fortzubewegen. Zu beurteilen sind hier ausschließlich motorische
Aspekte wie Körperkraft, Balance, Bewegungskoordination et cetera und nicht
die zielgerichtete Fortbewegung. Hier werden nicht die Folgen kognitiver Beeinträchtigungen
auf Planung, Steuerung und Durchführung motorischer Handlungen
abgebildet.''',
            'options': [
                {
                    'text': 'Selbständig',
                    'option_explanation': (
                        'Das Kind ist auch selbständig, wenn es seine Position unter Nutzung von Hilfsmitteln, '
                        'zum Beispiel Aufrichter, Bettseitenteil, Strickleiter, elektrisch verstellbares Bett, '
                        'ohne personelle Hilfe verändern kann.'
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'option_explanation': (
                        'Das Kind kann beispielsweise nach Anreichen eines Hilfsmittels oder Reichen der Hand '
                        'seine Lage im Bett verändern.'
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'option_explanation': (
                        'Das Kind kann beim Positionswechsel nur wenig mithelfen, zum Beispiel auf den Rücken '
                        'rollen, am Bettgestell festhalten oder zum Lagern die Arme vor der Brust verschränken '
                        'und den Kopf auf die Brust legen.'
                    )
                },
                {
                    'text': 'Unselbständig',
                    'option_explanation': (
                        'Das Kind kann sich beim Positionswechsel nicht oder nur minimal beteiligen.'
                    )
                }
            ]
        },
        {
            'id': '1.2',
            'text': 'Halten einer stabilen Sitzposition',
            'explanation': '''Sich auf einem Bett, Stuhl oder Sessel aufrecht halten''',
            'options': [
                {
                    'text': 'Selbständig',
                    'option_explanation': (
                        'Das Kind ist auch dann selbständig, wenn es beim Sitzen gelegentlich seine '
                        'Sitzposition korrigieren muss.'
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'option_explanation': (
                        '''Die Person kann sich nur kurz, zum Beispiel für die Dauer einer Mahlzeit oder
eines Waschvorgangs selbständig in der Sitzposition halten, darüber hinaus
benötigt sie aber personelle Unterstützung zur Positionskorrektur.'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'option_explanation': (
                        '''Das Kind kann sich wegen eingeschränkter Rumpfkontrolle auch mit Rücken-
und Seitenstütze nicht in aufrechter Position halten und benötigt auch während
der Dauer einer Mahlzeit oder eines Waschvorgangs personelle Unterstützung
zur Positionskorrektur.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'option_explanation': (
                        '''Das Kind kann sich nicht in Sitzposition halten. Bei fehlender Rumpf- und Kopf-
kontrolle kann das Kind nur im Bett oder Lagerungsstuhl liegend gelagert werden.'''
                    )
                }
            ]
        },
        {
            'id': '1.3',
            'text': 'Umsetzen',
            'explanation': '''Von einer altersentsprechend üblich hohen Sitzgelegenheit aufstehen und sich auf eine andere umsetzen''',
            'options': [
                {
                    'text': 'Selbständig',
                    'option_explanation': (
                        '''Das Kind ist auch dann selbständig, wenn es keine Personenhilfe benötigt, aber
ein Hilfsmittel oder einen anderen Gegenstand zum Festhalten oder Hochziehen
benutzt oder sich auf Tisch, Armlehnen oder sonstigen Gegenständen abstützen
muss, um aufzustehen. Als selbständig ist auch zu bewerten, wer zwar nicht
stehen kann, aber sich mit Armkraft ohne personelle Hilfe umsetzen kann
(zum Beispiel Rollstuhl – Toilette).'''
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'option_explanation': (
                        '''Das Kind kann aus eigener Kraft aufstehen oder sich umsetzen, wenn es eine
Hand oder einen Arm gereicht bekommt.'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'option_explanation': (
                        '''Die Eltern müssen beim Aufstehen, Umsetzen (erheblichen) Kraftaufwand auf-
bringen (hochziehen, halten, stützen, heben). Das Kind hilft jedoch in geringem
Maße mit, kann zum Beispiel kurzzeitig stehen.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'option_explanation': (
                        '''Das Kind muss gehoben oder getragen werden, Mithilfe ist nicht möglich.'''
                    )
                }
            ]
        },
        {
            'id': '1.4',
            'text': 'Fortbewegen innerhalb des Wohnbereichs',
            'explanation': '''Sich innerhalb einer Wohnung oder im Wohnbereich einer Einrichtung zwischen
den Zimmern sicher bewegen.
Als Anhaltsgröße für übliche Gehstrecken innerhalb einer Wohnung werden mindestens
acht Meter festgelegt.
Die Fähigkeiten zur örtlichen Orientierung und zum Treppensteigen sind unter
Punkt KF 4.2.2 beziehungsweise Punkt KF 4.1.5 zu berücksichtigen.''',
             'options': [
                {
                    'text': 'Selbständig',
                    'option_explanation': (
                        '''Das Kind kann sich ohne Hilfe durch andere Personen fortbewegen. Das kann gege-
benenfalls unter Nutzung von Hilfsmitteln, zum Beispiel Unterarmgehstützen, Rol-
lator, Rollstuhl oder sonstiger Gegenstände, zum Beispiel Möbelstück, geschehen.'''
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'option_explanation': (
                        '''Das Kind kann die Aktivität überwiegend selbständig durchführen. Personelle
Hilfe ist beispielsweise erforderlich im Sinne von Bereitstellen von Hilfsmitteln
(zum Beispiel Unterarmgehstützen oder Rollator), punktuellem Stützen/Unter-
haken oder Beobachtung (Anwesenheit aus Sicherheitsgründen).'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'option_explanation': (
                        '''Das Kind kann nur wenige Schritte gehen oder sich mit dem Rollstuhl nur wenige
Meter fortbewegen oder kann nur mit Stützung oder Festhalten der Eltern gehen.
Auch wenn sich das Kind darüber hinaus in der Wohnung krabbelnd oder rob-
bend fortbewegen kann, ändert dies nichts an der Bewertung als „überwiegend
unselbständig“.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'option_explanation': (
                        '''Das Kind muss getragen oder vollständig im Rollstuhl geschoben werden.'''
                    )
                }
            ]
        },
        {
            'id': '1.5',
            'text': 'Treppensteigen',
            'explanation': '''Überwinden von Treppen zwischen zwei Etagen in aufrechter Position''',
            'options': [
                {
                    'text': 'Selbständig',
                    'option_explanation': (
                    '''Das Kind kann ohne Hilfe durch andere Personen in aufrechter Position eine
Treppe steigen.'''
                    )
                },
                {
                    'text': 'Überwiegend selbständig',
                    'option_explanation': (
                        '''Das Kind kann eine Treppe alleine steigen, benötigt aber Begleitung wegen
eines Sturzrisikos (Anwesenheit aus Sicherheitsgründen).'''
                    )
                },
                {
                    'text': 'Überwiegend unselbständig',
                    'option_explanation': (
                        '''Treppensteigen ist nur mit Stützen oder Festhalten des Kindes möglich. Die aus-
schließliche Fähigkeit zur Überwindung von Stufen durch Krabbeln oder Robben
ist generell als „überwiegend unselbständig“ zu bewerten.'''
                    )
                },
                {
                    'text': 'Unselbständig',
                    'option_explanation': (
                        '''Das Kind muss getragen oder mit Hilfsmitteln transportiert werden, keine Eigen-
beteiligung.'''
                    )
                }
            ]
        },
        {
            'id': '1.B',
            'text': 'Besondere Bedarfskonstellation: Gebrauchsunfähigkeit beider Arme und beider Beine',
            'explanation': '''Eine Beurteilung ist bei Kindern altersunabhängig immer erforderlich.
Gebrauchsunfähigkeit beider Arme und beider Beine mit vollständigem Verlust
(Fehlen) der Greif-, Steh- und Gehfunktionen, die nicht durch Einsatz von Hilfs-
mitteln kompensiert werden''',
            'options': [
                {
                    'text': 'Nein',
                    'option_explanation': 'Trifft nicht zu.'
                },
                {
                    'text': 'Ja',
                    'option_explanation': (
                        '''Das Kriterium erfasst in der Regel Kinder mit einer Bewegungsunfähigkeit beider
Arme und beider Beine unabhängig von der Ursache. Gebrauchsunfähigkeit bei-
der Arme und beider Beine mit vollständigem Verlust der Greif-, Steh- und Geh-
funktionen liegt zum Beispiel vor bei kompletten Lähmungen aller Extremitäten
oder bei Kindern im Wachkoma oder mit schwersten Fehlbildungen. Auch bei
hochgradigen Kontrakturen, Spastiken oder Athetose kann die besondere
Bedarfskonstellation vorliegen.
Eine Gebrauchsunfähigkeit beider Arme und beider Beine liegt auch vor, wenn
eine minimale Restbeweglichkeit der Arme vorhanden ist.
Eine besondere Bedarfskonstellation liegt auch dann vor, wenn bei Säuglingen
keine Bewegungen der Extremitäten erkennbar sind.'''
                    )
                }
            ]
        }
    ]
}
