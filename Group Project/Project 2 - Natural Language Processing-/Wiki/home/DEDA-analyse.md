Tijdens de literatuurles op 4 december is de DEDA-tool gebruikt om te reflecteren op de ethische vraagstukken die spelen bij de ontwikkeling van de AI-tool voor de OVER-gemeente. Deze tool bestaat uit vier fasen waarin verschillende vragen worden beantwoord.

## **Fase één**

1. **Projectnaam en datum:**\
   AI als schrijfassistent voor heldere gemeentelijke brieven, gebaseerd op B1-niveau Nederlands, 4 december 2025.
2. **Projectteam:**\
   Team 2.
3. **Wat houdt het project in en wat is het doel?:**\
   Gemeentelijke brieven van de OVER-gemeenten worden herschreven volgens de schrijfwijzer, met als doel deze begrijpelijk te maken op B1-niveau.
4. **Wat zijn de eventuele maatregelen of acties op basis van de uitkomsten van dit project?:**\
   Wanneer het project succesvol verloopt, worden brieven eenvoudiger geschreven. Dit draagt bij aan betere begrijpelijkheid voor burgers en vergroot de kans dat de inhoud daadwerkelijk wordt begrepen.
5. **Wat voor data gebruikt u? Geef een korte beschrijving van de inhoud hiervan.:**\
   De volgende databronnen worden gebruikt:
   * Brieven van de gemeente Oostzaan
   * De schrijfwijzer van de OVER-gemeenten
   * Een inclusiviteitswoordenlijst
   * Een lijst met moeilijke woorden (Gemeente Amsterdam)
6. **Wie zijn de stakeholders van dit project en op wie/wat heeft het impact?**\
   Dit zijn de stakeholders van het project:
   * De ICT-afdeling
   * Medewerkers die brieven schrijven en controleren
   * De OVER-gemeente
   * Inwoners van de OVER-gemeente
   * De overheid

   Het project heeft impact op alle stakeholders, maar vooral op de medewerkers van de OVER-gemeenten zullen te maken krijgen met de AI-tool. De burgers zullen hierdoor hopelijk de brieven beter begrijpen. (Paragraaf 2.2)
7. **Wat zijn de nagestreefde voordelen van dit project?**
   * Consistenter en begrijpelijker schrijven van gemeentelijke brieven, waardoor er minder misverstanden en problemen ontstaan zoals beschreven in Paragraaf 1.2.
8. **Zijn er (mogelijke) problemen met het project?**
   * Het beoordelen van B1-niveau is deels subjectief
   * Onjuiste suggesties kunnen leiden tot betekenisverlies of verkeerd woordgebruik
   * Privacygevoelige gegevens mogen de gemeente niet verlaten en mogen niet worden gebruikt voor het trainen van het model
9. **Welke van de onderstaande onderwerpen (algoritmen, bron, anonimiseren etc.) zijn van toepassing op uw project? Beslis welke er eventueel tijdens de workshop kunnen worden overgeslagen.**\
   De volgende vragen worden tijdens de workshop overgeslagen:
   * Vraag 41
   * Vraag 42

---

## **Fase twee**

Bij de start van de analyse is vastgesteld dat de volgende waarden belangrijk zijn voor de OVER-gemeente bij de ontwikkeling en inzet van de AI-tool:

* **Privacy:** Privacy is essentieel, omdat persoonsgegevens van inwoners niet buiten de organisatie mogen worden verwerkt of gedeeld.
* **Menselijke eindverantwoordelijkheid:** Medewerkers van de gemeente vinden het belangrijk dat de mens eindverantwoordelijk blijft voor de output van de AI-tool (Bijlage \\ref{app:informatiegemeenteoostzaan}).
* **Gebruiksvriendelijkheid:** De AI-tool moet zo worden ontworpen dat deze daadwerkelijk consistent in de praktijk gebruikt kan worden, in tegenstelling tot de huidige schrijfwijzer die als lastig in gebruik wordt ervaren.
* **Inclusiviteit:** In de schrijfwijzer staat dat teksten bedoeld zijn voor alle inwoners en dat het belangrijk is dat iedereen zich betrokken voelt. Daarom moet de AI-tool inclusief taalgebruik ondersteunen en bevorderen.

---

## **Fase drie**

In deze fase worden vragen beantwoord met betrekking tot datagerelateerde overwegingen en algemene overwegingen.

### **Datagerelateerde overwegingen**

10. **Gebruikt u een algoritme in uw project?**
    * Ja
11. **Hoe gaat u om met false positives en false negatives?**
    * De medewerker is eindverantwoordelijk en keurt suggesties zelf.
12. **Is er iemand in het team die kan uitleggen hoe het gebruikte algoritme werkt? Is het noodzakelijk dat iemand kan uitleggen wat het doet?**
    * Ja, eenvoudig kunnen uitleggen is noodzakelijk.
13. **Gebruikt u de uitkomsten van het model als leidend of aanvullend in uw beslissingsmodel?**
    * Nee, alleen aanvullend.
14. **Is er menselijke controle op fouten die het algoritme kan maken? Hoeveel ruimte heeft een mens om van het systeem af te wijken wanneer nodig?**
    * Ja, medewerkers moeten de suggesties goed of afkeuren. De AI-tool vervangt niet meteen woorden die als 'foutief' worden gezien.
15. **Wat is de bron van de data?**
    * Gemeente Amsterdam
    * OVER-schrijfwijzer
    * Interne brieven van de OVER-gemeenten
16. **Heeft u de kwaliteit van de dataset(s) gecontroleerd?**
    * Ja, door twee personen (subjectief).
17. **Hebben de data een houdbaarheidsdatum?**
    * Nee, maar bijhouden is noodzakelijk, aangezien taal in de loop der jaren verandert.
18. **Verzamelt u de juiste informatie voor uw doel?**
    * Grotendeels, mogelijk aanvullende bronnen nodig.
19. **Is het nodig om de dataset(s) te anonimiseren, pseudonimiseren of te generaliseren?**
    * Alleen bij gebruik van echte brieven, wat in dit geval niet zo is. In de praktijk dus wel.
20. **In het geval van anonimiseren: is gecheckt of de data echt niet meer herleidbaar is?**
    * Dit is waarschijnlijk in de toekomst mogelijk, wanneer de tool geïmplementeerd wordt. Voor dit onderzoek is het in deze fase nog niet van toepassing.
21. **In het geval van pseudonimiseren: wie heeft de sleutel om de pseudonimisering terug te draaien?**
    * Dit is waarschijnlijk in de toekomst mogelijk, wanneer de tool geïmplementeerd wordt. Voor dit onderzoek is het in deze fase nog niet van toepassing.
22. **Hoe worden de uitkomsten van het project weergegeven? Worden deze gevisualiseerd?**
    * In een Word-extensie, zoals in het prototype is weergegeven.
23. **Wat zou een andere manier van visualiseren zijn?**
    * Dat de suggesties onder elkaar worden getoond is voorgesteld door testpersonen, maar omdat dit mogelijk leidt tot minder menselijke controle en een te groot vertrouwen in de tool (automation bias), passen we dit niet toe.
24. **Wie heeft toegang tot de dataset(s)?**
    * Iedereen heeft toegang tot de woordenlijsten, want deze zijn publiekelijk
    * De mensen die brieven schrijven, docenten van de master applied AI en studenten van deze master hebben toegang tot enkele brieven van de OVER-gemeente
    * Wanneer de applicatie echt gebruikt gaat worden, moet genoteerd worden hoe de data wordt opgeslagen en gebruikt
25. **Hoe wordt de toegang gemonitord?**
    * Wanneer de applicatie echt gebruikt gaat worden, moet later wel genoteerd worden hoe de data wordt opgeslagen en gebruikt.
26. **Zijn de resultaten geschikt om te worden hergebruikt? Zo ja, onder welke voorwaarden?**
    * Er zijn nog geen resultaten, maar de manier waarop de data gebruikt zal worden, wordt vastgelegd zodat hier in de toekomst rekening mee kan worden gehouden.
27. **Zijn (delen) van de (input)data geschikt om te worden hergebruikt? Zo ja, onder welke voorwaarden?**
    * Ja, want deze worden nu lokaal opgeslagen en de gebruikte instellingen ook. Echter moet de data in de toekomst misschien geüpdatet worden, vanwege bijvoorbeeld verandering in de samenleving over wanneer woorden worden gezien als inclusief.

### **Algemene overwegingen**

28. **Bestaan er binnen de organisatie beleid of richtlijnen die van toepassing zijn op dit project? Zo ja, welke?**
    * Nee, maar ze moeten zich houden aan algemene wetten en regelgeving, zoals artikel 50 en de AI-act.
29. **Wie is/zijn eindverantwoordelijk voor het project?**
    * De mensen die besluiten het systeem te implementeren (medewerkers van de gemeente).
30. **Zijn de verantwoordelijkheden van die persoon/personen helder?**
    * Nee, want die kent het systeem nog niet.
31. **Is dit project geschikt voor samenwerking met (commerciële) partners? Zo ja, welke partijen zouden dat kunnen zijn?**
    * Ja, niet met commerciële partijen, maar wel met andere gemeenten.
32. **Wat is de communicatiestrategie voor dit project? (Zowel voor de positieve als negatieve impact hiervan).**\
    In het geval van samenwerkingspartners: is deze strategie met hen afgestemd?
    * Ja, er is een communicatiestrategie voor dit project. Er zijn momenten afgesproken waarop vragen gesteld kunnen worden, zowel digitaal als in persoon. Daarnaast is op 1 december 2025 een prototype getest met medewerkers van de gemeente.
33. **Zijn er communicatiestrategieën voor het geval er iets mis gaat?**
    * Dat weten we niet, aangezien docenten als tussenpartij fungeren. Indien nodig kunnen wij zelf altijd nog contact zoeken.
    * Mogelijk moet aan de gemeente worden doorgegeven dat zij een communicatiestrategie opstellen voor het geval er iets misgaat, zodat er een duidelijk plan is voor hoe te handelen in zo’n situatie.
34. **Wie is er verantwoordelijk voor deze strategieën?**
    * De docenten van de opleiding applied AI
    * De communicatieafdeling en de mensen die het systeem maken (een ontwikkelteam)
35. **Bestaat het risico op publieke verontwaardiging, nu of in de toekomst?**
    * Ja, aangezien burgers zich kunnen afvragen of de inhoud van de brief wel correct is en of hun persoonlijke gegevens worden gebruikt in een AI-systeem.
36. **Hoe transparant bent u over uw project naar burgers toe?**
    * Hier hebben we nog geen conclusie over getrokken. Amber van Hassel doet hier onderzoek naar.
37. **Hoe worden burgers actief betrokken?**
    * Aan verschillende burgers worden vragen gesteld over wat zij ervan vinden dat de gemeente AI gebruikt bij het herschrijven van brieven en over hoe transparant de gemeente hierover moet zijn.
    * Ook worden medewerkers van de gemeente betrokken bij het ontwerpproces.
38. **Kunnen burgers bezwaar maken tegen uitkomsten van het project?**
    * Ja, burgers kunnen altijd klachten indienen. Zij worden geïnformeerd over de ontwikkeling van een AI-systeem dat brieven herschrijft. Daarnaast kunnen zij een klacht indienen als zij een brief niet begrijpen of het niet eens zijn met de inhoud.
39. **Is een opt-out mogelijk voor burgers? Zo ja, op welk moment kunnen burgers ervoor kiezen om deelname te beëindigen?**
    * Nee, deze is er niet. Wel wordt er tijdens het ontwikkelen van het systeem rekening gehouden met de privacyrechten van burgers, etc.
40. **Welke wetten, voorschriften en/of richtlijnen zijn van toepassing op uw project?**
    * Artikel 50, AI-act, etc. Zie requirements in het verslag.
41. **Heeft u de privacyfunctionaris en/of functionaris gegevensbescherming betrokken bij het project?**
    * Deze vraag slaan we over.
42. **Heeft u een DPIA (Data Protection Impact Assessment) gehanteerd?**
    * Deze vraag slaan we over.
43. **Wat is uw onderbuikgevoel over dit project? Heeft u zorgen?**\
    Er zijn verschillende onderbuikgevoelens gedeeld door Bibiëne Wüst, Kaan Göcay en Amir Jacobs.
    * Bibiëne Wüst is benieuwd of het model zich kan aanpassen naar het format van de brieven.
    * Amir Jacobs heeft zorgen over hoe het B1-niveau beoordeeld kan worden, aangezien dit subjectief lijkt om te beoordelen.
    * Kaan Göcay maakt zich zorgen over het project, omdat ongeveer 20 procent van de Nederlanders B1-niveau niet kan lezen en deze groep dus niet wordt bereikt.
44. **Bestaat het gevaar dat bepaalde mensen of groepen gediscrimineerd zouden kunnen worden door uw project?**
    * Ja, mensen die onder B1-niveau lezen, worden nog steeds niet bereikt. Dat ligt niet aan de uitvoering van het project, maar aan de eis die gesteld wordt door de overheid dat teksten op B1-niveau moeten zijn.
45. **Zijn alle verschillende groepen burgers vertegenwoordigd in de dataset(s)? Wie missen er of zijn niet zichtbaar?**
    * Ja, verschillende groepen burgers zijn vertegenwoordigd omdat er is gewerkt met een inclusiviteitslijst. Deze lijst zorgt ervoor dat rekening wordt gehouden met passende benamingen, zoals neutrale aanduidingen voor ouderen en het gebruik van “kinderen” in plaats van “jongens/meisjes”.
46. **Zit er een feedback loop in het model die negatieve consequenties kan hebben?**
    * Ja, er kan een feedbackloop ontstaan wanneer een medewerker een suggestie accepteert die in feite onjuist is. Als het model deze acceptaties gebruikt om verder te leren, kan het verkeerde patronen gaan overnemen. Dit risico wordt groter wanneer medewerkers te veel vertrouwen op de gegenereerde tekst en minder kritisch controleren. Daarom is het belangrijk dat datasets en modeluitvoer regelmatig worden beoordeeld en bijgewerkt door mensen om fouten en vertekening te voorkomen.
47. **Function creep: kunt u zich een toekomstig scenario voorstellen waarin de uitkomsten van dit project voor een ander doeleinde gebruikt worden?**
    * Ja, de uitkomsten van dit project kunnen ook gebruikt worden voor het versimpelen van brieven voor andere gemeenten.
48. **Veranderen uw antwoorden als u de mogelijke langetermijneffecten in acht neemt? Waarom?**
    * Ja, mijn antwoord verandert wanneer ik rekening houd met mogelijke langetermijneffecten. Taal verandert namelijk in de loop van de tijd. Het model zal daarom regelmatig moeten worden hertraind met bijgewerkte woordenlijsten en voorbeelden om relevant en bruikbaar te blijven.
49. **Wanneer wordt dit project geëvalueerd?**
    * Het project wordt geëvalueerd zodra de ontwikkelaars de vooraf vastgestelde doelen samen met de gemeente hebben behaald. Daarna kan het systeem worden ingevoerd bij de OVER-gemeenten, zodat medewerkers ermee kunnen testen. Tijdens de ontwikkeling wordt de AI-tool bovendien tussentijds beoordeeld aan de hand van verschillende kwaliteitscriteria.

---

## **Fase vier**

In deze fase wordt een conclusie gevormd aan de hand van antwoorden op een aantal vragen.

1. **Zijn de organisatiewaarden en persoonlijke waarden voldoende gewaarborgd?**
   * **Privacy:** Er wordt uitsluitend getraind met openbare, niet-privacygevoelige data. Brieven met privacygevoelige informatie worden alleen intern gebruikt. Vandaar dat de waarde privacy voldoende is gewaarborgd.
   * **Gebruiksvriendelijkheid:** Het systeem moet praktisch inzetbaar zijn en niet omslachtig in gebruik. Door het model te ontwikkelen als een Word-extensie wordt de gebruiksvriendelijkheid vergroot. Dit wordt geëvalueerd op basis van feedback van testgebruikers op het verbeterde prototype. Op deze manier kan deze waarde voldoende worden gewaarborgd.
   * **Menselijke eindverantwoordelijkheid:** In het ontwerp van de AI-tool is vastgelegd dat gemeentemedewerkers eindverantwoordelijk blijven voor de inhoud van hun brieven. De testpersonen hebben op 1 december 2025 bevestigd dat deze waarde in het prototype voldoende wordt gewaarborgd.
   * **Inclusiviteit:** De brieven moeten inclusief worden geschreven volgens de OVER-schrijfwijzer. Door een inclusieve woordenlijst van de Gemeente Amsterdam in het model te implementeren, wordt aan deze waarde voldaan.
2. **Wat zijn de belangrijkste ethische knelpunten?**
   * De belangrijkste ethische knelpunten zijn dat privacygevoelige informatie mogelijk wordt gebruikt bij het hertrainen van het model, wat risico’s oplevert voor gegevensbescherming. Daarnaast is er het risico dat een deel van de bevolking, ongeveer 20 procent van de Nederlanders, ook bij teksten op B1-niveau nog steeds niet goed wordt bereikt. Tot slot bestaat de kans dat gebruikers te veel vertrouwen op het systeem en suggesties klakkeloos accepteren, waardoor fouten onopgemerkt blijven en het model op basis van onjuiste input wordt hertraind.
3. **Wat zijn nieuwe en verrassende inzichten?**
   * Er is nog onvoldoende nagedacht over een mogelijke feedback-loop.
4. **Onder welke voorwaarden willen we wel of niet doorgaan met dit project?**
   * Wanneer medewerkers het systeem te veel vertrouwen, waardoor de inhoudelijke kwaliteit van brieven achteruitgaat.
5. **Bekijk alle actiepunten die hieronder worden weergegeven en schrijf voor elk punt de actiehouder op.**
   * De actiepunten worden verder uitgewerkt tijdens het schrijven van het verslag, met name in het hoofdstuk ‘Discussie’.