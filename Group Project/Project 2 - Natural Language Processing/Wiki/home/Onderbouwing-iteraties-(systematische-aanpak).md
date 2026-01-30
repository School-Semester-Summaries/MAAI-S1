Voor het ontwikkelen van het LLM-model werden meerdere iteraties uitgevoerd. Eerst werd een baseline-model ontwikkeld, gebaseerd op de naïve-RAG-architectuur (Paragraaf \\ref{sec:Baseline model}). Vervolgens werd een eerste iteratie uitgevoerd, waarbij een vector database werd toegevoegd voor het ophalen van onderdelen uit de OVER-schrijfwijzer. In deze eerste iteratie werden alle zinnen aangepast, ook wanneer de aangepaste zin een slechtere LiNT-II-score opleverde dan de originele zin. Om dit te voorkomen, werd in de tweede iteratie een if-statement toegevoegd, zodat suggesties voor zinnen alleen werden weergegeven wanneer deze een lagere LiNT-II-score opleverden.

In een derde iteratie werd het model uit iteratie 2 gebruikt en onderzocht of het model beter presteerde wanneer de volgende woordenlijsten werden meegenomen bij het ontwikkelen van het model:

- Moeilijk-woordenboek van de Gemeente Amsterdam \\cite{moeilijkwoordenboek}
- Helder juridisch woordenboek van de Gemeente Amsterdam \\cite{juridischjargon}
- Inclusieve woordenlijst van de Gemeente Amsterdam \\cite{inclusievelijst}
- Synoniemenwoordenlijsten van B1-teksten \\cite{b1teksten, DijkenWaard}