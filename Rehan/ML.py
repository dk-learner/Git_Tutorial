# ML.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Step 1: Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 4: Evaluate model
score = model.score(X_test, y_test)
print(f"Model accuracy: {score:.2f}")
