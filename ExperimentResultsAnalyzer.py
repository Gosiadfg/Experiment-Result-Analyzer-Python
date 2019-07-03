import random
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.utils.fixes import signature
from sklearn.metrics import average_precision_score
from sklearn.metrics import accuracy_score, roc_curve, auc

#dlugosc listy rekomendacyjnej
n=2000

#najlepsza rekomendacja
t1=[]

for i in range(n):
	t1.append(random.randrange(0, 2))
	
#rekomendacja 25% prawid³owa
t4=[]

for i in range(n):
		if i<=n/4:
			t4.append(t1[i])
		else: t4.append(random.randrange(0, 2))

#œrednia rekomendacja
t2=[]

for i in range(n):
	t2.append(random.randrange(0, 2))

#rekomendacja 75% prawid³owa
t5=[]

for i in range(n):
		if i<=(n-n/4):
			t5.append(t1[i])
		else: t5.append(random.randrange(0, 2))

#najgorsza rekomendacja
t3=[]

for i in range(n):
	if t1[i] is 0:
		t3.append(1)
	if t1[i] is 1:
		t3.append(0)

#average_precision = average_precision_score(t1, t1)
average_precision = average_precision_score(t1, t2)
#average_precision = average_precision_score(t1, t3)

print('Average precision-recall score: {0:0.2f}'.format(average_precision))

#precision, recall, _ = precision_recall_curve(t1, t1)
precision, recall, _ = precision_recall_curve(t1, t2)
#precision, recall, _ = precision_recall_curve(t1, t3)

step_kwargs = ({'step': 'post'}
				if 'step' in
signature(plt.fill_between).parameters
				else {})
plt.step(recall, precision, color='b', alpha=0.2, where='post')
plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
average_precision))

y_true = t1

#y_pred = t1
#y_pred = t2
y_pred = t3

print("Accuracy", accuracy_score(y_true, y_pred))

fpr, tpr, _ = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)

lw=2

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=1, label='ROC curve
(area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()