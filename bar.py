import numpy as np
import matplotlib.pyplot as plt

objects = ('Suisse', 'France', 'Allemagne')
incomes = [678,5986,12]
y_pos = np.arange(len(objects))

plt.bar(y_pos, incomes)
plt.show()
