from openpyxl import *
from openpyxl.styles import *

sv_xl = Workbook()
sv = sv_xl.active

border = Side(color="000000", border_style="thin")
t = Border(top=border)
tb = Border(top=border, bottom=border)
lt = Border(left=border, top=border)
rt = Border(right=border, top=border)
ltb = Border(left=border, top=border, bottom=border)
ltr = Border(left=border, top=border, right=border)
ltrb = Border(left=border, top=border, right=border, bottom=border)

# отрисовка таблицы
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

# цикл отрисовки
i = 0
for r in range(1, 26):
    for c in "abcdefghijklmn":
        if i <= len(borders_cells) - 1:
            sv[f"{c}{r}"].border = borders_cells[i]
            i += 1
        sv.column_dimensions[c].width = 10
        sv.row_dimensions[r].height = 20

#for cell in borders_cells:
#    sv.column_dimensions[cell[0][0]].width = 10
#    sv.row_dimensions[int(cell[0][1])].height = 20
#    #sv[cell[0]].font = Font(name="Calibri", size=14)
#    #sv[cell[0]].alignment = Alignment(vertical="center")
#    sv[cell[0]].border = cell[1]
#    sv[cell[0]] = cell[0]



"""border_side = Side(border_style="hair")
border = Border(top=border_side,
                right=border_side,
                bottom=border_side,
                left=border_side)
"""
"""sv["a1"] = "ДАТА"
sv["a1"].border = Border(left=border_side, top=border_side)
sv.merge_cells("c1:d1")
sv["c1"].border = Border(top=border_side)
sv["d1"].border = Border(right=border_side)
sv["e1"] = "БРИГАДА"
sv["e1"].border = Border(top=border_side)
sv.merge_cells("g1:o1")
sv["f1"].border = Border(top=border_side)
sv["g1"].border = Border(top=border_side)
sv["o1"].border = Border(right=border_side)

sv["b3"] = "Распилено пиловочника"
sv["b3"].border = Border(left=border_side, top=border_side)
sv["c3"].border = Border(top=border_side)
sv["d3"].border = Border(top=border_side)
sv.merge_cells("e3:j3")
sv["e3"] = "штук"
sv["e3"].alignment = Alignment(horizontal="center")
sv["e3"].border = Border(left=border_side, top=border_side)
sv.merge_cells("k3:o3")
sv["k3"] = "всего м\u00B3"
sv["k3"].alignment = Alignment(horizontal="center")
sv["k3"].border = Border(left=border_side, top=border_side)
sv["o3"].border = Border(right=border_side)

sv["b4"] = "диаметр"
sv["b4"].border = Border(left=border_side, top=border_side)
sv["c4"].border = Border(top=border_side)
sv["d4"].border = Border(top=border_side)
sv.merge_cells("e4:j4")
sv["e4"].border = Border(left=border_side, top=border_side)
sv.merge_cells("k4:o4")
sv["k4"].border = Border(left=border_side, top=border_side)
sv["o4"].border = Border(right=border_side)

sv["b5"] = "диаметр"
sv["b5"].border = Border(left=border_side, top=border_side)
sv["c5"].border = Border(top=border_side)
sv["d5"].border = Border(top=border_side)
sv.merge_cells("e5:j5")
sv["e5"].border = Border(left=border_side, top=border_side)
sv.merge_cells("k5:o5")
sv["k5"].border = Border(left=border_side, top=border_side)
sv["o5"].border = Border(right=border_side)

for i in range(6, 21, 7):
    sv[f"b{i}"].border = Border(left=border_side, top=border_side)
    sv[f"c{i}"] = "НАПИЛЕНО ДОСКИ"
    sv[f"c{i}"].border = Border(top=border_side)
    sv[f"d{i}"].border = Border(top=border_side)
    sv.merge_cells(f"e{i}:f{i}")
    sv[f"e{i}"].border = Border(top=border_side)
    for w in ["g", "h", "i", "j", "k", "l", "m", "n", "o"]:
        sv[f"{w}{i}"].border = Border(top=border_side)
    sv[f"o{i}"].border = Border(top=border_side, right=border_side)

for i in range(7, 22, 7):
    sv[f"b{i}"].border = Border(left=border_side, top=border_side)
    sv.merge_cells(f"c{i}:d{i}")
    sv[f"c{i}"] = "0-4 с."
    sv[f"c{i}"].alignment = Alignment(horizontal="center")
    sv[f"c{i}"].border = Border(left=border_side, top=border_side)
    sv.merge_cells(f"e{i}:f{i}")
    sv[f"e{i}"] = "5 с."
    sv[f"e{i}"].alignment = Alignment(horizontal="center")
    sv[f"e{i}"].border = Border(left=border_side, top=border_side)
    sv.merge_cells(f"g{i}:h{i}")
    sv[f"g{i}"] = "6 с."
    sv[f"g{i}"].alignment = Alignment(horizontal="center")
    sv[f"g{i}"].border = Border(left=border_side, top=border_side)
    sv.merge_cells(f"i{i}:j{i}")
    sv[f"i{i}"] = "7 с."
    sv[f"i{i}"].alignment = Alignment(horizontal="center")
    sv[f"i{i}"].border = Border(left=border_side, top=border_side)
    sv.merge_cells(f"k{i}:l{i}")
    sv[f"k{i}"] = "некондиция"
    sv[f"k{i}"].alignment = Alignment(horizontal="center")
    sv[f"k{i}"].border = Border(left=border_side, top=border_side)
    sv[f"m{i}"]= "всего"
    sv[f"m{i}"].border = Border(left=border_side, top=border_side)
    sv[f"n{i}"] = "общая"
    sv[f"n{i}"].border = Border(left=border_side, top=border_side)
    sv[f"o{i}"] = "%"
    sv[f"o{i}"].border = Border(left=border_side, top=border_side, right=border_side)

for i in range(8, 23, 7):
    sv[f"b{i}"].border =Border(left=border_side, top=border_side)
    for w in ["cd", "ef", "gh", "ij", "kl", "mn"]:
        sv[f"{w[0]}{i}"] = "шт."
        sv[f"{w[0]}{i}"].border = Border(left=border_side, top=border_side)
        sv[f"{w[1]}{i}"] = "м\u00B3"
        sv[f"{w[1]}{i}"].border = Border(left=border_side, top=border_side)
    sv[f"o{i}"] = "выхода"
    sv[f"o{i}"].border = Border(left=border_side, top=border_side, right=border_side)

for i in range(9, 24, 7):
    sv[f"b{i}"] = "4 м"
    sv[f"b{i}"].alignment = Alignment(horizontal="center")
    for w in "bcdefghijklmno":
        sv[f"{w}{i}"].border = Border(left=border_side, top=border_side)
    sv[f"o{i}"].border = Border(left=border_side, top=border_side, right=border_side)

for i in range(10, 25, 7):
    sv[f"b{i}"] = "3 м"
    sv[f"b{i}"].alignment = Alignment(horizontal="center")
    for w in "bcdefghijklmno":
        sv[f"{w}{i}"].border = Border(left=border_side, top=border_side)
    sv[f"o{i}"].border = Border(left=border_side, top=border_side, right=border_side)

for i in range(11, 26, 7):
    sv[f"b{i}"] = "2 м"
    sv[f"b{i}"].alignment = Alignment(horizontal="center")
    for w in "bcdefghijklmno":
        sv[f"{w}{i}"].border = Border(left=border_side, top=border_side)
    sv[f"o{i}"].border = Border(left=border_side, top=border_side, right=border_side)

for i in range(12, 27, 7):
    sv[f"b{i}"] = "Итого:"
    for w in "bcdefghijklmno":
        sv[f"{w}{i}"].border = Border(left=border_side, top=border_side, bottom=border_side)
    sv[f"o{i}"].border = Border(left=border_side, top=border_side, right=border_side, bottom=border_side)
"""
sv_xl.save(filename="сводка.xlsx")

from aspose.cells import Workbook, PageOrientationType, PaperSizeType
workbook = Workbook("сводка.xlsx")
worksheet = workbook.worksheets.get(0)

worksheet.page_setup.paper_size = PaperSizeType.PAPER_A4
worksheet.page_setup.orientation = PageOrientationType.LANDSCAPE
worksheet.page_setup.top_margin = 0.0
worksheet.page_setup.left_margin = 0.0
worksheet.page_setup.right_margin = 0.0
worksheet.page_setup.bottom_margin = 0.0
worksheet.page_setup.zoom = 90
worksheet.page_setup.center_vertically = True
worksheet.page_setup.center_horizontally = True


workbook.save("Out.jpg")