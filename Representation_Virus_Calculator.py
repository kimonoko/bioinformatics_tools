from decimal import Decimal

class style:
    BOLD = '\033[1m'
    END = '\033[0m'

Num_Guides = int(input(style.BOLD + "Please input the number of guides in your library. " + style.END))
Rep = int(input(style.BOLD + "Please input the representation you wish to keep in the screen (X). " + style.END))
MOI = float(input(style.BOLD + "Please input the target MOI. " + style.END))
Titer = float(input(style.BOLD + "Please input the titer of the library (TU/mL). " + style.END))

print("\n")
PartPerCond = Num_Guides * Rep
CellPerCond = (PartPerCond / MOI)

VolPerCond = (PartPerCond / Titer) * 1000

print("To achieve an MOI of " + style.BOLD + str(MOI) + style.END + " and " + style.BOLD +  str(Rep) + "X representation, " + style.END + "you will need to infect " + style.BOLD + str('%.2E' % Decimal(CellPerCond)) + " cells " + style.END + "with " + style.BOLD + str('%.2E' % Decimal(PartPerCond)) + " viral particles per condition." + style.END + "\n")
print("Based on the titer of this library, you will need to use " + style.BOLD + str("%.2f" % VolPerCond), "μL of virus." + style.END)
