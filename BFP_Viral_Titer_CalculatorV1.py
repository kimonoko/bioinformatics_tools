class style:
   BOLD = '\033[1m'
   END = '\033[0m'

from decimal import Decimal

print("Welcome to the BFP Viral Titer Calculator.")

#Before proceeding, you should have the following information ready: the initial number of cells you plated, the number of cells you analyzed for BFP and the number of BFP positive cells for each viral diultion.

Initial_Cells = int(input(style.BOLD + "Please input the initial cell count for all plates. " + style.END))

Cells_Analyzed = int(input(style.BOLD + "Please input the number of cells analyzed per sample. " + style.END))

One_To_Fifty = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:50 viral dilution. " + style.END))

f = ((One_To_Fifty / Cells_Analyzed) * Initial_Cells) * 50
print(style.BOLD + "\nThe viral titer of the 1:50 sample is", '%.2E' % Decimal(f), "TU/mL\n" + style.END)

One_To_Hundred = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:100 viral dilution. " + style.END))

h = ((One_To_Hundred / Cells_Analyzed) * Initial_Cells) * 100
print(style.BOLD + "\nThe viral titer of the 1:100 sample is", '%.2E' % Decimal(h), "TU/mL\n" + style.END)

One_To_Five_Hundred = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:500 viral dilution. " + style.END))

x = ((One_To_Five_Hundred / Cells_Analyzed) * Initial_Cells) * 500
print(style.BOLD + "\nThe viral titer of the 1:500 sample is", '%.2E' % Decimal(x), "TU/mL\n" + style.END)

One_To_Thousand = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:1000 viral dilution. " + style.END))

y = ((One_To_Thousand / Cells_Analyzed) * Initial_Cells) * 1000
print(style.BOLD + style.BOLD + "\nThe viral titer of the 1:1000 sample is", '%.2E' % Decimal(y), "TU/mL\n" + style.END)

One_To_Five_Thousand = int(input("Please input the BFP+ cell count for the 1:5000 viral dilution. " + style.END))

t = ((One_To_Five_Thousand / Cells_Analyzed) * Initial_Cells) * 5000
print(style.BOLD + "\nThe viral titer of the 1:5000 sample is", '%.2E' % Decimal(t), "TU/mL\n" + style.END)

One_To_Ten_Thousand = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:10000 viral dilution. " + style.END))

u = ((One_To_Ten_Thousand / Cells_Analyzed) * Initial_Cells) * 10000
print(style.BOLD + "\nThe viral titer of the 1:10000 sample is", '%.2E' % Decimal(u), "TU/mL\n" + style.END)

import numpy
Average_Titer = numpy.average([f, h, x, y, t, u])
print(style.BOLD + "\nThe average viral titer of this library is", '%.2E' % Decimal(Average_Titer), "TU/mL\n" + style.END)