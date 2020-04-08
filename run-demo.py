from flask import Flask, render_template, redirect, request, jsonify
from IPython import embed
import json
import numpy as np
from simpletransformers.classification import MultiLabelClassificationModel
import pickle
import random

# Call to preloading data
# 293 Answers:
ans_text = open('answers.txt').read().splitlines()
ans = []
for i in range(len(ans_text)):
    if(i%2==0):
        ans.append(ans_text[i])
# Preloaded Questions:
with open('questionset.pkl', 'rb') as f:
    tq = pickle.load(f)

random.seed(42)
random.shuffle(tq)
questionlist = ["Type your question below"] + tq
questiontext = [""] + tq

app = Flask(__name__)

# importing the saved Roberta Based model here:
model = MultiLabelClassificationModel('roberta', "data/checkpoint-102000", num_labels=291, use_cuda=False, args={'train_batch_size':8, 'gradient_accumulation_steps':1, 'learning_rate': 3e-5, 'num_train_epochs': 2, 'max_seq_length': 128, "fp16": False})

# Predictions
def getAnswer(paragraph):
    _, raw_outputs = model.predict([paragraph])
    print(float(raw_outputs[0][np.argmax(raw_outputs[0])]))
    if(raw_outputs[0][np.argmax(raw_outputs[0])]<0.95):
        return "I am sorry, your question does not provide enough detail for me to answer. Please rephrase your question."
    return ans[np.argmax(raw_outputs[0])]

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/select', methods=['GET', 'POST'])
def select():
    return jsonify(result={"context_title": questionlist ,"context_questions" : questiontext})

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    question = request.args.get('qid')
    answer = getAnswer(question)
    print (question, answer)
    return jsonify(result=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1995, threaded=True)

