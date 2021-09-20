import pandas as pd
from models import Features


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


def prepare_data(data: Features):
    df = pd.DataFrame([data.dict()])
    df["hypertension"] = df["hypertension"] * 1
    df["heart_disease"] = df["heart_disease"] * 1
    df["gender"] = df["gender"].map(gender_dict)
    df["ever_married"] = df["ever_married"].map(ever_married_dict)
    df["work_type"] = df["work_type"].map(work_type_dict)
    df["Residence_type"] = df["Residence_type"].map(residence_type_dict)
    df["smoking_status"] = df["smoking_status"].map(smoking_status_dict)

    return df
