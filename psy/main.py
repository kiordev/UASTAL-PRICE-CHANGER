import flet as ft

def main(page: ft.Page):
    
    def button_clicked(e):
        if test_button.text == "ПРОЙТИ ТЕСТ":
            print("pressed")
    
    # Page Settings
    page.title = "FoxMetal"
    page.bgcolor = "#370034"
    page.window_min_width = 1000
    page.window_max_width = 1000
    page.window_min_height = 600
    page.window_max_height = 600
    
    # Кнопки меню
    test_button = ft.ElevatedButton(text="ПРОЙТИ ТЕСТ", width=150, bgcolor="#84007B", color="#FFFFFF", on_click=button_clicked)
    express_button = ft.ElevatedButton("ЕКСПРЕСС", width=150, bgcolor="#84007B", color="#FFFFFF")
    faq_button = ft.ElevatedButton("FAQ", width=150, bgcolor="#84007B", color="#FFFFFF")
    table_button = ft.ElevatedButton("ТАБЛИЦЯ", width=150, bgcolor="#84007B", color="#FFFFFF")
    notes_button = ft.ElevatedButton("НОТАТНИК", width=150, bgcolor="#84007B", color="#FFFFFF")
    
    # Ряд с кнопками меню
    menu_buttons_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            test_button, 
            express_button,
            faq_button,
            table_button,
            notes_button
            ]
        )
    
    # Контейнер с кнопками меню
    top_bar = ft.Container(
        width=1000,
        height=100,
        bgcolor="#370034",
        content=menu_buttons_row,
    )
    
    # Основной контейнер
    main_bar = ft.Container(
        width=1000,
        height=400,
        bgcolor="#84007B",
        content=ft.Text("Hello world!")
    )
    
    faq = ft.Text("FAQ")
    expres = ft.Text("EXPRESS")
    test = ft.Text("TEST")
    notes = ft.Text("NOTES")
    table = ft.Text("TABLE")
    
    
    page.add (
        top_bar,
        main_bar
    )
    

ft.app(target=main)