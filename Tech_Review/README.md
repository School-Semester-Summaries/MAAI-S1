# Tech Review

## Tech Review Presentation
On the 2nd of October we had our Tech Review presentation. For some reason we had the presentation after delivering the tech review, so we got feedback on the tech review twice.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | Link each requirement to a stakeholder. Each requirement must be traceable to a source, rationale, or reasoning. Do not add requirements without justification. Think more about technical requirements. For example: is the model allowed to run in the United States? Include your metrics in your requirements. Other than that, the requirements look good. | - |
| B1 | The final dataset must be included in the report. The table that you showed in the presentation is missing from the report. | - |
| B2/B3 | Section 4.3 has no introduction; it starts directly with "regression vs. classification." Explain why regression is chosen instead of classification. Why is it useful to choose regression in this case? How are you going to handle the fact that an error of 17 versus 27 is penalized the same as an error of 57 versus 67? Both have a difference of 10, but do you really want to penalize them equally? | - |

## Tech Review Grading
We delivered the ontwerp review on the 29th of September and received feedback from Michiel and Rick on the 9th of October.

| Learning Outcome | Feedback | Grading |
|------------------|-----------|----------|
| A2 | This is a good list of requirements, well elaborated and sorted. An improvement could be to assign an owner or a source to each requirement. Other feedback: this sentence lacks an actor: "The camera is covered until a choice is made to use AI for age verification." The technical requirement does not exclude the possibility that data leaves the device. The rationale for a requirement is not indicated; the justification is missing. Metrics are hardly mentioned. Is fairness even considered a requirement in your case? | Op Niveau |
| B1 | Three datasets are discussed. Your choice is justified, ultimately selecting UTKFace, but are you aware that the ages are not real? Data preprocessing with YOLO and other steps is very good, compliments. There is no evidence in the report that the classes are well distributed or how large the final dataset is. This was, however, discussed in the presentation. | Op Niveau |
| B2 | I notice that I get lost here. ResNet and VGG seem to be mixed up. A good introduction in 4.3(.1) could resolve a lot. The elaboration of the models, however, is done very well. | Op Niveau |
| B3 | Multiple iterations were carried out. Literature was searched and discussed, compliments. But because I was already lost at B2, I get stuck here as well. | Op Niveau |
| C2 | The graphs in figures 11 and 12 showing age-MAE are very good, compliments. "This is due to a smaller representation of this age group in the dataset." I have an idea of this, but it is not substantiated because the dataset is not made transparent for B1. Fairness, etc., still needs to be addressed, and you still have enough time for that. | Op Niveau |

We implemented all the feedback in the following way:
- A2: We linked each requirement to a stakeholder and rewrote the technical requirements. The technical requirements now include numerical values, which makes it possible to concretely assess when a requirement has been met. We also incorporated the metric (MAE) into one of the technical requirements.
- B1: We are aware that the ages are not real and have also used the DEX paper as a source to support decisions within our project. We forgot to include the data distribution in the submitted paper.
- B2: We wrote a new introduction for section 4.3, clarifying that ResNet50 is used purely as a baseline to compare the performance of the final model.
- B3: We implemented the feedback from B2, so B3 should now also be clearer.
- C2: We still plan to add the fairness section and have created a task for this.


