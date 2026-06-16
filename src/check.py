from tkinter import NO

import numpy as np

NOW_WEEK = 16
PREVIOUS_WEEK = 15

NOW = np.load(rf"D:\Capstone_BBO\data\week_{NOW_WEEK}\function_5\initial_inputs.npy")
PREV = np.load(rf"D:\Capstone_BBO\data\week_{PREVIOUS_WEEK}\function_5\initial_outputs.npy")

print("Now shape:", NOW.shape)
print("Previous shape:", PREV.shape)

print("Last Week {NOW_WEEK} point:", NOW[-1], NOW[-1])
print("Last Week {PREVIOUS_WEEK} point:", PREV[-1], PREV[-1])