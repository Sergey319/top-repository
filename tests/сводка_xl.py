from openpyxl import *
from openpyxl.styles import *

sv_xl = Workbook()
sv = sv_xl.active

border_side = Side(border_style="hair")
border = Border(top=border_side,
                right=border_side,
                bottom=border_side,
                left=border_side)

sv["b2"] = "ДАТА"
sv["b2"].border = Border(left=border_side, top=border_side)
sv.merge_cells("c2:d2")
sv["c2"].border = Border(top=border_side)
sv["d2"].border = Border(right=border_side)
sv["e2"] = "БРИГАДА"
sv["e2"].border = Border(top=border_side)
sv.merge_cells("g2:o2")
sv["f2"].border = Border(top=border_side)
sv["g2"].border = Border(top=border_side)
sv["o2"].border = Border(right=border_side)

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

sv_xl.save(filename="сводка.xlsx")

import excel2img
excel2img.export_img("сводка.xlsx", "sv.png", "")


sv_xl.save(filename="сводка.xlsx")







