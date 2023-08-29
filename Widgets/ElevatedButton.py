import flet as ft 

def main(page: ft.Page):
    page.title="TextFields"
    page.bgcolor = ft.colors.INDIGO
    
    page.add (
        ft.ElevatedButton(
            text="Elevated button" # Текст
            ),
        
        ft.ElevatedButton(
            "Disabled button", # Текст
            disabled=True # Вкл выкл
            ),
        
        ft.ElevatedButton(
            "Button with icon", # Текст
            icon="chair_outlined"), # Иконка
        
        ft.ElevatedButton(
            "Button with colorful icon",# Текст
            icon="park_rounded",
            icon_color="green400",
        ),
    )
        

    

ft.app(target=main)