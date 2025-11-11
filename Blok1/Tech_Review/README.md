# Tech Review
We delivered the ontwerp review on the 29th of September and received feedback from Michiel and Rick on the 9th of October.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | Je hebt ten minste een lijst van ondubbelzinnige juridische, ethische, organisatorische en functionele en technische vereisten van de AI-oplossing. Deze zijn nader gedefinieerd aan de hand van de bestaande literatuur, experts of vereisten van belangrijke stakeholders. Deze zijn meegenomen in de ontwikkeling van de eindoplossing. | Op Niveau |
| B1 | Je maakt een opsomming van de datasets die worden gebruikt voor het trainen, fine-tunen en testen van je modellen. Je beschrijft de relevante kenmerken van de gekozen datasets voor de oplossing en onderbouwt je keuzes hierin. Gebruik bijvoorbeeld wetenschappelijke bronnen en voer een verkennende data-analyse uit, waarin de dataverdeling en mogelijke problemen zoals ontbrekende data en onevenwichtigheden worden onthuld. Deze data-analyse is op een technisch correcte manier toegepast. Dit komt terug in zowel het rapport als in code. | Op Niveau |
| B2 | Je beschrijft de gebouwde of geselecteerde (model)architecturen voor de gekozen oplossingsrichting. Hierbij beschrijf je welke metriek(en) je gebruikt om modellen te vergelijken en selecteren, evenals de onderbouwing van je keuzes. De toepassing is op een technisch correcte en methodologisch geaccepteerde wijze gedaan en dit kan het projectteam aantonen in de review | Op Niveau |
| B3 | Je dient een systematische aanpak te hanteren, waarin je duidelijk vermeldt hoe je je model traint of fine-tunet, valideert, optimaliseert, test en de resultaten communiceert. Voorlopige resultaten zijn op dit punt verplicht. | Op Niveau |
| C2 | Voor het evalueren van de kwaliteit van het AI-oplossing dien je ook andere door het veld erkende kwaliteitsmaten zoals robustness, scalability, explainability, model complexity en resource demand (en wellicht fairness metrics) in acht te nemen en te verantwoorden. Dit is op een technisch correcte wijze uitgevoerd en kan aangetoond worden in de review. | Op Niveau |

We implemented all the feedback in the following way:
- A2:  We hebben elke requirement gekoppeld aan een stakeholder. Ook hebben we de technische requirements herschreven. De technische requirements bevatten nu ook getallen, het voordeel hiervan is dat je concreet kunt beoordelen wanneer de requirement is voldaan. Ook hebben we de metric (MAE) verwerkt in een van de technische requirements. 
- B1: We zijn er van op de hoogte dat de leeftijden niet echt zijn en hebben de DEX paper ook gebruikt als bron om keuzes te onderbouwen binnen ons project. De data verdeling zijn we vergeten toe te voegen aan de ingeleverde paper. 
- B2: Nieuwe inleiding voor 4.3 geschreven. Duidelijk gemaakt dat de resnet50 puur als baseline wordt gebruikt om de prestaties van het uiteindelijke model te vergelijken. 
- B3: We hebben de feedback van B2 geïmplementeerd dus zou B3 nu ook duidelijker moeten zijn. 
- C2: De fairness zijn we nog van plan toe te voegen hier hebben we een taak voor aangemaakt
