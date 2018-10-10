from random_forest import *
import csv

csv_file = csv.reader(open("malignant_new.csv", "r"))

dcm_prob = []
dcm_class = []
dcm_label = []

for msg in csv_file:
    # print msg
    if msg[9] != "" and msg[10] != "" and msg[11] != "":
        if msg[9] != "dcm_rate":
            dcm_prob.append(float(msg[9]))
        if msg[10] != "dcm_bm":
            dcm_class.append(int(msg[10]))
        if msg[11] != "Pathological results\rBenign 0 and malignant 1":
            dcm_label.append(int(msg[11]))
print dcm_prob
print dcm_class
print dcm_label


label_data = [1, 0, 0, 0, 1, 0, 0, 0]
prediction_class = [1, 1, 1, 1, 1, 1, 1, 1]
prediction_prob = [0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.5]

# compute_metrics(label_data, prediction_class, prediction_prob,[0,1],{'mass','calcification'})
compute_metrics(dcm_label, dcm_class,dcm_prob,[0,1],{'mass','calcification'})
