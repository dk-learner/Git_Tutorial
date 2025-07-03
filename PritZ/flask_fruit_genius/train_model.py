import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample training data
fruit_data = [
    ("orange", "Citrus"),
    ("lemon", "Citrus"),
    ("lime", "Citrus"),
    ("blueberry", "Berry"),
    ("strawberry", "Berry"),
    ("blackberry", "Berry"),
    ("mango", "Tropical"),
    ("pineapple", "Tropical"),
    ("banana", "Tropical"),
    ("apple", "Pome"),
    ("pear", "Pome"),
    ("peach", "Stone Fruit"),
    ("plum", "Stone Fruit"),
    ("grapefruit", "Citrus"),
    ("tangerine", "Citrus"),
    ("mandarin", "Citrus"),
    ("pomelo", "Citrus"),
    ("kumquat", "Citrus"),
    ("raspberry", "Berry"),
    ("gooseberry", "Berry"),
    ("cranberry", "Berry"),
    ("mulberry", "Berry"),
    ("currant", "Berry"),
    ("papaya", "Tropical"),
    ("guava", "Tropical"),
    ("passionfruit", "Tropical"),
    ("lychee", "Tropical"),
    ("dragonfruit", "Tropical"),
    ("quince", "Pome"),
    ("loquat", "Pome"),
    ("medlar", "Pome"),
    ("apricot", "Stone Fruit"),
    ("nectarine", "Stone Fruit"),
    ("cherry", "Stone Fruit")
]

X, y = zip(*fruit_data)

# Train model
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])
model.fit(X, y)

# Save model and known fruit names
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("known_fruits.pkl", "wb") as f:
    pickle.dump([fruit.lower() for fruit in X], f)

print("Model and known fruits saved.")
