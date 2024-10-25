import flet as ft
import pandas as pd  # Для работы с Excel-файлами
from io import BytesIO  # Для работы с файлами в памяти

def main(page: ft.Page):
    # Настройки страницы
    page.title = "UASTAL змінювач цін"
    page.bgcolor = "#FFFFFF"
    page.window_height = 650
    page.window_width = 850
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 0

    # Переменная для хранения данных из Excel
    excel_data = {"Артикул": [], "Розничная цена": [], "Дилерская цена": []}

    # Функция для обработки загруженного файла
    def on_file_upload(result: ft.FilePickerResultEvent):
        if result.files:
            try:
                # Чтение файла через путь
                file_path = result.files[0].path

                # Загружаем нужные столбцы: A, F, G (с индексами 0, 5, 6)
                df = pd.read_excel(file_path, engine='xlrd', usecols=[0, 5, 6])

                # Переименовываем столбцы для удобства
                df.columns = ["Артикул", "Розничная цена", "Дилерская цена"]

                # Заполняем словарь данными из Excel
                excel_data["Артикул"] = df["Артикул"].tolist()
                excel_data["Розничная цена"] = df["Розничная цена"].tolist()
                excel_data["Дилерская цена"] = df["Дилерская цена"].tolist()

                # Обновляем кнопку после успешной загрузки
                ValikUpload.text = "Завантажено!"
                ValikUpload.bgcolor = ft.colors.GREEN
            except Exception as e:
                ValikUpload.text = "Помилка завантаження!"
                ValikUpload.bgcolor = ft.colors.RED
                print(f"Ошибка: {e}")
            
            page.update()

    # Инициализируем FilePicker
    file_picker = ft.FilePicker(on_result=on_file_upload)
    page.overlay.append(file_picker)

    # Функция для создания таблицы в контейнере
    def create_table():
        rows = []
        for i in range(len(excel_data["Артикул"])):
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(excel_data["Артикул"][i])),
                    ft.DataCell(ft.Text(str(excel_data["Розничная цена"][i]))),
                    ft.DataCell(ft.Text(str(excel_data["Дилерская цена"][i]))),
                ]
            )
            rows.append(row)

        # Создаем DataTable и обновляем содержимое TableFrame
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Артикул")),
                ft.DataColumn(ft.Text("Розничная цена")),
                ft.DataColumn(ft.Text("Дилерская цена")),
            ],
            rows=rows,
        )
        TableFrame.content = table
        page.update()

    # Кнопки
    ValikUpload = ft.ElevatedButton(
        "Завантажити таблицю Валентина",
        bgcolor=ft.colors.WHITE,
        color=ft.colors.ORANGE,
        height=50,
        on_click=lambda _: file_picker.pick_files(
            allowed_extensions=["xls"], allow_multiple=False  # Разрешаем только .xls файлы
        ),
    )

    adaptButton = ft.ElevatedButton(
        "Адаптувати",
        bgcolor=ft.colors.WHITE,
        color=ft.colors.ORANGE,
        height=50,
        on_click=lambda _: create_table(),
    )

    importButton = ft.ElevatedButton("Створити файл імпорту", bgcolor=ft.colors.WHITE, color=ft.colors.ORANGE)
    priceButton = ft.ElevatedButton("Оновити прайс", bgcolor=ft.colors.WHITE, color=ft.colors.ORANGE)
    uploadButton = ft.ElevatedButton("Завантажити прайс", bgcolor=ft.colors.WHITE, color=ft.colors.ORANGE)

    # Контейнер для таблицы
    TableFrame = ft.Container(
        bgcolor=ft.colors.GREY,
        width=750,
        height=400,
        content=None,  # Таблица появится после нажатия adaptButton
    )

    # Размещение элементов
    TextFieldsRow = ft.Row([ValikUpload, adaptButton], alignment=ft.MainAxisAlignment.CENTER)
    uploadRow = ft.Column([uploadButton])
    importPriceButtonRow = ft.Row(
        [importButton, uploadRow, priceButton],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    mainColumn = ft.Column(
        [TextFieldsRow, TableFrame, importPriceButtonRow],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Основной контейнер
    mainFrame = ft.Container(content=mainColumn, padding=10)

    # Добавляем основной контейнер на страницу
    page.add(mainFrame)

# Запуск приложения
ft.app(target=main)
