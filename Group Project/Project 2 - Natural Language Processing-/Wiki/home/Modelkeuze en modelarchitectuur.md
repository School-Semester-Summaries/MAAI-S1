# Versies

* [Versie 2](#versie-2)
* [Versie 1](#versie-1)

# Versie 1

# Architectuur(en)

Voor de ontwikkeling van het model is gekozen voor een naïeve RAG-implementatie \\cite{paetzold_survey_2017}. Deze implementatie maakt gebruik van een vectordatabase om aanvullende informatie toe te voegen aan de prompt. Als baseline voor de RAG-implementatie is gekozen voor het gebruik van alleen het taalmodel zonder aanvullende informatie uit de schrijfwijzer. Dit maakt het mogelijk om de prestaties van het toegevoegde RAG-systeem te vergelijken met het standaard taalmodel. Andere implementaties, zoals geavanceerde RAG zijn voor de eerste iteratie niet gekozen zodat dit een eenvoudiger uitgangspunt biedt voor verdere optimalisatie en uitbreiding in de toekomst.

De vectordatabase is gevuld met informatie uit de schrijfwijzer. Informatie uit deze database wordt opgehaald, en vervolgens toegevoegd aan de prompt die naar het taalmodel wordt gestuurd. Hierdoor kan het taalmodel gebruik maken van de richtlijnen uit de schrijfwijzer bij het genereren van teksten. In Figuur\~\\ref{} is de architectuur van het systeem visueel weergegeven.

---

# Het gebruikte LLM-model

Voor het maken van de AI-tool moet gekeken worden welk LLM-model gebruikt wordt in de model-architectuur die later besproken wordt. Dit LLM-model zal dienen als de component voor het genereren van vereenvoudigde Nederlandse teksten op basis van de opgehaalde documenten uit de retrieval-stap.

Een van de weinige Nederlandstalige LLM’s is het GEITje-model. Het model is specifiek gericht op toepassingen binnen de Nederlandse taal en onderscheidde zich doordat het verder getraind was op miljarden Nederlandstalige tokens. Hierdoor kon het beter omgaan met Nederlandse grammatica, woordgebruik en context dan generieke, Engelstalig modellen. GEITje was gebaseerd op Mistral 7B en vormde daarmee een van de eerste grootschalige open modellen die zich volledig richtten op Nederlandstalige verwerking. Het model is echter sinds 2025 niet langer beschikbaar. Op verzoek van Stichting BREIN zijn alle modelbestanden verwijderd uit de HuggingFace-repositories. De aanleiding hiervoor was dat een deel van de trainingsdata mogelijk auteursrechtelijk beschermd materiaal bevatte dat uit illegale bron afkomstig was. Hierdoor valt het model GEITje af voor dit onderzoek \\cite{rijgersberg_het_2025}.

Vanuit het gastcollege van Jenia Kim kwamen de Leesplank Noot models naar voren. Het bevat een set van drie Nederlandstalige LLM's, elk gefinetuned op een samengestelde Nederlandstalige dataset voor tekstvereenvoudiging naar B1-niveau. De modellen zijn ontwikkeld voor overheids- en publieke communicatie en sluiten aan bij de EU AI Act: transparant, herleidbaar, controleerbaar en veilig inzetbaar in gemeentelijke communicatie. In Tabel \\ref{tab:modellen} worden de drie modellen gegeven die door het UWV gemaakt zijn, waarbij één model gekozen wordt als LLM.

**Overzicht van verschillende LLM-modellen met bron, voordelen, nadelen en aantal parameters**

| LLM-model en bron | Voordelen | Nadelen | Aantal parameters |
|-------------------|-----------|---------|-------------------|
| Granite-3.3-2b \\cite{granite} | Biedt de hoogste kwaliteit volgens de bron, levert consistente en betrouwbare output en blijft dankzij de compacte omvang efficiënt inzetbaar op gangbare hardware. | Het model is trager dan de alternatieven en vraagt meer rekenkracht dan het lichtste model, waardoor het minder geschikt is voor situaties waar snelheid de hoogste prioriteit heeft. | 2B |
| Llama-3.2-3b \\cite{lama} | Combineert een goede outputkwaliteit met hogere snelheid dan Granite en profiteert van extra modelcapaciteit die het breed inzetbaar maakt. | De grotere modelgrootte zorgt voor hogere hardware-kosten, terwijl deze extra omvang geen duidelijke kwaliteitswinst oplevert ten opzichte van Granite. | 3B |
| EuroLLM-1.7b \\cite{eurollm} | Werkt snel, is lichtgewicht en daarmee geschikt voor toepassingen met beperkte hardware. | De lagere kwaliteit en minder stabiele verwerking van complexe context maken het minder betrouwbaar voor taken waar nauwkeurigheid belangrijk is. | 1.7B |

Voor de naïeve RAG-architectuur wordt gekozen voor het Granite-3.3-2B-model. Volgens de gepubliceerde evaluaties in de bron behaalt dit model de hoogste kwaliteitsscore van de drie modellen, wat zich ook in de praktijk vertaalt naar betrouwbaardere en consistenter geformuleerde output \\cite{noot}. Granite weet context beter te structureren en inhoudelijk nauwkeuriger weer te geven, terwijl het model qua omvang compact genoeg blijft om efficiënt te gebruiken.

De andere modellen bieden voordelen, maar sluiten minder goed aan bij de doelstelling. Llama-3.2-3B is groter, maar levert ondanks het hogere aantal parameters geen kwaliteitsverbetering. Daardoor wegen de extra rekenkosten niet op tegen de beperkte meerwaarde \\cite{lama}. EuroLLM-1.7B is juist het lichtste en snelste model, wat aantrekkelijk kan zijn voor taken die snel uitgevoerd dienen te worden. In deze context leidt het lagere kwaliteitsniveau echter sneller tot lagere scores, wat de betrouwbaarheid van de pipeline vermindert \\cite{eurollm}. Daarom vormt Granite-3.3-2B, met zijn volgens de bron hoogste kwaliteit en stabiele verwerking van context, de meest geschikte keuze voor de naïeve RAG-implementatie.

# Versie 2

# Globale modelkeuze

Tekstversimpeling kan worden gezien als een specifieke vorm van vertalen: van een complexe brontekst naar een eenvoudiger variant met behoud van kernbetekenis. Goede tekstversimpeling combineert begrip en vereenvoudiging \\cite{cooper_combinmt_2020}. Voor dit project moeten de taalmodellen de inhoud begrijpen en herformuleren volgens de regels van de OVER-schrijfwijzer. Om dit te ondersteunen zijn twee keuzes gemaakt: het gebruik van naïve-rag en het gebruik van een decoder-only model.

## Keuze voor Naïve-RAG

De architectuur waar het uiteindelijk gekozen model zich in zal bevinden is de naïve-RAG-architectuur. Hiervoor is gekozen omdat er voor het herschrijven van de gemeentelijke brieven gebruik gemaakt moet worden van de OVER-schrijfwijzer. Deze OVER-schrijfwijzer, indien er aanpassingen nodig zijn, kan op elk moment worden geüpdatet binnen de vector database. Ook kan er aanvullende informatie worden toegevoegd aan deze database, waaronder bijvoorbeeld synoniemenlijsten.

De belangrijkste rol dat deze naïve-RAG-architectuur dient is het ondersteunen van de tekstgeneratieproces door middel van extra context, waaronder bijvoorbeeld regels uit de OVER-schrijfwijzer. Dit is nuttig voor tekst versimpeling, omdat het de consistentie verhoogt en de kans op onjuiste toevoegingen (hallucinaties) verkleint \\cite{quSemanticChunkingWorth}.

## Modelsoorten

Bij de selectie van het taalmodel is eerst onderscheid gemaakt tussen verschillende architecturen: encoder-only, decoder-only en encoder-decoder. Hoewel deze indeling inzicht geeft in de globale werking van modellen, is de architectuur alleen niet voldoende om de geschiktheid voor deze taak te bepalen. Daarom is bij de verdere selectie gekeken naar aanvullende aspecten, zoals het kunnen volgen van de OVER-schrijfwijzer, ondersteuning voor de Nederlandse taal en de algehele betrouwbaarheid van het model.

## Encoder-only

Encoder-only modellen, zoals BERT, zijn sterk in tekstbegrip en analyse. Ze zijn geschikt voor taken zoals het inschatten van complexiteit of het vergelijken van betekenis. Omdat encoder-only modellen geen mechanisme hebben om zelfstandig nieuwe tekst te genereren, zijn ze niet bruikbaar als primair model voor het herschrijven van teksten \\cite{bl_understanding_2024}. Ze vallen daarom af voor de generatietaak.

## Decoder-only modellen

Decoder-only modellen zijn van oorsprong ontworpen voor tekstgeneratie. Waar oudere varianten soms minder accuraat waren, zijn moderne modellen verbeterd in het volgen van specifieke instructies (instruction following) \\cite{lamelas_evaluating_2026}. Dit maakt ze geschikt om tekststijlen, zoals die van de OVER-schrijfwijzer, toe te passen. In combinatie met de juiste prompts en context kunnen ze worden ingezet voor tekstversimpeling.

## Encoder-decoder modellen

Encoder-decoder modellen worden traditioneel veel gebruikt voor 'sequence-to-sequence' taken zoals vertalen en samenvatten. De encoder verwerkt/transformeert de input en de decoder genereert de output, wat vaak goede resultaten oplevert op simplificatiebenchmarks \\cite{wang_experimental_2016}. Daarmee vormen zij een logische en valide keuze voor deze taak, al vergt het toepassen van specifieke stijlinstructies soms meer finetuning dan bij decoder-only modellen.

## Modelkeuze binnen de Naïve-RAG

Voor dit onderzoek is uiteindelijk gekozen voor een decoder-only model. De doorslaggevende factor was de flexibiliteit waarmee deze modellen complexe instructies, zoals de specifieke regels van de OVER-schrijfwijzer, kunnen toepassen op de Nederlandse taal. Encoder-decoder modellen bieden hier minder flexibiliteit in. Verder zijn de risico's van decoder-only modellen, zoals het verzinnen van informatie in deze opzet verminderd door de RAG-architectuur. Hierbij gebruikt het model aanvullende informatie waarmee de herschrijf suggestie gegeven wordt \\cite{noot}.

Van de vele beschikbare modellen is uiteindelijk gekozen een model uit de Leesplank Noot-modellen te kiezen \\cite{noot}. Aangezien deze modellen specifiek ontwikkeld zijn voor het schrijven naar B1-niveau, en voor publieke overheidscommunicatie. Dit past goed binnen de context van gemeentelijke teksten versimpelen.

## Architectuur Diagrammen

Voor het systeem zijn 2 verschillende architectuur diagrammen gemaakt, een high-level (Figuur 1) en een low-level (Figuur 2) diagram. Deze diagrammen geven een overzicht van hoe het project is opgebouwd.

_Figuur 1: High-level architectuur diagram van de eerste iteratie_

<img width="641" height="581" alt="image" src="https://github.com/user-attachments/assets/038c542f-349d-49b9-9400-123dfe39417e" />


_Figuur 2: Low-level architectuur diagram van de eerste iteratie_


<img width="900" height="535" alt="image" src="https://github.com/user-attachments/assets/9c737837-ac33-4850-af4d-41354d9d7844" />
