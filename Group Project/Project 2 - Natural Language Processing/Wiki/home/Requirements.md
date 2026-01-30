## MoSCoW-analyse

De MoSCoW-analyse is uitgevoerd op alle ethische, juridische, organisatorische, functionele en technische vereisten. M staat voor must have, S staat voor should have, C staat voor could have en W staat voor won't have. De nummers bij een requirement (RQ) staan voor het type requirement. ER = ethische requirement, JR = juridische requirement, OR = organisatorische requirement, FR = functionele requirement, TR = technische requirement en DR = duurzaamheids requirement.

Deze versie is gebruikt voor de eerste versie van het rapport, na de ontvangen feedback is de layout van deze requirement-lijst aangepast zoals te zien is in het eindverslag van blok 2.

### **Ethische requirements**

<table>
<tr>
<th>RQ-nr</th>
<th>Categorie</th>
<th>Requirement</th>
<th>MoSCoW</th>
<th>Stakeholder</th>
</tr>
<tr>
<td>ER01</td>
<td>Ethisch</td>
<td>

Gebruikers moeten weten hoe de AI-tool werkt, waarbij geen AI gelettertheid nodig is \[1\].
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>ER02</td>
<td>Ethisch</td>
<td>

Een woordsuggestie mag niet zonder toestemming van de medewerker worden toegevoegd (bijv. om bias en fouten van het LLM te voorkomen). Het systeem moet een human-in-the-loop hebben; de mens blijft eindverantwoordelijk en de AI-tool ondersteunt slechts \[1\].
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren
* Overheid
</td>
</tr>
<tr>
<td>ER03</td>
<td>Ethisch</td>
<td>

Medewerkers hebben de mogelijkheid om het gebruik van de AI-tool vrijwillig in- of uit te schakelen, zodat de inzet van AI passend blijft bij de taak, context en professionele verantwoordelijkheid van de medewerker \[1\].
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>ER04</td>
<td>Ethisch</td>
<td>

Om automation bias te voorkomen, moeten de beperkingen en capaciteiten van de AI-tool aan de stakeholders worden gemeld; bijvoorbeeld dat de tool slechts een hulpmiddel is en niet altijd de beste suggesties geeft \[1\].
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>ER05</td>
<td>Ethisch</td>
<td>

De AI-tool moet worden beveiligd tegen kwetsbaarheden (bijv. hacks of technische storingen) \[1\].
</td>
<td>S</td>
<td>

* ICT-afdeling
* Overheid
* Inwoners van OVER-gemeenten
</td>
</tr>
<tr>
<td>ER06</td>
<td>Ethisch</td>
<td>

De AI-tool moet een uitwijkplan hebben voor situaties met problemen zoals hacks of technische storingen \[1\].
</td>
<td>S</td>
<td>

* ICT-afdeling
* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>ER07</td>
<td>Ethisch</td>
<td>

De stakeholder moet worden geïnformeerd dat een AI-tool is gebruikt bij het schrijven van de brief \[1\].
</td>
<td>C</td>
<td>

* Inwoners van OVER-gemeenten
</td>
</tr>
<tr>
<td>ER08</td>
<td>Ethisch</td>
<td>

Na installatie van de AI-tool moet regelmatig feedback worden gevraagd aan belanghebbenden \[1\].
</td>
<td>W</td>
<td>

* Medewerkers die brieven schrijven/controleren
* Inwoners van OVER-gemeenten
</td>
</tr>
<tr>
<td>ER09</td>
<td>Ethisch</td>
<td>

De gevolgen van het systeem op sociaal gebied moeten onderzocht worden \[1\].
</td>
<td>W</td>
<td>

* Inwoners van OVER-gemeenten
* OVER-gemeenten
</td>
</tr>
</table>

### **Organisatorische requirements**

<table>
<tr>
<th>RQ-nr</th>
<th>Requirement</th>
<th>MoSCoW</th>
<th>Stakeholder</th>
</tr>
<tr>
<td>OR01</td>
<td>

De Gemeente Oostzaan moet het gebruik van AI verwerken in hun beleid. \[2\]
</td>
<td>W</td>
<td>

* OVER-gemeenten
</td>
</tr>
<tr>
<td>OR02</td>
<td>

De Gemeente moet periodieke evaluaties inplannen om te controleren of brieven correct worden geschreven. \[2\]
</td>
<td>W</td>
<td>

* OVER-gemeenten
</td>
</tr>
<tr>
<td>OR03</td>
<td>

De medewerkers moeten een training krijgen over hoe de AI-tool werkt voor het herschrijven van brieven. \[2\]
</td>
<td>W</td>
<td>

* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>OR04</td>
<td>

De gemeente moet een beleid opstellen waarin wordt vastgelegd wie de eindverantwoordelijke is voor beslissingen die met behulp van de AI-tool tot stand komen. \[2\]
</td>
<td>W</td>
<td>

* OVER-gemeenten
</td>
</tr>
<tr>
<td>OR05</td>
<td>

De gemeente moet duidelijk maken aan de medewerkers dat zij niet volledig moeten vertrouwen op de tekstsuggesties van de AI-tool. \[2\]
</td>
<td>W</td>
<td>

* OVER-gemeenten
* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>OR06</td>
<td>

De gemeente moet een feedbackmechanisme implementeren waarmee medewerkers suggesties over de AI-tool kunnen indienen. \[2\]
</td>
<td>W</td>
<td>

* OVER-gemeenten
* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>OR07</td>
<td>

De gemeente moet een risicoanalyse opstellen waarin wordt beschreven wat de risico’s zijn van de implementatie van de AI-tool bij het herschrijven van brieven. \[2\]
</td>
<td>W</td>
<td>

* OVER-gemeenten
* Medewerkers die brieven schrijven/controleren
</td>
</tr>
</table>

## **Juridische requirements**

<table>
<tr>
<th>RQ-nr</th>
<th>Requirement</th>
<th>MoSCoW</th>
<th>Stakeholder</th>
</tr>
<tr>
<td>JR01</td>
<td>

Persoonlijke informatie van burgers mag niet worden opgeslagen of gebruikt voor (verdere) training van het model. De trainingsdata bestaat uit anonieme brieven \[5\]\[8\].
</td>
<td>M</td>
<td>

* Inwoners van OVER-gemeenten
</td>
</tr>
<tr>
<td>JR02</td>
<td>

De AI-tool mag geen persoonsgegevens delen met externe partijen of servers \[13\]\[14\].
</td>
<td>M</td>
<td>

* Overheden/toezichthouders
* Inwoners van OVER-gemeenten
* OVER-gemeenten
</td>
</tr>
<tr>
<td>JR03</td>
<td>

De AI-tool mag alleen worden gebruikt voor het herschrijven van brieven voor inwoners van de gemeente en niet voor andere doeleinden \[3\]\[4\]\[5\].
</td>
<td>S</td>
<td>

* Overheden/toezichthouders
</td>
</tr>
<tr>
<td>JR04</td>
<td>

Er moet aangetoond kunnen worden waar de trainingsdata vandaan komt en dat er toestemming is voor gebruik hiervan \[4\]\[5\].
</td>
<td>S</td>
<td>

* Overheden/toezichthouders
</td>
</tr>
<tr>
<td>JR05</td>
<td>

Het model moet worden getest op een representatieve set brieven om mogelijke fouten te identificeren. Hierbij moet specifiek worden gecontroleerd op bias (o.a. geslacht) zodat geen enkele groep wordt benadeeld en discriminatie wordt voorkomen \[15\]\[16\].
</td>
<td>S</td>
<td>

* Overheden/toezichthouders
</td>
</tr>
</table>

### **Functionele requirements**

<table>
<tr>
<th>RQ-nr</th>
<th>Requirement</th>
<th>MoSCoW</th>
<th>Stakeholder</th>
</tr>
<tr>
<td>FR01</td>
<td>

De AI-tool geeft uitsluitend suggesties en automatiseert geen beslissingen. De medewerker kan elke door de AI-tool gegenereerde suggestie expliciet goedkeuren of afwijzen, omdat menselijke beoordeling noodzakelijk is om context, juridische correctheid en verantwoordelijkheid bij het aanpassen van officiële communicatie te waarborgen. \[2\]
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren 
</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>FR03</td>
<td>

De AI-tool moet de klant informeren dat de suggesties slechts ter ondersteuning dienen en dat de medewerker de eindbeslissing neemt. \[2\]
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren 
</td>
</tr>
<tr>
<td>FR04</td>
<td>

De AI-tool moet na verwerking van de suggestie, de data bewaren zodat de suggestie in een soortgelijke situatie (her)gebruikt kan worden en de suggestie zo eerder wordt weergegeven. \[3\]
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>FR05</td>
<td>De AI-tool moet een lagere LINT II-score hebben dan het baseline model. </td>
<td>M</td>
<td>

* OVER-gemeenten
</td>
</tr>
<tr>
<td>FR06</td>
<td>Resultaten moeten betrouwbaar en reproduceerbaar zijn. </td>
<td>S</td>
<td>

* OVER-gemeenten
</td>
</tr>
<tr>
<td>FR07</td>
<td>De ontwikkeling van de AI-tool (datasets, modelkeuze, training) en de prestaties moeten gedocumenteerd worden</td>
<td>M</td>
<td>

* Overheid
* Medewerkers die brieven schrijven/controleren
</td>
</tr>
<tr>
<td>FR08</td>
<td>

De AI-tool biedt mogelijkheid om door een mens gecontroleerd te worden. \[2\] 
</td>
<td>C</td>
<td>

* ICT-afdeling
</td>
</tr>
</table>

### **Technische requirements**

<table>
<tr>
<th>RQ-nr</th>
<th>Requirement</th>
<th>MoSCoW</th>
<th>Stakeholder</th>
</tr>
<tr>
<td>TR01</td>
<td>

Bewonersinformatie wordt direct verwerkt en niet opgeslagen. Dit moet in de code van de AI-tool worden verwerkt. \[4\]
</td>
<td>M</td>
<td>

* Inwoners van OVER-gemeenten
* Overheden/toezichthouders 
</td>
</tr>
<tr>
<td>TR02</td>
<td>

User Interface (UI) elementen tonen aan dat de AI-tool ondersteunend is en niet beslissend. \[2\]
</td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren 
</td>
</tr>
<tr>
<td>TR03</td>
<td>De AI-tool moet gevalideerd worden ten opzichte van het nulmodel en prestaties moeten worden gedocumenteerd. </td>
<td>M</td>
<td>

* ICT-afdeling 
</td>
</tr>
<tr>
<td>TR04</td>
<td>De gebruikte datasets moet gesplitst worden in een train-, validatie- en testdataset van 64%, 16%, 20%. </td>
<td>M</td>
<td>

* ICT-afdeling 
</td>
</tr>
<tr>
<td>TR05</td>
<td>De AI-tool moet de brieven lokaal verwerken. </td>
<td>M</td>
<td>

* Overheden/toezichthouders 
* ICT-afdeling 
</td>
</tr>
<tr>
<td>TR06</td>
<td>De AI-tool moet sneller werken dan dat de medewerker handmatig de zin verbeterd.  </td>
<td>M</td>
<td>

* Medewerkers die brieven schrijven/controleren 
</td>
</tr>
<tr>
<td>TR07</td>
<td>

De AI-tool moet een representatieve dataset gebruiken. \[4\]
</td>
<td>S</td>
<td>

* ICT-afdeling 
* Overheden/toezichthouders 
</td>
</tr>
<tr>
<td>TR08</td>
<td>

Het model moet bias-mitigatie technieken gebruiken, zodat het om kan gaan met incorrect beoordeelde resultaten. \[4\]
</td>
<td>S</td>
<td>

* ICT-afdeling 
* Overheden/toezichthouders 
</td>
</tr>
<tr>
<td>TR09</td>
<td>Het systeem moet beveiligd zijn tegen hacks door middel van netwerksegmentatie. </td>
<td>W</td>
<td>

* ICT-afdeling 
* Overheden/toezichthouders 
</td>
</tr>
</table>

### **Duurzaamheids requirements**

<table>
<tr>
<th>RQ-nr</th>
<th>Requirement</th>
<th>MoSCoW</th>
<th>Stakeholder</th>
</tr>
<tr>
<td>DR01</td>
<td>De AI-tool wordt zo ontwikkeld dat het energie- en datagebruik minimaal is door inzet van efficiënte modellen en infrastructuur, waarbij deze keuzes aantoonbaar bijdragen aan een zo laag mogelijke milieu-impact.</td>
<td>W</td>
<td>

* Overheden/toezichthouders 
* ICT-afdeling 
</td>
</tr>
</table>

# 

## Alle must haves

<table>
<tr>
<th>RQ-nr</th>
<th>Requirement</th>
<th>Stakeholder</th>
<th>Stakeholder toelichting</th>
</tr>
<tr>
<td>ER01</td>
<td>

Gebruikers moeten weten hoe de AI-tool werkt, waarbij geen AI gelettertheid nodig is \[1\].
</td>
<td>Medewerkers die brieven schrijven/controleren</td>
<td>De medewerker moet in de AI-tool weten welke knoppen waarvoor dienen, zodat de tool correct gebruikt kan worden voor het herschrijven van brieven.</td>
</tr>
<tr>
<td>ER02</td>
<td>

Een woordsuggestie mag niet zonder toestemming van de medewerker worden toegevoegd (bijv. om bias en fouten van het LLM te voorkomen). Het systeem moet een human-in-the-loop hebben; de mens blijft eindverantwoordelijk en de AI-tool ondersteunt slechts \[1\].
</td>
<td>

Medewerkers die brieven schrijven/controleren <br><br>Overheid
</td>
<td>

Medewerkers: De medewerker wil het herschrijven niet volledig aan de AI overlaten omdat hij/zij verantwoordelijk blijft voor de inhoud van de brief.

\
Overheid: Wil dat inwoners correct worden geïnformeerd en dat risico op verkeerde verwoordingen wordt geminimaliseerd zodat wetgeving correct wordt vertaald.
</td>
</tr>
<tr>
<td>ER03</td>
<td>

Medewerkers hebben de mogelijkheid om het gebruik van de AI-tool vrijwillig aan- of uit te schakelen. De AI-tool wordt uitsluitend gebruikt ter ondersteuning en advisering en neemt geen autonome beslissingen; de professionele afweging en verantwoordelijkheid blijven volledig bij de medewerker \[1\].
</td>
<td>Medewerkers die brieven schrijven/controleren</td>
<td>Medewerkers moeten de AI-tool kunnen aan- of uitzetten wanneer zij deze niet willen gebruiken.</td>
</tr>
<tr>
<td>ER04</td>
<td>

Om automation bias te voorkomen, moeten de beperkingen en capaciteiten van de AI-tool aan de stakeholders worden gemeld; bijvoorbeeld dat de tool slechts een hulpmiddel is en niet altijd de beste suggesties geeft \[1\].
</td>
<td>Medewerkers die brieven schrijven/controleren</td>
<td>Medewerkers die brieven schrijven of controleren nemen inhoudelijke en juridische beslissingen. Wanneer zij onvoldoende inzicht hebben in de beperkingen van de AI-tool, bestaat het risico dat AI-suggesties onkritisch worden overgenomen (automation bias). Dit kan leiden tot feitelijke onjuistheden of onjuiste formuleringen in brieven, terwijl de medewerker eindverantwoordelijk blijft voor de inhoud.</td>
</tr>
<tr>
<td>JR01</td>
<td>

Persoonlijke informatie van burgers mag niet worden opgeslagen of gebruikt voor (verdere) training van het model. De trainingsdata bestaat uit anonieme brieven \[5\]\[8\].
</td>
<td>Inwoners van OVER-gemeenten</td>
<td>De persoonlijke gegevens van inwoners mogen niet zonder toestemming worden verspreid.</td>
</tr>
<tr>
<td>JR02</td>
<td>

De AI-tool mag geen persoonsgegevens delen met externe partijen of servers \[13\]\[14\].
</td>
<td>

Overheid <br><br>Inwoners van OVER-gemeenten<br><br>OVER-gemeenten
</td>
<td>

Overheid: Moet controleren of dit in de praktijk wordt nageleefd. <br><br>Inwoners: Hun persoonlijke gegevens mogen niet zonder toestemming worden verspreid. <br><br>Gemeente Oostzaan: Is eindverantwoordelijk en mag geen persoonlijke gegevens delen met externe partijen of servers.
</td>
</tr>
<tr>
<td>FR01</td>
<td>

De AI-tool geeft uitsluitend suggesties en automatiseert geen beslissingen. De medewerker kan elke door de AI-tool gegenereerde suggestie expliciet goedkeuren of afwijzen, omdat menselijke beoordeling noodzakelijk is om context, juridische correctheid en verantwoordelijkheid bij het aanpassen van officiële communicatie te waarborgen. \[2\]
</td>
<td>Medewerkers die brieven schrijven/controleren </td>
<td>De medewerker moet bij alle suggesties die de AI-tool geeft, zelf bepalen of de tekst aangepast wordt.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>FR03</td>
<td>

De AI-tool moet de klant informeren dat de suggesties slechts ter ondersteuning dienen en dat de medewerker de eindbeslissing neemt. \[2\]
</td>
<td>Medewerkers die brieven schrijven/controleren </td>
<td>De medewerkers mogen er niet vanuit gaan dat de AI-tool altijd de beste weerspiegeling geeft van hun eigen tekst. De AI-tool dient alleen als ondersteuning bij het schrijven.</td>
</tr>
<tr>
<td>FR04</td>
<td>

De AI-tool moet na verwerking van de suggestie, de data bewaren zodat de suggestie in een soortgelijke situatie (her)gebruikt kan worden en een suggestie zo eerder wordt weergegeven. \[3\]
</td>
<td>Medewerkers die brieven schrijven/controleren </td>
<td>De medewerkers kunnen op deze manier vaker suggesties te zien krijgen die gewenst zijn door data op te halen van eerdere keuzes die de medewerker heeft gemaakt.</td>
</tr>
<tr>
<td>FR05</td>
<td>De AI-tool moet een lagere LINT II-score hebben dan het baseline model. </td>
<td>OVER-gemeenten</td>
<td>Hierdoor wordt verzekerd dat de AI-tool beter presteert dan het nulmodel.</td>
</tr>
<tr>
<td>FR06</td>
<td>Resultaten moeten betrouwbaar en reproduceerbaar zijn. </td>
<td>OVER-gemeenten</td>
<td>Hierdoor worden de suggesties als betrouwbaar en reproduceerbaar gezien.</td>
</tr>
<tr>
<td>TR01</td>
<td>

Bewoners informatie wordt direct verwerkt en niet opgeslagen. Dit moet in de code van de AI-tool worden verwerkt. \[4\]
</td>
<td>

Inwoners van OVER-gemeenten

Overheden/toezichthouders 
</td>
<td>

Inwoners van Gemeente Oostzaan: Willen niet dat hun persoonlijke informatie buiten de gemeente lekt.

Overheden/toezichthouders: willen ook verzekerd zijn dat de informatie die zij schrijven, niet gelekt wordt buiten hun eigen netwerk.
</td>
</tr>
<tr>
<td>TR02</td>
<td>

User Interface (UI) elementen tonen aan dat de AI-tool ondersteunend is en niet beslissend. \[2\]
</td>
<td>Medewerkers die brieven schrijven/controleren </td>
<td>Medewerkers kunnen hierdoor zien dat de AI-tool als ondersteunend middel dient en niet wat altijd gebruikt dient te worden.</td>
</tr>
<tr>
<td>TR03</td>
<td>De AI-tool moet gevalideerd worden ten opzichte van het nulmodel en prestaties moeten worden gedocumenteerd. </td>
<td>ICT-afdeling </td>
<td>Hierdoor wordt duidelijk of de gemaakte AI-tool beter werkt in de praktijk dan het nulmodel.</td>
</tr>
<tr>
<td>TR04</td>
<td>De gebruikte datasets moet gesplitst worden in een train-, validatie- en testdataset van 64%, 16%, 20%. </td>
<td>ICT-afdeling </td>
<td>Op deze manier kan het model veilig getraind en gevalideerd worden, waarbij data-leakage voorkomen wordt.</td>
</tr>
<tr>
<td>TR05</td>
<td>De AI-tool moet de brieven lokaal verwerken. </td>
<td>

Overheden/toezichthouders 

ICT-afdeling 
</td>
<td>Willen niet dat persoonlijke informatie uit de brieven buiten de gemeente lekt.</td>
</tr>
<tr>
<td>TR06</td>
<td>De AI-tool moet sneller werken dan dat de medewerker handmatig de zin verbeterd.  </td>
<td>Medewerkers die brieven schrijven/controleren </td>
<td>Hierdoor is het handmatig zoeken naar suggesties in de schrijfwijzer overbodig geworden.</td>
</tr>
</table>

## Testmethode en acceptatiecriteria must have requirements

| RQ-nr | Testmethode | Acceptatiecriteria |
|-------|-------------|--------------------|
| ER01 | Interactief prototype | Gebruikerstesten uitvoeren waarbij wordt onderzocht of alle instructies duidelijk zijn en of testers het systeem begrijpen. |
| ER02 | Interactief prototype | Bij het ontwerpen van het AI-systeem moet de mens eindverantwoordelijk blijven voor de beslissing of een suggestie wordt goedgekeurd. |
| ER03 | Interactief prototype | In het interactief prototype moet de medewerker de optie krijgen om voor de AI-tool te kiezen. |
| ER04 | Documentatie | Stakeholders ontvangen informatie over prestaties en beperkingen van het systeem. |
| JR01 | Code en dataset | In de code staat dat persoonlijke informatie verwijderd wordt direct na het opslaan van de brief. In de dataset wordt gecontroleerd of de brieven anoniem zijn. |
| JR02 | Code controleren | Persoonlijke informatie wordt niet gebruikt voor verdere iteraties. Het opslaan en schrijven van de brief gebeurt lokaal. |
| FR01 | Interactief prototype | In het interactief prototype staat dat de weergegeven suggesties eerst door de medewerker geaccepteerd moeten worden voordat de zinnen of woorden aangepast worden. |
| FR02 | Interactief prototype | In het interactief prototype staat dat de medewerker de suggestie kan afwijzen of goedkeuren. |
| FR03 | Interactief prototype | In het interactief prototype staat een stuk tekst dat de AI-tool slechtst ter ondersteuning dient. |
| FR04 | End-to-end test | In de code staat dat de gemaakte keuzes door de medewerker worden opgeslagen, zodat bij een volgende soortgelijke suggestie dit woord of deze zin eerder als suggestie naar boven komt. |
| FR05 | Evaluatie | In de evaluatie worden de LINT II-scores van de AI-tool en het baseline model tegenover elkaar gezet. |
| FR06 | Evaluatie | De gemiddelde LiNT-II-score van de verschillende briefsoorten is hoger dan de LiNT-II-score op het baseline model. |
| FR07 | Documentatie | In de documentatie worden de ontwikkeling van het AI-systeem en de nauwkeurigheid van de suggesties weergegeven. |
| TR01 | End-to-end test | In de code staat dat bewonersinformatie uit de brieven direct verwerkt wordt en niet wordt opgeslagen. |
| TR02 | Interactief prototype | In het interactief prototype staat dat de AI-tool ondersteunend is voor de medewerker en niet beslissend. |
| TR03 | Evaluatie | In de evaluatie worden de AI-tool en het baseline model tegenover elkaar gezet. |
| TR04 | Code controleren | In de code staat een datasplitsing volgens een validatie- en test-set van 50% en 50%. |
| TR05 | Code controleren | De code wordt lokaal gedraaid. |
| TR06 | Interactief prototype | Er dient een test uitgevoerd te worden met een medewerker, waarin de medewerker een brief verbeterd door handmatig de schrijfwijzer te gebruiken en daarnaast dezelfde brief dient te verbeteren door het gebruik van de AI-tool. |

\[1\] https://www.betabit.nl/media/4614/ethicsguidelinesfortrustworthyai-nl.pdf

\[2\] G. M. Raimondo, U.S. Department of Commerce, National Institute of Standards and Technology, and L. E. Locascio, “Artificial Intelligence Risk Management Framework (AI RMF 1.0),” National Institute of Standards and Technology, Jan. 2023. \[Online\]. Beschikbaar op: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf

\[3\] N. Vollmer, “Artikel 6 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, Nicholas Vollmer, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-6-rechtmatigheid-van-de-verwerking-EU-AVG.htm

\[4\]N. Vollmer, “Artikel 9 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, Nicholas Vollmer, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-9-verwerking-van-bijzondere-categorieen-van-persoonsgegevens-EU-AVG.htm

\[5\] “AVG-randvoorwaarden voor generatieve AI”, Autoriteit Persoonsgegevens. https://www.autoriteitpersoonsgegevens.nl/documenten/avg-randvoorwaarden-voor-generatieve-ai

\[6\] N. Vollmer, “Artikel 22 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, Nicholas Vollmer, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-22-geautomatiseerde-individuele-besluitvorming-waaronder-profilering-EU-AVG.htm

\[7\] “Artikel II-61: De menselijke waardigheid”, Nederlandse Grondwet. https://www.denederlandsegrondwet.nl/id/vgt8md7movy0/artikel_ii_61_de_menselijke_waardigheid

\[8\] N. Vollmer, “Artikel 5 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, Nicholas Vollmer, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-5-beginselen-inzake-verwerking-van-persoonsgegevens-EU-AVG.htm

\[9\] N. Vollmer, “Artikel 13 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-13-te-verstrekken-informatie-wanneer-persoonsgegevens-bij-de-betrokkene-worden-verzameld-EU-AVG.htm

\[10\] N. Vollmer, “Artikel 14 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-14-te-verstrekken-informatie-wanneer-de-persoonsgegevens-niet-van-de-betrokkene-zijn-verkregen-EU-AVG.htm

\[11\] N. Vollmer, “Artikel 30 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-30-register-van-de-verwerkingsactiviteiten-EU-AVG.htm

\[12\] N. Vollmer, “Artikel 35 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-35-gegevensbeschermingseffectbeoordeling-EU-AVG.htm

\[13\] N. Vollmer, “Artikel 25 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-25-gegevensbescherming-door-ontwerp-en-door-standaardinstellingen-EU-AVG.htm

\[14\] N. Vollmer, “Artikel 32 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-32-beveiliging-van-de-verwerking-EU-AVG.htm

\[15\] “Artikel 21 - Non-discriminatie”, _European Union Agency For Fundamental Rights_, 24 september 2025. https://fra.europa.eu/nl/eu-charter/article/21-non-discriminatie#:\~:text=Discriminatie%20wegens%20godsdienst%2C%20levensovertuiging%2C%20politieke,dan%20ook%2C%20is%20niet%20toegestaan.

\[16\] “Artikel 1: Gelijke behandeling en discriminatieverbod”, _Nederlandse Grondwet_. https://www.denederlandsegrondwet.nl/id/vgrnb2er8avw/artikel_1_gelijke_behandeling_en#:\~:text=Allen%20die%20zich%20in%20Nederland,dan%20ook%2C%20is%20niet%20toegestaan.

\[17\] N. Vollmer, “Artikel 15 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-15-recht-van-inzage-van-de-betrokkene-EU-AVG.htm

\[18\] N. Vollmer, “Artikel 16 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-16-recht-op-rectificatie-EU-AVG.htm

\[19\] N. Vollmer, “Artikel 17 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-17-recht-op-gegevenswissing-recht-op-vergetelheid%E2%80%9D-EU-AVG.htm

\[20\] Vollmer, “Artikel 21 EU algemene verordening gegevensbescherming (EU-AVG). Privacy/Privazy according to plan.”, _Nicholas Vollmer_, 4 april 2023. https://www.privacy-regulation.eu/nl/artikel-21-recht-van-bezwaar-EU-AVG.htm