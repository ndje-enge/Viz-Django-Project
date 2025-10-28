# French Real Estate Analysis Project

Django web application for analyzing and visualizing real estate transaction data in France for the years 2020 and 2022.

## Description

This project is an interactive web application that allows you to visualize and analyze property values of real estate transactions in France. The application offers interactive graphical visualizations including scatter plots and choropleth maps showing average prices by region.

## ✨ Features

- **Property Value Visualization**: Scatter plots showing the relationship between property values, transaction months, and property types
- **Temporal Comparison**: Ability to compare data between 2020 and 2022
- **Geographic Maps**: Cartographic visualization of average prices by French region
- **Data Cleaning**: Automatic processing of outliers and enrichment with regional data
- **Interactive Interface**: Dynamic year selection and real-time visualizations

## Some Visualizations

### Real Estate Menu - Real Estate Analysis
![Menu Real Estate](ProjetP/Menu%20real%20estate.png)
*Interactive menu for selecting real estate analysis options*

### Real Estate Value Analysis
![Real Estate Value Analysis](ProjetP/Real%20Estate%20Value%20Analysis.png)
*Scatter plot visualization showing property values by month and property type*

### Regional Menu - Geographic Analysis
![Menu Regional](ProjetP/Menu%20regional.png)
*Interface for selecting regional map visualizations*

### Regional Property Value Map
![Regional Property Value Map](ProjetP/Regional%20Property%20Value%20Map.png)
*Choropleth map displaying average property values across French regions*

## Technologies Used

- **Backend**: Django 4.2.1
- **Data Analysis**: 
  - Pandas - data manipulation and analysis
  - NumPy - numerical calculations
- **Visualization**:
  - Plotly Express - interactive charts
  - Folium - interactive geographic maps

## 📊 Data Sources

The project uses official French property value data provided by the French government:
- `ValeursFoncieres-2020-S2.csv` - Second semester 2020 data
- `ValeursFoncieres-2022.csv` - Year 2022 data
- `regions.geojson` - GeoJSON file of French regions

## 📈 Data Processing

The application performs several cleaning and enrichment operations:

1. **Cleaning unnecessary columns**: Removal of irrelevant columns
2. **Outlier detection**: Using the 7 standard deviations method
3. **Geographic enrichment**: Automatic assignment of regions from department codes
4. **Temporal extraction**: Creation of a "Month" column from mutation dates

## Regions Covered

The application covers all French regions:
- Metropolitan France: 13 regions (Île-de-France, Auvergne-Rhône-Alpes, etc.)
- Overseas: Guadeloupe, Martinique, Guyana, La Réunion, Mayotte

### Main Settings

The `ProjetP/settings.py` file contains the Django configuration:
- `DEBUG = True`: Development mode (should be disabled in production)
- `ALLOWED_HOSTS = []`: Should be configured for production
- SQLite3 database by default

### URLs

Routes are defined in:
- `ProjetP/urls.py`: Main configuration (admin, polls)
- `polls/urls.py`: Application routes (index, page1, page2, etc.)

## Notes

School project completed in 2022 as an introduction at Django.
