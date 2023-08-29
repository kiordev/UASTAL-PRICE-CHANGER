import flet as ft 

def main(page: ft.Page):
    # Page config
    page.title="Login and Password"
    page.bgcolor = ft.colors.AMBER_900
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    login = "Sasha"
    password = "Kior"
    
    def check_password(e):
        if login.value == "Sasha" and password.value == "Kior":
            result.value = "WELCOME!"
            result.color = ft.colors.GREEN
            print("button ok")
        else:
            result.value = "WRONG INFO!"
            result.color = ft.colors.RED
            print("button bad")
        page.update()
            
        
    
    text = ft.Text(
        value="Welcome to Site!",
        size=22,
        weight=ft.FontWeight.W_600,
    )
    
    login = ft.TextField(
        label = "Enter login",
        width=250,
    )
    
    password = ft.TextField(
        label = "Enter password",
        width=250,
    )
    
    sumbit = ft.ElevatedButton(
        text="Sumbit",
        bgcolor=ft.colors.AMBER_900,
        color=ft.colors.WHITE,
        on_click=check_password
    )
    
    result = ft.Text(
        value="",
        size=22,
        weight=ft.FontWeight.W_600,
    )
    
    main_container = ft.Container(
        height=500,
        width=300,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.INDIGO,
        border_radius=20,
        # Content of Main
        content=ft.Column(
            controls=[text, login, password, sumbit, result], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
    )
    
    
    page.add(main_container)

ft.app(target=main)