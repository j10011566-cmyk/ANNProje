import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

DATA_PATH = "titanic.csv"
df = pd.read_csv(DATA_PATH)

df = df[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df['Sex'] = df['Sex'].map({'male':0,'female':1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

X = df.drop('Survived', axis=1)
y = df['Survived']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)
print("Logistic Regression Test Accuracy:", acc_lr)

ann_model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

ann_model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

history = ann_model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    verbose=0
)

y_pred_prob_ann = ann_model.predict(X_test)
y_pred_ann = (y_pred_prob_ann > 0.5).astype(int)
acc_ann = accuracy_score(y_test, y_pred_ann)
print("ANN Test Accuracy:", acc_ann)

plt.figure(figsize=(8,6))
models = ['Logistic Regression', 'ANN']
accuracy = [acc_lr, acc_ann]
colors = ['skyblue', 'lightgreen']

sns.barplot(x=models, y=accuracy, palette=colors)
plt.ylim(0,1)
plt.title("Model Karşılaştırması - Test Accuracy")
plt.ylabel("Accuracy")
for i, v in enumerate(accuracy):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

fig, axes = plt.subplots(1,2, figsize=(12,5))

cm_lr = confusion_matrix(y_test, y_pred_lr)
sns.heatmap(cm_lr, annot=True, fmt='d', ax=axes[0], cmap="Blues")
axes[0].set_title("Logistic Regression CM")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")

cm_ann = confusion_matrix(y_test, y_pred_ann)
sns.heatmap(cm_ann, annot=True, fmt='d', ax=axes[1], cmap="Greens")
axes[1].set_title("ANN CM")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

plt.show()

print("Logistic Regression Classification Report:\n", classification_report(y_test, y_pred_lr))
print("ANN Classification Report:\n", classification_report(y_test, y_pred_ann))

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title("ANN Loss Grafiği")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title("ANN Accuracy Grafiği")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
