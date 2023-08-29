import flet as ft 

def main(page: ft.Page):
    
    text = ft.Text("text")
    
    main = ft.View(
        bgcolor=ft.colors.AMBER,
        controls=[text]
    )
    
    page.add(
        main
    )

ft.app(target=main)