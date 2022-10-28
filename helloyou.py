import time

nederland = 0
engeland = 0
duitsland = 0
vliegtuigkost = 0
dood = 0

#rijs vragen 

def waarvluchten():
    print("Je bent een jongen van 16 jaar die in Syrie woont")
    time.sleep(2)
    print("Je woont zonder zorgen in Syrie en dan start er een oorlog dus je moet vluchten")
    time.sleep(2)
    print("Je moet kiezen waar je naartoe vlucht ga je naar")
    time.sleep(2)
    while True:
        vraag1 = input("A Nederland, B Engeland Of C Duitsland?: ").lower()
        if vraag1 == "a":
            print("je hebt er voor gekozen om naar Nederland te vluchten")
            break
        elif vraag1 == "b":
            print("je hebt er voor gekozen om naar Engeland te vluchten")
            break
        elif vraag1 =="c":
            print("je hebt er voor gekozen om naar Duitsland te vluchten")
            break
        else:
            print("je moet met A, B of C antwoorden")
    return vraag1

def hoevluchten():
    time.sleep(2)
    print("Hoe ga je uit Syrie vluchten?")
    while True:
        vraag2 = input("A een boot, B lopend of C een vliegtuig: ").lower()
        if vraag2 == "a":
            print("je hebt gekozen om met een boot te vluchten")
            break
        elif vraag2 == "b":
            print("je hebt gekozen om lopend te gaan vluchten")
            break
        elif vraag2 == "c":
            print("je hebt gekozen om met een vliegtuig te vluchten")
            break
        else:
            print("je moet met A, B of C antwoorden")
    return vraag2

def motorkapotned():
    time.sleep(2)
    print("je hebt zo snel mogelijk met je gezin een boot naar Nederland genomen maar de motor valt uit wat doe je?")
    while True:
        vraag3 = input("Ga je A proberen de motor te repareren of B je doet niks en wacht tot je land ziet: ").lower()
        if vraag3 == "a":
            print("je probeert de motor te repareren maar het lukt niet")
            break
        elif vraag3 == "b":
            print("je doet niks en wacht")
            break
        else:
            print("je moet met A of B antwoorden")
    time.sleep(2)
    print("ja ben 3 dagen op water zonder land te zien maar de 4de dag zie je eindelijk land en ga je aan land je komt er achter dat je in Libië bent")
    time.sleep(2)
    print("na 5 dagen lang lopen kom je eindelijk aan in marroko vanaf daar ga je met een andere boot naar Nederland voor 300 euro")
    time.sleep(2)
    print("je bent veilig in Nederland")

def motorkapoteng():
    time.sleep(2)
    print("je hebt zo snel mogelijk met je gezin een boot naar Engeland genomen maar de motor valt uit wat doe je?")
    while True:
        vraag3 = input("Ga je A proberen de motor te repareren of B je doet niks en wacht tot je land ziet: ").lower()
        if vraag3 == "a":
            print("je probeert de motor te repareren maar het lukt niet")
            break
        elif vraag3 == "b":
            print("je doet niks en wacht")
            break
        else:
            print("je moet met A of B antwoorden")
    time.sleep(2)
    print("ja ben 3 dagen op water zonder land te zien maar de 4de dag zie je eindelijk land en ga je aan land je komt er achter dat je in Libië bent")
    time.sleep(2)
    print("na 5 dagen lang lopen kom je eindelijk aan in marroko vanaf daar ga je met een andere boot naar Engeland voor 300 euro")
    time.sleep(2)
    print("je bent veilig in Engeland")

def motorkapotdui():
    time.sleep(2)
    print("je hebt zo snel mogelijk met je gezin een boot naar Duitsland genomen maar de motor valt uit wat doe je?")
    while True:
        vraag3 = input("Ga je A proberen de motor te repareren of B je doet niks en wacht tot je land ziet: ").lower
        if vraag3 == "a":
            print("je probeert de motor te repareren maar het lukt niet")
            break
        elif vraag3 == "b":
            print("je doet niks en wacht")
            break
        else:
            print("je moet met A, B of C antwoorden")
    time.sleep(2)
    print("ja ben 3 dagen op water zonder land te zien maar de 4de dag zie je eindelijk land en ga je aan land je komt er achter dat je in Libië bent")
    time.sleep(2)
    print("na 5 dagen lang lopen kom je eindelijk aan in marroko vanaf daar ga je met een andere boot naar Duitsland voor 300 euro")
    time.sleep(2)
    print("je bent veilig in Duitsland")

def lopenned():
    time.sleep(2)
    while True:
        vraag4 = input("je gaat lopen om uit Syrië terwel je loopt rijdt er een vreemdeling langs in een auto hij vraagt of je mee wil ga je A mee of B niet mee: ").lower()
        if vraag4 == "a":
            print("je gaat mee met de vreemdeling terwel je met hem mee rijdt houden soldaten jullie tegen")
            break
        elif vraag4 == "b":
            print("je gaat niet mee met de vreemdeling je gaat verder lopen en naa 1 hele lange week kom je in Turkije daarna loop je door naar griekenland")
            break
        else: 
            print("je moet met A of B antwoorden")
    return vraag4

def lopeneng():
    time.sleep(2)
    while True:
        vraag4 = input("je gaat lopen om uit Syrië terwel je loopt rijdt er een vreemdeling langs in een auto hij vraagt of je mee wil ga je A mee of B niet mee: ").lower()
        if vraag4 == "a":
            print("je gaat mee met de vreemdeling terwel je met hem mee rijdt houden soldaten jullie tegen")
            break
        elif vraag4 == "b":
            print("je gaat niet mee met de vreemdeling je gaat verder lopen en naa 1 hele lange week kom je in Turkije daarna loop je door naar griekenland")
            break
        else:
            print("je moet met A of B antwoorden")
    return vraag4

def lopendui():
    time.sleep(2)
    while True:
        vraag4 = input("je gaat lopen om uit Syrië terwel je loopt rijdt er een vreemdeling langs in een auto hij vraagt of je mee wil ga je A mee of B niet mee: ").lower()
        if vraag4 == "a":
            print("je gaat mee met de vreemdeling terwel je met hem mee rijdt houden soldaten jullie tegen")
            break
        elif vraag4 == "b":
            print("je gaat niet mee met de vreemdeling je gaat verder lopen en naa 1 hele lange week kom je in Turkije daarna loop je door naar griekenland")
            break
        else:
            print("je moet met A of B antwoorden")
    return vraag4

def nalopenned():
    time.sleep(2)
    print("je bent in Griekenland en moet de keuze maken om of met een boot voor 300 euro naar Nederland te gaan of met een vliegtuig voor 1000 euro naar Nederland te gaan")
    while True:
        vraag5 = input("ga je A met een boot of B met een vliegtuig: ").lower()
        if vraag5 == "a":
            print("je hebt gekozen om met een boot naar Nederland te gaan voor 300 euro")
            time.sleep(2)
            print("de boot kost 300 euro je kan het betalen")
            time.sleep(2)
            print("je bent veilig in Nederland")
            break
        elif vraag5 == "b":
            print("je hebt gekozen om met een vliegtuig naar Nederland te gaan voor 1000 euro")
            time.sleep(2)
            print("het vleigtuig kost 1000 euro je kan het niet betalen en moet in Nederland nog geld terug betalen")
            time.sleep(2)
            print("je bent veilig in Nederland")
            break
    return vraag5

def nalopeneng():
    time.sleep(2)
    print("je bent in Griekenland en moet de keuze maken om of met een boot voor 300 euro naar Engeland te gaan of met een vliegtuig voor 1000 euro naar Engeland te gaan")
    while True:
        vraag5 = input("ga je A met een boot of B met een vliegtuig: ").lower()
        if vraag5 == "a":
            print("je hebt gekozen om met een boot naar Engeland te gaan voor 300 euro")
            time.sleep(2)
            print("de boot kost 300 euro je kan het betalen")
            time.sleep(2)
            print("je bent veilig in Engeland")
            break
        elif vraag5 == "b":
            print("je hebt gekozen om met een vliegtuig naar Engeland te gaan voor 1000 euro")
            time.sleep(2)
            print("het vleigtuig kost 1000 euro je kan het niet betalen en moet in Engeland nog geld terug betalen")
            time.sleep(2)
            print("je bent veilig in Engeland")
            break
    return vraag5

def nalopendui():
    time.sleep(2)
    print("je bent in Griekenland en moet de keuze maken om of met een boot voor 300 euro naar Duitsland te gaan of met een vliegtuig voor 1000 euro naar Duitsland te gaan")
    while True:
        vraag5 = input("ga je A met een boot of B met een vliegtuig: ").lower()
        if vraag5 == "a":
            print("je hebt gekozen om met een boot naar Duitsland te gaan voor 300 euro")
            time.sleep(2)
            print("de boot kost 300 euro je kan het betalen")
            time.sleep(2)
            print("je bent veilig in Duitsland")
            break
        elif vraag5 == "b":
            print("je hebt gekozen om met een vliegtuig naar Duitsland te gaan voor 1000 euro")
            time.sleep(2)
            print("het vleigtuig kost 1000 euro je kan het niet betalen en moet in Duitsland nog geld terug betalen")
            time.sleep(2)
            print("je bent veilig in Duitsland")
            break
    return vraag5
#rijs vragen

antwo = waarvluchten()
if antwo == "a":
    nederland += 1
    #nederland
    antwo1 = hoevluchten()
    if antwo1 == "a":
        #boot
        antwo3ned = motorkapotned()
    elif antwo1 == "b":
        #lopen
        lopen = lopenned()
        if lopen == "a":
            #na lopen keuze
            naned = nalopenned()
            if naned == "b":
                vliegtuigkost += 1
        elif lopen == "b":
            dood = 1
    elif antwo1 == "c":
        #vliegtuig
        print("je gaat met een vliegtuig terwel je boven Syrië vliegt stort je neer en ga je dood")
        nederland -= 1
elif antwo == "b": 
    engeland += 1
    #engeland
    antwo1 = hoevluchten()
    if antwo1 == "a":
        #boot
        antwo3eng = motorkapoteng()
    elif antwo1 == "b":
        #lopen
        lopen = lopeneng()
        if lopen == "a":
            #na lopen keuze
            naeng = nalopeneng()
            if naeng == "b":
                vliegtuigkost += 1
        elif lopen == "b":
            dood = 1
    elif antwo1 == "c":
        #vliegtuig
        print("je gaat met een vliegtuig terwel je boven Syrië vliegt stort je neer en ga je dood")
        engeland -= 1
elif antwo == "c":
    duitsland += 1
    #duitsland
    antwo1 = hoevluchten()
    if antwo1 == "a":
        #boot
        antwo3eng = motorkapotdui()
    elif antwo1 == "b":
        #lopen
        lopen = lopendui()
        if lopen == "a":
            #na lopen keuze
            nadui = nalopendui()
            if nadui == "b":
                vliegtuigkost += 1
        elif lopen == "b":
            dood = 1
    elif antwo1 == "c":
        #vliegtuig
        print("je gaat met een vliegtuig terwel je boven Syrië vliegt stort je neer en ga je dood")
        duitsland -= 1
else:
    print("iets if fout gegaan")

#vragen in land
def watdoenned():
    vliegtuignietbetaald = 0
    time.sleep(2)
    print("je bent nu in Nederland en moet kiezen wat je gaat doen met je toekomst")
    if vliegtuigkost == 1:
        time.sleep(2)
        print("je moet nog je schuld van het vliegtuig terug betalen")
        while True:
            vraag6 = input("ga A voor het geld werken of B niks doen: ").lower()
            if vraag6 == "a":
                time.sleep(2)
                print("je gaat voor het geld werken en hebt je schuld terug betaald")
                break
            elif vraag6 == "b":
                vliegtuignietbetaald = 1
                time.sleep(2)
                print("je gaat niet werken om je schuld aftebetalen")
                time.sleep(2)
                print("omdat je je schuld niet hebt afbetaald ga je naar de gevangenis na dat je uit de gevangenis komt probeer je werk te vinden alleen niemand neemt je aan omdat je een staf blad hebt")
                time.sleep(2)
                print("een paar maanden later tijdens de winter vries je dood onder een brug")
                break
            else:
                print("je moet met A, B of C antwoorden")
    if vliegtuignietbetaald == 0:
        print("nu je in Nederland bent moet je gaan denken aan je toekomst wat ga je doen")
        time.sleep(2)
        print("je hebt de keuze om naar school te gaan of om te gaan werken je kan ook kiezen om niks te gaan doen")
        while True:
            vraag7 = input("ga je A naar school B werken of C niks doen: ").lower()
            if vraag7 == "a":
                print("je gaat naar de middelbare school je leer goed de Nederlandse taal")
                break
            elif vraag7 == "b":
                print("je gaat werken bij een winkel je verdient niet veel maar het is genoeg on me in leven te houden")
                break
            elif vraag7 == "c":
                print("je hebt gekozen om niks te gaan doen in Nederland na 21 jaar land niks te doen en zwerver zijn vries je dood in de kou")
                break
            else:
                print("je moet met A, B of C antwoorden")
    return vraag7

def watdoeneng():
    vliegtuignietbetaald = 0
    time.sleep(2)
    print("je bent nu in Engeland en moet kiezen wat je gaat doen met je toekomst")
    if vliegtuigkost == 1:
        time.sleep(2)
        print("je moet nog je schuld van het vliegtuig terug betalen")
        while True:
            vraag6 = input("ga A voor het geld werken of B niks doen: ").lower()
            if vraag6 == "a":
                time.sleep(2)
                print("je gaat voor het geld werken en hebt je schuld terug betaald")
                break
            elif vraag6 == "b":
                vliegtuignietbetaald = 1
                time.sleep(2)
                print("je gaat niet werken om je schuld aftebetalen")
                time.sleep(2)
                print("omdat je je schuld niet hebt afbetaald ga je naar de gevangenis na dat je uit de gevangenis komt probeer je werk te vinden alleen niemand neemt je aan omdat je een staf blad hebt")
                time.sleep(2)
                print("een paar maanden later tijdens de winter vries je dood onder een brug")
                break
            else:
                print("je moet met A, B of C antwoorden")
    if vliegtuignietbetaald == 0:
        print("nu je in Engeland bent moet je gaan denken aan je toekomst wat ga je doen")
        time.sleep(2)
        print("je hebt de keuze om naar school te gaan of om te gaan werken je kan ook kiezen om niks te gaan doen")
        while True:
            vraag7 = input("ga je A naar school B werken of C niks doen: ").lower()
            if vraag7 == "a":
                print("je gaat naar de middelbare school je leer goed de Engelse taal")
                break
            elif vraag7 == "b":
                print("je gaat werken bij een winkel je verdient niet veel maar het is genoeg on me in leven te houden")
                break
            elif vraag7 == "c":
                print("je hebt gekozen om niks te gaan doen in Engeland na 21 jaar land niks te doen en zwerver zijn vries je dood in de kou")
                break
            else:
                print("je moet met A, B of C antwoorden")
    return vraag7

def watdoendui():
    vliegtuignietbetaald = 0
    time.sleep(2)
    print("je bent nu in Duitsland en moet kiezen wat je gaat doen met je toekomst")
    if vliegtuigkost == 1:
        time.sleep(2)
        print("je moet nog je schuld van het vliegtuig terug betalen")
        while True:
            vraag6 = input("ga A voor het geld werken of B niks doen: ").lower()
            if vraag6 == "a":
                time.sleep(2)
                print("je gaat voor het geld werken en hebt je schuld terug betaald")
                break
            elif vraag6 == "b":
                vliegtuignietbetaald = 1
                time.sleep(2)
                print("je gaat niet werken om je schuld aftebetalen")
                time.sleep(2)
                print("omdat je je schuld niet hebt afbetaald ga je naar de gevangenis na dat je uit de gevangenis komt probeer je werk te vinden alleen niemand neemt je aan omdat je een staf blad hebt")
                time.sleep(2)
                print("een paar maanden later tijdens de winter vries je dood onder een brug")
                break
            else:
                print("je moet met A, B of C antwoorden")
    if vliegtuignietbetaald == 0:
        print("nu je in Duitsland bent moet je gaan denken aan je toekomst wat ga je doen")
        time.sleep(2)
        print("je hebt de keuze om naar school te gaan of om te gaan werken je kan ook kiezen om niks te gaan doen")
        while True:
            vraag7 = input("ga je A naar school B werken of C niks doen: ").lower()
            if vraag7 == "a":
                print("je gaat naar de middelbare school je leer goed de Duitse taal")
                break
            elif vraag7 == "b":
                print("je gaat werken bij een winkel je verdient niet veel maar het is genoeg on me in leven te houden")
                break
            elif vraag7 == "c":
                print("je hebt gekozen om niks te gaan doen in Duitsland na 21 jaar land niks te doen en zwerver zijn vries je dood in de kou")
                break
            else:
                print("je moet met A, B of C antwoorden")
    return vraag7

def schoolned():
    print("je bent naar school gegaan in Nederland je kan goed Nederlands praten nu ga je nu nog verder studeren of ga je werken?")
    while True:
        vraag8 = input("ga ja A verder studeren of B werken: ").lower()
        if vraag8 == "a":
            print("je gaat studeren voor doktor na 6 jaar studeren krijg je een baan als doktor")
            time.sleep(2)
            print("op je 70ste ga je met pensioen en op je 87ste ga je dood in het ziekenhuis gelukkig en met familie naast je")
            break
        elif vraag8 == "b":
            print("je gaat werken je verdient niet veel omdat je alleen naar de middelbare school bent gegaan")
            time.sleep(2)
            print("op je 70ste ga je met pensioen en op je 78ste ga je dood in het ziekenhuis je was niet de rijskte maar je gaat gelukkig en met familie naast je dood")
            break
        else: 
            print("je moet met A of B antwoorden")
    return vraag8

def schooleng():
    print("je bent naar school gegaan in Engeland je kan goed Engels praten nu ga je nu nog verder studeren of ga je werken?")
    while True:
        vraag8 = input("ga ja A verder studeren of B werken: ").lower()
        if vraag8 == "a":
            print("je gaat studeren voor doktor na 6 jaar studeren krijg je een baan als doktor")
            time.sleep(2)
            print("op je 70ste ga je met pensioen en op je 87ste ga je dood in het ziekenhuis gelukkig en met familie naast je")
            break
        elif vraag8 == "b":
            print("je gaat werken je verdient niet veel omdat je alleen naar de middelbare school bent gegaan")
            time.sleep(2)
            print("op je 70ste ga je met pensioen en op je 78ste ga je dood in het ziekenhuis je was niet de rijskte maar je gaat gelukkig en met familie naast je dood")
            break
        else: 
            print("je moet met A of B antwoorden")
    return vraag8

def schooldui():
    print("je bent naar school gegaan in Duitsland je kan goed Duits praten nu ga je nu nog verder studeren of ga je werken?")
    while True:
        vraag8 = input("ga ja A verder studeren of B werken: ").lower()
        if vraag8 == "a":
            print("je gaat studeren voor doktor na 6 jaar studeren krijg je een baan als doktor")
            time.sleep(2)
            print("op je 70ste ga je met pensioen en op je 87ste ga je dood in het ziekenhuis gelukkig en met familie naast je")
            break
        elif vraag8 == "b":
            print("je gaat werken je verdient niet veel omdat je alleen naar de middelbare school bent gegaan")
            time.sleep(2)
            print("op je 70ste ga je met pensioen en op je 78ste ga je dood in het ziekenhuis je was niet de rijskte maar je gaat gelukkig en met familie naast je dood")
            break
        else: 
            print("je moet met A of B antwoorden")
    return vraag8

def werken():
    time.sleep(2)
    print("je gaat werken maar omdat je geen goed onderwijs heb gehad verdien je niet veel")
    time.sleep(2)
    print("op je 70ste ga je met pensioen en op je 78ste ga je dood in het ziekenhuis je was niet de rijskte maar je gaat gelukkig en met familie naast je dood")

#vragen in land
if dood == 1:
    print("je bent dood")
else:
    if nederland == 1:
        watned = watdoenned()
        if watned == "a":
            #naar school nederland
            schoolned()
        elif watned == "b":
            werken()
    elif engeland == 1:
        wateng = watdoeneng()
        if wateng == "a":
            #naar school engeland
            schooleng()
        elif wateng == "b":
            werken()
    elif duitsland == 1:
        watdui = watdoendui()
        if watdui == "a":
            #naar school duitsland
            schooldui()
        elif watdui == "b":
            werken()

klaar = input("")