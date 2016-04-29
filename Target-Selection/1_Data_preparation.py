'''
    Author Yann HUET 2016
    
    Astro Fuel project
    Nasa Space Apps Challenge, 2016 Lyon france
    Subject Asteroid Mining

    The purpose of this script is to determine possible Asteroid targets to mine for water

    We used the http://www.asterank.com/ database along with the computed_dv
'''

import pandas as pd
import numpy as np

data=pd.read_csv("latest_fulldb.csv", low_memory=False)
Dv=pd.read_csv("computed_dv.csv")

'''
'id' : objet id
'full_name' : object name
'pdes' : colum needed to join delta V
'diameter' : diameter in Km
'diameter_sigma' : diameter sigma in Km
'albedo' : albedo to determine class
'rot_per' : Spin period in hrs
'GM' : mass expressed as product of mass grave const G
'BV' : color index B-V (mag)
'UB' : color index U-B (mag)
'IR' : color index I-R (mag)
'e' : eccentricity
'a' : semi major axis (Au)
'q' : perihelion dist (AU)
'i' : inclination (deg)
'moid' : Earth Min Orb Intersec dist (AU)

'''


#we only keep data needed for our project (cf target determination)
data=data[['id','full_name','prefix','pdes','class','diameter','diameter_sigma','albedo','rot_per','GM', 'BV', 'UB', 'IR','e', 'a', 'q', 'i','moid','spec_B', 'spec_T']]

#add Delta V data
data=pd.merge(data,Dv, on='pdes')

print(set(data['class']))
#Focus on 'APO','AMO','AST' type
data=data.loc[data['class'].isin(['APO','AMO','AST'])]

#export lighter csv for analysis
data.to_csv("dataset-astro-fuel.csv",sep=',')
