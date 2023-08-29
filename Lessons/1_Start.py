# Импортування флет
import flet as ft

# Головна функция
def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value=""
        new_task.focus()
        new_task.update()
        
    # Метод додавання віджетів на екран
    new_task = ft.TextField(hint_text="W111111f3fefefe", width=300)
    page.add(
        # Додавання ft Row (для рядку, та додавання віджетів через контролс)
        ft.Row(controls=[
            new_task,
            ft.ElevatedButton("Add", on_click=add_clicked)
        ])
    )

# Установки що до запуску
ft.app(target=main)