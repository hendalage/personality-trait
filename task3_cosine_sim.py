import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv("Results/harry_potter_all_aggregated_personality.csv")
print(data)

features = ['EXT', 'NEU', 'AGR', 'CON', 'OPN']

# Separating out the features
x = data.loc[:, features].values
# Separating out the character
y = data.loc[:, ['Character']].values

# Standardizing the features(this part is not essential for this step)
x_s = StandardScaler().fit_transform(x)
print(x)

# Cosine similarity
cos_array = cosine_similarity(x)

print(cos_array)
print(cos_array.shape)

# saving to csv(replace if necessary)
a = np.asarray(cos_array)
np.savetxt("Results/harry_potter_all_cosine_matrix.csv", a, delimiter=",")

# plot
plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()
fig.set_size_inches(20, 20)
fig.set_dpi(200)
ax.imshow(a)
plt.show()
