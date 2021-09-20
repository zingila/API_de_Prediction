import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.utils import compute_class_weight
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier

# Load data

df = pd.read_csv(
    "https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/strokes.csv"
)

# Data preparation
df = df.drop(columns=["id"])
df["bmi"] = df["bmi"].fillna(df.bmi.mean())
gender_dict = {"Male": 0, "Female": 1, "Other": 2}
ever_married_dict = {"No": 0, "Yes": 1}
work_type_dict = {
    "children": 0,
    "Never_worked": 1,
    "Govt_job": 2,
    "Private": 3,
    "Self-employed": 4,
}
residence_type_dict = {"Rural": 0, "Urban": 1}
smoking_status_dict = {
    "Unknown": 0,
    "never smoked": 1,
    "formerly smoked": 2,
    "smokes": 3,
}
df["gender"] = df["gender"].map(gender_dict)
df["ever_married"] = df["ever_married"].map(ever_married_dict)
df["work_type"] = df["work_type"].map(work_type_dict)
df["Residence_type"] = df["Residence_type"].map(residence_type_dict)
df["smoking_status"] = df["smoking_status"].map(smoking_status_dict)


X = df.drop(columns=["stroke"])
y = df["stroke"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

class_weights = compute_class_weight("balanced", classes=y_train.unique(), y=y_train)
class_weights = {i: class_weights[i] for i in range(len(class_weights))}

print()
print("##### RandomForestClassifier #####")


rf = GradientBoostingClassifier()


def score(y_true, y_pred):
    class_weights = compute_class_weight(
        "balanced", classes=y_train.unique(), y=y_train
    )
    class_weights = {i: class_weights[i] for i in range(len(class_weights))}
    return f1_score(y_true, y_pred, sample_weight=y_true.map(class_weights))


# score_params = {"class_weights": class_weights}
my_scorer = make_scorer(score, needs_proba=False)

param_grid = {
    "max_depth": range(1, 5),
    "min_samples_split": range(2, 5),
    "n_estimators": range(10, 200, 10),
}

clf = GridSearchCV(
    estimator=rf, param_grid=param_grid, n_jobs=-1, verbose=2, cv=5, scoring=my_scorer
)

search = clf.fit(X_train, y_train, sample_weight=y_train.map(class_weights))

print(search.best_params_)
print(search.best_score_)

best_estimator = search.best_estimator_

y_pred_train = best_estimator.predict(X_train)
y_pred_test = best_estimator.predict(X_test)

print("\n#### Train : ")

print(classification_report(y_train, y_pred_train))
print(confusion_matrix(y_train, y_pred_train))
print("F1 Score : ", f1_score(y_train, y_pred_train))


print("\n#### Test : ")

print(classification_report(y_test, y_pred_test))
print(confusion_matrix(y_test, y_pred_test))
print("F1 Score : ", f1_score(y_test, y_pred_test))

with open("./data/model.pkl", "wb") as f:
    pickle.dump(best_estimator, f)

with open("./data/scores.txt", "w") as f:
    f.write("# Train :\n")

    f.write(f"F1 Score : {f1_score(y_train, y_pred_train)}\n")
    f.write(f"Confusion Matrix :\n{str(confusion_matrix(y_train, y_pred_train))}")

    f.write("\n\n# Test :\n")

    f.write(f"F1 Score : {f1_score(y_test, y_pred_test)}\n")
    f.write(f"Confusion Matrix :\n{str(confusion_matrix(y_test, y_pred_test))}")
