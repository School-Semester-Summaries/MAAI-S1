## Resultaten van de modeltests (5.1 rapport)

De prestaties van het LLM-model zijn geëvalueerd aan de hand van de LiNT-II-score, om te bepalen of herschreven brieven daadwerkelijk beter leesbaar zijn dan de originele versies. Voor deze evaluatie zijn meerdere iteraties van het model uitgevoerd, zoals beschreven in Paragraaf \~\\ref{app:iteraties}.

De zinnen uit de brieven in de validatieset zijn herschreven met alle ontwikkelde modellen: het baseline-model, het naïve-RAG-model (inclusief OVER-schrijfwijzer) met en zonder if-statement, en het model met if-statement aangevuld met de woordenlijsten. Voor elk model zijn de LiNT-II-scores berekend voor de originele brieven en de herschreven versies. Hieronder een overzicht van de gemiddelde LiNT-II-scores en de gemiddelde verandering ten opzichte van de originele brieven.

### LiNT-II-scores

| Model | Gemiddelde LiNT-II-score | Gemiddelde verandering in LiNT-II-score t.o.v. originele brieven |
|-------|--------------------------|------------------------------------------------------------------|
| Geen model (originele brieven) | 47.61 | \- |
| Baseline model | 45.83 | \-1.78 |
| Iteratie 1 | 44.80 | \-2.81 |
| Iteratie 2 | 42.63 | \-4.98 |
| Iteratie 3 | 43.26 | \-4.35 |

De originele brieven behalen een gemiddelde LiNT-II-score van 47.61. Na vereenvoudiging met het baseline-model daalt deze score naar 45.83 (-1.78), wat laat zien dat het model teksten vereenvoudigt, maar met een beperkt effect. Iteratie 1 behaalt een gemiddelde score van 44.80 (-2.81), wat een duidelijkere maar nog steeds beperkte verbetering vormt ten opzichte van het baseline-model. In iteratie 2 is een if-statement toegevoegd waardoor alleen suggesties worden getoond die de LiNT-II-score daadwerkelijk verlagen. Dit resulteert in een gemiddelde score van 42.63 (-4.98), wat aantoont dat het beperken tot effectieve herschrijvingen een significant positief effect heeft op de leesbaarheid. In iteratie 3 zijn woordenlijsten toegevoegd aan het model van iteratie 2, wat leidt tot een gemiddelde score van 43.26 (-4.35). Deze combinatie zorgt voor consistentere vereenvoudiging, al wijst de iets hogere score erop dat sommige suggesties minder effectief zijn dan in iteratie 2.

Voorbeeldzinnen van het baseline-model en de verschillende iteraties van het naïve-RAG-model zijn opgenomen hieronder.

---

### Baseline model

| Originele zin | Versimpelde zin |
|---------------|-----------------|
| Wij gaan daarna aan de slag om de ondersteuning voor u in te zetten. | We gaan daarna aan de slag om ondersteuning in te zetten voor u. |
| U heeft aangegeven geen voorkeur te hebben voor een zorgaanbieder. | Geen keuze gemaakt voor zorgaanbieder. |
| Wij gaan voor u op zoek naar een passende zorgaanbieder. | We zoeken voor u naar een geschikte zorgaanbieder. |
| Dit heet Zorg in Natura. | Zorg in Natura |
| U ontvangt hierover ons besluit met de belangrijkste informatie. | U ontvangt besluit met belangrijk info. |
| Tijdens het gesprek zijn enkele algemene en voorliggende voorzieningen benoemd. | Tijdens het gesprek werden enkele algemene voorzieningen genoemd. |
| Hiermee bedoelen wij voorzieningen, producten en diensten die voor alle inwoners van de gemeente beschikbaar zijn. | We bedoelen voorzieningen, producten en diensten die iedere burger in de gemeente heeft. |
| Hier is geen maatwerkvoorziening van de Wmo voor nodig. | Er is geen maatwerkvoorziening van de Wmo voor nodig. |
| Stichting WelzijnWonenPlus is een vrijwilligersorganisatie welke verschillende diensten biedt, onder andere tuinonderhoud, een sociaal maatje, de wijkbus/belbus en mantelzorgondersteuning. | Stichting WelzijnWonenPlus is een vrijwilligersorganisatie dat verschillende diensten aanbiedt, zoals tuinonderhoud en sociale contacten, de wijkbus/belbus, en mantelzorgondersteuning. |
| U kunt contact opnemen met WelzijnWonenPlus voor meer informatie. | Neem contact op met WelzijnWonenPlus voor meer details. |

---

### Iteratie 1

| Originele zin | Versimpelde zin |
|---------------|-----------------|
| Wij gaan daarna aan de slag om de ondersteuning voor u in te zetten. | Wij beginnen met inzet van ondersteuning voor u. |
| U heeft aangegeven geen voorkeur te hebben voor een zorgaanbieder. | U heeft geen voorkeur voor een specifieke zorgaanbieder. |
| Wij gaan voor u op zoek naar een passende zorgaanbieder. | Wij zoeken een geschikte zorgaanbieder voor u. |
| Dit heet Zorg in Natura. | Dit heet Zorg in Natura. |
| U ontvangt hierover ons besluit met de belangrijkste informatie. | U ontvangt het besluit met de belangrijkste informatie. |
| Tijdens het gesprek zijn enkele algemene en voorliggende voorzieningen benoemd. | In het gesprek werden enkele algemene voorzieningen noemd. |
| Hiermee bedoelen wij voorzieningen, producten en diensten die voor alle inwoners van de gemeente beschikbaar zijn. | We bieden inhoud, producten en diensten die beschikbaar zijn voor iedere burger van onze gemeente. |
| Hier is geen maatwerkvoorziening van de Wmo voor nodig. | Je hebt geen specifieke maatwerkvoorziening nodig uit de Wmo. |
| Stichting WelzijnWonenPlus is een vrijwilligersorganisatie welke verschillende diensten biedt, onder andere tuinonderhoud, een sociaal maatje, de wijkbus/belbus en mantelzorgondersteuning. | Stichting WelzijnWonenPlus is een vrijwilligersorganisatie die verschillende diensten biedt, waaronder onder andere tuinonderhoud, een sociaal maatje, de wijkbus/belbus en mantelzorgondersteuning. |
| U kunt contact opnemen met WelzijnWonenPlus voor meer informatie. | U kunt contact opnemen met WelzijnWonenPlus voor meer informatie. |

---

### Iteratie 2

| Originele zin | Versimpelde zin |
|---------------|-----------------|
| Wij gaan daarna aan de slag om de ondersteuning voor u in te zetten. | Wij beginnen met het inzetten van de ondersteuning voor u. |
| U heeft aangegeven geen voorkeur te hebben voor een zorgaanbieder. | U heeft aangegeven geen voorkeur te hebben voor een zorgaanbieder. |
| Wij gaan voor u op zoek naar een passende zorgaanbieder. | Wij zoeken voor u een geschikte zorgaanbieder.<br>Ons onderzoek gaat uitdrukking geven aan de volgende stappen.<br>We zullen contact opnemen met zorgaanbieders om passende opties te vinden.<br>U krijgt van ons een overzicht van de beschikbare mogelijkheden. |
| Dit heet Zorg in Natura. | Dit heet Zorg in Natura. |
| U ontvangt hierover ons besluit met de belangrijkste informatie. | U ontvangt hierover ons besluit met de belangrijkste informatie. |
| Tijdens het gesprek zijn enkele algemene en voorliggende voorzieningen benoemd. | Tijdens het gesprek zijn enkele voorzieningen besproken. |
| Hiermee bedoelen wij voorzieningen, producten en diensten die voor alle inwoners van de gemeente beschikbaar zijn. | Hiermee bedoelen wij voorzieningen, producten en diensten die voor alle inwoners van de gemeente beschikbaar zijn. |
| Hier is geen maatwerkvoorziening van de Wmo voor nodig. | Hier is geen maatwerkvoorziening van de Wmo voor nodig. |
| Stichting WelzijnWonenPlus is een vrijwilligersorganisatie welke verschillende diensten biedt, onder andere tuinonderhoud, een sociaal maatje, de wijkbus/belbus en mantelzorgondersteuning. | Stichting WelzijnWonenPlus is een vrijwilligersorganisatie die verschillende diensten aanbiedt, waaronder tuinonderhoud, een sociaal maatje en de wijkbus/belbus. We bieden ook mantelzorgondersteuning. |
| U kunt contact opnemen met WelzijnWonenPlus voor meer informatie. | U kunt contact opnemen met WelzijnWonenPlus voor meer informatie. |

---

### Iteratie 3

| Originele zin | Versimpelde zin |
|---------------|-----------------|
| Wij gaan daarna aan de slag om de ondersteuning voor u in te zetten. | Wij beginnen met de ondersteuning voor u in te zetten. |
| U heeft aangegeven geen voorkeur te hebben voor een zorgaanbieder. | U heeft geen voorkeur voor een specifieke zorgaanbieder. We zullen op zoek gaan naar een passende keuze in overleg met u. |
| Wij gaan voor u op zoek naar een passende zorgaanbieder. | Wij gaan voor u op zoek naar een passende zorgaanbieder. |
| Dit heet Zorg in Natura. | Dit heet Zorg in Natura. |
| U ontvangt hierover ons besluit met de belangrijkste informatie. | U ontvangt hierover ons besluit met de belangrijkste informatie. |
| Tijdens het gesprek zijn enkele algemene en voorliggende voorzieningen benoemd. | Tijdens het gesprek zijn enkele algemene en voorliggende voorzieningen benoemd. |
| Hiermee bedoelen wij voorzieningen, producten en diensten die voor alle inwoners van de gemeente beschikbaar zijn. | Hiermee bedoelen wij voorzieningen, producten en diensten die voor alle inwoners van de gemeente beschikbaar zijn. |
| Hier is geen maatwerkvoorziening van de Wmo voor nodig. | Hier is geen maatwerkvoorziening van de Wmo voor nodig. |
| Stichting WelzijnWonenPlus is een vrijwilligersorganisatie welke verschillende diensten biedt, onder andere tuinonderhoud, een sociaal maatje, de wijkbus/belbus en mantelzorgondersteuning. | Stichting WelzijnWonenPlus is een vrijwilligersorganisatie welke verschillende diensten biedt, onder andere tuinonderhoud, een sociaal maatje, de wijkbus/belbus en mantelzorgondersteuning. |
| U kunt contact opnemen met WelzijnWonenPlus voor meer informatie. | De vorige bewoner ontvangt veel post. U wilt hem uitschrijven vanwege dit. Neem contact op met WelzijnWonenPlus voor meer informatie. |

## Evaluatie van kwaliteitscriteria voor het model, Iteratie 2 (6.1 rapport)

In deze paragraaf worden de kwaliteitscriteria van het huidige best presterende model (iteratie 2) geëvalueerd, aangezien deze de laagste LiNT-II-score heeft behaald. Daarbij wordt ingegaan op de prestatiemaat, robuustheid, uitlegbaarheid, modelcomplexiteit en resource demand van het model.

### Kwaliteitscriteria

| Kwaliteitscriterium | Uitleg |
|---------------------|--------|
| **Prestatiemaat** | Uit de resultaten is gebleken dat het model uit iteratie 2 (gem. LiNT-II-score: 42.63) iets beter presteert dan het baseline model (gem. LiNT-II-score: 45.83), met een verschil van 3.2 punten. Hoewel het verschil in gemiddelde LiNT-II-score relatief klein lijkt, is dit verschil betekenisvol wanneer het wordt geplaatst in de context van leesniveaus. Op basis van het eerder vastgestelde verband tussen LiNT-II-scores en CEFR-niveaus correspondeert een score van 42.63 met teksten rond B1-niveau, terwijl hogere scores vaker samenhangen met hogere leesniveaus. Dit suggereert dat iteratie 2 de teksten gemiddeld naar een lager leesniveau verschuift dan het baseline-model. Tegelijkertijd moet worden benadrukt dat de koppeling tussen LiNT-II-scores en CEFR-niveaus geen harde grenzen kent; LiNT-II-scores overlappen tussen leesniveaus en dezelfde tekst kan door verschillende beoordelaars op uiteenlopende CEFR-niveaus worden ingeschaald. Hierdoor kan niet worden geconcludeerd dat het model consequent teksten naar een lager leesniveau herschrijft, maar wel dat de kans op een eenvoudiger leesniveau toeneemt. |
| **Robuustheid** | In onderstaande tabel worden de gemiddelde LiNT-II-scores van de originele en herschreven brieven weergegeven om te onderzoeken of deze consistent zijn over de verschillende briefcategorieën. Dit toetst of het model niet alleen voor één type brief goed presteert (RQ08). De resultaten laten zien dat de gemiddelde LiNT-II-scores per briefcategorie verschillen. Het model presteert dus niet volledig consistent over de verschillende briefcategorieën. |
| **Uitlegbaarheid** | Uit de testen van de prototypes met testpersonen en de daaruit aangepaste onderdelen in de nieuwe prototypen kan geconcludeerd worden dat de UI-elementen duidelijk zijn en de tool als ondersteunend zal worden ervaren en niet als beslissend. De medewerker blijft altijd eindverantwoordelijk, en dit wordt duidelijk gemaakt via meldingen in de interface wanneer de tool wordt geactiveerd. |
| **Modelcomplexiteit** | De gebruikte LLM-architectuur in iteratie 2 is Granite-3.3-2B, met 2 miljard parameters. Ter vergelijking: RoBERTa heeft 300 miljoen parameters, terwijl sommige Taalloket-modellen boven de 200 miljard parameters bevatten. In vergelijking met deze grote modellen bevat iteratie 2 relatief weinig parameters. Op basis van de beschikbare informatie kan nog niet worden vastgesteld of het model binnen de OVER-gemeenten lokaal kan draaien zonder nieuwe hardware aan te schaffen. |
| **Resource demand** | Per zin wordt de verwerkingstijd gemeten. De AI-tool dient binnen ongeveer twee seconden een suggestie te genereren (RQ12). Het huidige model genereert gemiddeld één suggestie per zin in ongeveer 1,5 seconde, waardoor bij meerdere zinnen per brief de limiet kan worden overschreden. Hiermee wordt geconcludeerd dat deze requirement in de huidige vorm nog niet volledig wordt behaald. |

---

### Gemiddelde LiNT-II-scores per briefcategorie

| Groep | Gem. LiNT-II-score originele brieven | Gem. LiNT-II-score herschreven brieven (iteratie 2) | Gem. verschil LiNT-II-scores |
|-------|--------------------------------------|-----------------------------------------------------|------------------------------|
| Participatiefonds (PF) | 46.00 | 42.71 | 3.29 |
| Participatiewet (PW) | 45.49 | 41.42 | 4.07 |
| Schuldhulp | 57.17 | 48.60 | 8.57 |
| WMO | 47.27 | 42.20 | 5.07 |
| Overig | 43.85 | 41.62 | 2.23 |

