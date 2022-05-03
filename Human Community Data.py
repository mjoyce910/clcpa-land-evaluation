# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:32:30 2022

@author: mjoyce910
"""

#%% imports
import pandas as pd

#%% get data
# create DataFrame for disadvantaged community metrics
communities = pd.read_csv("Draft_Disadvantaged_Communities__DAC___2021.csv", dtype={'GEOID':str})

# print details of DataFrame
print("Columns of DF:", list(communities.columns),'\n')

# pull out DAC communities
disadvantaged = communities.query("DAC_Designation == 'Designated as a Draft DAC'")

#%% separate out land use data

keepvars = ['GEOID', 'Urban_Rural', 'Industrial_Land_Use', 'Agricultural_Land_Use', 'Low_Vegetative_Cover']
land_use = communities[keepvars].copy()

# change urban status into numbers
land_use.Urban_Rural[land_use.Urban_Rural == 'urban'] = 1
land_use.Urban_Rural[land_use.Urban_Rural == 'suburban'] = 1/2
land_use.Urban_Rural[land_use.Urban_Rural == 'rural'] = 0

# final conversion now worked
land_use[['Urban_Rural']] = land_use[['Urban_Rural']].astype(float)

#%% separate out risk data

keepvars = ['GEOID', 'Coastal_Flooding_Storm_Risk', 'Days_Above_90_Degrees_2050', 'Inland_Flooding_Risk']
risk = communities[keepvars].copy()

#%% write data to csv

land_use.to_csv('land_use_from_DAC',index=True)

risk.to_csv('risk_from_DAC.csv',index=True)

disadvantaged.to_csv('draft_DAC_designation.csv',index=True)