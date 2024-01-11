import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime
import numpy as np

WorldAtlasGraphs = pd.read_csv("data/merged_world_data.csv")

ISO_codes = pd.read_csv("data/merged_geo.csv")


# Data Cleaning // Columns to convert to float

column_to_float = ['Density(P/Km2)', 'Agricultural Land(%)', 'Land Area(Km2)',
                   'Birth Rate', 'Co2-Emissions', 'Forested Area (%)',
                   'CPI', 'CPI Change (%)', 'Fertility Rate', 'Gasoline Price', 'GDP',
                   'Gross primary education enrollment (%)', "Armed Forces size",
                   'Gross tertiary education enrollment (%)', 'Infant mortality',
                   'Life Expectancy', 'Maternal mortality ratio', 'Minimum wage',
                   'Out of pocket health expenditure', 'Physicians per thousand',
                   'Population', 'Population: Labor force participation (%)',
                   'Tax revenue (%)', 'Total tax rate', 'Unemployment rate', 'Urban_population']

for column in column_to_float:
    WorldAtlasGraphs[column] = WorldAtlasGraphs[column].astype(str)
    WorldAtlasGraphs[column] = WorldAtlasGraphs[column].str.replace(",", "")
    WorldAtlasGraphs[column] = WorldAtlasGraphs[column].str.replace("$", "")
    WorldAtlasGraphs[column] = WorldAtlasGraphs[column].str.replace(
        "%", "").astype(float)


def render_map(input):

    # Creating selected country color:

    # Adding new column making all columns fuchsia
    WorldAtlasGraphs["Color"] = "fuchsia"
    # Making Selected Country appears with yellow marker
    WorldAtlasGraphs.loc[WorldAtlasGraphs['Country'] ==
                            input.country_dropdown_map(), "Color"] = "yellow"

    # Accessing each country location from "Select Country" dropdown menu
    country_row = WorldAtlasGraphs[WorldAtlasGraphs['Country']
                                    == input.country_dropdown_map()].values[0]
    # .values[0] accessing first row to convert into single dimension
    country_lon = country_row[-8]
    country_lat = country_row[-9]
    # accessing near the last two columns of the df row: lon & lat

    WorldAtlasGraphs_filtered = WorldAtlasGraphs.copy()

    colnames_numerics_only = WorldAtlasGraphs_filtered.select_dtypes(
        include=np.number).columns.tolist()

    # Remove all numerical and categorical null values:

    for column in WorldAtlasGraphs_filtered.columns:
        if column in colnames_numerics_only:
            WorldAtlasGraphs_filtered[column] = WorldAtlasGraphs_filtered[column].fillna(
                0)
        else:

            WorldAtlasGraphs_filtered[column] = WorldAtlasGraphs_filtered[column].fillna(
                ' ')

    current_time = datetime.datetime.now()

    if current_time.hour < 17:

        mapbox_access_token = 'pk.eyJ1Ijoic2V5a290IiwiYSI6ImNscXZwbnlsMDVvZzMyaXAxMjN4aXVoeTYifQ.WFDSoidWdr6WfozdyrGdYg'
        px.set_mapbox_access_token(mapbox_access_token)
        white_mapfig = px.scatter_mapbox(WorldAtlasGraphs_filtered, lat="Latitude", lon="Longitude", color="Region", zoom=3, hover_name="Country",
                                            hover_data=[input.economic_dropdown(), input.education_dropdown(
                                            ), input.environmental_dropdown(), input.demographic_dropdown(), input.health_dropdown()],
                                            height=600, title="Mapping the World's Socioeconomic Indicators from 2023")
        white_mapfig.update_mapboxes(center={'lat': country_lat,
                                                'lon': country_lon
                                                })
        white_mapfig.update_layout(title_x=0.5)
        white_mapfig.update_layout(
            title_font_size=24, title_font_family='Times')
        return white_mapfig

    else:

        mapbox_access_token = 'pk.eyJ1Ijoic2V5a290IiwiYSI6ImNscXZwbnlsMDVvZzMyaXAxMjN4aXVoeTYifQ.WFDSoidWdr6WfozdyrGdYg'
        px.set_mapbox_access_token(mapbox_access_token)
        darkmap_fig = px.scatter_mapbox(WorldAtlasGraphs_filtered, lat="Latitude", lon="Longitude", color="Region", zoom=3, hover_name="Country",
                                        hover_data=[input.economic_dropdown(), input.education_dropdown(
                                        ), input.environmental_dropdown(), input.demographic_dropdown(), input.health_dropdown()],
                                        height=600, title="Mapping the World's Socioeconomic Indicators from 2023", mapbox_style='dark')
        darkmap_fig.update_mapboxes(center={'lat': country_lat,
                                            'lon': country_lon
                                            })
        darkmap_fig.update_layout(title_x=0.5)
        darkmap_fig.update_layout(
            title_font_size=24, title_font_family='Times')
        return darkmap_fig