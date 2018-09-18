from decimal import Decimal

class style:
    BOLD = '\033[1m'
    END = '\033[0m'

Num_Guides = int(input(style.BOLD + "Please input the number of guides in your library. " + style.END))
Rep = int(input(style.BOLD + "Please input the representation you wish to keep in the screen. " + style.END))
MOI = float(input(style.BOLD + "Please input the target MOI. " + style.END))
Titer = float(input(style.BOLD + "Please input the titer of the library. " + style.END))

print("\n")
PartPerCond = Num_Guides * Rep
CellPerCond = (PartPerCond / MOI)

VolPerCond = (PartPerCond / Titer) * 1000

print("To achieve an MOI of " + str(MOI) + " and " + str(Rep) + "X representation, you will need to infect " + str('%.2E' % Decimal(CellPerCond)) + " cells with " + str('%.2E' % Decimal(PartPerCond)) + " viral particles per condition." + style.END)
print("Based on the titer of this library, this means you will need to use " + str("%.2f" % VolPerCond), "μL of virus.")
