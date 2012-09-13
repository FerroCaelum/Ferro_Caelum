

NIEAKTUALNE, przechowywane na potrzeby wglądu w potrzebne atrybuty



Ability.when_and_where
when_and_where okresla przepis kiedy i gdzie stosowac zdolnosc. Jest reprezentowany prze 4 cyfry:
1. reprezentuje miejsce stosowania:
	1: statystyki glowne
	2: statystyki bojowe
	3: statsytyki niebojowe
	4: progres
2. reprezentuje czas stosowania:
	1: natychmiastowy - trwala zmiana lub na poczatku wyliczania statystyk pobocznych (np. +2 do punktow akcji)
	2: staly - przy kazdym wyliczaniu lub zmianie statystyk brany pod uwage (np. zwiekszenie obrazecn 5%)
	3: aktywowany - po aktywowaniu dziala przez okreslony czas
3-4. koszt w punktach akcji (tylko zdolność aktywowana)

Effect.effect	
Effect okresla efekt dzialania zdolnosci. Jest reprezentowany prze 8 cyfry:
1-2. reprezentuja na ktora statystyke ma wplyw dzialanie zdolnosci
3. informuje czy wartosc premi jest dodatnia czy ujemna
	0: dodatnia
	1: ujemna
4-7. reprezentuja wysokosc premii
8. cel zdolnosci (tylko dla aktywowanych)
	0: sam bohater
	1: przeciwnik
	2: srodowisko
9. informuje o typie czasu dzialania (tylko dla aktywowanych)
	0: do konca trwania starcia (walka) / do dezaktywacji (wplywajace na cos innego niz statystyki bojowe)
	1-9: liczba tur (zalezy od cyfry)

Stats_requierment.stats_requierment
Stats_requierment określa jedno z wymaga w cechach potrzebne do wzięcia specialnej zdolności.
Jest reprezentowany prze 8 cyfry:
1-2. reprezentuja ktorej statystyki dotyczy
3-6. reprezentuja ktorej statystyki dotyczy wymaganie
7-8. nie wykorzystywane (ich wartości są nieistotne)

#def get_stats_name(number, where):
#    return {1: {1: 'moc',
#                2: 'odporność',
#                3: 'sprawność',
#                4: 'perception',
#                5: 'percepcja',
#                6: 'inteligencja',
#                7: 'sieć',
#                8: 'spryt',
#                9: 'punkty życia',
#                10: 'punkty akcji',
#                11: 'prędkość poruszania',
#                12: 'ukrywanie',
#                13: 'wykrycie',
#                14: 'handel',
#                }[number],
#            2:  {1: 'punkty wytrzymałości',
#                2: 'maksymalne punkty akcji',
#                3: 'punkty akcji',
#                4: 'pancerz przeciwko energii',
#                5: 'pancerz przeciwko przebijającym',
#                6: 'pancerz przeciwko uderzającym',
#                7: 'unik przeciw atakom sieciowym',
#                8: 'unik przeciw atakom wręcz',
#                9: 'unik przeciw atakom dystansowym',
#                10: 'odporność na ataki wirusem',
#                11: 'szybkość poruszania',
#                12: 'możliwości uruchamiania oprogramowania',
#                13: 'ukrywanie',
#                14: 'wykrycie',
#                15: 'koszt ataku wręcz',
#                16: 'koszt ataku dystansowego',
#                17: 'koszt ataku siecią',
#                18: 'koszt tworzenia pola',
#                19: 'koszt uruchomienia pola',
#                20: 'koszt wruchomienia wirusa',
#                21: 'walka wręcz: atak',
#                22: 'walka wręcz: obrażenia od energii',
#                23: 'walka wręcz: obrażenia od uderzenia',
#                24: 'walka wręcz: szansa na trafienie krytyczne',
#                25: 'walka wręcz: siła trafienia krytycznego',
#                26: 'walka dystansowa: atak',
#                27: 'walka dystansowa: obrażenia od energii',
#                28: 'walka dystansowa: obrażenia przebijające',
#                29: 'walka dystansowa: szansa na trafienie krytyczne',
#                30: 'walka dystansowa: siła trafienia krytycznego',
#                31: 'walka siecią: atak',
#                32: 'walka siecią: obrażenia od energii',
#                33: 'walka siecią: obrażenia uderzające',
#                34: 'walka siecią: przebijające',
#                35: 'walka siecią: szansa na trafienie krytyczne',
#                36: 'walka siecią: siła trafienia krytycznego',
#                37: 'tworzenie pola: formowanie',
#                38: 'tworzenie pola: pole przeciw energii',
#                39: 'tworzenie pola: pole przeciw uderzeniom',
#                40: 'tworzenie pola: pole przeciw dystansowej',
#                41: 'tworzenie pola: wytrzymałość',
#                42: 'uruchomienie programu: formowanie',
#                43: 'uruchomienie programu: czas trwania',
#                44: 'uruchomienie wirusa: formowanie',
#                45: 'uruchomienie wirusa: trudność odparcia',
#                46: 'uruchomienie wirusa: czas trwania',
#                }[number],
#            3:  {1: 'handel',
#                }[number],
#            4:  {1: '',
#                2: '',
#                3: '',
#                4: '',
#                5: '',
#                6: '',
#                7: '',
#                8: '',
#                9: '',
#                10: '',
#                11: '',
#                12: '',
#                13: '',
#                14: '',
#                15: '',
#                16: '',
#                17: '',
#                18: '',
#                19: '',
#                20: '',
#                21: '',
#                22: '',
#                23: '',
#                24: '',
#                25: '',
#                26: '',
#                }[number],
#            }[where]
    
