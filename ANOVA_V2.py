# Conduct one-way ANOVA with effect sizes from imported CSV. Still broken, in progress.

import scipy.stats as stats
import numpy as np
import pandas as pd

df = pd.read_csv('anova_test_blank2.csv', header=0, skip_blank_lines=True, engine='python')
df.dropna(how="all", inplace=True)
df.dropna(how="all", inplace=True, axis=1)

Set1 = df.iloc[:, 0]
print(Set1)
Set2 = df.iloc[:, 1]
print(Set2)
Set3 = df.iloc[:, 2]
# Set4 = df.iloc[:, 3]
# Set5 = df.iloc[:, 4]

Number_Of_Sets = len(df.columns)
print("The number of sets is", str(Number_Of_Sets))

# Average of individual sets
Mean_Set1 = np.average(Set1)
print(Mean_Set1)
Mean_Set2 = np.average(Set2)
Mean_Set3 = np.average(Set3)
# Mean_Set4 = np.average(Set4)
# Mean_Set5 = np.average(Set5)   

# Average of all sets
Mean_All = np.average([Mean_Set1, Mean_Set2])
Mean_All = np.average([Mean_Set1, Mean_Set2, Mean_Set3])
# Mean_All = np.average([Mean_Set1, Mean_Set2, Mean_Set3, Mean_Set4, Mean_Set5])

# Error Sum of Squares for each set
Set1_SSE_List = [((i - Mean_Set1) ** 2) for i in Set1]
Set1_SSE = sum(Set1_SSE_List)

Set2_SSE_List = [((i - Mean_Set2) ** 2) for i in Set2]
Set2_SSE = sum(Set2_SSE_List)

Set3_SSE_List = [((i - Mean_Set3) ** 2) for i in Set3]
Set3_SSE = sum(Set3_SSE_List)

# Set4_SSE_List = [((i - Mean_Set4) ** 2) for i in Set4]
# Set4_SSE = sum(Set4_SSE_List)

# Set5_SSE_List = [((i - Mean_Set5) ** 2) for i in Set5]
# Set5_SSE = sum(Set5_SSE_List)

# Sum of Squares of Error

SSE = Set1_SSE + Set2_SSE + Set3_SSE

# Sum of Squares Between Treatments

SSB1 = (len(Set1) * ((Mean_Set1 - Mean_All) ** 2))
SSB2 = (len(Set2) * ((Mean_Set2 - Mean_All) ** 2))
SSB3 = (len(Set3) * ((Mean_Set3 - Mean_All) ** 2))
# SSB4 = (len(Set4) * ((Mean_Set4 - Mean_All) ** 2))
# SSB5 = (len(Set5) * ((Mean_Set5 - Mean_All) ** 2))

SSB = SSB1 + SSB2 + SSB3

# Sum of Squares Total

SST = SSB + SSE

# Degrees of Freedom Between Treatment

DFB = Number_Of_Sets - 1

# Degrees of Freedom of Error

Number_Of_Values = len(Set1) + len(Set2) + len(Set3)
print("The total number of values is", str(Number_Of_Values) + ".")

DFE = Number_Of_Values - Number_Of_Sets

# Degrees of Freedom Total

DFT = Number_Of_Values - 1

# Mean Square Between Treatments

MSB = SSB / DFB

# Mean Square for Error

MSE = SSE / DFE

# Determine F Statistic

F_Stat = MSB / MSE
print("The F statistic is " + str(F_Stat) + ".")

# Eta Squared or η², commonly used  for effect size

Eta_Squared_Set1 = SSB1 / SST
Eta_Squared_Set2 = SSB2 / SST
Eta_Squared_Set3 = SSB3 / SST
# Eta_Squared_Set4 = SSB4 / SST

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

stats.f_oneway(Set1, Set2, Set3)
