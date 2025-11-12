# Mini-Symposium
...

## PvA (Plan van Aanpak / Research Approach)
On the 26th of September 2025 I delivered my PvA and on the 7th of October I received feedback from Marcio.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| D2 & D3 | Hello Kaan,<br>Thank you for submitting your PvA. It is a good start. Below are my comments to help you refine your paper.<br><br>**Introduction**<br>(-) String statements are made without any supporting references. The entire introduction lacks citations. For example: "Deep learning methods, especially Convolutional Neural Networks (CNNs), have achieved high accuracy in predicting age from facial images." → Based on which source?<br>(-) The PvA promises more than it can realistically deliver: "By analysing dataset characteristics, training models on both imbalanced and balanced data, and testing bias mitigation methods, the study seeks to provide practical insights for developing models that try to reduce the bias between genders and try to get the results as equal as possible." At most, you can propose measuring bias and testing one or more mitigation techniques (e.g., undersampling, oversampling), but not overstate/oversell the outcomes.<br>(-) Sections contain redundant and overlapping information. Make the introduction more concise and less repetitive.<br>(-) Many strong statements without backing references: e.g. "So far, few studies have measured how much bias exists or how it affects model performance." → Based on which source?<br>(-) You propose training a CNN from scratch. What is the motivation for this instead of using pre-trained, off-the-shelf models? Defining your own architecture may reduce the experiment's relevance. If you want to pursue this, ensure that the architecture has already been used for age estimation.<br><br>**Research Question**<br>(-) The three research questions vary too much in depth and focus. Consider formulating a single main research question instead. For example: Quantifying gender bias in models X and Y on dataset Z, and investigating whether sampling techniques are useful to reduce this bias.<br>(=) You can also create sub-questions that support this central question. For instance:<br>• Sub-question 1: What can exploratory data analysis (EDA) reveal about the distribution of gender and age in the dataset?<br>• Sub-question 2: How can bias be measured and quantified in model performance across genders?<br>• Sub-question 3: Do sampling techniques (e.g., undersampling, oversampling) improve fairness while maintaining accuracy?<br><br>**Literature Review**<br>(-) Minimal set of references. The literature on this subject is extensive; it is surprising to find so few references in your draft.<br><br>**Methodology**<br>(-) You should justify why you are using MAE. It implies a regression setting, but why not RMSE or other regression metrics? Also, there are many fairness/bias metrics in the literature (e.g., demographic parity difference or equalised odds)<br>(-) Be very clear on which sampling technique(s) you will use—this is not the time to leave it open.<br>(-) If you are planning to train a model, you should specify in detail how you will split data (train/validation/test). Indicate whether the split is stratified or random, and describe how you will optimise the model and with which technique.<br>(=) To go beyond: Use statistical tests (t-tests, ANOVA, ... ) across subgroups to make your conclusions even more credible.<br> | Hier is nog werk nodig |

To sum it up, I implemented the feedback in my paper by reducing overlap, scaling down the research and being more specific about what I am going to do. Also, I tried to add sources for claims I make, but I think my research could use more references do make it stronger.


## Presentations

### PvA Presentation
On the 3rd of October I presented my PvA to Marcio and directly after received my feedback on DLO.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| D1 / D2 | • You presented in less than 3 minutes, whereas the amount of time was 10 minutes.<br>• You should give better definitions of some terms, like Model Types.<br>• Research questions should be more specific towards one technique or another <br>• The problem you chose is around the disparity of data between males and females | Hier is nog werk nodig / <br>Hier is nog werk nodig |

I disagree with the first point. Yes, it was very short, but we weren't informed how long the presentation was ment to be. I scaled down the research drastically, and made all the unclarities clear (the PvA was a collection of vagueness).

### Poster Presentation

On the 6th of November I presented my poster to Lamia Elloumi and on the 7th of november I received an update: a comment on my poster presentation and an upgraded grade.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| D2 | Thank you for your poster presentation. Your presentation was fine, and as you noted there were few mistakes in your poster.<br>We are upgrading D2 from onder niveau to op niveau.| Op Niveau |

Partially agree since there was only one mistake in the poster. But I am satisfied with the grade.


## Artikel
...
