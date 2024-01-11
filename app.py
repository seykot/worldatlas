# Use AnalyticsEnv 3.12

# -----------------------------------------------------

# Imports

from pathlib import Path
from shiny import App, ui, reactive
import plotly.express as px
import pandas as pd
import numpy as np
from shinywidgets import render_widget

# Import layouts
from app_layout.layout import (
    info_button,
    get_homepage, get_map_layout, get_2023_layout, get_historical_layout
)
from graphs.historical_plots import (
    plotly_LifeExp, plotly_CO2, regionalGDPbar, regionalPopbar,
    scatterGeomap, choroplethCO2, choroplethLifeExp, lifestripbar
) 
from graphs.plots_2023 import (
    TopCurrencies, Top10GDP, Lowest10GDP, TopCPIChange, 
    EduBirthRate, EduLifeExp, EduLevels, EduHealth, HigherEd,
    EnvironmentPlot, TopAgricultureCountries, TopLowestAgricultureCountries, UrbanPopCO2, FoodSecurity,
    scatterGeoPop, UrbanPop, MostEmployed, LeastEmployed, MostCommonLanguages, 
    PhysiciansImpact, InfantViolin, BirthMortalityTrends, HealthScatter3D, BabyHealth, outofpocket,
    LifeExp_Sunburst, LifeExpHisto, LifeExpTreeMap, LifeExpViolin, Top20LifeExp, Top20LowestLifeExp, LifeExp80Club
)
from graphs.map_plots import (render_map)

# -----------------------------------------------------

# | context: setup / read datasets, drop null values

WorldAtlasGraphs = pd.read_csv("data/merged_world_data.csv")

HistoricalWorldData = pd.read_csv("data/final_df.csv")

ISO_codes = pd.read_csv("data/merged_geo.csv")
# ^ Country Alpha 3 codes needed for Plotly Scatter Geo + Plotly Choropleth map functionality

# ----------------------------------------------

# DATA CLEANING

# Columns to convert to float

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

# ----------------------------------------------

# CREATING APP Style with CSS

css_path = Path("www/my-styles.css")

# -----------------------------------------------------

# CREATING SIDEBAR

countries = list(WorldAtlasGraphs["Country"])

# Extract unique values from the column

dropdown_options_indicators = WorldAtlasGraphs.select_dtypes(
    [np.number]).columns.tolist()
dropdown_options_countries = WorldAtlasGraphs["Country"].unique().tolist()
dropdown_options_countries.insert(0, "Select")
dropdown_options_continents = HistoricalWorldData["Continent"].unique(
).tolist()
dropdown_options_continents.insert(0, "All")

# -----------------------------------------------------

# Defining World Atlas app complete navigation layout

homepage_layout = get_homepage(dropdown_options_countries, dropdown_options_indicators)

map_layout = get_map_layout(dropdown_options_countries)

current_year_graphs_layout = get_2023_layout()

historical_layout = get_historical_layout(dropdown_options_continents, dropdown_options_countries)

# -----------------------------------------------------

# Navigation
app_ui = ui.page_fluid(
    # Top header bar with the app name and navigation buttons
    ui.div(
        ui.div(
            {"style": "background-color: rgba(0, 128, 255, 0.1); \
             font-family: Times; \
             color: black; \
             text-align: center; \
             display: flex;"},

            # Header Title
            ui.div(ui.h1("World Atlas"),
                   {"style": "background-color: rgba(0, 128, 255, 0.1); \
                    text-align: center; \
                    width: 90%"}),

            # Info button
            ui.div(
                ui.input_action_button(
                    id="info_icon",
                    label=None,
                    icon=ui.tags.i(class_="glyphicon glyphicon-info-sign"),
                    class_="navbar-info",
                ),
                {"style": "background-color: rgba(0, 128, 255, 0.1); \
                 text-align: center; \
                 width: 10%"}
            ),

        ),
        ui.div(
            {"style": "background-color: rgba(0, 128, 255, 0.1); \
                 text-align: center;"},
            ui.navset_tab(
                ui.nav("Home", homepage_layout),
                ui.nav("Map", map_layout),  
                ui.nav("2023 Data", current_year_graphs_layout),
                ui.nav("Historical Data", historical_layout),
                id="navset",
            )
        )
    )
)
# https://shiny.posit.co/py/docs/ui-navigation.html

# -----------------------------------------------------

# Define the server logic required to draw a plot
def server(input, output, session):
    # Server logic will go here

    info_button()

    @reactive.Effect
    @reactive.event(input.info_icon)
    def _():
        info_button()

# Reactivity

    @reactive.Calc
    def scatter_selection():
        return (str(input.scatter_plot()))

    @reactive.Calc
    def current_year_graphs():
        return (str(input.current_year_graphs()))

    @output
    @render_widget
    def satellite_map():
        WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
            subset=[input.indicator_dropdown_homepage()])
        mapbox_access_token = 'pk.eyJ1Ijoic2V5a290IiwiYSI6ImNscXZwbnlsMDVvZzMyaXAxMjN4aXVoeTYifQ.WFDSoidWdr6WfozdyrGdYg'
        WorldAtlasGraphs_filtered.loc[WorldAtlasGraphs_filtered['Country']
                                      == input.country_dropdown_homepage_map(), "Color"] = "yellow"
        # Accessing each country location from "Select Country" dropdown menu
        country_row = WorldAtlasGraphs_filtered[WorldAtlasGraphs_filtered['Country']
                                                == input.country_dropdown_homepage_map()].values[0]
        # .values[0] accessing first row to convert into single dimension
        country_lon = country_row[-8]
        country_lat = country_row[-9]

        px.set_mapbox_access_token(mapbox_access_token)

        satellite_fig = px.scatter_mapbox(WorldAtlasGraphs_filtered, lat="Latitude", lon="Longitude", color="Region", zoom=3,
                                          hover_name="Country", height=600, mapbox_style='satellite-streets', hover_data=[input.indicator_dropdown_homepage()],
                                          title="Global Pulse: 2023 Country Data at a Glance"
                                          )
        satellite_fig.update_layout(
            title_font_size=24, title_font_family='Times')
        satellite_fig.update_layout(title_x=0.5)
        satellite_fig.update_mapboxes(center={'lat': country_lat,
                                              'lon': country_lon
                                              })

        return satellite_fig

    @output
    @render_widget
    def render_map_widget():
        return render_map(input)

# -----------------------------------------------------

    @output
    @render_widget
    def current_year_widget():
        chart_type = current_year_graphs()
        if chart_type == "Regional Life Expectancy Sunburst Chart":
            fig = LifeExp_Sunburst()
        elif chart_type == "Life Expectancy Histogram":
            fig = LifeExpHisto()
        elif chart_type == "Life Expectancy Tree Map":
            fig = LifeExpTreeMap()
        elif chart_type == "Regional Life Expectancy Violin Plot":
            fig = LifeExpViolin()
        elif chart_type == "Top 15 Countries with Lowest Unemployment Rates":
            fig = MostEmployed()
        elif chart_type == "Top 15 Countries with Highest Unemployment Rates":
            fig = LeastEmployed()
        elif chart_type == "Top 20 Countries by CPI Change %":
            fig = TopCPIChange()
        elif chart_type == "Higher Education's Impact on Birth Rate":
            fig = EduBirthRate()
        elif chart_type == "Higher Education's Impact on Life Expectancy":
            fig = EduLifeExp()
        elif chart_type == "Distribution of Agricultural Land and Forested Area":
            fig = EnvironmentPlot()
        elif chart_type == "Countries with Highest Agricultural Land %":
            fig = TopAgricultureCountries()
        elif chart_type == "Countries with Lowest Agricultural Land %":
            fig = TopLowestAgricultureCountries()
        elif chart_type == "Most Commonly Spoken Official Languages":
            fig = MostCommonLanguages()
        elif chart_type == "Physicians Impact on a Society's Well-being":
            fig = PhysiciansImpact()
        elif chart_type == "Top 20 Countries by Highest Life Expectancy":
            fig = Top20LifeExp()
        elif chart_type == "Top 20 Countries by Lowest Life Expectancy":
            fig = Top20LowestLifeExp()
        elif chart_type == "80 Club: The Only Countries With a Life Expectancy of 80+":
            fig = LifeExp80Club()
        elif chart_type == "Health Indicator 3D Scatterplot":
            fig = HealthScatter3D()
        elif chart_type == "Infant Mortality Rates":
            fig = InfantViolin()
        elif chart_type == "Birth and Mortality Trends Across Continents":
            fig = BirthMortalityTrends()
        elif chart_type == "Global Population in 2023":
            fig = scatterGeoPop()
        elif chart_type == "Top 10 Countries with Highest GDP":
            fig = Top10GDP()
        elif chart_type == "Top 10 Countries with Lowest GDP":
            fig = Lowest10GDP()
        elif chart_type == "Educational Enrollment Ratios of Top Economies":
            fig = EduLevels()
        elif chart_type == "Urban Population Impact on Climate Change":
            fig = UrbanPopCO2()
        elif chart_type == "Global Overview: Agricultural Land %, Life Expectancy, and Urban Populations":
            fig = FoodSecurity()
        elif chart_type == "Higher Education's Correlation to Number of Physicians":
            fig = EduHealth()
        elif chart_type == "Physicians Impact on Healthy Newborns":
            fig = BabyHealth()
        elif chart_type == "Most Commonly Used Currencies":
            fig = TopCurrencies()
        elif chart_type == "Countries with the Highest Out of Pocket Health Expenditure":
            fig = outofpocket()
        elif chart_type == "Countries with the Highest Urban Population":
            fig = UrbanPop()
        elif chart_type == "Top Countries in Higher Education Enrollment Rate":
            fig = HigherEd()
        return (fig)

    @output
    @render_widget
    def scatterplot_widget():
        chart_type = scatter_selection()
        if chart_type == "Health and Wealth":
            fig = plotly_LifeExp(input)
        elif chart_type == "GDP and CO2 Emissions":
            fig = plotly_CO2(input)
        elif chart_type == "Regional GDP Growth":
            fig = regionalGDPbar(input)
        elif chart_type == "Regional Population Growth":
            fig = regionalPopbar(input)
        elif chart_type == "CO2 Scatter Geo Map":
            fig = scatterGeomap(input)
        elif chart_type == "CO2 Choropleth Map":
            fig = choroplethCO2(input)
        elif chart_type == "Life Expectancy Choropleth":
            fig = choroplethLifeExp(input)
        elif chart_type == "Life Expectancy Strip Bar":
            fig = lifestripbar(input)
        return (fig)


# Create the Shiny app
app = App(app_ui, server)
