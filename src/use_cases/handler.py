from h2o_wave import Q
from src.use_cases.service import get_all_use_cases
from src.use_cases.view import create_use_case_details_page, create_use_cases_tab


async def show_use_cases_page(q: Q) -> None:
    if not q.client.use_cases_dict:
        q.client.use_cases_dict = await get_all_use_cases(q)

    if not q.client.use_cases_cards:
        q.client.use_cases_cards = set()
    else:
        for card_name in q.client.use_cases_cards:
            del q.page[card_name]

    handle_use_cases_tab_inputs(q)

    if q.client.use_case_id:
        create_use_case_details_page(q, q.client.use_case_id)
    else:
        create_use_cases_tab(q)


def handle_use_cases_tab_inputs(q: Q) -> None:
    industry_type_name: str = q.args.use_cases_filtering_industry_dropdown
    data_type_name: str = q.args.use_cases_filtering_data_type_dropdown
    problem_type_name: str = q.args.use_cases_filtering_problem_type_dropdown
    license_type_name: str = q.args.use_cases_filtering_license_type_dropdown
    reset_filter: bool = q.args.reset_use_cases_filter_button
    use_case_id: str = q.args.view_use_case_button
    back_to_use_cases: bool = q.args.back_use_case_details_page_button

    if industry_type_name:
        q.client.industry_type_name = industry_type_name
    if data_type_name:
        q.client.data_type_name = data_type_name
    if problem_type_name:
        q.client.problem_type_name = problem_type_name
    if license_type_name:
        q.client.license_type_name = license_type_name
    if reset_filter:
        q.client.industry_type_name = None
        q.client.data_type_name = None
        q.client.problem_type_name = None
        q.client.license_type_name = None
    if use_case_id:
        q.client.use_case_id = use_case_id
    if back_to_use_cases:
        q.client.use_case_id = None
