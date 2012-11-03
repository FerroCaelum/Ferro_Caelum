# coding: utf-8

def get_stats_name(number, where):
    if where==1: #Statystyki główne
        if number==1:
             str=u'moc'
        elif number==2:
            str=u'odporność'
        elif number==3:
            str=u'sprawność'
        elif number==4:
            str=u'percepcja'
        elif number==5:
            str=u'inteligencja'
        elif number==6:
            str=u'sieć'
        elif number==7:
            str=u'spryt'
        elif number==8:
            str=u'punkty życia'
        elif number==9:
            str=u'punkty akcji'
        elif number==10:
            str=u'prędkość poruszania'
        elif number==11:
            str=u'ukrywanie'
        elif number==12:
            str=u'wykrycie'
        elif number==13:
            str=u'handel'
        elif number==14:
            str=u'poziom'
        else:
            str=u''
    elif where==2: #Statystyki bojowe
        if number==1:
             str=u'punkty wytrzymałości'
        elif number==2:
            str=u'maksymalne punkty akcji'
        elif number==3:
            str=u'punkty akcji'
        elif number==4:
            str=u'pancerz przeciwko energii'
        elif number==5:
            str=u'pancerz przeciwko przebijającym'
        elif number==6:
            str=u'pancerz przeciwko uderzającym'
        elif number==7:
            str=u'unik przeciw atakom sieciowym'
        elif number==8:
            str=u'unik przeciw atakom wręcz'
        elif number==9:
            str=u'unik przeciw atakom dystansowym'
        elif number==10:
            str=u'odporność na ataki wirusem'
        elif number==11:
            str=u'szybkość poruszania'
        elif number==12:
            str=u'możliwości uruchamiania oprogramowania'
        elif number==13:
            str=u'ukrywanie'
        elif number==14:
            str=u'wykrycie'
        elif number==15:
            str=u'prędkość poruszania'
        elif number==16:
            str=u'koszt ataku wręcz'
        elif number==17:
            str=u'koszt ataku dystansowego'
        elif number==18:
            str=u'koszt ataku siecią'
        elif number==19:
            str=u'koszt tworzenia pola'
        elif number==20:
            str=u'koszt uruchomienia pola'
        elif number==21:
            str=u'koszt wruchomienia wirusa'
        elif number==22:
            str=u'walka wręcz: atak'
        elif number==23:
            str=u'walka wręcz: obrażenia od energii'
        elif number==24:
            str=u'odporność'
        elif number==25:
            str=u'walka wręcz: obrażenia od uderzenia'
        elif number==26:
            str=u'walka wręcz: szansa na trafienie krytyczne'
        elif number==27:
            str=u'walka wręcz: siła trafienia krytycznego'
        elif number==28:
            str=u'walka dystansowa: atak'
        elif number==29:
            str=u'walka dystansowa: obrażenia od energii'
        elif number==30:
            str=u'walka dystansowa: obrażenia przebijające'
        elif number==31:
            str=u'walka dystansowa: szansa na trafienie krytyczne'
        elif number==32:
            str=u'walka dystansowa: siła trafienia krytycznego'
        elif number==33:
            str=u'walka siecią: atak'
        elif number==34:
            str=u'walka siecią: obrażenia od energii'
        elif number==35:
            str=u'walka siecią: obrażenia uderzające'
        elif number==36:
            str=u'walka siecią: przebijające'
        elif number==37:
            str=u'walka siecią: szansa na trafienie krytyczne'
        elif number==38:
            str=u'walka siecią: siła trafienia krytycznego'
        elif number==39:
            str=u'tworzenie pola: formowanie'
        elif number==40:
            str=u'tworzenie pola: pole przeciw energii'
        elif number==41:
            str=u'tworzenie pola: pole przeciw uderzeniom'
        elif number==42:
            str=u'tworzenie pola: pole przeciw przebiciom'
        elif number==43:
            str=u'tworzenie pola: wytrzymałość'
        elif number==44:
            str=u'uruchomienie programu: formowanie'
        elif number==45:
            str=u'uruchomienie programu: czas trwania'
        elif number==46:
            str=u'uruchomienie wirusa: formowanie'
        elif number==47:
            str=u'uruchomienie wirusa: trudność odparcia'
        elif number==48:
            str=u'uruchomienie wirusa: czas trwania'
        else:
            str=u''
    elif where==3: #Statystyki niebojowe
        if number==1:
            str=u'handel'
        else:
            str=u''
    elif where==4: # Progres       
        if number==1:
            str=u''
        else:
            str=u'' 
    else:
         str=u''      
    return str