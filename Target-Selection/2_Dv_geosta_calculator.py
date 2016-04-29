"""
Author Yann HUET 2016

Calculates delta-v for asteroids according to Shoemaker and Helin (1978)

Add delta-v to rendevouzing with asteroids from geostationary orbit

Solution inspired by http://www.asterank.com/
"""

import numpy as np
import operator
import pandas as pd


data = pd.read_csv("dataset-astro-fuel.csv")
df = pd.read_csv("dataset-astro-fuel.csv")

df.i = df.i * np.pi / 180      # inclination in radians
df['Q'] = df.a * (1.0 + df.e)  # aphelion

def AtensDeltaV(df):
  """Delta V calculation for Atens asteroids, where a < 1."""
  df['ut2'] = 2 - 2*np.cos(df.i/2)*np.sqrt(2*df.Q - df.Q**2)
  df['uc2'] = 3/df.Q - 1 - (2/df.Q)*np.sqrt(2 - df.Q)
  df['ur2'] = 3/df.Q - 1/df.a - ((2/df.Q)*np.cos(df.i/2)*np.sqrt(df.a*(1-df.e**2)/df.Q))
  return df

def ApollosDeltaV(df):
  """Delta V calculation for Apollo asteroids, where q <= 1, a >= 1."""
  df['ut2'] = 3 - 2/(df.Q + 1) - 2*np.cos(df.i/2)*np.sqrt(2*df.Q/(df.Q+1))
  df['uc2'] = 3/df.Q - 2/(df.Q+1) - (2/df.Q)*np.sqrt(2/(df.Q+1))
  df['ur2'] = 3/df.Q - 1/df.a - ((2/df.Q)*np.cos(df.i/2)*np.sqrt((df.a/df.Q)*(1-df.e**2)))
  return df

def AmorsDeltaV(df):
  """Delta V calculation for Amors asteroids, where q > 1 and a >= 1."""
  df['ut2'] = 3 - 2/(df.Q+1) - 2*np.cos(df.i/2)*np.sqrt(2*df.Q/(df.Q+1))
  df['uc2'] = 3/df.Q - 2/(df.Q+1) - ((2/df.Q)*np.cos(df.i/2)*np.sqrt(2/(df.Q+1)))
  df['ur2'] = 3/df.Q - 1/df.a - (2/df.Q)*np.sqrt(df.a*(1-df.e**2)/df.Q)
  return df

atens = AtensDeltaV(df[df.a < 1])
apollos = ApollosDeltaV(df[(df.q <= 1) & (df.a >= 1)])
amors = AmorsDeltaV(df[(df.q > 1) & (df.a >= 1)])

df = pd.concat((atens, apollos, amors))

v_earth = 29.784    # earth orbital velocity
U0 = 3.074 / v_earth;  # Normalized geostationary velocity
S = np.sqrt(2) * U0    # Normalied escape velocity from geostationary

# Impulse for leaving geostationary.
df['ul'] = np.sqrt(df.ut2 + S**2) - U0

# Impulse for rendevouzing at asteroid.
df['ur'] = np.sqrt(df.uc2 - (2*np.sqrt(df.ur2*df.uc2)*np.cos(df.i/2)) + df.ur2)

# Figure of merit, from Shoemaker and Helin.
df['F'] = df.ul + df.ur

# Delta V.
data['dv2'] = (30*df.F) + .5

data.to_csv("dataset-astro-fuel-dvgeo.csv",sep=',')
