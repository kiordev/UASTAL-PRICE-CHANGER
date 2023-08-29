import flet as ft 

def main(page: ft.Page):
    
    t = ft.Tabs(
        selected_index=1, # Обраний таб
        animation_duration=300, # Швидкість анімації
        divider_color=ft.colors.GREEN, # Колір смуги під табами
        indicator_border_radius = 0, # Кут бордеру індикатору
        indicator_color = ft.colors.RED, # Колір індекатору
        label_color=ft.colors.BLUE, # Колір обранного табу
        
        tabs=[ # Вписуємо самі сторінки
            ft.Tab (
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS, #Таб може бути іконкою
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Tab 4",
                icon=ft.icons.SETTINGS,
                content=ft.Text("Testing Tab"),
            ),
            
        ],
    )
    page.add(t)

ft.app(target=main)