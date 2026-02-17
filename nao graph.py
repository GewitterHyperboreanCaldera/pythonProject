import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nao = pd.read_csv('norm.nao.monthly.b5001.current.ascii', sep = '\s+', header=None, names=['year', 'month', 'NAO'])
nao_jan = nao[nao.month == 1]

colors = np.zeros(nao_jan.NAO.shape, dtype=str)

colors[nao_jan.NAO >= 0] = 'red'
colors[nao_jan.NAO < 0] = 'blue'

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('1950-2025 January NAO index')

ax1.bar(np.arange(1950, 2024, 1), nao_jan.NAO, color=colors)

ax1.axhline(0, c='k')
plt.show()