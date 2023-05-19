from enum import Enum

from h2o_wave import Q, ui


class Config(Enum):
    AppTitle = "DL-HT-Catalog | Hydrogen Torch | H2O Wave"
    AppLogo = "static/h2o_logo.png"
    AppIcon = "ProductCatalog"
    SubTitle = "Fifty deep learning models that are created using Hydrogen Torch"
    FooterText = "Copyright 2023 @h2o.ai Google Drive, Made using <a href='https://wave.h2o.ai' target='_blank'>H2O Wave</a>"  # noqa: E501
    StyleSheet = "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We' crossorigin='anonymous'>"  # noqa: E501


class Theme(Enum):
    Light = "light"
    Dark = "dark"


async def init_app(q: Q) -> None:
    q.app.title = Config.AppTitle.value
    (q.app.logo,) = await q.site.upload([Config.AppLogo.value])
    q.app.icon = Config.AppIcon.value
    q.app.sub_title = Config.SubTitle.value
    q.app.footer_text = Config.FooterText.value
    q.app.style_sheet = Config.StyleSheet.value


def init_user(q: Q) -> None:
    if not q.user.theme:
        q.user.theme = Theme.Light.value


def init_client(q: Q) -> None:
    pass


def init_ui(q: Q) -> None:
    q.page.drop()
    create_meta(q)
    create_header(q)
    create_footer(q)


def create_meta(q: Q) -> None:
    q.page["meta"] = ui.meta_card(
        box="",
        title=q.app.title,
        layouts=[
            ui.layout(
                breakpoint="xs",
                zones=[
                    ui.zone(
                        name="header",
                        size="72px",
                        direction=ui.ZoneDirection.ROW,
                    ),
                    ui.zone(
                        name="full_body",
                        direction=ui.ZoneDirection.ROW,
                        justify=ui.ZoneJustify.CENTER,
                    ),
                    ui.zone(
                        name="body",
                        zones=[
                            ui.zone(name="left"),
                            ui.zone(
                                name="right",
                                zones=[
                                    ui.zone(
                                        name="title",
                                        direction=ui.ZoneDirection.ROW,
                                    ),
                                    ui.zone(
                                        name="content",
                                        direction=ui.ZoneDirection.ROW,
                                        wrap=ui.ZoneWrap.STRETCH,
                                    ),
                                ],
                            ),
                        ],
                        direction=ui.ZoneDirection.ROW,
                    ),
                    ui.zone(name="footer"),
                ],
            )
        ],
        themes=[
            ui.theme(
                name="dark",
                primary="#FEC925",
                text="#F1F1F1",
                card="#121212",
                page="#080808",
            )
        ],
        theme=q.user.theme,
    )


def create_header(q: Q) -> None:
    q.page["header"] = ui.header_card(
        box="header",
        title=q.app.title,
        subtitle=q.app.sub_title,
        icon=q.app.icon,
        icon_color="primary" if q.user.theme == Theme.Light else None,
        items=[
            ui.text(q.app.style_sheet),
            ui.toggle(
                name="change_theme_toggle",
                label="Dark Theme",
                value=q.user.theme == Theme.Dark.value,
                trigger=True,
            ),
            ui.text(f"<img src='{q.app.logo}' width='50px'>"),
        ],
    )


def create_footer(q: Q) -> None:
    q.page["footer"] = ui.footer_card(box="footer", caption=q.app.footer_text)


def handle_change_theme_toggle(q: Q) -> None:
    if q.args.change_theme_toggle is not None:
        if q.user.theme == Theme.Dark.value:
            q.user.theme = Theme.Light.value
            q.page["meta"].theme = Theme.Light.value
            q.page["header"].items[1].toggle.value = False
        else:
            q.user.theme = Theme.Dark.value
            q.page["meta"].theme = Theme.Dark.value
            q.page["header"].items[1].toggle.value = True
