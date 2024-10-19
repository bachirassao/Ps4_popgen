#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd

# Base URL for the GBIF API
url = 'https://api.gbif.org/v1/species/search'

# Define the parameters for the search (e.g., searching for "Puma concolor")
params = {
    'q': 'Puma concolor',
    'rank': 'species',
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    species_data = response.json()

    # Convert the results to a DataFrame
    df_species = pd.DataFrame(species_data['results'])

    # Display the first few rows of species data
    print("Species Data:")
    print(df_species.head())
else:
    print(f"Error fetching data: {response.status_code}")


# In[2]:


import requests
import pandas as pd

# Base URL for GBIF occurrence search API
url = 'https://api.gbif.org/v1/occurrence/search'

# Define parameters for the search (e.g., finding occurrences of 'Puma concolor')
params = {
    'scientificName': 'Puma concolor',
    'limit': 10
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    occurrence_data = response.json()

    # Convert the results to a DataFrame
    df_occurrence = pd.DataFrame(occurrence_data['results'])

    # Display the first few rows of occurrence data
    print("Occurrence Data:")
    print(df_occurrence.head())
else:
    print(f"Error fetching data: {response.status_code}")


# In[3]:


import requests
import pandas as pd

# Base URL for GBIF country enumeration
url = 'https://api.gbif.org/v1/enumeration/country'

# Send a GET request to fetch the country list
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    country_data = response.json()

    # Convert the results to a DataFrame
    df_countries = pd.DataFrame(country_data)

    # Display the first few rows of country data
    print("Country Data:")
    print(df_countries.head())
else:
    print(f"Error fetching data: {response.status_code}")


# In[4]:


import requests
from IPython.display import Image

# Base URL for the GBIF Maps API
url = 'https://api.gbif.org/v2/map/occurrence/density/{z}/{x}/{y}@1x.png'

# Example parameters for generating the map (you can modify these)
params = {
    'style': 'classic.point',
    'taxonKey': 2435099,  # Puma concolor taxonKey
    'mode': 'GEO_CENTROID',
    'srs': 'EPSG:4326',
    'x': 0,
    'y': 0,
    'z': 0,
}

# Construct the full URL
map_url = url.format(z=params['z'], x=params['x'], y=params['y'])

# Display the map image
Image(url=map_url)


# In[5]:


import requests
import pandas as pd

# Base URL for GBIF literature search API
url = 'https://api.gbif.org/v1/literature/search'

# Define parameters for the search
params = {
    'q': 'GBIF',
    'limit': 10
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    literature_data = response.json()

    # Convert the results to a DataFrame
    df_literature = pd.DataFrame(literature_data['results'])

    # Display the first few rows of literature data
    print("Literature Data:")
    print(df_literature.head())
else:
    print(f"Error fetching data: {response.status_code}")


# In[26]:


#  Heatmap of Species Occurrences by Country

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming `df_occurrence` contains occurrence data with 'country' and 'occurrenceCount' fields
occurrence_counts = df_occurrence.groupby('country')['key'].count().reset_index()
occurrence_counts.columns = ['Country', 'Occurrence Count']

# Plot heatmap
plt.figure(figsize=(12,6))
sns.barplot(x='Country', y='Occurrence Count', data=occurrence_counts)
plt.xticks(rotation=90)
plt.title('Species Occurrences by Country')
plt.show()


# In[27]:


# Time Series of Occurrences Over Time
# Assuming df_occurrence has a 'year' column
occurrence_by_year = df_occurrence.groupby('year')['key'].count().reset_index()
occurrence_by_year.columns = ['Year', 'Occurrence Count']

# Plot time series
plt.figure(figsize=(10,6))
plt.plot(occurrence_by_year['Year'], occurrence_by_year['Occurrence Count'], marker='o')
plt.title('Species Occurrences Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')
plt.grid(True)
plt.show()


# In[28]:


# Bar Plot of Species by Family
import seaborn as sns

# Assuming df_species has a 'family' column
species_by_family = df_species['family'].value_counts().reset_index()
species_by_family.columns = ['Family', 'Species Count']

# Plot bar chart
plt.figure(figsize=(12,6))
sns.barplot(x='Family', y='Species Count', data=species_by_family.head(20))  # Limit to top 20 families
plt.xticks(rotation=90)
plt.title('Top 20 Families by Species Count')
plt.show()


# In[ ]:




