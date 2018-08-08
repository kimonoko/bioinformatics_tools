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
CellTrans = (PartPerCond / MOI)
CellPerCond = CellTrans * MOI
CellPerPlate = CellPerCond / PlatesPerCond

PartPerPlate = CellPerCond * MOI
VolPerCond = (PartPerCond / Titer) * 1000

print("You will need to transduce", style.BOLD + str('%.2E' % Decimal(PartPerCond)), "viral particles (" + str("%.2f" % VolPerCond), "μL of virus) " + style.END + "into", style.BOLD + str('%.2E' % Decimal(CellTrans)) + " cells" + style.END, "to achieve", str(Rep) + "X representation at an", style.BOLD + "MOI of", str(MOI) + style.END + ".\n")
print("After infection, for each condition you will need to maintain at least", style.BOLD + str('%.2E' % Decimal(CellPerCond)), "cells per condition " + style.END + "or", style.BOLD + str("%.2E" % (CellPerPlate)), "cells per plate." + style.END + "\n")
print("Calculated using the MOI/Representation Calculator.")
