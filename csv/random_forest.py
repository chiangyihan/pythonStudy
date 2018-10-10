import os
import sys
import numpy as np
import pandas as pd
import argparse
# import cv2
from sklearn.ensemble import RandomForestClassifier as rtc
from sklearn.externals import  joblib
from metrics import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

TUMOR_LABEL=0
NORMAL_LABEL=1

def compute_metrics(label_data,prediction_class,prediction_prob,labels,class_string):
    out_dir = ""
    post_str = ""
    plt.figure()
    plt.subplot(1,2,1)
    ##### Confusion Matrix
    sklearn_confusion_matrix(label_data,prediction_class,labels=labels,classes=class_string)

    plt.subplot(1,2,2)
    plt.axis('off')
    ##### Acc Precision Recall,F1
    acc,precision,recall,f1 = sklearn_computer_metrics(label_data,prediction_class)

    font_size=16
    plt.text(0.1,0.2,'accuracy = '+str(acc),fontsize=font_size)
    plt.text(0.1,0.4,'precision = '+str(precision),fontsize=font_size)
    plt.text(0.1,0.6,'recall = '+str(recall),fontsize=font_size)
    plt.text(0.1,0.8,'f1 = '+str(f1),fontsize=font_size)

    cm_out_png = os.path.join(out_dir,'confusion_matrix_'+str(post_str)+'.png')
    plt.savefig(cm_out_png)
    print('Save to '+ cm_out_png)
    ##### ROC AUC
    plt.figure()
    sklearn_roc_auc(label_data,prediction_prob)
    tumor_roc_out_png = os.path.join(out_dir,'tumor_roc_'+str(post_str)+'.png')
    plt.savefig(tumor_roc_out_png)
    print('Save to ' + tumor_roc_out_png)

