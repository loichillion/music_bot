# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 17:48:49 2021

@author: 99loi
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler



#----------------------------------------------------------------------------------------#

####load data###########

df = pd.read_csv('C:/Users/99loi/Desktop/music_bot_final/bot/static/bot/data/data.csv', sep=',')


data_music = df.loc[:,['artists','name','key','tempo']]


#print(df.shape)
#print(data_music.shape)

data_music['full name']= data_music['artists'] + data_music['name']

df_music = data_music.drop(columns=['artists', 'name'])

df_music_final = df_music.set_index('full name')

df_music_final2 = df_music.loc[:,'full name']

#df_music.head()
#df_music_final.head()
#df_music_final2.head()

keys = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def get_key(artist,song):
    name = "['"+artist+"']"+song
    a = df_music_final.loc[name, "key"]
    if type(a)==type(df_music_final.loc["['KC & The Sunshine Band']Boogie Shoes - 45 Version", "key"]):
        b=a
    else:
        a = a.reset_index()
        b=a.iloc[0,1]
    c=int(b)
    key = keys[c]
    return [key,b]

def get_tempo(artist,song):
    name = "['"+artist+"']"+song
    a = df_music_final.loc[name, "tempo"]
    if type(a)==type(df_music_final.loc["['KC & The Sunshine Band']Boogie Shoes - 45 Version", "tempo"]):
        b=a
    else:
        a = a.reset_index()
        b=a.iloc[0,1]
    return b

#print(pca.explained_variance_ratio_) 
#print(pca.components_)

#axis = pca.components_.T
#axis /= axis.std()
#x_axis, y_axis = axis
#
#plt.plot(0.1 * x_axis, 0.1 * y_axis, linewidth=1 )
#plt.quiver(0, 0, x_axis, y_axis, zorder=11, width=0.01, scale=6, color='red')
#
#plt.savefig('pca_example_1.png')
#plt.show()

############# ACP ##############"

a= df_music_final.values
#print(a[:2,:])
#c = get_key("['Mamie Smith']Keep A Song In Your Soul")
#print(c)
#d = dict()
#for j, i in enumerate(df_music_final2):
#    if i in d :
#        d[(int(a[j][0]), int(round(a[j][1])))]+=[i]
#    else:
#        d[(int(a[j][0]), int(round(a[j][1])))]=[i]
#print(d[tuple([5,80])])
#print(d.keys())


    
a= df_music_final.values
scaler = StandardScaler()
a=scaler.fit_transform(a)
#plt.scatter(a[:,0],a[:,1])
pca = PCA(n_components=1)

a = pca.fit(a).transform(a)

#print(a.shape)
#print(a[:6])
a=a.reshape(-1)
indices = np.argsort(a)
a = a[indices]
b= df_music_final2.values[indices]
tab = list(zip(a, b))

def get_near_song(name):
    id = 0
    l=[]
    for i in b:
        if i == name:
            idn = id-1 if (a[id]-a[id-1])<(a[id+1]-a[id]) else id+1
            l.append(b[idn])
            l.append(b[idn-2])
            l.append(b[idn-3])
            l.append(b[idn+1])
            l.append(b[idn+2])
            l.append(b[idn+3])
            return l
        else:
            id +=1



def prediction(artist,song):
    name = "['"+artist+"']"+song
    pred =  get_near_song(name)
    return pred
    
# print(f"near song of Elton John : Your Song")
# prediction("Ed Sheeran","Shape of You")

# key = get_key("Elton John","Your Song")
# print(key)
# tempo = get_tempo("Elton John","Your Song")
# print(tempo)
    
# "['KC & The Sunshine Band']Boogie Shoes - 45 Version"
    
# key2 = get_key("KC & The Sunshine Band","Boogie Shoes - 45 Version")
# print(key2)
# tempo2 = get_tempo("KC & The Sunshine Band","Boogie Shoes - 45 Version")
# print(tempo2)
    
    
    
    
    
    
    
    
    
    