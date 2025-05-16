"""
Отрисовка таблицы сводки, заполнение начальным текстом,
сохранение в xlsx и в jpg в определенный каталог
"""
from openpyxl import *
from print_sv import print_jpg
from openpyxl.styles import *

sv_xl = Workbook()
def create_jpg():
    sv = sv_xl.active

    """установка линий ячеек"""
    border = Side(color="000000", border_style="thin")
    t = Border(top=border)
    tb = Border(top=border, bottom=border)
    lt = Border(left=border, top=border)
    rt = Border(right=border, top=border)
    ltb = Border(left=border, top=border, bottom=border)
    ltr = Border(left=border, top=border, right=border)
    ltrb = Border(left=border, top=border, right=border, bottom=border)

    """отрисовка таблицы линиями (A1:N25)"""
    borders_cells = (  lt,   t,   t,  lt,   t,   t,   t,   t,   t,   t,   t,   t,   t,  rt,
                       lt,   t,   t,  lt,   t,   t,   t,   t,   t,  lt,   t,   t,   t,  rt,
                       lt,   t,   t,  lt,   t,   t,   t,   t,   t,  lt,   t,   t,   t,  rt,
                       lt,   t,   t,  lt,   t,   t,   t,   t,   t,  lt,   t,   t,   t,  rt,
                       lt,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,  rt,
                       lt,  lt,   t,  lt,   t,  lt,   t,  lt,   t,  lt,   t,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,  rt,
                       lt,  lt,   t,  lt,   t,  lt,   t,  lt,   t,  lt,   t,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,   t,  rt,
                       lt,  lt,   t,  lt,   t,  lt,   t,  lt,   t,  lt,   t,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                       lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt,  lt, ltr,
                      ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltb, ltrb)

    """установка в ячейку текста, его выравнивание и объединение ячеек"""
    text_cells = [
        # cell, value, alignment, merge_cells
        # "", "", None, None
        # пример
        # "A1", "text", Alignment(vertical="center", horizontal="center"), "A3"
        ["A1", "ДАТА", None, None],
        ["D1", "БРИГАДА", None, None],
        ["E1", "", None, "N1"],
        ["A2", "Распилено пиловочника", None, None],
        ["D2", "штук", Alignment(horizontal="center"), "I2"],
        ["J2", "м\u00B3", Alignment(horizontal="center"), "N2"],
        ["A3", "диаметр", None, None],
        ["B3", "", None, "C3"],
        ["D3", "", Alignment(horizontal="center"), "I3"],
        ["J3", "", Alignment(horizontal="center"), "N3"],
        ["A4", "диаметр", None, None],
        ["B4", "", None, "C4"],
        ["D4", "", Alignment(horizontal="center"), "I4"],
        ["J4", "", Alignment(horizontal="center"), "N4"],
        ["B5", "НАПИЛЕНО ДОСКИ", None, None],
        ["D5", "", Alignment(horizontal="center"), "E5"],
        ["B6", "0-4 с.", Alignment(horizontal="center"), "C6"],
        ["D6", "5 с.", Alignment(horizontal="center"), "E6"],
        ["F6", "6 с.", Alignment(horizontal="center"), "G6"],
        ["H6", "7 с.", Alignment(horizontal="center"), "I6"],
        ["J6", "некондиция", Alignment(horizontal="center"), "K6"],
        ["L6", "всего", None, None],
        ["M6", "общая", None, None],
        ["N6", "%", None, None],
        ["B7", "шт.", None, None],
        ["C7", "м\u00B3", None, None],
        ["D7", "шт.", None, None],
        ["E7", "м\u00B3", None, None],
        ["F7", "шт.", None, None],
        ["G7", "м\u00B3", None, None],
        ["H7", "шт.", None, None],
        ["I7", "м\u00B3", None, None],
        ["J7", "шт.", None, None],
        ["K7", "м\u00B3", None, None],
        ["L7", "шт.", None, None],
        ["M7", "м\u00B3", None, None],
        ["N7", "выхода", None, None],
        ["A8", "4 м", Alignment(horizontal="center"), None],
        ["A9", "3 м", Alignment(horizontal="center"), None],
        ["A10", "2 м", Alignment(horizontal="center"), None],
        ["A11", "Итого:", None, None],
        ["B12", "НАПИЛЕНО ДОСКИ", None, None],
        ["D12", "", Alignment(horizontal="center"), "E12"],
        ["B13", "0-4 с.", Alignment(horizontal="center"), "C13"],
        ["D13", "5 с.", Alignment(horizontal="center"), "E13"],
        ["F13", "6 с.", Alignment(horizontal="center"), "G13"],
        ["H13", "7 с.", Alignment(horizontal="center"), "I13"],
        ["J13", "некондиция", Alignment(horizontal="center"), "K13"],
        ["L13", "всего", None, None],
        ["M13", "общая", None, None],
        ["N13", "%", None, None],
        ["B14", "шт.", None, None],
        ["C14", "м\u00B3", None, None],
        ["D14", "шт.", None, None],
        ["E14", "м\u00B3", None, None],
        ["F14", "шт.", None, None],
        ["G14", "м\u00B3", None, None],
        ["H14", "шт.", None, None],
        ["I14", "м\u00B3", None, None],
        ["J14", "шт.", None, None],
        ["K14", "м\u00B3", None, None],
        ["L14", "шт.", None, None],
        ["M14", "м\u00B3", None, None],
        ["N14", "выхода", None, None],
        ["A15", "4 м", Alignment(horizontal="center"), None],
        ["A16", "3 м", Alignment(horizontal="center"), None],
        ["A17", "2 м", Alignment(horizontal="center"), None],
        ["A18", "Итого:", None, None],
        ["B19", "НАПИЛЕНО ДОСКИ", None, None],
        ["D19", "", Alignment(horizontal="center"), "E19"],
        ["B20", "0-4 с.", Alignment(horizontal="center"), "C20"],
        ["D20", "5 с.", Alignment(horizontal="center"), "E20"],
        ["F20", "6 с.", Alignment(horizontal="center"), "G20"],
        ["H20", "7 с.", Alignment(horizontal="center"), "I20"],
        ["J20", "некондиция", Alignment(horizontal="center"), "K20"],
        ["L20", "всего", None, None],
        ["M20", "общая", None, None],
        ["N20", "%", None, None],
        ["B21", "шт.", None, None],
        ["C21", "м\u00B3", None, None],
        ["D21", "шт.", None, None],
        ["E21", "м\u00B3", None, None],
        ["F21", "шт.", None, None],
        ["G21", "м\u00B3", None, None],
        ["H21", "шт.", None, None],
        ["I21", "м\u00B3", None, None],
        ["J21", "шт.", None, None],
        ["K21", "м\u00B3", None, None],
        ["L21", "шт.", None, None],
        ["M21", "м\u00B3", None, None],
        ["N21", "выхода", None, None],
        ["A22", "4 м", Alignment(horizontal="center"), None],
        ["A23", "3 м", Alignment(horizontal="center"), None],
        ["A24", "2 м", Alignment(horizontal="center"), None],
        ["A25", "Итого:", None, None]
    ]

    def rendering_table(bd_cells):
        """цикл отрисовки и установка размеров строк (20 ед.) и столбцов (10 ед.)"""
        index = 0
        for r in range(1, 26):
            for c in "abcdefghijklmn":
                if index <= len(bd_cells) - 1:
                    sv[f"{c}{r}"].border = bd_cells[index]
                    index += 1
                sv.column_dimensions[c].width = 10
                sv.row_dimensions[r].height = 20

    def setting_text(txt_cells, fontName, size):
        """цикл установки в ячейку текста, его выравнивание и объединение ячеек"""
        i = 0
        while i <= len(txt_cells) - 1:
            sv[f"{txt_cells[i][0]}"] = f"{txt_cells[i][1]}"
            sv[f"{txt_cells[i][0]}"].font = Font(name=fontName,
                                                  size=size)
            if txt_cells[i][2]:
                sv[f"{txt_cells[i][0]}"].alignment = \
                txt_cells[i][2]
            if txt_cells[i][3]:
                sv.merge_cells(
                    f"{txt_cells[i][0]}:{txt_cells[i][3]}")
            i += 1

    setting_text(text_cells, "Calibri", 11)
    rendering_table(borders_cells)

    """сохранение таблицы в xlsx в каталог с выполняемым файлом py"""
    sv_xl.save(filename="сводка.xlsx")

    from aspose.cells import Workbook, PageOrientationType, PaperSizeType

    workbook = Workbook("сводка.xlsx")
    worksheet = workbook.worksheets.get(0)

    """установка таблицы в листа A4 для печати или отправки"""
    worksheet.page_setup.paper_size = PaperSizeType.PAPER_A4
    worksheet.page_setup.orientation = PageOrientationType.LANDSCAPE
    worksheet.page_setup.top_margin = 0.0
    worksheet.page_setup.left_margin = 0.0
    worksheet.page_setup.right_margin = 0.0
    worksheet.page_setup.bottom_margin = 0.0
    worksheet.page_setup.zoom = 90
    worksheet.page_setup.center_vertically = True
    worksheet.page_setup.center_horizontally = True

    import os

    """сохранение листа в jpg в определенный каталог"""
    path = fr"C:\Users\SERGO\Documents\апрель"
    if not os.path.isdir(path):
        os.makedirs(path)
    date = 25.04
    name = fr"Сводка{date}.jpg"
    workbook.save(name)

    print_jpg(name)

    os.remove("сводка.xlsx")
    #os.remove(fr"Сводка{date}.jpg")
    #subprocess.call("/usr/bin/lpr " + fr"Сводка{date}.jpg", shell=True)
    """сохранение в jpg в каталог с выполняемым файлом py"""
    #workbook.save(fr"Сводка.jpg")

