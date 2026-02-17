import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#读取資料
ao = pd.read_csv('AO.txt', sep='\s+', header=None, names=['year', 'month', 'AO'])
ao_jan = ao[ao.month == 1]
#創建顏色陣列
colors = np.zeros(ao_jan.AO.shape, dtype=str)
colors[ao_jan.AO >= 0] = 'red'
colors[ao_jan.AO < 0] = 'blue'
#创建 Figure
fig = plt.figure(figsize=(10, 8))
#创建 Axes
ax1 = fig.add_subplot(1, 1, 1)
#绘制折线图
ax1.bar(np.arange(1950, 2020, 1), ao_jan.AO, color=colors)
#添加图题
ax1.set_title('1950-2019 January AO Index')
#添加 y=0 水平参考线
ax1.axhline(0, c='k')
plt.show()