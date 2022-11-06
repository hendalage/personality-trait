import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("aggregated_personality.csv")
print(data)

features = ['EXT', 'NEU', 'AGR', 'CON', 'OPN']

# Separating out the features
x = data.loc[:, features].values
# Separating out the character
y = data.loc[:, ['Character']].values

# Standardizing the features
x_s = StandardScaler().fit_transform(x)
print(x)

# Cosine similarity
cos_array = cosine_similarity(x)

print(cos_array)
print(cos_array.shape)

# saving to csv(replace if necessary)
a = np.asarray(cos_array)
np.savetxt("Cosine Matrix", a, delimiter=",")
