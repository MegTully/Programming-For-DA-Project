import numpy as np
import pandas as pd
# Needed for plotting
import matplotlib.colors
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Needed for generating classification, regression and clustering datasets
import sklearn.datasets as dt

# Needed for generating data from an existing dataset
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
seed = 11

rand_state = 11
metacritic = pd.read_csv(r"C:\Users\Owner\repos\Programming For DA\metacritic_game_info.csv")

df_meta = pd.DataFrame(metacritic, columns=["Title","Year","Metascore","Avg_Userscore"])


# Fit a kernel density model using GridSearchCV to determine the best parameter for bandwidth
bandwidth_params = {'bandwidth': np.arange(0.01,1,0.05)}
grid_search = GridSearchCV(KernelDensity(), bandwidth_params)
grid_search.fit(df_meta)
kde = grid_search.best_estimator_

# Generate/sample 100 new rows from this dataset
ai = kde.sample(100, random_state=rand_state)
