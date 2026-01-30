## OVER-schrijfwijzer

De OVER-schrijfwijzer bevat richtlijnen voor duidelijke en toegankelijke gemeentelijke communicatie. Teksten horen op B1-niveau geschreven te worden: kort, concreet en met direct de kernboodschap. Elke alinea bevat één duidelijke boodschap en heeft een logische opbouw. Medewerkers vermijden jargon, formele taal en onnodige afkortingen, en schrijven in een actieve, positieve en adviserende toon.

De lezer staat centraal; medewerkers leggen uit wat informatie betekent voor de persoonlijke situatie van inwoners. De schrijfwijzer vraagt om inclusief taalgebruik, consequent gebruik van de u-vorm en vaste notaties voor onder andere data, bedragen en adressen, waarbij terminologie en schrijfwijze consistent blijven.

In de OVER-schrijfwijzer staan echter geen synoniemen of weinig moeilijke woorden die naar B1-niveau worden geschreven, wat dit een nadeel maakt van de OVER-schrijfwijzer.

---

## Externe data

Aangezien de OVER-schrijfwijzer weinig synoniemen op B1-niveau van moeilijke woorden bevat, is ervoor gekozen om externe data te gebruiken om uiteindelijk het AI-model mee te trainen. Er is gebruik gemaakt van vijf verschillende bronnen, die in Tabel _Woordenlijsten_ genoemd zijn.

**Overzicht van gebruikte woordenlijsten**

| Naam dataset / bron | Uitleg | Voordeel | Nadeel |
|---------------------|--------|----------|--------|
| Moeilijk-woordenboek (Gemeente Amsterdam) | Synoniemenlijst met 747 eenvoudiger alternatieven voor ‘moeilijke’ Nederlandse woorden. | Woorden zijn afgestemd op B1-niveau. | Geen voorbeeldzinnen, waardoor geen zinsverbeteringen geleerd kunnen worden. |
| Helder juridisch woordenboek (Gemeente Amsterdam) | Lijst met 134 juridische termen met alternatieven op B1-niveau; gebaseerd op praktijk van de gemeente en aangevuld met Gebruiker Centraal. | Vermijdt juridisch jargon en stimuleert B1-niveau. | Geen zinnen opgenomen, dus geen zinsverbeteringen mogelijk. |
| Inclusieve woordenlijst (Gemeente Amsterdam) | Lijst met 43 termen met inclusieve alternatieven. | Bevordert inclusief taalgebruik. | Termen kunnen verouderen. |
| Synoniemen woordenlijst (B1-teksten) | Lijst met tien B1-synoniemen. | Gericht op B1-niveau en ondersteuning van eenvoudiger taalgebruik. | Beperkte lijst (10 woorden) en geen zinnen voor zinsverbetering. |
| B1 synoniemenlijst (Dijk en Waard) | Lijst met zeven synoniemen op B1-niveau. | Gericht op B1-niveau en eenvoudiger taalgebruik. | Zeer beperkte omvang (7 woorden) en geen zinnen opgenomen. |

---

## Brieven van de OVER-gemeenten

OVER-gemeente heeft verschillende brieven aangeleverd die de bestaande situatie beschrijven. Omdat deze brieven nog niet volgens de schrijfwijzer zijn herschreven, vormen zij geen representatieve voorbeelden voor het gewenste eindresultaat. Daarom is besloten om deze brieven niet te gebruiken om het AI-model te trainen.

Wel worden deze brieven ingezet om te beoordelen hoe goed het model later functioneert. De brieven dienen daarom gesplitst te worden in een validatie- en testset. Hierover is meer te lezen in de paragrafen _Data-preparatie_ en _Data-splitsing_.

---

## Data-preparatie

Voor zowel de externe bronnen als de vrijgegeven brieven van de OVER-gemeenten is data-preparatie uitgevoerd. De **externe data** was niet direct als databestand beschikbaar en is daarom via webscraping van de betreffende websites verzameld. Dit leverde vier datasets op.

**Overzicht van gebruikte datasets**

| Naam dataset | Aantal woorden | Datatype | Bron |
|--------------|----------------|----------|------|
| Moeilijk-woordenboek | 747 | String | Gemeente Amsterdam |
| Helder juridisch woordenboek | 134 | String | Gemeente Amsterdam |
| Inclusieve woordenlijst | 43 | String | Gemeente Amsterdam |
| Synoniem woordenlijst | 17 | String | B1-teksten / Dijk en Waard |

Naast deze externe data is ook data-preparatie uitgevoerd voor de **brieven van de OVER-gemeenten**. Voordat de data kon worden opgesplitst in een validatie- en testset, zijn de briefnamen eerst gegroepeerd. Deze groepering zorgt voor een eerlijke en representatieve verdeling van de documenten over beide sets.

**Overzicht van documentgroepen**

| Groepnaam | Uitleg | Aantal brieven |
|-----------|--------|----------------|
| Schuldhulp | Brieven die betrekking hebben tot schuldhulp vanuit de OVER-gemeenten. | 4 |
| WMO | Brieven die betrekking hebben tot WMO en zorgvoorzieningen vanuit de OVER-gemeenten. | 13 |
| Participatiewet (PW) | Brieven die betrekking hebben tot PW en uitkeringszaken. | 13 |
| Participatiefonds (PF) | Brieven die betrekking hebben tot participatiefondsen. | 4 |
| Overig | Brieven die niet vallen binnen de bovenste vier categorieën. | 2 |

Zoals eerder benoemd wordt de OVER-schrijfwijzer gebruikt tijdens het trainen van het AI-model. Deze pre-processing stappen worden bij het onderdeel _Model_ verder toegelicht, aangezien hier een vector-database van gemaakt dient te worden.

---

## Data-splitsing

De brieven van de OVER-gemeenten worden gebruikt als validatie- en testset. Hiervoor is een _stratified split_ toegepast op de verschillende briefgroepen, zodat iedere groep evenveel is vertegenwoordigd in zowel de validatie- als de testset.

Er is gekozen voor een verdeling van **50% validatie** en **50% test**. Brieven over de Participatiewet (PW) en de WMO komen het meest voor in de validatieset en worden daardoor relatief vaker gevalideerd dan de overige briefgroepen.

---

## Vector database

Om delen van de schrijfwijzer mee te geven als context voor het LLM, is gekozen voor het gebruik van een vector database. In een vector database wordt tekstuele informatie opgeslagen in de vorm van vectoren. Door een zoekopdracht (bijvoorbeeld: _“welke regels zijn belangrijk voor adviserend schrijven”_) om te zetten naar een vector en vergelijkbare vectoren op te halen, kan relevante informatie worden teruggevonden.

Er bestaan meerdere open-source vector databases, waaronder ChromaDB, LanceDB en Qdrant.

## Vergelijking van vector databases

|  | ChromaDB | LanceDB | Qdrant |
|--|----------|---------|--------|
| Architectuur | Hybride | Embedded | Client-server |
| Open-source | Ja (Apache 2.0) | Ja (Apache 2.0) | Ja (Apache 2.0) |
| Metadata filtering | Filteren op metadata en documentinhoud | SQL-strings en Pandas-integratie | Geografische, tekst- en numerieke filters |

Uit deze opties is **LanceDB** het meest geschikt. Vanwege onder andere de AVG moeten OVER-gemeenten zorgvuldig omgaan met persoonsgegevens. LanceDB kan lokaal worden ingezet op de bestaande serveromgeving, zonder extra client-server-architectuur.

---

## Pre-processing stappen

Voor het opslaan van de schrijfwijzer in een vector database is een geschikte _chunking_-strategie nodig. Deze strategie bepaalt hoe tekst wordt opgesplitst en opgeslagen, zodat relevante context later kan worden teruggevonden.

**Strategieën voor text chunking**

| Type | Strategie | Voordelen | Nadelen |
|------|-----------|-----------|---------|
| Klassiek | Opsplitsen op vaste lengte (bijv. elke 100 karakters) | Eenvoudig; voorspelbare chunk-grootte | Contextverlies; kan zinnen breken |
| Klassiek | Opsplitsen op zinnen | Behoudt grammaticale structuur | Weinig context; variabele lengte |
| Klassiek | Opsplitsen met overlap | Minder contextverlies | Redundantie; hogere kosten |
| Gespecialiseerd | Opsplitsen op structuur (HTML/Markdown/LaTeX) | Behoudt semantische hiërarchie | Afhankelijk van bronkwaliteit |
| Gespecialiseerd | Semantisch | Optimale contextbehoud | Rekenintensief; onvoorspelbare grenzen |

Het opsplitsen van de schrijfwijzer met klassieke methoden is niet geschikt. De regels bestaan vaak uit meerdere zinnen en gerelateerde subsecties. Een voorbeeld is de hoofdtitel **“Opbouw”**, met subsecties zoals _“Bedenk voordat je begint met schrijven wie de lezer is”_ en _“Bepaal de kernboodschap”_.