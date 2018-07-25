class style:
   BOLD = '\033[1m'
   END = '\033[0m'

#Determine IQR
titers = [6.47E+05, 2.06E+06, 5.10E+06, 5.10E+06, 2.96E+06]

import numpy as np
from decimal import *
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
