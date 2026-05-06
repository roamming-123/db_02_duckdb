import flet as ft
def main(page: ft.Page):
    page.title = "카운터";
    page.add(
        ft.Row(
            controls=
            [ft.Text('안녕하세요'),
             ft.Button('눌러주세요')
            ]
    )
    )
    

if __name__ == "__main__":
    ft.run(main)
