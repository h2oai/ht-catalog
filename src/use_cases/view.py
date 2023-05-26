from typing import Dict, List

from h2o_wave import Component, Q, ui
from src.use_cases.model import (
    DataType,
    IndustryType,
    LicenseType,
    ProblemType,
    UseCase,
)


def create_use_cases_tab(q: Q) -> None:
    create_filtering_panel(q)
    create_use_cases_grid_view(q)


def create_filtering_panel(q: Q) -> None:
    q.client.use_cases_cards.add("filtering_panel")
    q.page["filtering_panel"] = ui.form_card(
        box=ui.box(
            zone="left",
            width="300px",
            height="calc(100vh - 100px)",
        ),
        items=get_filtering_panel_items(
            data_type_name=q.client.data_type_name,
            industry_type_name=q.client.industry_type_name,
            problem_type_name=q.client.problem_type_name,
            license_type_name=q.client.license_type_name,
        ),
    )


def create_use_cases_grid_view(q: Q) -> None:
    filtered_use_cases: List[UseCase] = _filter_use_cases(
        use_cases=q.client.use_cases_dict,
        data_type_name=q.client.data_type_name,
        industry_type_name=q.client.industry_type_name,
        problem_type_name=q.client.problem_type_name,
        license_type_name=q.client.license_type_name,
    )

    q.client.use_cases_cards.add("use_cases_title")
    q.page["use_cases_title"] = ui.form_card(
        box=ui.box(zone="title", width="1387px"),
        items=get_use_cases_title_items(
            filtered_use_cases_count=len(filtered_use_cases)
        ),
    )

    for uc in filtered_use_cases:
        card_name = f"use_case_{uc.use_case_id}"
        q.client.use_cases_cards.add(card_name)

        q.page[card_name] = ui.profile_card(
            box=ui.box(
                zone="content",
                width="400px",
            ),
            persona=ui.template(" "),
            image=uc.cover_image_path,
            items=get_use_case_card_items(
                use_case=uc,
            ),
        )


def get_filtering_panel_items(
    data_type_name: str,
    industry_type_name: str,
    problem_type_name: str,
    license_type_name: str,
) -> List[Component]:
    return [
        ui.text_m(content="Filter"),
        ui.template(content=" "),
        ui.dropdown(
            name="use_cases_filtering_industry_dropdown",
            label="Industry",
            placeholder="Select industry type",
            value=industry_type_name,
            choices=[ui.choice(i.name, i.value) for i in IndustryType],
            trigger=True,
        ),
        ui.template(content=" "),
        ui.dropdown(
            name="use_cases_filtering_data_type_dropdown",
            label="Data Type",
            placeholder="Select data type",
            value=data_type_name,
            choices=[ui.choice(d.name, d.value) for d in DataType],
            trigger=True,
        ),
        ui.template(content=" "),
        ui.dropdown(
            name="use_cases_filtering_problem_type_dropdown",
            label="Problem Type",
            placeholder="Select problem type",
            value=problem_type_name,
            choices=[ui.choice(p.name, p.value) for p in ProblemType],
            trigger=True,
        ),
        ui.template(content=" "),
        ui.dropdown(
            name="use_cases_filtering_license_type_dropdown",
            label="License Type",
            placeholder="Select license type",
            value=license_type_name,
            choices=[ui.choice(l.name, l.value) for l in LicenseType],
            trigger=True,
        ),
        ui.template(content=" "),
        ui.template(content=" "),
        ui.template(content=" "),
        ui.buttons(
            items=[
                ui.button(
                    name="reset_use_cases_filter_button",
                    label="Reset",
                    primary=True,
                ),
            ],
            justify=ui.ButtonsJustify.END,
        ),
    ]


def get_use_cases_title_items(filtered_use_cases_count: int) -> List[Component]:
    return [
        ui.text_xl("Use Cases"),
        ui.template(content=" "),
        ui.text(f"We have <b>{filtered_use_cases_count}</b> use cases"),
    ]


def get_use_case_card_items(use_case: UseCase) -> List[Component]:
    return [
        ui.inline(
            items=[
                get_badge_content("#514644", "#efc8b1", use_case.industry_type.value),
                ui.text(" | "),
                get_badge_content("#270540", "#F2E3FA", use_case.data_type.value),
                # ui.text(" | "),
                # get_badge_content("red","blue",use_case.problem_type.value),
            ],
            justify=ui.InlineJustify.CENTER,
        ),
        ui.text_l(f"<p style='text-align: center;'>{use_case.name}</p>"),
        ui.text(f"<p style='text-align: center;'>{use_case.prediction_target}.</p>"),
        # ui.template(content=" "),
        # ui.inline(
        #     items=[
        #         ui.text("Industry: "),
        #         ui.text(f"{use_case.industry_type.value}"),
        #     ],
        # ),
        # ui.template(content=" "),
        # ui.inline(
        #     items=[
        #         ui.text("Data Type: "),
        #         ui.text(f"{use_case.data_type.value}"),
        #     ],
        # ),
        ui.template(content=" "),
        ui.buttons(
            items=[
                ui.button(
                    name="view_use_case_button",
                    label="View More",
                    value=use_case.use_case_id,
                    primary=True,
                ),
            ],
            justify=ui.ButtonsJustify.END,
        ),
    ]


def create_use_case_details_page(q: Q, use_case_id: str) -> None:
    use_case: UseCase = q.client.use_cases_dict[use_case_id]

    q.client.use_cases_cards.add("use_case_details")
    q.page["use_case_details"] = ui.form_card(
        box=ui.box(
            zone="full_body",
            width="80%",
        ),
        items=get_use_case_details_page_items(
            use_case=use_case,
        ),
    )


def get_use_case_details_page_items(use_case: UseCase) -> List[Component]:
    return [
        ui.inline(
            items=[
                ui.button(
                    name="back_use_case_details_page_button",
                    label="Back",
                    primary=True,
                    icon="NavigateBack",
                ),
                ui.inline(
                    items=[
                        get_badge_content(
                            "#514644", "#efc8b1", use_case.industry_type.value.upper()
                        ),
                        ui.text_l(" | "),
                        get_badge_content(
                            "#270540", "#F2E3FA", use_case.data_type.value.upper()
                        ),
                        ui.text_l(" | "),
                        get_badge_content(
                            "#132B13", "#E3FAE4", use_case.problem_type.value.upper()
                        ),
                    ],
                    justify=ui.InlineJustify.CENTER,
                ),
            ],
            justify=ui.InlineJustify.BETWEEN,
        ),
        ui.inline(
            items=[
                ui.text_xl(
                    f"<p style='text-transform: uppercase;'>{use_case.name}</p>"
                ),
            ],
            justify=ui.InlineJustify.CENTER,
        ),
        ui.separator(),
        ui.text_xl("<p style='text-transform: uppercase;'>Business Problem</p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;'>{use_case.description}.</p>"
        ),
        ui.template(content=" "),
        ui.text_xl("<p style='text-transform: uppercase;'>Business Impact</p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;'>{use_case.business_impact}</p>"
        ),
        ui.template(content=" "),
        ui.text_xl("<p style='text-transform: uppercase;'>Dataset</p>"),
        ui.text_l(
            f"""<ui>
                <li>{use_case.dataset.capitalize()} dataset has been used.</li>
                <li>You can access the dataset <a href='{use_case.dataset_source}' target='_blank'>here</a>.</li>
                <li>{use_case.dataset_description}</li>
                <br>
                <p><img src='{use_case.train_data_image_path}'></p>
            </ui>"""
        ),
        ui.template(content=" "),
        ui.text_xl("<p style='text-transform: uppercase;'>Prediction Output</p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;'>{use_case.prediction_target}</p>"
        ),
        ui.template(content=" "),
        ui.text_xl("<p style='text-transform: uppercase;'>Model Training</p>"),
        ui.text_l("<p style='font-family:JackInput Regular;'><b>Architecture</b></p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: {use_case.cfg_log_dict['architecture']['backbone']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: {use_case.cfg_log_dict['architecture']['pretrained']}</p>"
        ),
        ui.text_l("<p style='font-family:JackInput Regular;'><b>Augmentation</b></p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>augmentations_strategy: {use_case.cfg_log_dict['augmentation']['augmentations_strategy']}</p>"
        ),
        ui.text_l("<p style='font-family:JackInput Regular;'><b>Training</b></p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: {use_case.cfg_log_dict['training']['batch_size']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: {use_case.cfg_log_dict['training']['epochs']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: {use_case.cfg_log_dict['training']['gradient_clip']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: {use_case.cfg_log_dict['training']['learning_rate']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: {use_case.cfg_log_dict['training']['optimizer']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: {use_case.cfg_log_dict['training']['schedule']}</p>"
            f"<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: {use_case.cfg_log_dict['training']['weight_decay']}</p>"
        ),
        ui.text(f"<p><img src='{use_case.chart_image_path}'></p>"),
        ui.template(content=" "),
        ui.text_xl("<p style='text-transform: uppercase;'>Model Predictions</p>"),
        ui.text(f"<p><img src='{use_case.validation_predictions_image_path}'></p>"),
        ui.template(content=" "),
        ui.text_xl("<p style='text-transform: uppercase;'>License</p>"),
        ui.text_l(
            f"<p style='text-align: justify; text-indent: 30px;'>{use_case.license_type.value}</p>"
        ),
        ui.template(content=" "),
        ui.inline(
            items=[
                ui.button(
                    name="download_cfg_button",
                    label="View cfg.yaml file",
                    path=f"{use_case.cfg_log_path}",
                    primary=True,
                ),
                ui.button(
                    name="download_charts_button",
                    label="View charts.json file",
                    path=f"{use_case.charts_log_path}",
                    primary=True,
                ),
                ui.button(
                    name="download_logs_button",
                    label="View log file",
                    path=f"{use_case.logs_log_path}",
                    primary=True,
                ),
                ui.button(
                    name="download_logs_button",
                    label="Download logs",
                    value=f"{use_case.cfg_log_path},{use_case.charts_log_path},{use_case.logs_log_path}",
                    primary=True,
                ),
            ],
            justify=ui.InlineJustify.END,
        ),
        ui.template(content=" "),
    ]


def _filter_use_cases(
    use_cases: Dict[str, UseCase],
    industry_type_name: str,
    data_type_name: str,
    problem_type_name: str,
    license_type_name: str,
) -> List[UseCase]:
    return list(
        filter(
            lambda uc: (
                not data_type_name
                or data_type_name == DataType.All.value
                or uc.data_type.name == data_type_name
            )
            and (
                not industry_type_name
                or industry_type_name == IndustryType.All.value
                or uc.industry_type.name == industry_type_name
            )
            and (
                not problem_type_name
                or problem_type_name == ProblemType.All.value
                or uc.problem_type.name == problem_type_name
            )
            and (
                not license_type_name
                or license_type_name == LicenseType.All.value
                or uc.license_type.name == license_type_name
            ),
            use_cases.values(),
        )
    )


def get_badge_content(fcolor, bcolor, text):
    return ui.markup(
        f"""
                <svg width="{len(text)*8+21}" height="25">
                    <rect width="{len(text)*8+21}" height="25" rx="5" ry="5" style="fill:{bcolor};"/>
                    <text x="6" y="17" fill={fcolor}>{text}</text>
                </svg>
                """
    )
