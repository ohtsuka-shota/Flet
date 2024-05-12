import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

    input_example = ft.TextField(
        label="input_example",
    )

    page.add(input_example)

ft.app(main)