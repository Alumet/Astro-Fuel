#Target selection
Scripts aim to extract from asteroid database, the most suitable asteroid for 2nd stage

##Database

The databse is too large to include in this repository, and downloading it takes some time. 

#####Download options: 

  - http://www.ianww.com/latest_fulldb.csv (Asterank project https://github.com/typpo/asterank/blob/master/README.md)
  - http://ssd.jpl.nasa.gov/sbdb_query.cgi and downloading all attributes for all objects in CSV format.

## Python Scripts

#####1_Dat_prepartion.py

Extract asteroid from database and add the corresponding Delta-V required to rendezvous form LEO

#####2_Dv_geosta_calculator.py

Calculates delta-v for asteroids form Geostationary orbit according to Shoemaker and Helin (1978)

#####3_Data_processing.py

Extract asteroids meeting mission requirement.
  -	C type asteroids 
  -	Low spin. Objects with rotation period greater than 1hr
  -	Delta-V needed to rendezvous smaller than 5km/s
  -	MOID smaller than 0.02 AU (5x dist Earth – Moon)
  -	Orbit inclination smaller than 10°

