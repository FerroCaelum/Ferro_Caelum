# coding: utf-8

class dictionary():
    names = [
                [
                'moc',
                'odporność',
                'sprawność',
                'perception',
                'percepcja',
                'inteligencja',
                'sieć',
                'spryt',
                'punkty życia',
                'punkty akcji',
                'prędkość poruszania',
                'ukrywanie',
                'wykrycz'
                ],
                [
                'punkty wytrzymałości',
                'maksymalne punkty akcji',
                'punkty akcji',
                'pancerz przeciwko energii',
                'pancerz przeciwko przebijającym',
                'pancerz przeciwko uderzającym',    
                'unik przeciw atakom sieciowym',
                'unik przeciw atakom wręcz',
                'unik przeciw atakom dystansowym',
                'odporność na ataki wirusem',
                'szybkość poruszania',
                'możliwości uruchamiania oprogramowania',
                'ukrywanie',
                'wykrycie',
                'koszt ataku wręcz',
                'koszt ataku dystansowego',
                'koszt ataku siecią',
                'koszt tworzenia pola',
                'koszt uruchomienia pola',
                'koszt wruchomienia wirusa',
                'walka wręcz: atak',
                'walka wręcz: obrażenia od energii',
                'walka wręcz: obrażenia od uderzenia',
                'walka wręcz: szansa na trafienie krytyczne',
                'walka wręcz: siła trafienia krytycznego',
                'walka dystansowa: atak',
                'walka dystansowa: obrażenia od energii',
                'walka dystansowa: obrażenia przebijające',
                'walka dystansowa: szansa na trafienie krytyczne',
                'walka dystansowa: siła trafienia krytycznego',
                'walka siecią: atak',
                'walka siecią: obrażenia od energii',
                'walka siecią: obrażenia uderzające',
                'walka siecią: przebijające',
                'walka siecią: szansa na trafienie krytyczne',
                'walka siecią: siła trafienia krytycznego',
                'tworzenie pola: formowanie',
                'tworzenie pola: pole przeciw energii',
                'tworzenie pola: pole przeciw uderzeniom',
                'tworzenie pola: pole przeciw dystansowej',
                'tworzenie pola: wytrzymałość',
                'uruchomienie programu: formowanie',
                'uruchomienie programu: czas trwania',
                'uruchomienie wirusa: formowanie',
                'uruchomienie wirusa: trudność odparcia',
                'uruchomienie wirusa: czas trwania',
                ],
                [
                  'handel',
                ],
                [
                ]
            ]
    def get_stats_name(self, number, where):
#            print number
#            print where
#            print self.names
            return self.names[where][number]


