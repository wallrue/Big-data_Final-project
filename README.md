# NTUST_Big-data_Final-project: AI matchmaking - customer questions and preferences

## Introduction

This is repository for final project of Big data analysis course. Topic of final project is [AI matchmaking - customer questions & preferences](materials/第3組_AI_人工智慧_報告_v2_20220512_V2.pdf).
## Dataset Description
I. <strong>Raw dataset:</strong>

  [Raw dataset](dataset/project_textmining_rawdata_20220518) includes 2,526 eml files which imply 2,526 emails sent from customers. Those emails were gathered in the period from 2015 - 2018. The records from various sources such as Mail2000, MailCloud, MailGates, Green Edm.

  <strong>* Overview Dataset</strong>: The raw dataset is described as below image.
  
  <img src="dataset/raw_dataset_img.png" alt="1" width = auto height = auto>

II. <strong>Organized dataset:</strong>

  [Organized dataset](dataset/organized_dataset/) is result of converting raw dataset into compuatable format. In detail, 2,526 emails from raw dataset were allocated in an CSV file. This CSV file consists of 2,526 tuples corresponding to 2,526 emails and 7 attributes (﻿Date, Subject, From, From Email, To, Cc, Bcc, Body) of each email.

  <strong>* Overview Dataset</strong>: The organized dataset is described as below image.
  
  <img src="dataset/organized_dataset_img.png" alt="1" width = auto height = auto>

## <strong>Architecture and Methodology:</strong> 
I. <strong>Project statement:</strong> Find the topics and sentiment from unlabeled emails. Then, building a model for predictn 

II. <strong>Project description:</strong> The dataset contains 2,526 Outlook email without label. Therefore, the main process should be contained steps  

- Data convert and prepocessing  
- Using topic modeling to find the main topics of the dataset and in each email  
- Finding the sentiments expressed in the dataset and in each email  
- (if possible) verify the result of step 2 and 3 and labeling quality to decide futher classification model for new email coming.

III. <strong>Approaches:</strong> Using unsuperised model (and Semi-supervised if step 4 above is feasible)  

1. **Topics Analysis:** Using LDA (Latent Dirichlet Allocation) to find appropriate cluster number (number of topics) . Output: csv file of emails and their possible topics  

2. **Sentiment Analysis:**

- We explored  a sentiment dataset from Snownlp includes 16,548 samples for positive and 18,576 samples for negative. Then, we train a bayes-based model for giving sentiment score for input words as known as a sentiment classifier.

- We assessed content of an email is positive or negative by sentiment scores of words in this email from sentiment classifier. If the sentiment score is higher than 0.5, the content will be positive and vice verse.

IV. **Evaluation**   

Based on the result from sentient model and topic model. Each email will be demonstrated on a graph. The attribute of sentiment will be displayed by shape of points and attribute of topic will be displayed by color. Thorughout the graph, we can conclude the relation between sentiment and topic of each email. 

## <strong>Architecture and Methodology:</strong> 
  
  From organized dataset, we manipulate some pre-processing steps to get sentences which are corresponding to each email. Then, each sentence will be taken to model for classify unsupervisedly. 
  
  <img src="materials/architecture.png" alt="1" width = auto height = auto>  
  
  **tobeupdated**
  
## <strong>Task division:</strong> 
  
  * **Vo Van Truc**: Data handling (review data, organise data, clean dataset)
  * **洪郡澤 (Nick)**: Explore dataset, process data for training (topic analysis)
  * **Trinh TT Quynh**: Propose Idea, topic modeling, Experiment
  * **Le Minh Tuong**: Propose Idea, process data for training (sentiment analysis), manage project
  * **Nguyen PT Nguyen**: Decision making (visualization, conclusion, making decision)
  
  <img src="materials/workload.png" alt="1" width = auto height = auto>


