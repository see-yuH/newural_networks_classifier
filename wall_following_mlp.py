"""
Wall-Following Robot Navigation - Neural Network Classifier
=============================================================
Predicts robot movement (Move-Forward, Slight-Right-Turn,
Sharp-Right-Turn, Slight-Left-Turn) using 24 ultrasound sensor readings.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1. LOAD THE DATA
columns = [f"US{i+1}" for i in range(24)] + ["Class"]
data = pd.read_csv("wall_data/sensor_readings_24.data", header=None, names=columns)

X = data.drop("Class", axis=1)   # 24 sensor readings (features)
y = data["Class"]                # movement label (target)

print("Dataset shape:", X.shape)
print("\nClass distribution:\n", y.value_counts())

# Plot class distribution
y.value_counts().plot(kind="bar", color="steelblue")
plt.title("Distribution of Target Classes")
plt.xlabel("Movement Class")
plt.ylabel("Count")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("class_distribution.png")
plt.close()


# 2. PREPROCESS THE DATA
# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text labels (e.g. "Move-Forward") into numbers (e.g. 0, 1, 2, 3)
encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

# Scale features so every sensor reading has similar range/weight
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. BUILD AND TRAIN THE NEURAL NETWORK
model = MLPClassifier(
    hidden_layer_sizes=(64, 32),  # two hidden layers
    activation="relu",
    max_iter=500,
    random_state=42
)
model.fit(X_train, y_train)

# 4. EVALUATE THE MODEL
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nTest Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))
