from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BaseEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value == value:
                return member
        return cls.Unknown


class IndustryType(BaseEnum):
    All = "All"
    Banking = "Banking"
    Manufacturing = "Manufacturing"
    Healthcare = "Healthcare"
    AI_Good = "AI for Good"
    Agriculture = "Agriculture / AI for Good"
    Content_Creation = "Content Creation"
    FnB = "FnB"
    Unknown = "Unknown"


class DataType(BaseEnum):
    All = "All"
    Text = "Text"
    Image = "Image"
    Audio = "Audio"
    Unknown = "Unknown"


class ProblemType(BaseEnum):
    All = "All"
    Classification = "Classification"
    Regression = "Regression"
    Segmentation = "Segmentation"
    Object_Detecton = "Object Detecton"
    Metric_Learning = "Metric Learning"
    Text_Sequence = "Text sequence to sequence"
    Unknown = "Unknown"


class LicenseType(BaseEnum):
    All = "All"
    CC0 = "CC0: Public Domain"
    MIT = "MIT License"
    GPL2 = "GPL 2"
    CCSA40 = "CC BY-SA 4.0"
    CCNCSA40 = "CC BY-NC-SA 4.0"
    A40 = "Attribution 4.0 International (CC BY 4.0)"
    OA = "Data files © Original Authors"
    Unknown = "Unknown"

    # Some more


@dataclass
class UseCase:
    use_case_id: Optional[str] = None
    name: Optional[str] = None
    industry_type: IndustryType = IndustryType.Unknown
    data_type: DataType = DataType.Unknown
    problem_type: ProblemType = ProblemType.Unknown
    description: Optional[str] = None
    dataset: Optional[str] = None
    dataset_source: Optional[str] = None
    dataset_description: Optional[str] = None
    prediction_target: Optional[str] = None
    ht_instance_link: Optional[str] = None
    chart_image_path: Optional[str] = None
    train_data_image_path: Optional[str] = None
    validation_predictions_image_path: Optional[str] = None
    cover_image_path: Optional[str] = None
    license_type: LicenseType = LicenseType.Unknown
