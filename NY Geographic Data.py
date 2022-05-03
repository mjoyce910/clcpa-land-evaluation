# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:12:00 2022

@author: mjoyce910
"""

#%% imports
import pandas as pd

#%% import ny county data

# create DataFrame for counties
counties = pd.read_csv("New_York_State_ZIP_Codes-County_FIPS_Cross-Reference.csv", dtype={'GEOID':str})

