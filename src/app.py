from h2o_wave import app, Q, main  # noqa: F401
from src.init import (
    handle_change_theme_toggle,
    init_app,
    init_client,
    init_ui,
    init_user,
)
from src.use_cases.handler import show_use_cases_page


@app("/")
async def serve(q: Q) -> None:
    print(q.args)
    if not q.app.initialized:
        await init_app(q)
        q.app.initialized = True
    if not q.user.initialized:
        init_user(q)
        q.user.initialized = True
    if not q.client.initialized:
        init_client(q)
        init_ui(q)
        q.client.initialized = True

    handle_change_theme_toggle(q)

    await show_use_cases_page(q)

    await q.page.save()
