# Viral titer calculation generated by looking at linear regression between percent fluorescent population and dilution of virus
# Slope is then used as the titer of the virus

from decimal import Decimal
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from numpy.polynomial.polynomial import polyfit

class style:
    BOLD = '\033[1m'
    END = '\033[0m'

print(style.BOLD + "Welcome to the BFP Viral Titer Calculator." + style.END)
print("\n")

# Dilutions are assumed to be 1:50, 1:100, 1:500, 1:1000, 1:5000, 1:10000

dils = [0.02, 0.01, 0.002, 0.001, 0.0002, 0.0001]

# Before proceeding, you should have the following information ready: the number of cells analyzed and the number of BFP positive cells for each viral diultion.

Cells_Analyzed = int(input(style.BOLD + "Please input the number of cells analyzed per sample. " + style.END))
print("\n")

One_To_Fifty = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:50 viral dilution. " + style.END))

f = (One_To_Fifty / Cells_Analyzed)

One_To_Hundred = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:100 viral dilution. " + style.END))

h = (One_To_Hundred / Cells_Analyzed)

One_To_Five_Hundred = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:500 viral dilution. " + style.END))

x = (One_To_Five_Hundred / Cells_Analyzed)

One_To_Thousand = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:1000 viral dilution. " + style.END))

y = (One_To_Thousand / Cells_Analyzed)

One_To_Five_Thousand = int(input("Please input the BFP+ cell count for the 1:5000 viral dilution. " + style.END))

t = (One_To_Five_Thousand / Cells_Analyzed)

One_To_Ten_Thousand = int(input(style.BOLD + "Please input the BFP+ cell count for the 1:10000 viral dilution. " + style.END))

u = (One_To_Ten_Thousand / Cells_Analyzed)

# Create percents list as y for linregress
percents = [f, h, x, y, t, u]

# Convert dilutions and cell percents to arrays for plotting

dils = np.array(dils)
percents = np.array(percents) * 100

# Generate linear regression line

c, m = polyfit(dils, percents, 1)

# Multiply the slope by 10E5
titer = m * 10000

# Scatter plot and linear regression

plt.figure(num=1, figsize=(15, 11.28), dpi=300, facecolor='w', edgecolor='k')
plt.plot(dils, percents, '.')
plt.plot(dils, c + m * dils, '-')
plt.xlabel("Viral Dilution", fontsize=14, fontweight='bold', labelpad=20)
plt.ylabel("BFP Positive Cells (Percent)", fontsize=14, fontweight='bold', labelpad=20)
plt.xticks(np.arange(0, max(dils) + .001, step=.005))
plt.yticks(np.arange(0, max(percents) + 1, step=5))
plt.show()

print(style.BOLD + "\nThe viral titer of this library is", '%.2E' % Decimal(titer), "TU/mL.\n" + style.END)

# Calculate Pearson

a = dils
b = percents

num_values = len(a)

sqr_a = a ** 2
sqr_b = b ** 2

# All a values multiplied by values in b

c = a * b

# Sum of values in c

sum_c = sum(c)

# Sum of all values in a and b

sum_a = sum(a)
sum_b = sum(b)

# Sum of squares of values in a and b

sum_sqr_a = sum(sqr_a)
sum_sqr_b = sum(sqr_b)

# Calculate the correlation coefficient for a and b (Pearson Product-moment Coefficient)

r = (num_values * sum_c - sum_a * sum_b) / ((np.sqrt(num_values * sum_sqr_a - (sum_a ** 2))) * (np.sqrt(num_values * sum_sqr_b - (sum_b ** 2))))
print("The Pearson Product-moment coefficient of this data is", str(r) + ".")

# Threshholds for evaluating the correlation coefficient
if r > -.30 and r < .30:
    print("This r indicates there is no linear association between the input variables.")
elif r >= .30 and r < .50:
    print("This r indicates there is a weak uphill association between the input variables.")
elif r >= .50 and r < .70:
    print("This r indicates there is a moderate uphill association between the input variables.")
elif r >= .70 and r < 1:
    print("This r indicates there is a strong uphill association between the input variables.")
elif r == 1:
    print("This r indicates there is perfect uphill association between the input variables.")
elif r <= -.30 and r > -.50:
    print("This r indicates there is a weak downhill association between the input variables.")
elif r <= -.50 and r > -.70:
    print("This r indicates there is a moderate downhill association between the input variables.")
elif r <= -.70 and r > -1:
    print("This r indicates there is a strong downhill association between the input variables.")
elif r == -1:
    print("This r indicates there is a perfect downhill association between the input variables.")

print("\n")

# Calculate the percentage of variance in the dependent variable accounted for by the indepdendent variable.

r_sqr = r ** 2
print('{:.2%}'.format(r_sqr), "of the variation of the dependent variable is accounted for by the independent variable.")
