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


## Final targets

| Full Name                    | Class         | Type  | Rotation (h/rot)  | Delta-V (km/s)|
| -----------------------------|---------------|-------|-------------------|---------------|
| 162173 Ryugu (1999 JU3)      |Apollo         |Cg     |7,627              |3,235          |
|       (2006 CT)              |Apollo         |       |16,69              |3,568          |
|101955 Bennu (1999 RQ36)      |Apollo         |       |4,288              |3,602          |
|       (2014 WF201)           |Apollo         |       |31,2               |3,614          |
|              (1999 NW2)      |Apollo         |       |4,2                |3,632          |
|       (2013 NJ)              |Apollo         |       |4,5                |3,707          |
|       (2007 CX50)            |Apollo         |       |1,45               |3,815          |
|       (2008 TT26)            |Apollo         |       |7,1                |4,010          |
|207945 (1991 JW)              |Apollo         |       |3,15               |4,085          |
|       (2006 UA216)           |Apollo         |       |2,5037             |4,183          |
|  3361 Orpheus (1982 HR)      |Apollo         |       |3,532              |4,242          |
|       (2009 FK)              |Apollo         |       |1                  |4,281          |
|163249 (2002 GT)              |Apollo         |       |3,7663             |4,535          |
|       (2001 EC16)            |Apollo         |       |200                |4,592          |
|136617 (1994 CC)              |Apollo         |       |2,3886             |4,886          |
|       (2014 BR57)            |Apollo         |       |5,07               |4,912          |
