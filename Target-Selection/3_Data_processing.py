'''
    Astro Fuel project
    Nasa Space Apps Challenge, 2016 Lyon france
    Subject Asteroid Mining

    The purpose of this script is to determine possible Asteroid targets to yeild for water

    We used the http://www.asterank.com/ database along with the computed_dv
'''

import pandas as pd
import numpy as np

#data=pd.read_csv("dataset-astro-fuel.csv", low_memory=False)
data=pd.read_csv("dataset-astro-fuel-dvgeo.csv", low_memory=False)

'''
'id' : objet id
'full_name' : object name
'pdes' : colums needed to join delta V
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
'dv': delta V to reach asteroid

'''


#select asteroid dependig on criterias
#Keep Type C and unknown type asteroid
data=data.loc[data['spec_B'].isin([np.nan,'C type','B','C:','Cg','Ch','Cgh','Cb'])]

#Keep object with low spin, time to rotate greater than 5hrs
data=data[data['rot_per']>=1]

#Keep object that requier less than 5km/s Delta-V to reach from geostationary orbit
data=pd.concat((data[data['dv2']<=5],data[data['dv']<=5]))
data=data.drop_duplicates().reset_index(drop=True)

#Keep object with 'moid' less than 0.02 AU (~5x dist(earth-moon))
data=data[data['moid']<=0.02]

#Keep object with inclinaison less than 10°
data=data[data['i']<=10]


print('Nb of possible targets =',len(data))
print(list(data['full_name']))


#export lighter csv for analysis
data.to_csv("targets.csv",sep=',')
