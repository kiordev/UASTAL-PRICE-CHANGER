import flet as ft
import openpyxl

def main(page: ft.Page):
    
    # Метод для замены прайса
    def change_price(e):
        pass
        # # Создание списка с артикулами
        # articles = [item.strip() for item in art.value.split(',')]
        # print(articles)
        
        # # Создание списка с основной ценой
        # price_retail = [float(item.strip()) for item in price.value.split(',')]
        # print(price_retail)
        
        # # Создание списка с основной ценой
        # price_wholesale = [float(item.strip()) for item in altprice.value.split(',')]
        # print(price_wholesale)
        
        # # Открытие таблицы Excel
        # wb = openpyxl.load_workbook('C:\\Users\\Admin\\VSCProjects\\FLET\\price_changer\\TableTest.xlsx')
        # sheet = wb.active

        # # Сравнение значений столбца "Артикул" и присваивание цен
        # start_row = 7
        # row = start_row
        # col_article = 'J'
        # col_retail = 'H'
        # col_wholesale = 'I'

        # while sheet[col_article + str(row)].value:
        #     article = sheet[col_article + str(row)].value
        #     if article in articles:
        #         index = articles.index(article)
        #         sheet[col_retail + str(row)].value = price_retail[index]
        #         sheet[col_wholesale + str(row)].value = price_wholesale[index]
        #     row += 1

        # # Сохранение обновленной таблицы
        # wb.save('Прайс_Uastal_Конфеденц_сегодня.xlsx')
        
    # Метод форматирования значений    
    def format_values(e):
        # Форматирование артикула
        art_string = broken_art.value
        format_art_string = art_string.replace('\r', ', ') # Удаление кареток
        art.value = format_art_string
        
        # Форматирование прайса
        price_string = broken_price.value
        format_price_string = price_string.replace(',', '.') # Замена запятых на точку
        final_format_price_string = format_price_string.replace('\r', ', ') # Удаление кареток
        price.value = final_format_price_string
        
        # Форматирование диллеской цены
        altprice_string = broken_altprice.value
        format_altprice_string = altprice_string.replace(',', '.') # Замена запятых на точку
        final_format_altprice_string = format_altprice_string.replace('\r', ', ') # Удаление кареток
        altprice.value = final_format_altprice_string
        
        # Обновление
        page.update()
        
    # Page Settings
    page.title = "ОНОВЛЮВАЧ ПРАЙСУ"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    page.window_max_height = 750
    page.window_min_height = 750
    page.window_max_width = 600
    page.window_min_width = 600
    
    # Поля для форматирования
    broken_art = ft.TextField(
        label="Артикули",
        color="black",
        border_color="#FF5E00"
    )
    
    broken_price = ft.TextField(
        label="Основна ціна",
        color="black",
        border_color="#FF5E00"
        
    )
    
    broken_altprice = ft.TextField(
        label="Дилерська ціна",
        color="black",
        border_color="#FF5E00"
    )
    
    # Поля после форматирования
    art = ft.TextField(
        read_only=True,
        color="black"
    )
    
    price = ft.TextField(
        read_only=True,
        color="black"
    )
    
    altprice = ft.TextField(
        read_only=True,
        color="black"
    )
    
    # Логотип юастал
    img = ft.Image(
        src=f"C:\\Users\\Admin\\VSCProjects\\FLET\\price_changer\\uastal_orange.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    # Название
    text = ft.Text(
        value="ОНОВЛЮВАЧ ПРАЙСУ",
        size=25,
        weight=ft.FontWeight.W_600,
        color="#FF5E00"
    )
    
    # Ряд с значениями для форматирования
    broken_row = ft.Column(
        controls=[
            broken_art,
            broken_price,
            broken_altprice
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    # Контейнер со значениями для форматирования
    text_fields = ft.Container(
        width=550,
        height=200,
        bgcolor="white",
        content=broken_row
    )
    
    # Кнопка "Форматировать"
    factor_button = ft.ElevatedButton(text="Форматувати", on_click=format_values)
    
    # Ряд с готовыми значениями
    fixed_row = ft.Column(
        controls=[
            art,
            price,
            altprice
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    # Контейнер с готовыми значениями
    ready_text_fields = ft.Container(
        width=550,
        height=200,
        bgcolor="white",
        content=fixed_row
    )
    
    # Кнопка изменить цену
    change_button = ft.ElevatedButton(text="Змінити", on_click=change_price)
    
    # Secondary = TextFields
    page.add(
        img,
        text,
        text_fields,
        factor_button,
        ready_text_fields,
        change_button
    )

ft.app(target=main)