from random_forest import *


label_data = [1, 0, 0, 0, 1, 0, 0, 0]
prediction_class = [1, 1, 1, 1, 1, 1, 1, 1]
prediction_prob = [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.5]

compute_metrics(label_data, prediction_class, prediction_prob,[0,1],{'mass','calcification'})
