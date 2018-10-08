import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve,auc


def plot_confusion_matrix(cm,classes,normalize=False,title='Confusion Matrix',cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:,np.newaxis]
        print('Normalized confusion matrix')
    else:
        print('Confusion matrix without normalization')
   #plt.subplots_adjust(left=0.25)
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()

    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks,classes)
    plt.yticks(tick_marks,classes,rotation=90)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,format(cm[i,j],fmt),
                 horizontalalignment='center',
                 color='white' if cm[i,j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def sklearn_confusion_matrix(y_true,y_pred,labels,classes=['0','1'],show_flag=True,normalize=False,title='ConfusionMatrix',cmap=plt.cm.Blues):
    cm = confusion_matrix(y_true,y_pred,labels)
    if show_flag:
        plot_confusion_matrix(cm,classes,normalize,title,cmap)
    return cm

def sklearn_computer_metrics(label_data,prediction_class):
    acc = accuracy_score(label_data,prediction_class)
    precision = precision_score(label_data,prediction_class)
    recall = recall_score(label_data,prediction_class)
    f1 = f1_score(label_data,prediction_class)
    fmt = '.3f'
    acc = format(acc,fmt)
    precision = format(precision,fmt)
    recall = format(recall,fmt)
    f1 = format(f1,fmt)
    return acc,precision,recall,f1

def sklearn_roc_auc(label_data,predict_prob,pos_label=None):
    fpr,tpr,thresh = roc_curve(label_data,predict_prob,pos_label)
    auc_score = auc(fpr,tpr)
    lw = 2

    plt.plot(fpr,tpr,color = 'deeppink',lw=lw,label='ROC curve(area = %0.2f)' % auc_score)
    plt.plot([0,1],[0,1],color='navy',lw=lw,linestyle='--')
    plt.xlim([0.0,1.0])
    plt.xlim([0.0,1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Pathology--Tumor--ROC')
    plt.legend(loc='lower right')
    return auc_score
