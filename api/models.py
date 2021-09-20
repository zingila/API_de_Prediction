from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel


class WorkType(str, Enum):
    children = "children"
    never_worked = "Never_worked"
    govt_job = "Govt_job"
    private = "Private"
    self_employed = "Self-employed"


class ResidenceType(str, Enum):
    rural = "Rural"
    urban = "Urban"


class SmokingStatus(str, Enum):
    unknown = "Unknown"
    never_smoked = "never smoked"
    formerly_smoked = "formerly smoked"
    smokes = "smokes"


class GenderType(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class EverMarried(str, Enum):
    yes = "Yes"
    no = "No"


class Features(BaseModel):
    gender: GenderType
    age: int
    hypertension: bool
    heart_disease: bool
    ever_married: EverMarried
    work_type: WorkType
    Residence_type: ResidenceType
    avg_glucose_level: float
    bmi: float
    smoking_status: SmokingStatus

    class Config:
        use_enum_values = True
        extra = "forbid"


class Prediction(BaseModel):
    prediction: int
    proba: float
