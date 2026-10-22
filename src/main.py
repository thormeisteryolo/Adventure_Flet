import flet as ft
import monsterData as mData
import itemData as iData

playerData = {"name": None, "armor": None, "weapon": None, "health": 100, "currentloc": "village", "gold": 100, "class": None}


@ft.control
class itemCoicebox(ft.Container):
    width: int = 300
    height: int = 300
    bgcolor: str = "#1E1E1E"


@ft.control
class charCreateTitle(ft.Row):
    alignment: ft.MainAxisAlignment = ft.MainAxisAlignment.CENTER


def main(page: ft.Page):
    page.title = "Adventure App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    def startGame_buttonClicked(e: ft.Event[ft.Button]):
        mainmenu.visible = False
        charCreate.visible = True

    def charName_buttonClicked(e: ft.Event[ft.Button]):
        playerData["name"] = charName.value
        # playerName.value = playerData["name"]
        charCreate.visible = False

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                bgcolor="#121212",
                content=ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        mainmenu := ft.Container(
                            expand=True,
                            content=ft.Column(
                                expand=True,
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Image(
                                                expand=True,
                                                src="Forest.png",
                                                fit=ft.BoxFit.FILL,
                                                ),
                                        ]
                                    ),
                                    ft.Divider(),
                                    ft.Row(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Button(content="Start", on_click=startGame_buttonClicked),
                                        ]
                                    ),
                                ]
                            )
                        ),

                        charCreate := ft.Container(
                            expand=True,
                            visible=False,
                            content=ft.Column(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Character Creator", size=24),
                                    charName := ft.TextField(
                                        label="Name",
                                        hint_text="Enter your adventurers name",
                                    ),
                                    ft.Container(
                                        ft.Row(
                                            expand=True,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                itemCoicebox(
                                                    content=ft.Column(
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                            ft.Container(
                                                                bgcolor="#9a9a9a",
                                                                content=charCreateTitle(
                                                                    controls=[
                                                                        ft.Text(
                                                                            "Title",
                                                                            size=20,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            ft.Divider(
                                                                height=0,
                                                                thickness=4,
                                                                color="#6d638f",
                                                            ),
                                                            ft.Column(
                                                                expand=True,
                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                controls=[
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                itemCoicebox(
                                                    content=ft.Column(
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                            ft.Container(
                                                                bgcolor="#9a9a9a",
                                                                content=charCreateTitle(
                                                                    controls=[
                                                                        ft.Text(
                                                                            "Title2",
                                                                            size=20,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            ft.Divider(
                                                                height=0,
                                                                thickness=4,
                                                                color="#6d638f",
                                                            ),
                                                            ft.Column(
                                                                expand=True,
                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                controls=[
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                itemCoicebox(
                                                    content=ft.Column(
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                            ft.Container(
                                                                bgcolor="#9a9a9a",
                                                                content=charCreateTitle(
                                                                    controls=[
                                                                        ft.Text(
                                                                            "Title3",
                                                                            size=20,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            ft.Divider(
                                                                height=0,
                                                                thickness=4,
                                                                color="#6d638f",
                                                            ),
                                                            ft.Column(
                                                                expand=True,
                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                controls=[
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                itemCoicebox(
                                                    content=ft.Column(
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        spacing=2,
                                                        controls=[
                                                            ft.Container(
                                                                bgcolor="#9a9a9a",
                                                                content=charCreateTitle(
                                                                    controls=[
                                                                        ft.Text(
                                                                            "Title4",
                                                                            size=20,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            ft.Divider(
                                                                height=0,
                                                                thickness=4,
                                                                color="#6d638f",
                                                            ),
                                                            ft.Column(
                                                                expand=True,
                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                controls=[
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                    ft.Button(
                                                                        content="wip"
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        )
                                    ),
                                    ft.Button(
                                        content="Finalize",
                                        on_click=charName_buttonClicked,
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(expand=True, visible=False),
                    ],
                ),
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
