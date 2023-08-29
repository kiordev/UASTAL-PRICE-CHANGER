import flet as ft

def main(page: ft.Page):
    
    page.title="Containers" # Назва сторінки
    page.bgcolor = ft.colors.BLACK # Колір заднього фону
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Y
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # X
    
    page.add ( # Метод деплою віджетів
        ft.Container (
            content=ft.Text(value="Indigo"), # Текст
            width=100, # Ширина
            height=100, # Висота
            bgcolor=ft.colors.INDIGO # Колір
        ),
        
        ft.Container (
            content=ft.Text(value="Red"), # Текст
            width=100, # Ширина
            height=100, # Висота
            bgcolor=ft.colors.RED # Колір
        ),
        
        ft.Container (
            content=ft.Text(value="White"), # Текст
            width=100, # Ширина
            height=100, # Висота
            bgcolor=ft.colors.WHITE # Колір
        ),
        
        ft.Container (
            content=ft.Text(value="Orange", color=ft.colors.INDIGO), # Текст
            width=100, # Ширина
            height=100, # Висота
            bgcolor=ft.colors.ORANGE, # Колір
            margin = 10, # Отступ
            border_radius = 10, # Закруглення кутів
            alignment=ft.alignment.center, # Рівніння контенту у Контейрені по центру
        ),
        
        ft.Container (
            content=ft.Text(value="White"), # Текст
            width=100, # Ширина
            height=100, # Висота
            gradient=ft.LinearGradient( # Настройки градиента
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[
                    ft.colors.BLUE, 
                    ft.colors.YELLOW,
                    ft.colors.RED,
                    ],
            )
        ),
        
    )
    
ft.app(target=main)