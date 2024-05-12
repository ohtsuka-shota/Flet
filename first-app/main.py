import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    input_example = ft.TextField(
        label="test",
    )

    return ft.Column(controls=[input_example])

ft.app(main)
