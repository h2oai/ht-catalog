import os
from typing import Dict

import yaml
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
            dataset_source=uc["Dataset Link"],
            dataset_description=uc["Dataset Description (1 liner)"],
            prediction_target=uc["Prediction Target"],
            ht_instance_link=uc["Hydrogen Torch - Instance Link"],
            license_type=LicenseType(uc["License"]),
            business_impact=uc["Business Impact"],
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
        (use_case.cfg_log_path, use_case.logs_folder) = await _get_use_case_log_path(
            q=q,
            use_case=use_case,
            log_name="cfg",
        )
        use_case.charts_log_path = (
            await _get_use_case_log_path(
                q=q,
                use_case=use_case,
                log_name="charts",
            )
        )[0]
        use_case.logs_log_path = (
            await _get_use_case_log_path(
                q=q,
                use_case=use_case,
                log_name="logs",
            )
        )[0]
        use_case.cfg_log_dict = _get_cfg_log_dict(use_case=use_case)

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


async def _get_use_case_log_path(q: Q, use_case: UseCase, log_name: str) -> str:
    folder_path = f"{USE_CASES_FOLDER_PATH}/{use_case.use_case_id}_{use_case.dataset}"
    usecase_files = os.listdir(folder_path)
    for usecase_file in usecase_files:
        if "logs" in usecase_file:
            folder_path = f"{folder_path}/{usecase_file}"
            log_files = os.listdir(folder_path)
            for log_file in log_files:
                if log_name in log_file:
                    log_name = log_file
                    break
            break

    file_path = f"{folder_path}/{log_name}"
    (log_path,) = await q.site.upload([file_path])
    return (log_path, folder_path)


def _get_cfg_log_dict(use_case: UseCase):
    folder_path = f"{USE_CASES_FOLDER_PATH}/{use_case.use_case_id}_{use_case.dataset}"
    usecase_files = os.listdir(folder_path)
    for usecase_file in usecase_files:
        if "logs" in usecase_file:
            folder_path = f"{folder_path}/{usecase_file}"
            log_files = os.listdir(folder_path)
            for log_file in log_files:
                if "cfg" in log_file:
                    yaml_file_path = f"{folder_path}/{log_file}"
                    break
            break

    with open(yaml_file_path, "r") as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    return yaml_dict
