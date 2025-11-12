# Feedback
In this document I present the feedback I received, the related work, the linked learning outcomes and how I used this feedback.

- [Eindoplevering](#eindoplevering)
- [M&T](mt)

## Eindoplevering
...

## M&T
In this section I cover the exercises I made for M&T, the feedback I received and how I used this feedback.

- [M&T 1a Exercise](#mt-1a-exercise)
- [M&T 1b Exercise](#mt-1b-exercise)

### M&T 1a Exercise
On the 20th of september I delivered my M&T 1a exercise, and on the 6th of Oktober Michelangelo (My M&T teacher) provided me feedback on my M&T 1a exercise.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | (+)<br>• vanuit de opdracht en data bepaalt wanneer het model ‘voldoende genoeg’ is.<br><br>(+-)<br>• Je had kunnen opmerken dat met zo een scheve verdeling, zoveel klasses en zo weinig waarnemingen niet elke klasse voldoende gerepresenteerd kan zijn.<br><br>(–)<br>• Je had kunnen opmerken dat het aantal waarnemingen laag is ten opzichte van het aantal variabelen. | Hier is nog werk nodig |
| B1 | (+)<br>• Data is correct gesplitst.<br><br>(+-)<br>• Je maakt geen gebruik van een stratisfied split, terwijl dat in deze situatie wel de conventie is. Waarom?<br>• Herschaling wordt niet verantwoord.<br><br>(–)<br>• Je laat tussentijds testresultaten zien. Pas hiermee op. Als je beslissingen hebt genomen naar aanleiding van deze resultaten, dan is er sprake van data-leakage.<br><br>(––)<br>• Je doet een dataverkenning op de gehele dataset (zonder splitsing). Dit is niet volgens de conventies en kan leiden tot data-leakage. | Hier is nog werk nodig |
| B2 | (+)<br>• Correcte verantwoording van nulmodel.<br><br>(–)<br>• Prestatiemaat wordt niet correct verantwoord.<br>• Het is onduidelijk uit welke modellen je gekozen hebt.<br>• De keuze van het model is niet logisch (KNN werkt niet goed bij veel waarnemingen).<br>• Verantwoording voor het model is niet overtuigend. Er zijn heel veel modellen die aan dat argument voldoen (classificatie en "een keer gehoord").<br>• Je besluit een variabelenselectie te gebruiken. De keuze voor de methode wordt niet verantwoord. | Hier is nog werk nodig |
| B3 | (-)<br>• Niet van alle hyperparameters wordt de keuze verantwoord (ook "default" is een keuze) | Hier is nog werk nodig |
| C2 | (+)<br>• Testresultaten van de modellen worden gegeven.<br>• Model wordt vergeleken met nulmodel.<br><br>(+-)<br>• Confusion matrix wordt gegeven, maar is lastig te interpreteren, omdat de labels niet overeenkomen met de klasses in de variabele S.<br><br>(–)<br>• Fouten van het model worden niet besproken.<br>• Jouw confusion matrix is 5 bij 5, terwijl er 6 klasses zijn. Hoe kan dat? | Hier is nog werk nodig |

The feedback made me realize I took the exercise too lightly. The next time I will invest more time into the exercise and more time into researching and ellaboring my choices.

### M&T 1b Exercise
On the 15th of October 2025 I delivered my first version of the M&T 1b exercise and on the 16th I delivered my final version. The 4th of November I received feedback from Michelangelo, my M&T teacher.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | (+)<br>• Correcte bespreking van interpreteerbaarheid voor deze opdracht.<br>• Vanuit de opdracht en data bepaalt wanneer het model ‘voldoende genoeg’ is. | Op niveau |
| B1 | (+)<br>• Correcte splitsing.<br><br>(–)<br>• Normalisatie niet correct besproken. | Hier is nog werk nodig |
| B2 | (+)<br>• Nulmodel correct verantwoord.<br>• Geschikte architectuur gedeeltelijk gerelateerd aan f(x).<br><br>(+-)<br>• Keuze van activatiefunctie niet helemaal overtuigend. We willen de functie f(x) die uit tanh's is opgebouwd zien te benaderen. Je had gebruik mogen maken van die informatie.<br><br>(–)<br>• Foutmaat niet correct verantwoord. Je zegt: "aangezien MAE beter presteert dan MSE als er ruis is". Waar is dat op gebaseerd? Wat betekent dit precies?<br>• In deel 3 ga je hier verder op in: "omdat MAE grote outliers met een korrel zout neemt terwijl MSE het zoveel mogelijk probeert mee te nemen in de lijnvorm". Dit is niet echt precies verwoord, maar komt al dichter in de buurt van de werkelijkheid.<br>• De MSE en de MAE zullen anders omgaan met uitschieters. Wat heeft dat te maken met of er ruis is of niet? | Hier is nog werk nodig |
| B3 | (+)<br>• Het onderzoekje naar learning rate (LR) is goed, maar misschien te gedetailleerd en op het verkeerde moment. Je zou liever niet achteraf op zoek gaan naar de beste LR, maar vanaf het begin. Zeker bij grotere modellen is vooral de orde van grootte belangrijk (bijv. 0.1, 0.01, 0.001).<br><br>(+-)<br>• Je schrijft in deel 3: "Om zeker te weten dat mijn model niet overfit is, predict ik ook de validatie set." Dat is inderdaad verstandig. Is het mogelijk om in deze situatie (complexiteit van model en aantal waarnemingen) te overfitten?<br><br>(–)<br>• Je merkt terecht op dat early-stopping een goed idee zou zijn geweest bij zo’n groot aantal epochs. Probeer jezelf aan te leren dat standaard te doen (of begin met een klein aantal epochs om te controleren of alles goed werkt en of er geleerd wordt). In latere fasen van de opleiding zullen de modellen en rekentijden veel groter zijn. | Op niveau |
| C2 | (+)<br>• Correcte bespreking van prestatie (van eindmodel).<br>• Fout van het model vergeleken met dat van het nulmodel.<br><br>(+-)<br>• Interpretatie van coefficienten niet helemaal duidelijk. Je vergelijkt onderdelen van de werkelijke functie met die van de gevonden functie. Maar vergelijk je wel de juiste onderdelen met elkaar?<br>• Waarom vergelijk je de gewichten niet expliciet met elkaar (je had ze naast elkaar kunnen laten zien)?<br>• Minimum voor fout niet besproken. | Op niveau |

I implemented the feedback from exercise 1a, and managed to improve 3 outcomes to "Op Niveau". My goal is to maintain this momentum and keep improving over the following M&T exercises.

