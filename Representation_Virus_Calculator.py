from decimal import Decimal

class style:
    BOLD = '\033[1m'
    END = '\033[0m'

Num_Guides = int(input(style.BOLD + "Please input the number of guides in your library. " + style.END))
Rep = int(input(style.BOLD + "Please input the representation you wish to keep in the screen. " + style.END))
MOI = float(input(style.BOLD + "Please input the target MOI. " + style.END))
PlatesPerCond = int(input(style.BOLD + "Please input the number of plates per condition. " + style.END))
Titer = float(input(style.BOLD + "Please input the titer of the library. " + style.END))

print("\n")
PartPerCond = Num_Guides * Rep
CellPerCond = (PartPerCond / MOI)
CellPerPlate = CellPerCond / PlatesPerCond

PartPerPlate = CellPerPlate * MOI
VolPerPlate = (PartPerPlate / Titer) * 1000

print("You will need", style.BOLD + str('%.2E' % Decimal(PartPerCond)), "viral particles per condition" + style.END, "and", style.BOLD +  str('%.2E' % Decimal(CellPerPlate)), "cells per plate (" + str('%.2E' % Decimal(CellPerCond)) + " cells per condition)" + style.END, "to maintain", str(Rep) + "X representation.\n")
print("To achieve", style.BOLD + str('%.2E' % Decimal(PartPerPlate)), "viral particles per plate" + style.END, "for an MOI of", str(MOI) + ", you will need to use", style.BOLD + str("%.2f" % VolPerPlate), "μL of virus.\n" + style.END)
print("Calculated using the MOI/Representation Calculator.")
