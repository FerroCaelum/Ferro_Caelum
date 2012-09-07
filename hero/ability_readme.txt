hero_Effect.type
Type okresla przepis kiedy i gdzie stosowac zdolnosc. Jest reprezentowany prze 2 cyfry:
1. reprezentuje miejsce stosowania:
	0: statystyki glówne
	1: statystyki bojowe
	2: statsytyki niebojowe
	3: progres
2. reprezentuje czas stosowania:
	0: natychmiastowy - trwala zmiana lub na poczatku wyliczania statystyk pobocznych (np. +2 do punktów akcji)
	1: staly - przy kazdym wyliczaniu lub zmianie statystyk brany pod uwage (np. zwiekszenie obrazecn 5%)
	2: aktywowany - po aktywowaniu dziala przez okreslony czas

hero_Effect.effect	
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

hero_Stats_requierment.stats_requierment
Stats_requierment określa jedno z wymaga w cechach potrzebne do wzięcia specialnej zdolności.
Jest reprezentowany prze 8 cyfry:
1-2. reprezentuja której statystyki dotyczy
3-6. określa wymaganą wartość
7-8. są nie wykorzystywane (ich wartości są nieistotne)
