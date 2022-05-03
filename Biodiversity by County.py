# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:53:54 2022

@author: mjoyce910
"""

#%% imports
import pandas as pd

#%%  biodiversity data 

# create DataFrame for biodiversity
biodiversity = pd.read_csv("Biodiversity_by_County_-_Distribution_of_Animals__Plants_and_Natural_Communities.csv")

# print details of DataFrame
print("Columns of biodiversity:", list(biodiversity.columns),'\n')

# rename columns so they're one word
biodiversity = biodiversity.rename(columns={'Distribution Status':'Sighting', 
                                        'Taxonomic Group':'Group', 
                                        'Taxonomic Subgroup':'Subgroup', 'NY Listing Status':'NYStatus', 
                                        'Federal Listing Status':'FederalStatus', 'State Conservation Rank':'StateRank', 
                                        'Global Conservation Rank':'GlobalRank'})

# master list of groups and subgroups
groups = biodiversity.drop_duplicates( subset = 'Group').copy()
groups = groups['Group'].tolist()

subgroups = biodiversity.drop_duplicates( subset = 'Subgroup').copy()
subgroups = subgroups['Subgroup'].tolist()

categories = biodiversity.drop_duplicates( subset = 'Category').copy()
categories = categories['Category'].tolist()

# keep recently confirmed biodiversity only
biodiversity = biodiversity.query("Sighting == 'Recently Confirmed'")
biodiversity = biodiversity.drop(columns=['Sighting', 'Common Name', 'Year Last Documented'])

#%% get counts of biodiversity per county

county_biodiversity = biodiversity.groupby(['County', 'Subgroup']).size()
county_biodiversity = county_biodiversity.unstack(['Subgroup'])

county_biodiversity = county_biodiversity.fillna(0)

# write data to csv
county_biodiversity.to_csv('county_biodiversity.csv', index=True)

#%% master biodiversity by county df 
# reference county names

counties = pd.read_csv("New_York_State_ZIP_Codes-County_FIPS_Cross-Reference.csv", dtype=str)
counties = counties.drop_duplicates( subset = 'County Name')
counties = counties.drop(columns = 'File Date') 
