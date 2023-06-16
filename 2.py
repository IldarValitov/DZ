import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(20).cumsum(), index = np.arange(0,200,10))
s.plot()
plt.show()
