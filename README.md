# clcpa-land-evaluation
# Pathway to Land Tract Evaluation with Regards to the New York State Climate Leadership and Community Protection Act (CLCPA)'s Scoping Plan
Megan Joyce
PAI 789 Advanced Policy Analysis
======

## Summary
New York State signed the Climate Leadership and Community Protection Act (CLCPA) into law and is currently (spring 2022) in public scoping. This act aims for a carbon neutral economy and wants to in part:
- Develop policies and programs to reduce risks threatening ecosystems and biodiversity. (AR10)
- Enhance climate resilience and adaptive capacity of agricultural community, while preparing to take advantage of emerging opportunities. (AR11)
- Preserve and protect the ability of forest ecosystems to sequester carbon. (AR12)

## Goal
This project aims to begin identifying a pathway to evaluate land in New York that may be beneficial for the protection of biodiversity, the sequestration of carbon through conserved land, and the reduction of risk for disadvantaged communities through nature-based solutions. The CLCPA is an ambitious act, and this project is only the beginning of identifying where the state should look in evaluating potential regions or areas to put effort into restoring or protecting. 

## Data
Data for this project can be accessed through New York State's open data platform: https://data.ny.gov/

Parcel Counts By Type By Municipality: Beginning Roll Year 2000 
https://data.ny.gov/Government-Finance/Parcel-Counts-By-Type-By-Municipality-Beginning-Ro/tnwc-mx3q

Biodiversity by County - Distribution of Animals, Plants and Natural Communities
https://data.ny.gov/Energy-Environment/Biodiversity-by-County-Distribution-of-Animals-Pla/tk82-7km5 

Draft Disadvantaged Communities (DAC): 2021Energy & Environment
https://data.ny.gov/Energy-Environment/Draft-Disadvantaged-Communities-DAC-2021/xj7e-q8ja

New York State ZIP Codes-County FIPS Cross-Reference
https://data.ny.gov/Government-Finance/New-York-State-ZIP-Codes-County-FIPS-Cross-Referen/juva-r6g2 

County information for the state of New York was also pulled from the Census Shapefile database
https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html 

## Scripts
1. Biodiversity by County.py: This script aggregates biodiversity data by county and by group, subgroup, and category of species. It takes only species that have been recently confirmed.  
Input files:   
"Biodiversity_by_County_-_Distribution_of_Animals__Plants_and_Natural_Communities.csv"  
"New_York_State_ZIP_Codes-County_FIPS_Cross-Reference.csv"  
Output files:   
"county_biodiversity.csv"  

2. Land Use by County.py: This script caluclates the percentage of land in each county that is categorized by type of land use. It also adds information for the counties that are part of New York City.  
Input files:   
"Parcel_Counts_By_Type_By_Municipality__Beginning_Roll_Year_2000.csv"  
Output files:   
"county_land_use.csv"  

3. Human Community Data.py: This script separates out different indicators that the State of New York uses in their draft designation of disadvantaged communities. It outputs different csv files based on land use, risk factors, and the designations themselves, as well as two spatial datasets for use with visualizations.  
Input files:   
"Draft_Disadvantaged_Communities__DAC___2021.csv"  
"cb_2019_us_county_500k_36.zip"  
Output files:    
"land_use_from_DAC.csv"  
"risk_from_DAC.csv"  
"draft_DAC_designation.csv"  
"disavantaged_communities.gpkg"  
"disadvantaged_communities.json"  

## Tableau Dashboard
The tableau dashboard allows you to compare counties across multiple metrics (biodiversity, land use) against locations of NY State's draft designations for disadvantaged communities (and each community's risk factors). The visual depiction of counties in New York State shows areas with high biodiversity and some corresponding areas with a high percentage of parcels in conservation, but also shows counties with lower biodiversity (especially for certain species) and a higher percentage of vacant lots. Looking at draft designated disavantaged communities and how they align with county data for biodiversity or land use also shows some communities that are rural or suburban in higher biodiversity areas.

See more and explore through the interactive dashboard:  
https://prod-useast-a.online.tableau.com/t/evaluationofnycountiesforconservationpotential/views/NewYorkEvaluations/Dashboard1/3ac01929-d223-46a6-8cf6-59002814f3e2/a02cfacd-def1-4467-88a9-2304770ff14b?:display_count=n&:showVizHome=n&:origin=viz_share_link 

## Next Steps
Moving forward, this project would take a look at vacant lot data from counties with high numbers of vacant lots in order to identify land that would be suitable (based on habitat connectivity, flood mitigation, high prevalence of heat islands, etc.) for potential conservation projects, especially in the context of carbon sequestration. This analysis would be useful as the state implements the CLCPA and identifies opportunities to lower risk for disadvantaged communities as well as meet its targets for carbon neutrality.
