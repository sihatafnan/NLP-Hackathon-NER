# nlp_hackathon_bd_2023

## 1. Instructions
1. Download the data to your computing environment from https://github.com/cryptexcode/nlp_hackathon_bd_2023

2. Start analysing the data and developing your models.

3. We expect you to develop two models. One can involve fine-tuning/training neural (deep learning) models and at least one feature-based model is a must. Macro F1 will be used as the official evaluation metric.
4. Maintain a development log and a project report.

The test set will be pushed to this repository two hours before the hackathon ends.

## 2. Scoring Criteria 
A total score will be computed from three broad elements. We will use a weighted scoring scheme. 

a) Macro F1 achieved by the developed models [65% weight]

You can submit predictions from two models. One is primary, and another is secondary. One of the model should be a handcrafted feature based model, and another can be a deep learning based model. The best model will be considered as the primary model and will carry 50% weight towards the final score. Secondary model’s score will carry 15% weight.

b) Report Document and development log [25% weight]

* [10 points] Exploratory data analysis and interesting insights on the data.

* [30 points] A Methodology section: Description of the methods behind each model. Motivations behind each modeling choice/decision. 

* [30 points] A Results section: A table containing the results for each model/feature experimented with. Explaining the results with for the final models.

    [10 points] Analysis of the models (what worked well, what not so good, strength and weakness of each approach). What can be done as the next steps for modeling.

* [20 points] Complete experiment and discussion logs as bullet points. An example can be https://docs.google.com/document/d/1qbIkhd6bvbOsJOWXL7SfKQ0jey3MWQYQb_SshqH1LII/edit#heading=h.j2xflyo7glz.
We expect that reading this will help us to know how the team iteratively developed the final systems.


c) Source Code [10% weight]
Clean, readable, and well-organized code will get more points.




## 3. What to submit
1. Two txt files with the predicted labels. Name them as 'deep_model.txt' for predictions for a deep neural net based model, and 'feature_model.txt' for predictions made from a model built with handcrafted features. If you work on only one model, submit only one file with the appropriate name.

2. A Doc file, Microsoft Word/ Latex is fine.

3. Create a public github repository and push everything generated as part of the hackathon. Put the URL in the doc.


### 3.1 Prediction File Format
Put the predicted label for each token at each line. For example, for this sample test file,
```
তিনি _ _ O
বর্তমানে _ _ O
জাপানের _ _ B-GRP
সাংবিধানিক _ _ I-GRP
গণতান্ত্রিক _ _ I-GRP
দল _ _ I-GRP
এর _ _ O
সদস্য। _ _ O

সিরিজটি _ _ O
প্রযোজনা _ _ O
করেছে _ _ O
জোনাথন _ _ B-PER
এম _ _ I-PER
শিফ _ _ I-PER
। _ _ O
```

The prediction file should be like this

```
O
O
B-GRP
I-GRP
I-GRP
I-GRP
O
O

O
O
O
B-PER
I-PER
I-PER
O
```

## 4. What to avoid
1. Submitting predictions from a publicly available model without own work/effort.
2. Using labels from any other sources rather than the model predicted labels.
3. Simply copy-pasting code from tutorials or blogs than doing own work. You are free to use any public resource like code, pre-trained models, knowledge base. But your report should highlight **what have you done**.

**Please list all the links of the resources that you have used.**