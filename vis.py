# -*- coding: utf-8 -*-
"""vis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19QDKcrwlNLCbZIvNT88-iLjNvKRCTzYi

Vis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aXfXJuni8lF9iwvBtnm78o79fKfZZB16
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
file_path = sys.argv[1]
data = pd.read_csv(file_path)

#plotting of 2 categorical variables
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1: Traffic Situation
data['Traffic Situation'].value_counts().plot(kind='bar', ax=axes[0])
axes[0].set_title('Traffic Situation')
axes[0].set_xlabel('Traffic Situation')
axes[0].set_ylabel('Frequency')

# Plot 2: Day of the week
data['Day of the week'].value_counts().plot(kind='bar', ax=axes[1])
axes[1].set_title('Day of the week')
axes[1].set_xlabel('Day of the week')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig("vis.png")
plt.show()

import subprocess
subprocess.run(["python3", "model.py", "res_dpre.csv"])