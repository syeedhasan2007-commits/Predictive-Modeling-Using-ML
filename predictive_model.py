import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
df = pd.read_csv("studentsPerformance.csv")

print(df.head())
df['Result'] = np.where(df['math score'] >= 50, 1, 0)

X = df[['reading score','writing score']]
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm,
            annot=True,
            fmt='d')

plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()


y_prob = model.predict_proba(X_test)[:,1]

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_prob
)

roc_auc = auc(fpr, tpr)

plt.plot(fpr,
         tpr,
         label=f"AUC = {roc_auc:.2f}")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()
plt.savefig("roc_curve.png")
plt.show()

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

pred = rf.predict(X_test)

print("Random Forest Accuracy:",
      accuracy_score(y_test, pred))