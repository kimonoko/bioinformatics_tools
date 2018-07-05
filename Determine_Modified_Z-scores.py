import numpy as np

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

#Determine Modified Z-scores
titers = [7.29E+08, 6.80E+06, 5.44E+06, 4.20E+06, 3.99E+06, 6.65E+06]

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