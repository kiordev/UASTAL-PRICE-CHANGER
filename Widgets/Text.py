import flet as ft

def main(page: ft.Page):
    page.title="Text"
    page.bgcolor = ft.colors.INDIGO
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Y
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # X
    
    page.add(
        ft.Text(
            value="Some text about something", # Текст
            size=10, # Розмір шрифту
            color=ft.colors.WHITE, # Колір тексту
            bgcolor=ft.colors.BLUE_600, # Фоновий колір
            weight=ft.FontWeight.W_100,
            
        )
    )
    
ft.app(target=main)