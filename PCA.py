import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#loading data into dataframe
# df_personality = pd.read_csv("aggregated_personality.csv", names=['name','EXT','NEU','AGR','CON','OPN'])
data = pd.read_csv("aggregated_personality.csv")
print (data)

features = ['EXT','NEU', 'AGR' ,'CON', 'OPN']

# Separating out the features
x = data.loc[:, features].values
# Separating out the target
y = data.loc[:,['Character']].values

# Standardizing the features
x_s = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x_s)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['PC1', 'PC2'])

finalDf = pd.concat([principalDf, data[['Character']]], axis = 1)


# # calculating the %
per_var = np.round(pca.explained_variance_ratio_ * 100)
print(per_var)

# labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
# plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
# plt.ylabel('Percentage of Explained Variance')
# plt.xlabel('Principal Component')
# plt.title('Scree Plot')
# plt.show()

# print(finalDf)


#plotting

plt.scatter(finalDf.PC1, finalDf.PC2)
plt.title('PCA Visualization')


for sample in finalDf.index:
    plt.annotate(sample, (finalDf.PC1.loc[sample], finalDf.PC2.loc[sample]))

plt.show()