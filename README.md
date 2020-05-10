# Question and Answer Matching

Given a pre-defined set of questions and its responses just like a set of FAQ's we try to predict
an appropriate response for a user defined query.

We frame the problem as the Multilabel Classification Problem capitalizing on the power of the
state of the art models, RoBerta in this project. Also we use a novel training approach to mitigate
the lack of the training data across the closed domain.

# Getting Started

Install the dependencies in the requirements.txt:

# To run the demo :

python3 run-demo.py

then open the link on the browser: http://0.0.0.0:1995/

this can be modified in the run-demo.py file.

# To train the model for the QnA Matching (Roberta),

python3 train_roberta.py

# To use a pretrained model and get the accuracy score,

python3 roberta.py


## Authors/Contact

**Rajat Mittal**- Jan 2020 - May 2020


## Acknowledgments

**Andrew Koh Jin Jie** and **Prof. Chng Eng Siong**  **Nanyang Technological University**
For the mentorship and assitance.


