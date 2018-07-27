# Conduct one-way ANOVA with effect sizes from list data.

import scipy.stats as stats
import numpy as np

Set1 = [8, 9, 6, 7, 3]
Set2 = [2, 4, 3, 5, 1]
Set3 = [3, 5, 4.5, 2, 3]
Set4 = [2, 2, -1, 100, 3]
# Set5 = []

Number_Of_Sets = 4

# Average of individual sets
Mean_Set1 = np.average(Set1)
Mean_Set2 = np.average(Set2)
Mean_Set3 = np.average(Set3)
Mean_Set4 = np.average(Set4)
# Mean_Set5 = np.average(Set5)

# Average of all sets
Mean_All = np.average([Mean_Set1, Mean_Set2, Mean_Set3, Mean_Set4])

# Error Sum of Squares for each set
Set1_SSE_List = [((i - Mean_Set1) ** 2) for i in Set1]
Set1_SSE = sum(Set1_SSE_List)

Set2_SSE_List = [((i - Mean_Set2) ** 2) for i in Set2]
Set2_SSE = sum(Set2_SSE_List)

Set3_SSE_List = [((i - Mean_Set3) ** 2) for i in Set3]
Set3_SSE = sum(Set3_SSE_List)

Set4_SSE_List = [((i - Mean_Set4) ** 2) for i in Set4]
Set4_SSE = sum(Set4_SSE_List)

# Set5_SSE_List = [((i - Mean_Set5) ** 2) for i in Set5]
# Set5_SSE = sum(Set5_SSE_List)

# Sum of Squares of Error

SSE = Set1_SSE + Set2_SSE + Set3_SSE + Set4_SSE

# Sum of Squares Between Treatments

SSB1 = (len(Set1)) * ((Mean_Set1 - Mean_All) ** 2)
SSB2 = (len(Set2)) * ((Mean_Set2 - Mean_All) ** 2)
SSB3 = (len(Set3)) * ((Mean_Set3 - Mean_All) ** 2)
SSB4 = (len(Set4)) * ((Mean_Set4 - Mean_All) ** 2)

SSB = SSB1 + SSB2 + SSB3 + SSB4

# Sum of Squares Total

SST = SSB + SSE

# Degrees of Freedom Between Treatment

DFB = Number_Of_Sets - 1

# Degrees of Freedom of Error

Number_Of_Values = len(Set1) + len(Set2) + len(Set3) + len(Set4)
DFE = Number_Of_Values - Number_Of_Sets

# Degrees of Freedom Total

DFT = Number_Of_Values - 1

# Mean Square Between Treatments

MSB = SSB / DFB

# Mean Square for Error

MSE = SSE / DFE

# Determine F Statistic

F_Stat = MSB / MSE
print("The F-statistic is " + str(F_Stat) + ".")

# Eta Squared or η², commonly used  for effect size

Eta_Squared_Set1 = SSB1 / SST
Eta_Squared_Set2 = SSB2 / SST
Eta_Squared_Set3 = SSB3 / SST
Eta_Squared_Set4 = SSB4 / SST

Eta_Squared_Error = SSE / SST
print("The η² error is " + str("{:.1%}".format(Eta_Squared_Error)) + ".")

Eta_Squared = SSB / SST
print("η² is " + str("{:.1%}".format(Eta_Squared)) + ".")

# Eta-squared is somewhat biased (based purely on sums of squares from the sample). Less biased effect size measure is Omega squared:

Omega_Squared = (SSB - (DFB * MSE)) / (SST + MSE)
print("ω² is " + str("{:.1%}".format(Omega_Squared)) + ".")

# Cohen's F can be used to describe effect size for multiple datasets

Cohen_F = np.sqrt(Eta_Squared/(1 - Eta_Squared))
print("Cohen's F for this data is " + str("{:.1%}".format(Cohen_F)) + ".")

# p-value Calculation

p = stats.f.sf(F_Stat, DFB, DFE)
print("The p-value is " + str(p) + ".")
