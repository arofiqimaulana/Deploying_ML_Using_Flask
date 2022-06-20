from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Data
iris = load_iris()
X = iris.data
y = iris.target

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Model
model = RandomForestClassifier(n_estimators=10, random_state=42)

# Train Model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Check Accuracy
print(accuracy_score(y_test, predictions))

# save model into pickle object, so we can use it later
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)