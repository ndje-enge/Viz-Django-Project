from django.http import HttpResponse
from django.template import loader
import pandas as pd
import numpy as np
import folium
import json
import plotly.express as px


def index(request):

    
                     
    df2=pd.read_csv('ValeursFoncieres-2020-S2.csv', sep='|', decimal=",", low_memory=False)
    
    df2 = df2.drop(columns=["Identifiant de document", "Reference document", "1 Articles CGI", "2 Articles CGI", "3 Articles CGI", "4 Articles CGI", "5 Articles CGI"])
    df2 = df2.drop(columns=["Surface Carrez du 5eme lot","Prefixe de section","Surface Carrez du 4eme lot","B/T/Q","4eme lot","2eme lot","Surface Carrez du 2eme lot","3eme lot","5eme lot","Surface Carrez du 3eme lot","Identifiant local","Nature culture speciale"])
    df2 = df2.drop(columns=["No Volume"])
    mean_value2019 = df2["Valeur fonciere"].mean()
    std_value2019 = df2["Valeur fonciere"].std()

    outlier_limit2019 = mean_value2019 + 7 * std_value2019

    df2 = df2[df2["Valeur fonciere"] <= outlier_limit2019]
                     
    


    df2 = df2.drop(df2[df2['Code departement'].isin(['2A', '2B'])].index)
    df2['Code departement'] = df2['Code departement'].astype(str)

    auvergne_rhone_alpes = ['1', '3', '7', '15', '26', '38', '42', '43', '63', '69', '73', '74']
    bourgogne_franche_comte = ['21', '25', '39', '58', '70', '71', '89', '90']
    bretagne = ['22', '29', '35', '56']
    centre_val_de_loire = ['18', '28', '36', '37', '41', '45']
    corse = ['2A', '2B']
    grand_est = ['8', '10', '51', '52', '54', '55', '57', '67', '68', '88']
    hauts_de_france = ['02', '59', '60', '62', '80']
    ile_de_france = ['75', '77', '78', '91', '92', '93', '94', '95']
    normandie = ['14', '27', '50', '61', '76']
    nouvelle_aquitaine = ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87']
    occitanie = ['9', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82']
    pays_de_la_loire = ['44', '49', '53', '72', '85']
    provence_alpes_cote_dazur = ['04', '05', '06', '13', '83', '84']
# Overseas regions
    guadeloupe = ['971']
    martinique = ['972']
    guyane = ['973']
    la_reunion = ['974']
    mayotte = ['976']

# Use .loc with isin to assign regions to corresponding department codes.
    df2.loc[df2['Code departement'].isin(auvergne_rhone_alpes), 'Region'] = 'Auvergne-Rhône-Alpes'
    df2.loc[df2['Code departement'].isin(bourgogne_franche_comte), 'Region'] = 'Bourgogne-Franche-Comté'
    df2.loc[df2['Code departement'].isin(bretagne), 'Region'] = 'Bretagne'
    df2.loc[df2['Code departement'].isin(centre_val_de_loire), 'Region'] = 'Centre-Val de Loire'
    df2.loc[df2['Code departement'].isin(corse), 'Region'] = 'Corse'
    df2.loc[df2['Code departement'].isin(grand_est), 'Region'] = 'Grand Est'
    df2.loc[df2['Code departement'].isin(hauts_de_france), 'Region'] = 'Hauts-de-France'
    df2.loc[df2['Code departement'].isin(ile_de_france), 'Region'] = 'Île-de-France'
    df2.loc[df2['Code departement'].isin(normandie), 'Region'] = 'Normandie'
    df2.loc[df2['Code departement'].isin(nouvelle_aquitaine), 'Region'] = 'Nouvelle-Aquitaine'
    df2.loc[df2['Code departement'].isin(occitanie), 'Region'] = 'Occitanie'
    df2.loc[df2['Code departement'].isin(pays_de_la_loire), 'Region'] = 'Pays de la Loire'
    df2.loc[df2['Code departement'].isin(provence_alpes_cote_dazur), 'Region'] = 'Provence-Alpes-Côte d\'Azur'
    df2.loc[df2['Code departement'].isin(guadeloupe), 'Region'] = 'Guadeloupe'
    df2.loc[df2['Code departement'].isin(martinique), 'Region'] = 'Martinique'
    df2.loc[df2['Code departement'].isin(guyane), 'Region'] = 'Guyane'
    df2.loc[df2['Code departement'].isin(la_reunion), 'Region'] = 'La Réunion'
    df2.loc[df2['Code departement'].isin(mayotte), 'Region'] = 'Mayotte'
    
# Verify that regions have been correctly assigned
        
    df2['Date mutation'] = pd.to_datetime(df2['Date mutation'], dayfirst=True)

# Create a new 'Month' column
    df2['Mois'] = df2['Date mutation'].dt.month

                     
    template = loader.get_template ('template0.html')
    
    
    
    
    
    
    fig=px.scatter(df2,x="Valeur fonciere",y="Mois",color="Type local"
               ,hover_data=["Valeur fonciere"])
    plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {
    
    'plot_html':plot_html,}
    return HttpResponse (template.render (context, request))


def index1(request):

    
                     

                     
    template = loader.get_template ('template1.html')
    

    context = {
    
    }
    return HttpResponse (template.render (context, request))
def index4(request):

    
                     

                     
    template = loader.get_template ('template2.html')
    

    context = {
    
    }
    return HttpResponse (template.render (context, request))

def index2(request):

    
                     
    df2=pd.read_csv('ValeursFoncieres-2020-S2.csv', sep='|', decimal=",", low_memory=False)
    
    df2 = df2.drop(columns=["Identifiant de document", "Reference document", "1 Articles CGI", "2 Articles CGI", "3 Articles CGI", "4 Articles CGI", "5 Articles CGI"])
    df2 = df2.drop(columns=["Surface Carrez du 5eme lot","Prefixe de section","Surface Carrez du 4eme lot","B/T/Q","4eme lot","2eme lot","Surface Carrez du 2eme lot","3eme lot","5eme lot","Surface Carrez du 3eme lot","Identifiant local","Nature culture speciale"])
    df2 = df2.drop(columns=["No Volume"])
    mean_value2019 = df2["Valeur fonciere"].mean()
    std_value2019 = df2["Valeur fonciere"].std()

    outlier_limit2019 = mean_value2019 + 7 * std_value2019

    df2 = df2[df2["Valeur fonciere"] <= outlier_limit2019]
                     
    


    df2 = df2.drop(df2[df2['Code departement'].isin(['2A', '2B'])].index)
    df2['Code departement'] = df2['Code departement'].astype(str)

    auvergne_rhone_alpes = ['1', '3', '7', '15', '26', '38', '42', '43', '63', '69', '73', '74']
    bourgogne_franche_comte = ['21', '25', '39', '58', '70', '71', '89', '90']
    bretagne = ['22', '29', '35', '56']
    centre_val_de_loire = ['18', '28', '36', '37', '41', '45']
    corse = ['2A', '2B']
    grand_est = ['8', '10', '51', '52', '54', '55', '57', '67', '68', '88']
    hauts_de_france = ['02', '59', '60', '62', '80']
    ile_de_france = ['75', '77', '78', '91', '92', '93', '94', '95']
    normandie = ['14', '27', '50', '61', '76']
    nouvelle_aquitaine = ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87']
    occitanie = ['9', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82']
    pays_de_la_loire = ['44', '49', '53', '72', '85']
    provence_alpes_cote_dazur = ['04', '05', '06', '13', '83', '84']
# Overseas regions
    guadeloupe = ['971']
    martinique = ['972']
    guyane = ['973']
    la_reunion = ['974']
    mayotte = ['976']

# Use .loc with isin to assign regions to corresponding department codes.
    df2.loc[df2['Code departement'].isin(auvergne_rhone_alpes), 'Region'] = 'Auvergne-Rhône-Alpes'
    df2.loc[df2['Code departement'].isin(bourgogne_franche_comte), 'Region'] = 'Bourgogne-Franche-Comté'
    df2.loc[df2['Code departement'].isin(bretagne), 'Region'] = 'Bretagne'
    df2.loc[df2['Code departement'].isin(centre_val_de_loire), 'Region'] = 'Centre-Val de Loire'
    df2.loc[df2['Code departement'].isin(corse), 'Region'] = 'Corse'
    df2.loc[df2['Code departement'].isin(grand_est), 'Region'] = 'Grand Est'
    df2.loc[df2['Code departement'].isin(hauts_de_france), 'Region'] = 'Hauts-de-France'
    df2.loc[df2['Code departement'].isin(ile_de_france), 'Region'] = 'Île-de-France'
    df2.loc[df2['Code departement'].isin(normandie), 'Region'] = 'Normandie'
    df2.loc[df2['Code departement'].isin(nouvelle_aquitaine), 'Region'] = 'Nouvelle-Aquitaine'
    df2.loc[df2['Code departement'].isin(occitanie), 'Region'] = 'Occitanie'
    df2.loc[df2['Code departement'].isin(pays_de_la_loire), 'Region'] = 'Pays de la Loire'
    df2.loc[df2['Code departement'].isin(provence_alpes_cote_dazur), 'Region'] = 'Provence-Alpes-Côte d\'Azur'
    df2.loc[df2['Code departement'].isin(guadeloupe), 'Region'] = 'Guadeloupe'
    df2.loc[df2['Code departement'].isin(martinique), 'Region'] = 'Martinique'
    df2.loc[df2['Code departement'].isin(guyane), 'Region'] = 'Guyane'
    df2.loc[df2['Code departement'].isin(la_reunion), 'Region'] = 'La Réunion'
    df2.loc[df2['Code departement'].isin(mayotte), 'Region'] = 'Mayotte'
    
# Verify that regions have been correctly assigned
        
    df2['Date mutation'] = pd.to_datetime(df2['Date mutation'], dayfirst=True)

# Create a new 'Month' column
    df2['Mois'] = df2['Date mutation'].dt.month
    
    
#####2022#####    
    
    df=pd.read_csv('ValeursFoncieres-2022.csv', sep='|', decimal=",", low_memory=False)
    
    df = df.drop(columns=["Identifiant de document", "Reference document", "1 Articles CGI", "2 Articles CGI", "3 Articles CGI", "4 Articles CGI", "5 Articles CGI"])
    df = df.drop(columns=["Surface Carrez du 5eme lot","Prefixe de section","Surface Carrez du 4eme lot","B/T/Q","4eme lot","2eme lot","Surface Carrez du 2eme lot","3eme lot","5eme lot","Surface Carrez du 3eme lot","Identifiant local","Nature culture speciale"])
    df = df.drop(columns=["No Volume"])
    mean_value2019 = df["Valeur fonciere"].mean()
    std_value2019 = df["Valeur fonciere"].std()

    outlier_limit2019 = mean_value2019 + 7 * std_value2019

    df = df[df["Valeur fonciere"] <= outlier_limit2019]
                     
    


    df = df.drop(df[df['Code departement'].isin(['2A', '2B'])].index)
    df['Code departement'] = df['Code departement'].astype(str)

   

# Use .loc with isin to assign regions to corresponding department codes.
    df.loc[df['Code departement'].isin(auvergne_rhone_alpes), 'Region'] = 'Auvergne-Rhône-Alpes'
    df.loc[df['Code departement'].isin(bourgogne_franche_comte), 'Region'] = 'Bourgogne-Franche-Comté'
    df.loc[df['Code departement'].isin(bretagne), 'Region'] = 'Bretagne'
    df.loc[df['Code departement'].isin(centre_val_de_loire), 'Region'] = 'Centre-Val de Loire'
    df.loc[df['Code departement'].isin(corse), 'Region'] = 'Corse'
    df.loc[df['Code departement'].isin(grand_est), 'Region'] = 'Grand Est'
    df.loc[df['Code departement'].isin(hauts_de_france), 'Region'] = 'Hauts-de-France'
    df.loc[df['Code departement'].isin(ile_de_france), 'Region'] = 'Île-de-France'
    df.loc[df['Code departement'].isin(normandie), 'Region'] = 'Normandie'
    df.loc[df['Code departement'].isin(nouvelle_aquitaine), 'Region'] = 'Nouvelle-Aquitaine'
    df.loc[df['Code departement'].isin(occitanie), 'Region'] = 'Occitanie'
    df.loc[df['Code departement'].isin(pays_de_la_loire), 'Region'] = 'Pays de la Loire'
    df.loc[df['Code departement'].isin(provence_alpes_cote_dazur), 'Region'] = 'Provence-Alpes-Côte d\'Azur'
    df.loc[df['Code departement'].isin(guadeloupe), 'Region'] = 'Guadeloupe'
    df.loc[df['Code departement'].isin(martinique), 'Region'] = 'Martinique'
    df.loc[df['Code departement'].isin(guyane), 'Region'] = 'Guyane'
    df.loc[df['Code departement'].isin(la_reunion), 'Region'] = 'La Réunion'
    df.loc[df['Code departement'].isin(mayotte), 'Region'] = 'Mayotte'
    
# Verify that regions have been correctly assigned
        
    df['Date mutation'] = pd.to_datetime(df['Date mutation'], dayfirst=True)

# Create a new 'Month' column
    df['Mois'] = df['Date mutation'].dt.month

                     
    
    
    
    template = loader.get_template ('template1.html')
    
    
    
    
    if(request.GET['model']=="annee2020"):
       fig=px.scatter(df2,x="Valeur fonciere",y="Mois",color="Type local"
                  ,hover_data=["Valeur fonciere"])
       plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    if (request.GET ['model']=="annee2022"):
        fig=px.scatter(df,x="Valeur fonciere",y="Mois",color="Type local"
                ,hover_data=["Valeur fonciere"])
        plot_html=fig.to_html(full_html=False, default_height=500, default_width=700)
    

    

    context = {
    
    'plot_html':plot_html,}
    return HttpResponse (template.render (context, request))


def index3(request):
                       
    df2=pd.read_csv('ValeursFoncieres-2020-S2.csv', sep='|', decimal=",", low_memory=False)
    
    df2 = df2.drop(columns=["Identifiant de document", "Reference document", "1 Articles CGI", "2 Articles CGI", "3 Articles CGI", "4 Articles CGI", "5 Articles CGI"])
    df2 = df2.drop(columns=["Surface Carrez du 5eme lot","Prefixe de section","Surface Carrez du 4eme lot","B/T/Q","4eme lot","2eme lot","Surface Carrez du 2eme lot","3eme lot","5eme lot","Surface Carrez du 3eme lot","Identifiant local","Nature culture speciale"])
    df2 = df2.drop(columns=["No Volume"])
    mean_value2019 = df2["Valeur fonciere"].mean()
    std_value2019 = df2["Valeur fonciere"].std()

    outlier_limit2019 = mean_value2019 + 7 * std_value2019

    df2 = df2[df2["Valeur fonciere"] <= outlier_limit2019]
                     
    


    df2 = df2.drop(df2[df2['Code departement'].isin(['2A', '2B'])].index)
    df2['Code departement'] = df2['Code departement'].astype(str)

    auvergne_rhone_alpes = ['1', '3', '7', '15', '26', '38', '42', '43', '63', '69', '73', '74']
    bourgogne_franche_comte = ['21', '25', '39', '58', '70', '71', '89', '90']
    bretagne = ['22', '29', '35', '56']
    centre_val_de_loire = ['18', '28', '36', '37', '41', '45']
    corse = ['2A', '2B']
    grand_est = ['8', '10', '51', '52', '54', '55', '57', '67', '68', '88']
    hauts_de_france = ['02', '59', '60', '62', '80']
    ile_de_france = ['75', '77', '78', '91', '92', '93', '94', '95']
    normandie = ['14', '27', '50', '61', '76']
    nouvelle_aquitaine = ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87']
    occitanie = ['9', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82']
    pays_de_la_loire = ['44', '49', '53', '72', '85']
    provence_alpes_cote_dazur = ['04', '05', '06', '13', '83', '84']
# Overseas regions
    guadeloupe = ['971']
    martinique = ['972']
    guyane = ['973']
    la_reunion = ['974']
    mayotte = ['976']

# Use .loc with isin to assign regions to corresponding department codes.
    df2.loc[df2['Code departement'].isin(auvergne_rhone_alpes), 'Region'] = 'Auvergne-Rhône-Alpes'
    df2.loc[df2['Code departement'].isin(bourgogne_franche_comte), 'Region'] = 'Bourgogne-Franche-Comté'
    df2.loc[df2['Code departement'].isin(bretagne), 'Region'] = 'Bretagne'
    df2.loc[df2['Code departement'].isin(centre_val_de_loire), 'Region'] = 'Centre-Val de Loire'
    df2.loc[df2['Code departement'].isin(corse), 'Region'] = 'Corse'
    df2.loc[df2['Code departement'].isin(grand_est), 'Region'] = 'Grand Est'
    df2.loc[df2['Code departement'].isin(hauts_de_france), 'Region'] = 'Hauts-de-France'
    df2.loc[df2['Code departement'].isin(ile_de_france), 'Region'] = 'Île-de-France'
    df2.loc[df2['Code departement'].isin(normandie), 'Region'] = 'Normandie'
    df2.loc[df2['Code departement'].isin(nouvelle_aquitaine), 'Region'] = 'Nouvelle-Aquitaine'
    df2.loc[df2['Code departement'].isin(occitanie), 'Region'] = 'Occitanie'
    df2.loc[df2['Code departement'].isin(pays_de_la_loire), 'Region'] = 'Pays de la Loire'
    df2.loc[df2['Code departement'].isin(provence_alpes_cote_dazur), 'Region'] = 'Provence-Alpes-Côte d\'Azur'
    df2.loc[df2['Code departement'].isin(guadeloupe), 'Region'] = 'Guadeloupe'
    df2.loc[df2['Code departement'].isin(martinique), 'Region'] = 'Martinique'
    df2.loc[df2['Code departement'].isin(guyane), 'Region'] = 'Guyane'
    df2.loc[df2['Code departement'].isin(la_reunion), 'Region'] = 'La Réunion'
    df2.loc[df2['Code departement'].isin(mayotte), 'Region'] = 'Mayotte'
    
# Verify that regions have been correctly assigned
        
    df2['Date mutation'] = pd.to_datetime(df2['Date mutation'], dayfirst=True)

# Create a new 'Month' column
    df2['Mois'] = df2['Date mutation'].dt.month
    
    
#####2022#####    
    
    df=pd.read_csv('ValeursFoncieres-2022.csv', sep='|', decimal=",", low_memory=False)
    
    df = df.drop(columns=["Identifiant de document", "Reference document", "1 Articles CGI", "2 Articles CGI", "3 Articles CGI", "4 Articles CGI", "5 Articles CGI"])
    df = df.drop(columns=["Surface Carrez du 5eme lot","Prefixe de section","Surface Carrez du 4eme lot","B/T/Q","4eme lot","2eme lot","Surface Carrez du 2eme lot","3eme lot","5eme lot","Surface Carrez du 3eme lot","Identifiant local","Nature culture speciale"])
    df = df.drop(columns=["No Volume"])
    mean_value2019 = df["Valeur fonciere"].mean()
    std_value2019 = df["Valeur fonciere"].std()

    outlier_limit2019 = mean_value2019 + 7 * std_value2019

    df = df[df["Valeur fonciere"] <= outlier_limit2019]
                     
    


    df = df.drop(df[df['Code departement'].isin(['2A', '2B'])].index)
    df['Code departement'] = df['Code departement'].astype(str)

   

# Use .loc with isin to assign regions to corresponding department codes.
    df.loc[df['Code departement'].isin(auvergne_rhone_alpes), 'Region'] = 'Auvergne-Rhône-Alpes'
    df.loc[df['Code departement'].isin(bourgogne_franche_comte), 'Region'] = 'Bourgogne-Franche-Comté'
    df.loc[df['Code departement'].isin(bretagne), 'Region'] = 'Bretagne'
    df.loc[df['Code departement'].isin(centre_val_de_loire), 'Region'] = 'Centre-Val de Loire'
    df.loc[df['Code departement'].isin(corse), 'Region'] = 'Corse'
    df.loc[df['Code departement'].isin(grand_est), 'Region'] = 'Grand Est'
    df.loc[df['Code departement'].isin(hauts_de_france), 'Region'] = 'Hauts-de-France'
    df.loc[df['Code departement'].isin(ile_de_france), 'Region'] = 'Île-de-France'
    df.loc[df['Code departement'].isin(normandie), 'Region'] = 'Normandie'
    df.loc[df['Code departement'].isin(nouvelle_aquitaine), 'Region'] = 'Nouvelle-Aquitaine'
    df.loc[df['Code departement'].isin(occitanie), 'Region'] = 'Occitanie'
    df.loc[df['Code departement'].isin(pays_de_la_loire), 'Region'] = 'Pays de la Loire'
    df.loc[df['Code departement'].isin(provence_alpes_cote_dazur), 'Region'] = 'Provence-Alpes-Côte d\'Azur'
    df.loc[df['Code departement'].isin(guadeloupe), 'Region'] = 'Guadeloupe'
    df.loc[df['Code departement'].isin(martinique), 'Region'] = 'Martinique'
    df.loc[df['Code departement'].isin(guyane), 'Region'] = 'Guyane'
    df.loc[df['Code departement'].isin(la_reunion), 'Region'] = 'La Réunion'
    df.loc[df['Code departement'].isin(mayotte), 'Region'] = 'Mayotte'
    
# Verify that regions have been correctly assigned
        
    df['Date mutation'] = pd.to_datetime(df['Date mutation'], dayfirst=True)

# Create a new 'Month' column
    df['Mois'] = df['Date mutation'].dt.month

                     
    
    template = loader.get_template ('template2.html')
    if(request.GET['model']=="carte2020"):
        # Load the GeoJSON file for French regions
        with open('regions.geojson', 'r') as file:
            regions_geo = json.load(file)

        # Calculate average property value per region
        average_price_per_region = df2.groupby('Region')['Valeur fonciere'].mean().reset_index()
        bins = list(average_price_per_region['Valeur fonciere'].quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))
        # Create a map centered on France
        map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

        # Add a choropleth layer to the map
        folium.Choropleth(
            geo_data=regions_geo,
            data=average_price_per_region,
            columns=['Region', 'Valeur fonciere'],
            key_on='feature.properties.nom',
            fill_color='YlOrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Average property value by region 2020',
            bins=bins
        ).add_to(map)

        #folium.LayerControl().add_to(map)

        plot_html = map._repr_html_()

    if (request.GET ['model']=="carte2022"):
        with open('regions.geojson', 'r') as file:
            regions_geo = json.load(file)
        average_price_per_region = df.groupby('Region')['Valeur fonciere'].mean().reset_index()
        bins = list(average_price_per_region['Valeur fonciere'].quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))

        # Create a map centered on France
        map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

        # Add a choropleth layer to the map
        folium.Choropleth(
            geo_data=regions_geo,
            data=average_price_per_region,
            columns=['Region', 'Valeur fonciere'],
            key_on='feature.properties.nom',
            fill_color='YlOrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Average property value by region 2022',
            bins=bins
        ).add_to(map)

        plot_html = map._repr_html_()
        

    context = {
    
    'plot_html':plot_html,}
    
    return HttpResponse (template.render (context, request))