import os
from typing import Dict

import pandas as pd
from h2o_wave import Q
from src.use_cases.model import (
    DataType,
    IndustryType,
    LicenseType,
    ProblemType,
    UseCase,
)

USE_CASES_FILE_PATH = "./Assets/docs/use_cases.csv"
USE_CASES_FOLDER_PATH = "./Assets/DL_Models"


async def get_all_use_cases(q: Q) -> Dict[str, UseCase]:
    use_cases_df = pd.read_csv(USE_CASES_FILE_PATH)
    use_cases_df = use_cases_df.fillna("None")

    use_cases: Dict[str, UseCase] = {}
    for i in range(len(use_cases_df)):
        uc = use_cases_df.loc[i]
        use_case = UseCase(
            use_case_id=str(uc["Sr. No"]),
            name=uc["Usecase"],
            industry_type=IndustryType(uc["Industry"]),
            data_type=DataType(uc["Data Type"]),
            problem_type=ProblemType(uc["Deep Learning Problem"]),
            description=uc["Use Case Description"],
            dataset=uc["Dataset"],
            dataset_source=uc["Dataset Source"],
            dataset_description=uc["Dataset Description (1 liner)"],
            prediction_target=uc["Prediction Target"],
            ht_instance_link=uc["Hydrogen Torch - Instance Link"],
            license_type=LicenseType(uc["License"]),
        )
        use_case.chart_image_path = await _get_use_case_image_path(
            q=q,
            use_case=use_case,
            image_name="chart.png",
        )
        use_case.train_data_image_path = await _get_use_case_image_path(
            q=q,
            use_case=use_case,
            image_name="train data.png",
        )
        use_case.validation_predictions_image_path = await _get_use_case_image_path(
            q=q,
            use_case=use_case,
            image_name="Validation Predictions.png",
        )
        use_case.cover_image_path = await _get_use_case_image_path(
            q=q,
            use_case=use_case,
            image_name="cover",
        )
        use_cases[use_case.use_case_id] = use_case

    return use_cases


async def _get_use_case_image_path(q: Q, use_case: UseCase, image_name: str) -> str:
    folder_path = f"{USE_CASES_FOLDER_PATH}/{use_case.use_case_id}_{use_case.dataset}"
    if "." not in image_name:
        usecase_files = os.listdir(folder_path)
        for usecase_file in usecase_files:
            if image_name in usecase_file:
                image_name = usecase_file
                break

    file_path = f"{folder_path}/{image_name}"
    (image_path,) = await q.site.upload([file_path])
    return image_path
