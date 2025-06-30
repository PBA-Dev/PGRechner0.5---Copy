# modules/child_module4.py

child_module4 = {
    'id': 4,
    'name': 'Modul 4: Selbstversorgung (Kinder)',
    'weight': 40, # Weight in percent for final score calculation
    'questions': [
        {
            'id': '4.4.0',
            'text': 'Bestehen gravierende Probleme bei der Nahrungsaufnahme, die einen außergewöhnlich pflegeintensiven Hilfebedarf im Bereich der Ernährung auslösen?',
            'explanation': '''Dieses Kriterium ist erfüllt, wenn der Aufwand bei der Nahrungsaufnahme das
altersübliche Maß in Frequenz oder Zeitaufwand deutlich übersteigt.
Die Bedarfslage dieser Kinder ist unabhängig vom zugrunde liegenden Krank-
heitsbild (zum Beispiel frühkindliche Hirnschädigung, angeborene Herzfehler) in
der Regel gekennzeichnet von Trinkschwäche, „tröpfchenweiser“ oder beson-
ders häufiger Nahrungsaufnahme, Schluckstörungen, Erbrechen et cetera.''',
            'options': [
                {'text': 'Nein', 'score': 0},
                {'text': 'Ja', 'score': 20}
            ]
        },
        {
            'id': '4.4.1',
            'text': 'Waschen des vorderen Oberkörpers',
            'explanation': 'Sich die Hände, das Gesicht, die Arme, die Achselhöhlen sowie den vorderen Hals- und Brustbereich waschen und abtrocknen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        }, {
            'id': '4.4.2',
            'text': 'Körperpflege im Bereich des Kopfes',
            'explanation': 'Kämmen, Zahnpflege, Rasieren. Im Kindesalter kommt dem Erlernen des Zähneputzens eine entscheidende Bedeutung zu und dieses ist daher hier maßgeblich zu beurteilen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.3',
            'text': 'Waschen des Intimbereichs',
            'explanation': 'Den Intimbereich waschen und abtrocknen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.4',
            'text': 'Duschen und Baden einschließlich Waschen der Haare',
            'explanation': 'Durchführung des Dusch- und Wannenbades einschließlich des Waschens der Haare.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.5',
            'text': 'An- und Auskleiden des Oberkörpers',
            'explanation': 'Bereitliegende Kleidungsstücke, zum Beispiel Unterhemd, T-Shirt, Sweatshirt, Pullover, Jacke, Schlafanzugoberteil, an- und ausziehen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.6',
            'text': 'An- und Auskleiden des Unterkörpers',
            'explanation': 'Bereitliegende Kleidungsstücke, zum Beispiel Unterwäsche, Hose, Rock, Strümpfe und Schuhe, an- und ausziehen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.7',
            'text': 'Mundgerechtes Zubereiten der Nahrung und Eingießen von Getränken',
            'explanation': 'Zerteilen von Nahrung in mundgerechte Stücke und Eingießen von Getränken.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.8',
            'text': 'Essen',
            'explanation': 'Bereitgestellte, mundgerecht zubereitete Speisen essen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig', 'score': 3},
                {'text': 'Überwiegend unselbständig', 'score': 6},
                {'text': 'Unselbständig', 'score': 9}
            ]
        },
        {
            'id': '4.4.9',
            'text': 'Trinken',
            'explanation': 'Bereitstehende Getränke aufnehmen, gegebenenfalls mit Gegenständen wie Strohhalm, Spezialbecher mit Trinkaufsatz.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig', 'score': 2},
                {'text': 'Überwiegend unselbständig', 'score': 4},
                {'text': 'Unselbständig', 'score': 6}
            ]
        },
        {
            'id': '4.4.10',
            'text': 'Benutzen einer Toilette oder eines Toilettenstuhls',
            'explanation': 'Gehen zur Toilette, Hinsetzen und Aufstehen, Sitzen während der Blasen- oder Darmentleerung, Intimhygiene und Richten der Kleidung.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig', 'score': 2},
                {'text': 'Überwiegend unselbständig', 'score': 4},
                {'text': 'Unselbständig', 'score': 6}
            ]
        },
        {
            'id': '4.4.11',
            'text': 'Bewältigen der Folgen einer Harninkontinenz und Umgang mit Dauerkatheter und Urostoma',
            'explanation': 'Inkontinenz- und Stomasysteme sachgerecht verwenden, nach Bedarf wechseln und entsorgen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.12',
            'text': 'Bewältigen der Folgen einer Stuhlinkontinenz und Umgang mit Stoma',
            'explanation': 'Inkontinenz- und Stomasysteme sachgerecht verwenden, nach Bedarf wechseln und entsorgen.',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Überwiegend selbständig'},
                {'text': 'Überwiegend unselbständig'},
                {'text': 'Unselbständig'}
            ]
        },
        {
            'id': '4.4.13',
            'text': 'Ernährung parenteral oder über Sonde',
            'explanation': 'Ernährung über einen parenteralen Zugang (zum Beispiel einen Port) oder über einen Zugang in Magen oder Dünndarm (PEG/PEJ).',
            'options': [
                {'text': 'Selbständig'},
                {'text': 'Nicht täglich, nicht auf Dauer', 'score': 1},
                {'text': 'Täglich, zusätzlich zu oraler Ernährung', 'score': 2},
                {'text': 'Ausschließlich oder nahezu ausschließlich', 'score': 3}
            ]
        }
    ]
}
