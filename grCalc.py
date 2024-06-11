import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data from the project
magnitudes = np.array([3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5])
N_m = np.array([3991, 1125, 317, 89, 25, 7, 2, 1])
Tc = 80  # catalog period in years

# Calculate lambda(m) and log[lambda(m)]
lambda_m = N_m / Tc
log_lambda_m = np.log10(lambda_m)

# Perform linear regression to find a and b for log[λ(m)] = a - bm
slope, intercept, r_value, p_value, std_err = linregress(magnitudes, log_lambda_m)
a = intercept
b = -slope

# Gutenberg-Richter relation plot
plt.scatter(magnitudes, log_lambda_m, label='Observed data')
plt.plot(magnitudes, intercept + slope * magnitudes, label='Fitted G-R relation', color='red')
plt.xlabel('Magnitude (m)')
plt.ylabel('log[λ(m)]')
plt.legend()
plt.title('Gutenberg-Richter Relation')
plt.grid(True)
plt.show()

a, b
# Constants
m_min = 4.0
m_max = 7.0
alpha = 2.3026 * a
beta = 2.3026 * b

# Calculate ν
nu = np.exp(alpha - beta * m_min)

# Magnitude range
m_values = np.arange(m_min, m_max + 0.1, 0.1)

# Bounded G-R relationship calculation
lambda_m_bounded = nu * (np.exp(-beta * (m_values - m_min)) - np.exp(-beta * (m_max - m_min))) / (1 - np.exp(-beta * (m_max - m_min)))
log_lambda_m_bounded = np.log10(lambda_m_bounded)

# Plotting the bounded G-R relationship
plt.scatter(magnitudes, log_lambda_m, label='Observed data')
plt.plot(magnitudes, intercept + slope * magnitudes, label='Fitted G-R relation', color='red')
plt.plot(m_values, log_lambda_m_bounded, label='Bounded G-R relation', color='blue')
plt.xlabel('Magnitude (m)')
plt.ylabel('log[λ(m)]')
plt.legend()
plt.title('Bounded Gutenberg-Richter Relation')
plt.grid(True)
plt.show()