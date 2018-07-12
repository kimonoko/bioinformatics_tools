# Correlation Coefficient (r), also known as the Pearson Product-moment Coefficient, and the Coefficient of Determination (r-squared)

from scipy import stats
import numpy as np

# Replace the lists below with your own data.
a = np.random.randn(100)
b = np.random.randn(100)

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