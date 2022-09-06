#Importing all possible packages to be used in data science as provided in class
import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files

##Project Deliverables

##Section1:
# Find or create 1 excel (.xls) file that contains at least two tabs.
# Bring in the first tab as a data frame; label that dataset as ‘tab1’, 
#A second data frame that represents the 2nd tab of the excel file, name this 'tab2' 
#Data imported from https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers

## get tab names in xlsx file
xls = xlrd.open_workbook('hha-data-ingestion/data/oasis_cross-sectional+longitudinal.xls', on_demand=True)

##used this code to find the sheet names
xls.sheet_names()
## import local xls file
tab1 = pd.read_excel('hha-data-ingestion/data/oasis_cross-sectional+longitudinal.xlsx',  sheet_name='oasis_cross-sectional') ## read xls file
tab2 = pd.read_excel('hha-data-ingestion/data/oasis_cross-sectional+longitudinal.xlsx',  sheet_name='oasis_longitudinal') ## read xls file


#Section 2:
#Find 1 open source json API via CMS, and bring it in using the 'requests' package ;
#Call the dataset ‘apiDataset’ 

apiDataset = requests.get ('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data')
apiDataset = apiDataset.json()

###Section3:
# Bring in 2 open source bigquery datasets;
# Limit your query to get the first 100 rows from each, as either a dataframe or dictionary;
# Please call the first dataset ‘bigquery1’ and the second dataset ‘bigquery2’;  
# Follow instructions from https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries to get started

### BIGQUERY
## first need to load api key that you created based on readme instructions
# connect to bigquery, be sure to update the name of your file, this is currently mine
client = bigquery.Client.from_service_account_json('hha-data-ingestion/bigquery/assignment-1-361014-c84bafec507e.json') ## create bigquery client

# Find dataset from https://cloud.google.com/datasets
# Query public dataset

#Dataset 1
query_job = client.query("SELECT * FROM `bigquery-public-data.sdoh_cdc_wonder_natality` LIMIT 100") ## query public dataset
## get results
results = query_job.result() ## get results
## putresults into dataframe
bigquery1 = pd.DataFrame(results.to_dataframe())

#Dataset 2
query_job = client.query("SELECT * FROM `bigquery-public-data.sdoh_cms_dual_eligible_enrollment` LIMIT 100") ## query public dataset
## get results
results = query_job.result() ## get results
## putresults into dataframe
bigquery2 = pd.DataFrame(results.to_dataframe()) 