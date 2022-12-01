import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv("Results/harry_potter_all_aggregated_personality.csv")
print(data)

features = ['EXT', 'NEU', 'AGR', 'CON', 'OPN']

# Separating out the features
x = data.loc[:, features].values
# Separating out the target
y = data.loc[:, ['Character']].values

# testing purposes
print(x.shape)

# Standardizing the features
x_s = StandardScaler().fit_transform(x)
print(x_s)
print(x_s.shape)

# performing PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x_s)
principalDf = pd.DataFrame(data=principalComponents
                           , columns=['PC1', 'PC2'])
# testing purposes
print(principalDf)

# adding character names to the finalDF dataframe
finalDf = pd.concat([data[['Character']], principalDf], axis=1)
print(finalDf)

# # calculating the % variance ratio
per_var = np.round(pca.explained_variance_ratio_ * 100)
print(per_var)

# plotting

plt.scatter(finalDf.PC1, finalDf.PC2)

plt.ylabel('Principle component 2')
plt.xlabel('Principle component 1')
plt.title('PCA Visualization')

for sample in finalDf.index:
    plt.annotate(sample, (finalDf.PC1.loc[sample], finalDf.PC2.loc[sample]))

plt.show()
