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
- A2: We linked each requirement to a stakeholder and rewrote the technical requirements. The technical requirements now include numerical values, which makes it possible to concretely assess when a requirement has been met. We also incorporated the metric (MAE) into one of the technical requirements.
- B1: We are aware that the ages are not real and have also used the DEX paper as a source to support decisions within our project. We forgot to include the data distribution in the submitted paper.
- B2: We wrote a new introduction for section 4.3, clarifying that ResNet50 is used purely as a baseline to compare the performance of the final model.
- B3: We implemented the feedback from B2, so B3 should now also be clearer.
- C2: We still plan to add the fairness section and have created a task for this.


