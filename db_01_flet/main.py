import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text_counter = ft.Text(
        value='0',
        size=100,
        width=200,
        text_align=ft.TextAlign.CENTER,
    )

    def minus_click(e):
        text_counter.value = str(int(text_counter.value) - 1)

    def plus_click(e):
        text_counter.value = str(int(text_counter.value) + 1)
    page.add(
        ft.Container (
            content=ft.Row(
                # alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                    ft.Container(
                        content=ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                        bgcolor=ft.Colors.RED_400,
                    ),
                    ft.Container(
                        content=text_counter,
                        bgcolor=ft.Colors.BLUE_400,
                    ),
                    ft.Container(
                        content=ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                        bgcolor=ft.Colors.GREEN_700,
                    ),
                ],
            ),
        bgcolor=ft.Colors.YELLOW_900,
    )
)
        

if__name__ = "main"
ft.run(main)
