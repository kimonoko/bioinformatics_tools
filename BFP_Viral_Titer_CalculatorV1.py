class style:
   BOLD = '\033[1m'
   END = '\033[0m'

from decimal import Decimal

print("Welcome to the BFP Viral Titer Calculator.")
print("\n")
#Before proceeding, you should have the following information ready: the initial number of cells you plated, the number of cells you analyzed for BFP and the number of BFP positive cells for each viral diultion.

Initial_Cells = int(input(style.BOLD + "Please input the initial cell count for all plates. " + style.END))
print("\n")
Cells_Analyzed = int(input(style.BOLD + "Please input the number of cells analyzed per sample. " + style.END))
print("\n")
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

titers = [f, h, x, y, t, u]

#Determine IQR
import pandas as pd
import numpy as np
from scipy.stats import iqr
x = np.array(titers)
x
Interquartile_Range = iqr(x)
Sci_Interquartile_Range = "%.2E" % Decimal(Interquartile_Range)

print(style.BOLD + "The interquartile range for this data is", Sci_Interquartile_Range + style.END)

Q1 = np.percentile(titers, 25)
Median = np.percentile(titers, 50)
Q3 = np.percentile(titers, 75)

Lower_Inner_Fence = Q1 - (Interquartile_Range * 1.5)
Upper_Inner_Fence = Q3 + (Interquartile_Range * 1.5)

Lower_Outer_Fence = Q1 - (Interquartile_Range * 3)
Upper_Outer_Fence = Q3 + (Interquartile_Range * 3)

print("\n")
print(style.BOLD + "According to this interquartile range:" + style.END)
print("\n")
for titer in titers:
    if titer > Lower_Inner_Fence and titer < Upper_Inner_Fence and titer > Lower_Outer_Fence and titer < Upper_Outer_Fence:
        print(str("%.2E" % Decimal(titer)), "is not a major or minor outlier.")
    elif titer < Lower_Outer_Fence or titer > Upper_Outer_Fence:
        print(style.BOLD + str("%.2E" % Decimal(titer)), "is a major outlier." + style.END)
    elif titer < Lower_Inner_Fence or titer > Upper_Inner_Fence:
        print(style.BOLD + str("%.2E" % Decimal(titer)), "is a minor outlier." + style.END)

#Determine Modified Z-scores
Mean = np.average(titers)
Median = np.median(titers)
#MAD Step 1 - subtract median from each value and make new list
DiffList = [np.abs(i - Median) for i in titers]
#MAD Step 2 - Find the absolute value of the median of that list
MAD = np.median(DiffList)
StdDev = np.std(titers, dtype=np.float64)
Const = .6745

ModZ = [(Const * (i - Median))/MAD for i in titers]
ModZ2 = ["%.2f" % round(l,2) for l in ModZ]
ModZ3 = [float(f) for f in ModZ2]
print("\n")
print(style.BOLD + "The modified Z-scores for this data are:" + style.END)
print("\n")
print(ModZ3)
print("\n")
print(style.BOLD + "According to the modified Z-scores for this data (cutoff |3.5|):" + style.END)
print("\n")

for z in ModZ:
    if np.abs(z) > 3.5:
        print(style.BOLD + str("%.2f" % round(z,2)), "is an outlier." + style.END)
    else:
        print(str("%.2f" % round(z,2)), "is not an outlier.")
