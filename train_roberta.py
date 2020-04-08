import torch
import tqdm
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
from sklearn.model_selection import train_test_split
from simpletransformers.classification import MultiLabelClassificationModel

# import the training set
train_df = pd.read_csv("data/3_permutations_original_sampled.csv",header=None)
li = train_df[1]
multilbl = []
for i in range(len(li)):
    temp = li[i][1:-1]
    temp = temp.split(',')
    lis = [int(a) for a in temp]
    multilbl.append(lis)

# Preparing the data for training
one_hot = MultiLabelBinarizer()
arr = one_hot.fit_transform(multilbl)
arr = list(arr)
txt = train_df[2]
d = {'text': txt, 'labels': arr}
df = pd.DataFrame(d)
df['text'] = df['text'].apply(lambda x: x.replace('\n', ' '))

train_df, eval_df = train_test_split(df, test_size=0.2, random_state=42)

# Using Roberta Model for Multilabel Classification
model = MultiLabelClassificationModel('roberta', "roberta-base", num_labels=291, use_cuda=True, args={'train_batch_size':8, 'gradient_accumulation_steps':1, 'learning_rate': 3e-5, 'num_train_epochs': 4, 'max_seq_length': 128, "fp16": False})

model.train_model(train_df)

result, model_outputs, wrong_predictions = model.eval_model(eval_df)

