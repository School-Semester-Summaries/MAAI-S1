Om meer inzicht te krijgen in de huidige situatie en context van de OVER-gemeenten konden alle projectgroepen tot **6 januari** vragen indienen. De docenten selecteerden vervolgens de vragen om doublures te voorkomen. Medewerkers van de OVER-gemeenten hebben deze vragen beantwoord. De antwoorden zijn hieronder te vinden.

* **Q1: Vinden jullie het goed als deze woordenlijsten worden toegepast in de toepassing voor het herschrijven van de gemeentelijke brieven?**
  * **Juridisch jargon:**\
    https://www.amsterdam.nl/schrijfwijzer/heldere-taal-basis-onze-huisstijl/helder-juridisch-schrijven
  * **Synoniemen woordenlijst:**\
    https://b1teksten.nl/artikel/voorbeelden-van-b1-teksten\ https://site.dijkenwaard.nl/huisstijl/heldere-taal/direct-duidelijk-dijken-waard/taalniveau-b1
  * **Moeilijke woorden:**\
    https://www.amsterdam.nl/schrijfwijzer/moeilijke-woorden
  * **Inclusieve lijst:**\
    https://www.amsterdam.nl/schrijfwijzer/inclusieve-taal-richtlijnen-tips/inclusieve-woordenlijst/

  Bedoelen jullie hiermee dat het jargon uit deze woordenlijsten wordt goedgekeurd en dus niet als suggestie wordt aangegeven om te verbeteren naar B1? Als dat het geval is, dan zou ik zeggen: nee, liever niet.

  Deze woordenlijsten zijn erg uitgebreid en een hoop kan zeker aangepast worden naar B1.

  Het is fijner als wij zelf de mogelijkheid hebben om in de AI-tool woorden toe te voegen die hij moet “negeren”. Dit kan namelijk ook per afdeling verschillen in verband met vaktermen. Als we al deze woorden zouden toevoegen en accepteren, blijft er naar mijn idee te veel moeilijke taal in staan.

  Mocht je deze websites echter willen gebruiken om woorden om te zetten naar B1 of synoniemen, dan hebben we het liefst dat je gebruikmaakt van het advies van Stichting Lezen en Schrijven. Zij adviseren de volgende websites:
  * Eenvoudige taal
  * Wil je weten of een woord op B1-niveau is? Gebruik: https://www.ishetb1.nl
  * Zoek eenvoudige woorden op taalniveau A2 en B1 via: https://www.zoekeenvoudigewoorden.nl
* **Q2: Welke specificaties heeft de server waarop het model kan runnen? (Dan weten wij hoe zwaar het model kan worden)**
  * OVG heeft geen vooraf vastgestelde AI-server specificaties, maar:
    * Het moet een Windows Server 2019 of hoger zijn
    * Deze moet virtueel gehost kunnen worden
    * Deze moet voorzien kunnen worden van policies ten behoeve van security
    * Deze moet M365 Copilot kunnen draaien
  * OVG heeft aangegeven dat een Word-plugin en/of in combinatie met een Copilot Agent de voorkeur heeft boven een dedicated server.
  * Het lijkt zinvoller om eerst een model neer te zetten, waarna aan OVG wordt aangegeven wat de specificaties voor een server zouden moeten zijn om dat model efficiënt te laten draaien (dus omgekeerd).
  * Daarnaast is het niet gezegd dat OVG per definitie akkoord gaat met een dedicated server:
    * Een AI-server moet een zinvolle en aantoonbare kosten-batenanalyse hebben (kosten niet ten laste van het ICT-budget).
    * Een voorstel voor een AI-server zal worden beoordeeld op de criteria van BIO2, Common Ground (VNG) en gemeentelijke architectuurprincipes en security-overwegingen, waarbij de CISO een kritieke rol heeft.
* **Q3: Welke fouten in een tekst vindt u zo ernstig dat deze altijd moeten leiden tot een lage beoordeling volgens de schrijfwijzer?**\
  _(Denk bijvoorbeeld aan te lange zinnen, een onjuiste lay-out of onnodig moeilijke formuleringen.)_
  * Te lange zinnen
  * Geen of weinig alinea’s
  * Geen kernkopzinnen
  * Onnodig moeilijke formulering
  * Spel- en grammaticafouten
* **Q4: Wat moet de schrijfcoach strenger beoordelen: zinnen die al duidelijk en eenvoudig zijn maar ten onrechte als ‘te complex’ worden aangemerkt, of zinnen die eigenlijk ingewikkeld zijn maar door de schrijfcoach als ‘eenvoudig genoeg’ worden gezien?**

  Zinnen die eigenlijk ingewikkeld zijn, maar door de schrijfcoach als eenvoudig genoeg worden gezien.
* **Q5: Wanneer zou u vertrouwen hebben in het oordeel van een AI-schrijfcoach die beoordeelt of het voldoet aan de schrijfwijzer?**

  Als ik tips krijg waar ik mij in herken, en die mij helpen mijzelf en mijn teksten te verbeteren. Als zowel ik als de AI-schrijfcoach van elkaar kunnen leren, om zo veel voorkomende “fouten” te voorkomen van beide kanten.
* **Q6: De AI-schrijfcoach geeft een cijfer als beoordeling. Wat maakt een tekst volgens u een 10 en wat een 6?**

  Een dikke 10 als alles volgens de schrijfwijzer is (duidelijke tekst, kernkopzinnen, alle details volgens de richtlijnen, geen spel- of grammaticafouten).

  Een 6 wanneer de brief geen spel- of grammaticafouten heeft, maar nog wel ingewikkeldere taal gebruikt.
* **Q7: Welke juridische termen mogen niet worden herschreven?**

  Daar kan ik zo geen antwoord op geven. Er zou misschien een waarschuwing kunnen komen dat deze tekst niet voldoet aan B1, om een bepaalde reden, en dat het aan de schrijver is om in te schatten of dit wel of niet onvermijdelijk is.

  Handig zou zijn als we zelf de optie hebben om deze termen te kunnen toevoegen. Bijvoorbeeld: bij Word kun je ook woorden toevoegen aan de woordenlijst of ervoor kiezen een woord te negeren.
* **Q8: Hoe vaak komt het voor dat er data van de bewoner lopend of per ongeluk in de brief terechtkomt?**

  Dit zijn incidenten. Vaak wordt vanuit een systeem gewerkt en niet vanuit standaardbrieven; wij proberen dit te voorkomen. Wel staan standaard de NAW-gegevens in de brieven die gemaakt worden vanuit de systemen waarmee we werken.

  De brief wordt automatisch gegenereerd vanuit het systeem in Word. Hier passen we vervolgens de inhoud van de brief aan.
* **Q9: Hoe belangrijk is de herkomst van de dataset waarop getraind is?**

  Ik begrijp de vraag niet helemaal; voor de volledigheid geef ik onze kaders aan:
  * OVG werkt met M365 Copilot en niet met andere AI’s zoals ChatGPT, Perplexity, enz.
  * De LLM van M365 Copilot mag gebruikt worden, maar de data mag **niet** gebruikt worden door de LLM.
  * De herkomst van de dataset moet volledig transparant en duidelijk zijn.
  * Als er data naar een dataset wordt gestuurd, is er zeer waarschijnlijk een verwerkersovereenkomst nodig en mogelijk zelfs een DPIA.