Completely changing the layout, for old readme click [here](./README_old.md) 

---

# MAAI-S1 Portfolio (wip)
## Introductie
In deze README leg ik zo beknopt mogelijk uit wat ik allemaal heb gedaan. Belangrijke dingen om te weten, er zijn 4 leeruitkomsten (A, B, C, D) en 13 sub leeruitkomsten (A1, A2, A3, A4, B1, B2, B3, C1, C2, C3, D1, D2, D3). [Hier een beschrijving per leeruitkomst en sub-leeruikomst die golden voor MAAI-S1 Blok 1 (2025-2026)](./LearningOutcomes.md) (in blok 2 zijn de leeruitkomsten minimaal veranderd). Het eerste semester bestaat uit 2 blokken. Blok 1 is gericht op beeldherkenning (computer vision) en blok 2 is gericht op taalmodellen (Natural Language Processing). 

In het eerste semester waren er in totaal 18 datapunten. Een datapunt is een moment waarop je beoordeeld wordt op sub-leeruitkomsten. Een datapunt heeft geen vast aantal sub-leeruitkomsten waarop je beoordeeld wordt. Zo wordt het logboek (week 44) enkel op D1 beoordeeld, maar M&T opdracht 1a (week 39) op A2, B1, B2, B3 en C2 (Figuur 1).

<img width="1711" height="734" alt="B1" src="https://github.com/user-attachments/assets/6b92158d-5d5a-4a99-a72d-ca10bc72b94d" />

*Figuur 1: Datapunten Blok 1*

<img width="1888" height="819" alt="B2" src="https://github.com/user-attachments/assets/3997c731-5e65-4f9d-bbff-5d4473427f57" />

*Figuur 2: Datapunten Blok 2*


Bij de beoordeling op je datapunt, kun je 3 verschillende beoordelingen krijgen. Onder Niveau, Op Niveau en Boven Niveau. In deze repo gebruik ik emojis om aan te tonen welke beoordeling ik behaald heb.
- 🔴 Onder Niveau
- 🔵 Op Niveau
- ⭐ Boven Niveau

Aan het eind van het semester bepalen de docenten op holistische wijze of je het semester behaald hebt. Dit doen ze apart per leeruitkomst. Zo kijken ze voor leeruitkomst A naar alle sub-leeruitkomsten van A (A1, A2, A3, A4). Als alle 4 de sub-leeruitkomsten van A minimaal Op Niveau, dan heb je leeruitkomst A behaald. Als de sub-leeruikomsten niet leiden naar een duidelijke beoordeling gaan de docenten in beraad om samen tot een conclusie te komen. Uit gesprekken met docenten heb ik vernomen dat individuele datapunten en groeps-datapunten apart van elkaar worden bekeken, én dat individuele datapunten iets belangrijker zijn dan groeps-datapunten. Mocht je individueel alle sub-leeruitkomsten van A onder niveau hebben, maar in groeps alles boven niveau, dan heb je leeruikomst A hoogstwaarschijnlijk niet gehaald. Mocht je alle individuele sub-leeruikomsten van A boven niveau hebben maar in groeps alles onder, dan wordt je waarschijnlijk een bespreek geval.



# Vakken/Onderdelen
Er zijn x aantal vakken/onderdelen in het eerste semester: M&T (Statistiek en Machine Learning), Mini-Symposium (Artikels schrijven), Groep Project en het Logbook. Per vak wordt je beoordeeld op datapunten over verschillende sub-leeruitkomsten. Hieronder een overzicht per vak/onderdeel. 


## Bootcamp (wip)
De bootcamp was de eerste week van de master. In deze week ga je met een klein groepje een project casus verzinnen en een model bouwen en die aan het eind van de week presenteren aan de klas. In deze week wordt je nergens op beoordeeld

[link bootcamp dingen]

## M&T
We hebben in het eerste semester 4 verschillende M&T opdrachten gehad. In chronologische volgorder: 1a, 2a, 1b, 2b. M&T opdrachten zijn erg belangrijk voor leeruikomst B, aangezien het de enige manier is om de B sub-leeruitkomsten individueel aan te tonen. Hieronder mijn uitwerkingen en behaalde beoordelingen.

| Opdracht | Topic | A2 | B1 | B2 | B3 | C2 |
| ------------- | ------------- |-|-|-|-|-|
| [M&T 1a](./M&T/1a/) | Classification Task | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [M&T 2a](./M&T/1b/) | Machine Translation | 🔵 | 🔴 | 🔴 | 🔵 | 🔵 |
| [M&T 1b](./M&T/1b/) | Function Approximation | 🔵 | 🔵 | 🔴 | 🔵 | 🔴 |
| [M&T 2b](./M&T/2b/) | Semi-supervised learning with VAE | 🔵 | 🔴 | 🔵 | 🔴 | 🔵 |

<details>
  <summary><h4>➡️ Feedback on M&T Exercise 1a</h4></summary>
  
On the 20th of september I delivered my M&T 1a exercise, and on the 6th of Oktober Michelangelo (My M&T teacher) provided me feedback on my M&T 1a exercise.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | (+)<br>• vanuit de opdracht en data bepaalt wanneer het model ‘voldoende genoeg’ is.<br><br>(+-)<br>• Je had kunnen opmerken dat met zo een scheve verdeling, zoveel klasses en zo weinig waarnemingen niet elke klasse voldoende gerepresenteerd kan zijn.<br><br>(–)<br>• Je had kunnen opmerken dat het aantal waarnemingen laag is ten opzichte van het aantal variabelen. | 🔴 Onder Niveau |
| B1 | (+)<br>• Data is correct gesplitst.<br><br>(+-)<br>• Je maakt geen gebruik van een stratisfied split, terwijl dat in deze situatie wel de conventie is. Waarom?<br>• Herschaling wordt niet verantwoord.<br><br>(–)<br>• Je laat tussentijds testresultaten zien. Pas hiermee op. Als je beslissingen hebt genomen naar aanleiding van deze resultaten, dan is er sprake van data-leakage.<br><br>(––)<br>• Je doet een dataverkenning op de gehele dataset (zonder splitsing). Dit is niet volgens de conventies en kan leiden tot data-leakage. | 🔴 Onder Niveau |
| B2 | (+)<br>• Correcte verantwoording van nulmodel.<br><br>(–)<br>• Prestatiemaat wordt niet correct verantwoord.<br>• Het is onduidelijk uit welke modellen je gekozen hebt.<br>• De keuze van het model is niet logisch (KNN werkt niet goed bij veel waarnemingen).<br>• Verantwoording voor het model is niet overtuigend. Er zijn heel veel modellen die aan dat argument voldoen (classificatie en "een keer gehoord").<br>• Je besluit een variabelenselectie te gebruiken. De keuze voor de methode wordt niet verantwoord. | 🔴 Onder Niveau |
| B3 | (-)<br>• Niet van alle hyperparameters wordt de keuze verantwoord (ook "default" is een keuze) | 🔴 Onder Niveau |
| C2 | (+)<br>• Testresultaten van de modellen worden gegeven.<br>• Model wordt vergeleken met nulmodel.<br><br>(+-)<br>• Confusion matrix wordt gegeven, maar is lastig te interpreteren, omdat de labels niet overeenkomen met de klasses in de variabele S.<br><br>(–)<br>• Fouten van het model worden niet besproken.<br>• Jouw confusion matrix is 5 bij 5, terwijl er 6 klasses zijn. Hoe kan dat? | 🔴 Onder Niveau |

The feedback made me realize I took the exercise too lightly. The next time I will invest more time into the exercise and more time into researching and ellaboring my choices. Also a major finding after this grading is that I was one of the only ones that didn't use Generative AI to generate code since I thought it was forbidden. However, in class many students admitted to have used Generative AI and the teacher was fine with this as long as you were able to explain what is happening and elaborate why you do X. The usage of Generative AI will help me pass roadblocks easier and overall speeds up the coding process by a lot, allowing me to spend more time on the exercise.

</details>

<details>
  <summary><h4>➡️ Feedback on M&T Exercise 1b</h4></summary>
  
On the 15th of October 2025 I delivered my first version of the M&T 1b exercise and on the 16th I delivered my final version. The 4th of November I received feedback from Michelangelo, my M&T teacher.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | (+)<br>• Correcte bespreking van interpreteerbaarheid voor deze opdracht.<br>• Vanuit de opdracht en data bepaalt wanneer het model ‘voldoende genoeg’ is. | 🔵 Op niveau |
| B1 | (+)<br>• Correcte splitsing.<br><br>(–)<br>• Normalisatie niet correct besproken. | 🔴 Onder Niveau |
| B2 | (+)<br>• Nulmodel correct verantwoord.<br>• Geschikte architectuur gedeeltelijk gerelateerd aan f(x).<br><br>(+-)<br>• Keuze van activatiefunctie niet helemaal overtuigend. We willen de functie f(x) die uit tanh's is opgebouwd zien te benaderen. Je had gebruik mogen maken van die informatie.<br><br>(–)<br>• Foutmaat niet correct verantwoord. Je zegt: "aangezien MAE beter presteert dan MSE als er ruis is". Waar is dat op gebaseerd? Wat betekent dit precies?<br>• In deel 3 ga je hier verder op in: "omdat MAE grote outliers met een korrel zout neemt terwijl MSE het zoveel mogelijk probeert mee te nemen in de lijnvorm". Dit is niet echt precies verwoord, maar komt al dichter in de buurt van de werkelijkheid.<br>• De MSE en de MAE zullen anders omgaan met uitschieters. Wat heeft dat te maken met of er ruis is of niet? | 🔴 Onder Niveau |
| B3 | (+)<br>• Het onderzoekje naar learning rate (LR) is goed, maar misschien te gedetailleerd en op het verkeerde moment. Je zou liever niet achteraf op zoek gaan naar de beste LR, maar vanaf het begin. Zeker bij grotere modellen is vooral de orde van grootte belangrijk (bijv. 0.1, 0.01, 0.001).<br><br>(+-)<br>• Je schrijft in deel 3: "Om zeker te weten dat mijn model niet overfit is, predict ik ook de validatie set." Dat is inderdaad verstandig. Is het mogelijk om in deze situatie (complexiteit van model en aantal waarnemingen) te overfitten?<br><br>(–)<br>• Je merkt terecht op dat early-stopping een goed idee zou zijn geweest bij zo’n groot aantal epochs. Probeer jezelf aan te leren dat standaard te doen (of begin met een klein aantal epochs om te controleren of alles goed werkt en of er geleerd wordt). In latere fasen van de opleiding zullen de modellen en rekentijden veel groter zijn. | 🔵 Op niveau |
| C2 | (+)<br>• Correcte bespreking van prestatie (van eindmodel).<br>• Fout van het model vergeleken met dat van het nulmodel.<br><br>(+-)<br>• Interpretatie van coefficienten niet helemaal duidelijk. Je vergelijkt onderdelen van de werkelijke functie met die van de gevonden functie. Maar vergelijk je wel de juiste onderdelen met elkaar?<br>• Waarom vergelijk je de gewichten niet expliciet met elkaar (je had ze naast elkaar kunnen laten zien)?<br>• Minimum voor fout niet besproken. | 🔵 Op niveau |

I implemented the feedback from exercise 1a, and managed to improve 3 outcomes to "Op Niveau". My goal is to maintain this momentum and keep improving over the following M&T exercises. In class, I also asked Michalangelo to ellaborate his points on why I didn't receive Op Niveau on B1 and B2. For B1, the dataset was normalised but I didn't acknowledge that. At least I should acknowledge that and point it out. For B2, we are taught that default options are also decisions, but in this case it is okay to choose MSE if there is no valid reason to choose a different metric. In my case, I chose the MAE metric, but I wasn't able to validate correctly why I chose that metric, therefore my grade. I now understand why my teacher decided to give me "Onder Niveau" for these learning outcomes and I know now how to improve on them. The next time I will beter analyze the data and I will more carefully choose a metric.

</details>

<details>
  <summary><h4>➡️ Feedback on M&T exercise 2a </h4></summary>
  
On the 18th of December I received feedback on my 2a exercise.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | (+)<br>• Er is een lijst van eisen waarvan het duidelijk is wat de verbetering zou moeten zijn<br>• Er is een kwaliteitsmaat gegeven om de verbetering te kunnen meten | 🔵 Op niveau |
| B1 | (+)<br>• Splitsing correct gebruikt<br>• Voor- en nadelen van data besproken<br>• Voor- en nadelen van data gekoppeld aan model-kwaliteit, maar niet altijd correct verantwoord<br><br>(+/-)<br>• Voor- en nadelen van data soms gekoppeld aan kwaliteit van het model en vertalingen, maar niet altijd<br><br>(–)<br>• Je zegt: "In NLP kan dit een voordeel zijn, áls je de betekenissen van de woorden in acht neemt." Waar is dat op gebaseerd?<br>• Wat is het voordeel van een "diverse dataset"? | 🔵 Op niveau |
| B2 | (+)<br>• Keuze van prestatiemaat is verantwoord. Je hebt correct besproken dat dit niet de logische keuze is en dat de literatuur iets anders suggereert.<br><br>(-)<br>• Eerste iteratie is verantwoord (met bron) en deels gerelateerd aan de specifieke situatie<br>• De bron suggereert dat de vocabulary 20 duizend tokens zou moeten bevatten<br>• De bron suggereert niet dat n-grams nuttig zouden zijn in een sequence-model. Dit is wat ongewoon en zou echt beter verantwoord moeten worden. Standaard is juist dat je kiest tussen een sequence-model of een set-model met N-grams | 🔴 Onder Niveau | 
| B3 | (+)<br>• Basismodel werkend gekregen<br>• Verschillen met model uit slides besproken<br>• Eerste iteratie is uitgevoerd<br><br>(+/-)<br>• Tweede iteratie is verantwoord en gerelateerd aan resultaten, maar is wel een vreemde suggestie. N-grams combineren met een sequence-model is niet standaard. Heb je hier literatuur bij gevonden? | 🔵 Op niveau |
| C1 | (+)<br>• Modellen worden vergeleken op kwaliteitsmaat<br><br>(-)<br>• Fouten in vertalingen worden niet besproken<br>• Je evalueert de modellen op dezelfde dataset die gebruik maakt van de laatste tokenization. Dat lijkt mij geen eerlijke vergelijking.<br>• Je merkt op dat de test-prestatie in de buurt komt van de validatie-prestatie en noemt dat opmerkelijk. Onduidelijk is waarom dat je verbaast. | 🔴 Onder Niveau |

At first I didn't fully agree about B2, and I didn't understand C2. So I had a talk with Michelangelo about these learning outcomes. He explained me what he ment with the description in outcome C2, and it appeared that I made a small coding mistake. I noticed that the results were very strange but I didn't realize my code was faulty. So that's just whatever. We also talked about B2. I used Deep Learning with Python as reasoning for my approach, and the model did indeed get better! However, this approach was suggested for a **Set-Model** whilst the exercise was covering a **Sequence Model**. This is a detail that I didn't catch. I agreed with Michelangelo on both points. 2 silly minor mistakes, if I can learn anything here then it's just to make sure I 100% understand the exercise context and the resources that I am using since I overlooked that the source was specifically for Set-Models. AND, if I notice weird things happpen in my code such as an accuracy of 2% start wondering why that happens instead of just accepting it. I did ask classmates if anyone else was getting test scores of 2% but for some reason no-one was using the test set so I was really close to noticing it but unfortunately. I still have high hopes for exercise 2b since I know I am capable of getting "Op Niveau" on all the learning outcomes.


</details>

## Mini-Symposium
Mini-Symposium is de enige manier om sub-leeruitkomsten D2 en D3 aan te tonen. Hierdoor speelt het Mini-Symposium een erg grote factor in leeruitkomst D. Het onderdeel *Poster Presentatie zie je niet terug in het datapunten overzicht. De poster presentatie was een soort van herkansing om je presentatie skills opnieuw aan te tonen. Mocht je deze presentatie beter presenteren dan je Topic Presentatie, dan wordt het cijfer bij je topic presentatie vervangen door de poster presentatie.

| Opdracht | D2 | D3 |
| ------------- | ------------- |-|
| [Topic Presentatie](./Mini-Symposium/Mini-Symposium_Blok1_Presentation.pdf) | 🔴 -> 🔵* | 🔴 -> 🔴* |
| [PvA Artikel](./Mini-Symposium/Mini-Symposium_Blok1_PvA.pdf) | 🔴 | 🔴 |
| [Artikel](./Mini-Symposium/Mini-Symposium_Blok1_Artikel.pdf) | 🔴 | 🔴 |
| [*Poster Presentatie](./Mini-Symposium/Mini-Symposium_Blok1_Poster.pdf) | * | * |
| [Topic Presentatie 2](./Mini-Symposium/Mini-Symposium_Blok2_Presentation.pdf) | 🔵 | 🔵 |
| [PvA Artikel 2](./Mini-Symposium/Mini-Symposium_Blok2_PvA.pdf) | 🔴 | 🔴 |
| [Artikel 2](./Mini-Symposium/Mini-Symposium_Blok2_Artikel.pdf) | 🔵 | 🔵 |


## Coaching (Logbook)
Het enige onderdeel binnen coaching met datapunten is het logboek. In het logboek houd log je alle feedback die je hebt ontvangen van docenten. Het is in deze opleiding ook de bedoeling dat je zelf actief op zoek gaat naar feedback. Het logboek moet de volgende dingen bevatten volgens de studiehandleiding:
- Wat de feedback was,
- Waar deze over ging (bijv. code, samenwerking, onderzoeksaanpak),
- Hoe dit aansluit bij jouw leerdoelen of ontwikkeling,
- Wat jij ermee doet (accepteren, aanpassen, nog onderzoeken).

| Opdracht | D1 |
| ------------- | ------------- |
| Logboek Blok 1 | 🔵 |
| [Logboek Blok 1 en 2](./README_old.md) | ⭐ |

## Group Project (wip)
Project 1 ging over automatische leeftijdscontrole aan zelfscan kassa's. Project 2 ging over het versimpelen van gemeentelijke brieven. 

| Opdracht | Topic | A1 | A2 | A3 | A4 | B1 | B2 | B3 | C1 | C2 | C3 |
| ------------- | ------------- |-|-|-|-|-|-|-|-|-|-|
| Tech Review 1 | ... | - | 🔵 | - | - | 🔵 | 🔵 | 🔵 | - | 🔵 | - |
| Ontwerp Review 1 | ... | ⭐ | 🔵 | 🔴 | 🔵 | - | - | - | 🔵 | - | 🔴 | 
| Eindoplevering 1 | ... | ⭐ | ⭐ | 🔴 | 🔵 | 🔵 | 🔵 | ⭐ | 🔵 | 🔴 | 🔵 |
| Tech Review 2 | ... | - | 🔵 | - | - | ⭐ | 🔵 | 🔵 | - | 🔵 | - |
| Ontwerp Review 2 | ... |  🔵 | 🔵 | 🔵 | 🔴  | - | - | - | 🔵 | - | 🔵 | 
| Eindoplevering 2 | ... | ⭐ | ⭐ | 🔵 | 🔵 | ⭐ | 🔵 | 🔵 | 🔵 | 🔵 | 🔵 |



