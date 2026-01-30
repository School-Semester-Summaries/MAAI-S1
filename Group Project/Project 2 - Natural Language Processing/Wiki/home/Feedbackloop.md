## Feedbackloop en doorontwikkeling van de AI-tool

Om de AI-tool na implementatie in de praktijk verder te verbeteren, wordt een feedbackloop ingericht die inzicht geeft in het gebruik en de effectiviteit van de gegenereerde schrijfsuggesties. Hierbij wordt onderscheid gemaakt tussen **evolving** en **adaptive** verbetermechanismen.

### **Evolving verbetering**

De evolving component richt zich op periodieke hertraining van het taalmodel met nieuwe, externe en algemeen beschikbare taaldata (bijvoorbeeld actuele B1-richtlijnen of geactualiseerde schrijfwijzers). Deze vorm van verbetering is niet gebaseerd op gebruikersfeedback, maar op inhoudelijke verrijking van het model. De evolving aanpak valt daarom buiten de directe feedbackloop, maar draagt wel bij aan de structurele kwaliteit en actualiteit van het model.

### **Adaptive verbetering (gebruikersfeedback)**

De kern van de feedbackloop is de adaptive component. Tijdens het gebruik van de AI-tool in Microsoft Word krijgen medewerkers per suggestie verschillende keuzemogelijkheden, zoals:

* _Accepteren_ van de suggestie
* _Aanpassen_ van de suggestie
* _Negeren_ van de suggestie
* _Nieuwe suggestie_ aanvragen

Deze interacties vormen impliciete gebruikersfeedback. Zonder extra handelingen of vragen voor de gebruiker kan worden vastgelegd hoe suggesties in de praktijk worden gebruikt. Bij implementatie in de praktijk kan deze feedbackloop worden gevalideerd door het gebruik te analyseren, zonder medewerkers expliciet te vragen naar hun voorkeuren of meningen.

### **Analyse en optimalisatie**

Als analysemethode zullen de volgende gegevens (geanonimiseerd) kunnen worden verzameld en geëvalueerd:

* Het percentage suggesties dat wordt geaccepteerd, aangepast of genegeerd
* Het type zinnen waarbij suggesties vaker worden overgenomen of juist niet
* De mate van overlap tussen oorspronkelijke zinnen en uiteindelijke versies

Door zowel de oorspronkelijke als de aangepaste zinnen te analyseren, krijgen ontwikkelaars inzicht in welke formuleringen goed aansluiten bij de praktijk en waar het model verbetering nodig heeft. Deze inzichten kunnen worden gebruikt om de suggesties voor zinnen, prioritering en formuleringen van het model verder te optimaliseren.

### **Privacy en persoonsgegevens**

Omdat gemeentelijke brieven persoonsgegevens kunnen bevatten, wordt privacybescherming expliciet meegenomen in de feedbackloop. Bij de opslag en analyse van zinnen kan gebruik worden gemaakt van technieken zoals Named Entity Recognition (NER) om persoonsgegevens (zoals namen, adressen en BSN’s) automatisch te herkennen en te anonimiseren \[1\]. Hierdoor wordt voorkomen dat ontwikkelaars toegang krijgen tot herleidbare persoonsgegevens. Wel is aanvullend onderzoek nodig om te bepalen welke anonimiseringstechnieken hiervoor het meest geschikt en betrouwbaar zijn.

Daarnaast bestaat een groot deel van gemeentelijke brieven uit vaste tekststructuren met invulvelden voor persoonlijke informatie. Deze velden kunnen standaard worden geanonimiseerd of uitgesloten van analyse. Optioneel kan de medewerker die de brief opstelt persoonlijke informatie in een zin visueel markeren, zodat deze gegevens automatisch geanonimiseerd worden. Op deze manier wordt voorkomen dat ontwikkelaars privacygevoelige inhoud te zien krijgen tijdens het beoordelen, analyseren en optimaliseren van de AI-tool.

\[1\] https://www.ibm.com/think/topics/named-entity-recognition