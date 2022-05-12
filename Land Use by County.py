# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:19:13 2022

@author: mjoyce910
"""

#%% imports

import pandas as pd

#%% land use data 

# create DataFrame for land use
parcels = pd.read_csv("Parcel_Counts_By_Type_By_Municipality__Beginning_Roll_Year_2000.csv")

# print details of DataFrame
print("Columns of parcels:", list(parcels.columns),'\n')

# rename columns 
parcels = parcels.rename(columns={'Broad Use 100 - Agricultural Property Count':'Ag', 
                                        'Broad Use 200 - Residential Property Count':'Res', 
                                        'Broad Use 300 - Vacant Land Property Count':'Vacant', 
                                        'Broad Use 400 - Commercial Property County':'Commercial', 
                                        'Broad Use 500 - Recreation Property Count':'Rec', 
                                        'Broad Use 600 - Community Service Property Count':'Comm Service',
                                        'Broad Use 700 - Industrial Property Count':'Industrial',
                                        'Broad Use 800 - Public Service Property Count':'Public Service',
                                        'Broad Use 900 - Forest and Conservation Property Count':'Conservation'})

#%% get counts of land use parcels per county

land_use1 = parcels.groupby(['County Name']).sum()

land_use1 = land_use1.drop(columns = ['Roll Year', 'Swis Code'])

#%% change over to percentage of parcels in each land use

land_use = land_use1.div(land_use1['Total Parcel Count'],axis='rows')
 
land_use = land_use.drop(columns = ['Total Parcel Count'])

New_York_City = ['New York', 'Kings', 'Bronx', 'Richmond', 'Queens']

land_use = pd.concat([land_use.loc['New York']]*4, ignore_index=True)
#%% write data to csv

land_use.to_csv('county_land_use.csv', index=True)

