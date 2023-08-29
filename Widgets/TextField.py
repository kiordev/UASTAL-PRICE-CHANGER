import flet as ft 

def main(page: ft.Page):
    page.title="TextFields"
    page.bgcolor = ft.colors.INDIGO
    
    page.add (
        ft.TextField(
            label="Disabled", # Назва поля
            disabled=False, # Выключена/включена
            value="First name" # Значение внутри поля
        ),
    
        ft.TextField(
            label="Read-only", # Назва поля
            read_only=True, # Только для чтения
            value="Last name" # Значение внутри поля
            ),
    
        ft.TextField(
            label="With placeholder", # Назва поля
            hint_text="Please enter text here" # Подсказка
            ),
    
        ft.TextField(
            label="With an icon", # Назва поля
            icon=ft.icons.EMOJI_EMOTIONS # Іконка поруч з полем
            ),
    )
        

    

ft.app(target=main)