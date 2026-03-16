Als uitgangspunt voor de vergelijking met het ontwikkelde naïve-RAG-model is gekozen voor een baseline op basis van een generiek large language model (LLM) dat teksten herschrijft naar eenvoudiger Nederlands. Dit model werkt uitsluitend met een vaste, korte prompt en dient als referentiepunt voor latere iteraties waarin extra context wordt toegevoegd, zoals de OVER-schrijfwijzer en externe woordenlijsten. Voor de baseline is hetzelfde taalmodel gebruikt als in de naïve-RAG-architectuur.

De eerder geprepareerde validatieset, bestaande uit brieven van OVER-gemeenten, is ingeladen en per zin herschreven met behulp van één uniforme prompt. Deze prompt is bewust eenvoudig gehouden om de prestaties van een generiek LLM te meten, zonder invloed van aanvullende richtlijnen, domeinkennis of expliciete schrijfregels. De gebruikte prompt luidde:

_“Je bent een assistent die teksten herschrijft naar eenvoudiger Nederlands (B1-niveau).\
Herschrijf de volgende tekst:\
Prompt\
Geef uitsluitend de herschreven tekst, zonder toelichting.”_

Met deze aanpak wordt inzicht verkregen in hoeverre een LLM, zonder domeinspecifieke instructies of expliciete schrijfprincipes, in staat is om gemeentelijke teksten te vereenvoudigen. De resultaten van deze baseline vormen het uitgangspunt voor vergelijking met vervolgmodellen waarin onder meer de OVER-schrijfwijzer en human-in-the-loop-principes zijn geïntegreerd.