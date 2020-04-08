# Evaluating the Roberta model
import numpy as np
from simpletransformers.classification import MultiLabelClassificationModel
lines = open('answers.txt').read().splitlines()
ans = []
for i in range(len(lines)):
    if(i%2==0):
        ans.append(lines[i])

# test_questions.txt and test_answers.txt should be the testing set.
testq = open('test_questions.txt').read().splitlines()
tq = []
for i in range(len(testq)):
    if(i%2==0):
        tq.append(testq[i])

testa = open('test_answers.txt').read().splitlines()
ta = []
for i in range(len(testa)):
    if(i%2==0):
        ta.append(int(testa[i]))

# this will store how many questions were correct in TOP-1 out of all the questions in the test set.
c = 0

# Loading the weights of the pre-trained Roberta based finetuned model for the task
model = MultiLabelClassificationModel('roberta', "data/checkpoint-102000", num_labels=291, use_cuda=False, args={'train_batch_size':8, 'gradient_accumulation_steps':1, 'learning_rate': 3e-5, 'num_train_epochs': 2, 'max_seq_length': 128, "fp16": False})
# Predictions
predictions, raw_outputs = model.predict(tq)
# Right
rt = []
# Wrong
wr = []

for i in range(len(raw_outputs)):
    print(i)
    if(np.argmax(raw_outputs[i]) == ta[i]):
        rt.append(tq[i])
        c = c + 1
    else:
        wr.append(tq[i])
        wr.append(raw_outputs[i][np.argmax(raw_outputs[i])])

print("Correct ans:")
print(rt)
print("Wrong ans:")
print(wr)
print("")
print("Result:")
print(c)
