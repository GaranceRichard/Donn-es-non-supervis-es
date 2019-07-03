
# coding: utf-8

# Récupération

# In[299]:


import os
os.chdir('/home/garance/Bureau')
import pandas as pd
data = pd.read_csv("decathlon.txt", sep="\t")
#data = data.head(13)
mydata = data.drop(['Points', 'Rank', 'Competition'], axis=1)
X = mydata.values
print(data.head())


# Standardisation

# In[300]:


from sklearn import preprocessing
std_scale = preprocessing.StandardScaler().fit(X)
X_scaled = std_scale.transform(X)


# ACP

# In[301]:


from sklearn import decomposition

pca = decomposition.PCA(n_components=2)
pca.fit(X_scaled)
print(pca.explained_variance_ratio_)


# In[302]:


print pca.explained_variance_ratio_.cumsum()


# In[303]:


X_projected = pca.transform(X_scaled)
print X_projected.shape


# Visualisation

# In[304]:


import matplotlib.pyplot as plt
color = data.get("Rank")
color *= -1
fig = plt.figure(figsize=(20,10))
plt.scatter(X_projected[:,0],X_projected[:,1],c=color, s=1000)
for i, (x,y) in enumerate(zip(X_projected[:,0],
                             X_projected[:,1])):
    plt.text(x,y, data.index[i])
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.colorbar()
plt.show()


# In[305]:


#Structure de composition
pcs = pca.components_
figure = plt.figure(figsize=(15,15))
for i, (x,y) in enumerate(zip(pcs[0,:],pcs[1,:])):
    plt.plot([0,x],[0,y])
    plt.text(x,y,data.columns[i])
plt.xlabel("PC 1")
plt.ylabel("PC 2")

plt.show()


# 3D ?

# In[306]:


from sklearn import decomposition

pca = decomposition.PCA(n_components=3)
pca.fit(X_scaled)
print(pca.explained_variance_ratio_)


# In[307]:


print pca.explained_variance_ratio_.cumsum()


# In[308]:


X_projected = pca.transform(X_scaled)
print X_projected.shape


# Visualisation

# In[312]:


from mpl_toolkits.mplot3d import Axes3D
coulour = data.get("Rank")
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
size = X_projected[:,0]**0+1000
p=ax.scatter(X_projected[:,0],X_projected[:,1], X_projected[:,2], c=coulour, s=size)

for i, (x,y,z) in enumerate(zip(X_projected[:,0],
                             X_projected[:,1],
                               X_projected[:,2])):
    ax.text(x,y,z, data.index[i],color='k')
    
ax.set_xlabel("PC 1")
ax.set_ylabel("PC 2")
ax.set_zlabel("PC 3")
"""ax.set_xlim([-6, 2])
ax.set_ylim([0, 5])
ax.set_zlim([-3, 1.5])"""
fig.colorbar(p)

plt.show()


# In[320]:


#Structure de composition
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
1

pcs = pca.components_

for i, (x,y,z) in enumerate(zip(pcs[0,:],pcs[1,:], pcs[2,:])):
    ax.plot([0,x],[0,y],[0,z])
    ax.text(x,y,z,data.columns[i])
    
ax.set_xlabel("PC 1")
ax.set_ylabel("PC 2")
ax.set_zlabel("PC 3")
ax.set_xlim([-1,0.1])
ax.set_ylim([0.3,.8])
ax.set_zlim([-1,0.2])


plt.show()

