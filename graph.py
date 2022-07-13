import numpy as np
import matplotlib.pyplot as plt

data = [180000, 30000, 5900]
plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
plt.title('График бабла', size=14)
plt.pie(data, labels=('ИИС', 'Сбербанк-брокер', 'Бинанс'))
plt.show()