# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:18:17 2022

@author: mjoyce910
"""

#%% EXTRA CODE DONT RUN

#%% imports
import json
import pandas as pd
import geopandas as gpd
import numpy as np
import requests
import scipy.optimize as opt
import seaborn as sns
import zipfile
import fiona
import os


#%% get counts of biodiversity per county

county_biodiversity = biodiversity.groupby(['County', 'Category','Group', 'Subgroup']).size()
county_biodiversity = county_biodiversity.unstack(['Subgroup', 'Category', 'Group'])

county_biodiversity = county_biodiversity.fillna(0)

# write data to csv
county_biodiversity.to_csv('county_biodiversity.csv', index=True)


co = counties['County Name'].tolist()

# create DataFrame for amphibians and reptiles
amphibians = pd.read_csv("Amphibian_and_Reptile_Biodiversity_by_County.csv")

# print details of DataFrame
print("Columns of DF:", list(amphibians.columns),'\n')

# rename columns so they're one word
amphibians = amphibians.rename(columns={'Distribution Status':'Sighting', 
                                        'Taxonomic Group':'Group', 'Taxonomic Subgroup':'Subgroup'})

# pull out existing amphibians
amphibian_bio = amphibians.query("Sighting == 'Recently Confirmed'")
amphibian_bio = amphibian_bio.query("Group == 'Amphibians'")
keepvars = ['County', 'Subgroup', 'NY Listing Status', 
            'Federal Listing Status', 'State Conservation Rank', 
            'Global Conservation Rank']
amphibian_bio = amphibian_bio[keepvars]

county_bio = county.groupby(‘state’)[‘pop’].sum()
county_bio = {}

# test calculate amphibian diversity for albany county

# select just albany records
albany_biodiversity = biodiversity.query("County == 'Albany'").copy()

# get a bool series representing which rows have salamanders 
albany_biodiversity = albany_biodiversity.apply(lambda x : True if x['Group'] == "Amphibians" else False, axis = 1)

# count number of rows in the series with salamaders
num_amp = len(albany_biodiversity[albany_biodiversity == True].index)
print('Number of amphibians in Albany County:', num_amp)

# add number to master df
county_biodiversity.at['Albany', 'Amphibians'] = num_amp

# test calculate salamander diversity for albany county

# select just albany records
albany_biodiversity = biodiversity.query("County == 'Albany'").copy()

# get a bool series representing which rows have salamanders 
albany_biodiversity = albany_biodiversity.apply(lambda x : True if x['Subgroup'] == "Salamanders" else False, axis = 1)

# count number of rows in the series with salamaders
num_sal = len(albany_biodiversity[albany_biodiversity == True].index)
print('Number of salamanders in Albany County:', num_sal)

# add number to master df
county_biodiversity.at['Albany', 'Salamanders'] = num_sal

#%% from human community datat

# set GIS
utm18n = 26918
out_file = 'draft_DAC_designation.csv'

if os.path.exists(out_file):
    os.remove(out_file)
    
row_list = risk.json()
colnames = row_list[0]
datarows = row_list[1:]
risk = pd.DataFrame(columns=colnames, data=datarows)
    
disadvantaged = pd.DataFrame()
land_use = pd.DataFrame(columns=colnames, data=datarows)
risk = pd.DataFrame(columns=colnames, data=datarows)

row_list = communities.json()
colnames = row_list[0]
datarows = row_list[1:]
communities = pd.DataFrame(columns=colnames, data=datarows)

row_list = disadvantaged.json()
colnames = row_list[0]
datarows = row_list[1:]
disadvantaged = pd.DataFrame(columns=, data=datarows)

row_list = land_use.json()
colnames = row_list[0]
datarows = row_list[1:]


risk = risk.to_crs(epsg=utm18n)


# return list of rows (with call method built into response)
framelist = [communities, disadvantaged, land_use, risk]
for df in framelist