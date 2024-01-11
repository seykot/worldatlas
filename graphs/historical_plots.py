import plotly.express as px
import pandas as pd

HistoricalWorldData = pd.read_csv("data/final_df.csv")

ISO_codes = pd.read_csv("data/merged_geo.csv")
# ^ Country Alpha 3 codes needed for Plotly Scatter Geo + Plotly Choropleth map functionality

# Defining Historical a Plotly functions

def plotly_LifeExp(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = HistoricalWorldData.loc[HistoricalWorldData['Year'] == curr_year]
    df = df.dropna(subset=['Life Expectancy', 'GDP', 'Annual Population'])
    # conditional statement for choosing continent + country
    if input.country_dropdown() == "Select":
        if input.continent_dropdown() == "All":
            df2 = df
        else:
            df2 = df[df["Continent"] == input.continent_dropdown()]
    else:
        df2 = df[df["Country"] == input.country_dropdown()]
    animated_ScatterGDP = px.scatter(df2, x="GDP", y="Life Expectancy",  size="Annual Population", color="Continent", hover_name="Country", template="simple_white",
                                     log_x=True, size_max=55, range_x=[1, 30000], range_y=[35, 90], height=450, width=1000,
                                     title="Measuring Nations' Health and Wealth",
                                     labels=dict(
                                         continent='Continent', pop='Populations',
                                         GDP="GDP in Billions (price-adjusted to $USD)")
                                     )
    animated_ScatterGDP.update_layout(title_x=0.5)

    animated_ScatterGDP.update_layout(font_family="Rockwell",
                                      legend=dict(orientation="h", title="", y=1.0, x=1, xanchor="right", yanchor="bottom"))

    animated_ScatterGDP.update_xaxes(tickprefix="$", range=[.1, 4.6], dtick=1)

    return animated_ScatterGDP


def plotly_CO2(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = HistoricalWorldData.loc[HistoricalWorldData['Year'] == curr_year]
    df = df.dropna(subset=['CO2', 'GDP', 'Annual Population'])
    # conditional statement for choosing continent + country
    if input.country_dropdown() == "Select":
        if input.continent_dropdown() == "All":
            df2 = df                             # df2 = filtering of drop down select boxes
        else:
            # filter by continent
            df2 = df[df["Continent"] == input.continent_dropdown()]
    else:
        # filter by country
        df2 = df[df["Country"] == input.country_dropdown()]
    animated_ScatterCO2 = px.scatter(df2, x="GDP", y="CO2",
                                     size="Annual Population", color="Continent", hover_name="Country", template="simple_white",
                                     log_x=True, size_max=55, range_x=[1, 22000], range_y=[-5, 30], height=450, width=1000,
                                     title="Measuring Correlation between GDP and CO2 emissions",
                                     labels=dict(
                                         continent='Continent', pop='Populations',
                                         GDP="GDP in Billions (US$, price-adjusted)", CO2="CO2 (metric tons per person)"))

    animated_ScatterCO2.update_layout(font_family="Rockwell",
                                      legend=dict(orientation="h", title="", y=1.0, x=1, xanchor="right", yanchor="bottom"))

    animated_ScatterCO2.update_xaxes(tickprefix="$", range=[.1, 4.6], dtick=1)

    animated_ScatterCO2.update_layout(title_x=0.5)

    return animated_ScatterCO2


def regionalGDPbar(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
        # conditional statement for choosing continent + country
    df = HistoricalWorldData.loc[HistoricalWorldData['Year'] == curr_year]
    df = df.dropna(subset=['GDP'])
    if input.country_dropdown() == "Select":
        if input.continent_dropdown() == "All":
            df2 = df
        else:
            df2 = df[df["Continent"] == input.continent_dropdown()]
    else:
        df2 = df[df["Country"] == input.country_dropdown()]
    df = HistoricalWorldData.loc[HistoricalWorldData['Year'] == curr_year]
    df = df.dropna(subset=['Region', 'GDP'])
    animated_barchart = px.bar(df, x="Region", y="GDP", color="Continent", template="simple_white",
                               hover_name="Country", animation_group="Country", range_y=[1, 33000],
                               title="Regional GDP Growth")

    animated_barchart.update_layout(title_x=0.5)

    return animated_barchart


def regionalPopbar(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = HistoricalWorldData.loc[HistoricalWorldData['Year'] == curr_year]
    df = df.dropna(subset=['Region', 'Annual Population'])
    Animated_PopBar = px.bar(df, x="Region", y="Annual Population", color="Continent",
                             range_y=[0, 4500000000], template="simple_white",
                             height=650, width=900,
                             title="Regional Population Growth")

    Animated_PopBar.update_layout(title_x=0.5)

    return Animated_PopBar


def scatterGeomap(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = ISO_codes.loc[ISO_codes['Year'] == curr_year]
    df = df.dropna(subset=['CO2'])
    ScatterGeo = px.scatter_geo(df, locations="Alpha-3 code", color="Continent", hover_name="Country",
                                size="CO2", projection="natural earth", opacity=.8,
                                height=650, width=900,
                                title="CO2 Emissions Measured in metric tons per person")

    ScatterGeo.update_layout(title_x=0.5)

    return ScatterGeo


def choroplethCO2(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = ISO_codes.loc[ISO_codes['Year'] == curr_year]
    df = df.dropna(subset=['CO2'])
    choropleth_CO2 = px.choropleth(df, locations="Alpha-3 code", color="CO2", hover_name="Country",
                                   title="CO2 Choropleth Map", height=650, width=900,)

    choropleth_CO2.update_layout(title_x=0.5)

    return choropleth_CO2


def choroplethLifeExp(input):
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = ISO_codes.loc[ISO_codes['Year'] == curr_year]
    df = df.dropna(subset=['Life Expectancy'])
    choropleth_life = px.choropleth(df, locations="Alpha-3 code", color="Life Expectancy", hover_name="Country",
                                    title="Life Expectancy Choropleth",  height=650, width=900,)

    choropleth_life.update_layout(title_x=0.5)

    return choropleth_life


def lifestripbar(input):

    
    curr_year = input.year_slider()
    if curr_year == 2011:
        curr_year = 2012
    if curr_year == 2016 or curr_year == 2017:
        curr_year = 2018
    df = ISO_codes.loc[ISO_codes['Year'] == curr_year]
    df = df.dropna(subset=['Life Expectancy'])
    LifeExpStrip = px.strip(df, x="Life Expectancy", color="Continent", hover_name="Country", height=450, width=900,
                            title="Life Expectancy Strip Bar", range_x=[40, 90], template="simple_white")

    LifeExpStrip.update_layout(title_x=0.5)

    return LifeExpStrip