import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
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
    

# Defining 2023 Plotly functions


def LifeExp_Sunburst():

    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy', 'Population'])
    sunburst_chart = px.sunburst(WorldAtlasGraphs_filtered, color="Life Expectancy", values="Population",
                                 path=["Region", "Country"], height=700,
                                 title="Regional Life Expectancy Sunburst Chart")
    sunburst_chart.update_layout(title_x=0.5)

    return sunburst_chart


def LifeExpHisto():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy', 'Population'])
    histogram_chart = px.histogram(WorldAtlasGraphs_filtered, x="Life Expectancy", y="Population",
                                   color="Continent", hover_name="Country", marginal="rug", height=600,
                                   title="Life Expectancy Histogram", template="simple_white")
    histogram_chart.update_layout(title_x=0.5)

    return histogram_chart


def LifeExpTreeMap():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy', 'Population'])
    treemap_chart = px.treemap(WorldAtlasGraphs_filtered, color="Life Expectancy", values="Population",
                               path=["Region", "Country"], height=600,
                               title="Life Expectancy Tree Map", template="simple_white")
    treemap_chart.update_layout(title_x=0.5)

    return treemap_chart


def MostEmployed():

    # Sorting the data by 'Unemployment rate' and taking the top 15 for lowest unemployment rates
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Unemployment rate'])
    top_15_lowest_unemployment = WorldAtlasGraphs_filtered.sort_values(
        by='Unemployment rate', ascending=True).head(15)
    # Creating a bar chart for the top 15 countries with the lowest unemployment rates
    lowest_unemployment_bar_chart = px.bar(top_15_lowest_unemployment, x='Country', y='Unemployment rate',
                                           color='Country', template="simple_white", height=600,
                                           title='Top 15 Countries with Lowest Unemployment Rates')
    lowest_unemployment_bar_chart.update_yaxes(title="Unemployment Rate %")
    lowest_unemployment_bar_chart.update_layout(title_x=0.5)
    return lowest_unemployment_bar_chart


def LeastEmployed():

    # Sorting the data by 'Unemployment rate' and taking the top 15 for highest unemployment rates
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Unemployment rate'])
    top_15_highest_unemployment = WorldAtlasGraphs_filtered.sort_values(
        by='Unemployment rate', ascending=True).tail(15)
    # Creating a bar chart for the top 15 countries with the lowest unemployment rates
    highest_unemployment_bar_chart = px.bar(top_15_highest_unemployment, x='Country', y='Unemployment rate',
                                            color='Country', template="simple_white", height=600,
                                            title='Top 15 Countries with Highest Unemployment Rates')
    highest_unemployment_bar_chart.update_yaxes(title="Unemployment Rate %")
    highest_unemployment_bar_chart.update_layout(title_x=0.5)
    return highest_unemployment_bar_chart


def LifeExpViolin():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy'])
    lifeExp_violin_plot = px.violin(WorldAtlasGraphs_filtered, y='Life Expectancy', x='Region', range_y=[40, 95],
                                    box=True,  # Displays box plots within the violin plot
                                    points="all",  # Show all points of data
                                    hover_name="Country",
                                    color="Region", template="simple_white", height=700,
                                    title='Regional Life Expectancy Violin Plot')
    lifeExp_violin_plot.update_layout(title_x=0.5)

    return lifeExp_violin_plot


def InfantViolin():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Birth Rate', 'Infant mortality'])
    infant_violin_plot = px.scatter(WorldAtlasGraphs_filtered, x="Birth Rate", y="Infant mortality", color="Region",
                                    marginal_y="violin", trendline="ols", hover_name="Country", height=600,
                                    title="Infant Mortality", template="simple_white")
    infant_violin_plot.update_layout(title_x=0.5)

    return infant_violin_plot


def PhysiciansImpact():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Physicians per thousand', 'Life Expectancy'])
    Physicians_Impact = px.scatter(WorldAtlasGraphs_filtered, x="Physicians per thousand", y="Life Expectancy", color="Region",
                                   marginal_y="violin", trendline="ols", height=600, range_y=[50, 90],
                                   title="Physicians Impact on a Society's Wellbeing", template="simple_white")
    Physicians_Impact.update_layout(title_x=0.5)

    return Physicians_Impact


def EduBirthRate():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Birth Rate', 'Gross tertiary education enrollment (%)'])
    HigherEducationBirth = px.scatter(WorldAtlasGraphs_filtered, x="Gross tertiary education enrollment (%)", y="Birth Rate", color="Region",
                                      marginal_y="violin", trendline="ols", height=600,
                                      title="Higher Education's Impact on Birth Rate", template="simple_white")
    HigherEducationBirth.update_layout(title_x=0.5)

    return HigherEducationBirth


def EduLifeExp():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Gross tertiary education enrollment (%)', 'Life Expectancy'])
    HigherEducationLifeExp = px.scatter(WorldAtlasGraphs_filtered, x="Gross tertiary education enrollment (%)", y="Life Expectancy", color="Region",
                                        marginal_y="violin", trendline="ols", height=600,
                                        title="Higher Education's Impact on Life Expectancy", template="simple_white")
    HigherEducationLifeExp.update_layout(title_x=0.5)

    return HigherEducationLifeExp


def BirthMortalityTrends():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=["Birth Rate", "Fertility Rate",
                                                        "Infant mortality", "Maternal mortality ratio"])
    BirthTrends = px.scatter_matrix(WorldAtlasGraphs_filtered, dimensions=["Birth Rate", "Fertility Rate",
                                                                           "Infant mortality", "Maternal mortality ratio"],
                                    hover_name="Country",
                                    color="Continent", height=800,
                                    title="Birth and Mortality Trends Across Continents")
    BirthTrends.update_layout(title_x=0.5)

    return BirthTrends


def EnvironmentPlot():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Agricultural Land(%)', 'Forested Area (%)'])
    Environment_Chart = px.violin(WorldAtlasGraphs_filtered, y=['Agricultural Land(%)', 'Forested Area (%)'],
                                  box=True,  # Displays box plot inside the violin
                                  points="all",  # Shows all points
                                  height=700, hover_name="Country", color="Region", template="simple_white",
                                  title="Distribution of Agricultural Land and Forested Area")
    Environment_Chart.update_layout(title_x=0.5)

    return Environment_Chart


def HealthScatter3D():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Birth Rate', 'Infant mortality', 'Maternal mortality ratio'])
    HealthScatterFig = px.scatter_3d(WorldAtlasGraphs_filtered, x='Birth Rate', y='Infant mortality', z='Maternal mortality ratio',
                                     color='Region', height=600, hover_name="Country",
                                     title="Health Indicator 3D Scatterplot")
    HealthScatterFig.update_layout(title_x=0.5)

    return HealthScatterFig


def TopAgricultureCountries():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Agricultural Land(%)'])
    # Sorting by 'Agricultural Land percentage and selecting the top 20 countries
    top_agricultural_land = WorldAtlasGraphs_filtered.sort_values(
        by='Agricultural Land(%)', ascending=False).head(20)
    # Making an agricultural land bar chart
    agricultural_land_chart = px.bar(top_agricultural_land, x='Country', y='Agricultural Land(%)',
                                     title='Countries with Highest Agricultural Land %', height=600,
                                     color="Country", template="simple_white")
    agricultural_land_chart.update_layout(title_x=0.5)

    return agricultural_land_chart


def TopLowestAgricultureCountries():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Agricultural Land(%)'])
    # Sorting by 'Agricultural Land percentage and selecting the top 20 countries
    top_agricultural_land = WorldAtlasGraphs_filtered.sort_values(
        by='Agricultural Land(%)', ascending=False).tail(20)
    # Making an agricultural land bar chart
    lowest_agricultural_land_chart = px.bar(top_agricultural_land, x='Country', y='Agricultural Land(%)',
                                            title='Countries with Lowest Agricultural Land %', height=600,
                                            color="Country", template="simple_white")
    lowest_agricultural_land_chart.update_layout(title_x=0.5)

    return lowest_agricultural_land_chart


def MostCommonLanguages():

    # Specifying top 10 count
    top_languages_count = 10
    # Counting the occurrences of each official language
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Official language'])
    language_counts = WorldAtlasGraphs_filtered['Official language'].value_counts(
    ).nlargest(top_languages_count)
    # Creating a bar chart with Plotly
    top10_language_chart = px.bar(language_counts, x=language_counts.values, y=language_counts.index,
                                  orientation='h', title='Most Commonly Spoken Official Languages',
                                  labels={'x': 'Number of Countries', 'index': 'Official Language'}, height=600,
                                  color=language_counts.index, template="simple_white")
    top10_language_chart.update_layout(title_x=0.5)

    return top10_language_chart


def TopCPIChange():

    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['CPI Change (%)'])
    # Sorting by 'CPI Change (%)' and selecting the top 15
    top_20_cpi_change = WorldAtlasGraphs_filtered.sort_values(
        by='CPI Change (%)', ascending=False).head(20)

    # Creating a vertical bar chart with Plotly, using 'Currency Code' as the color legend
    country_cpi_chart_vertical = px.bar(top_20_cpi_change, x='Country', y='CPI Change (%)',
                                        title='Top 20 Countries by CPI Change %', template="simple_white",
                                        labels={
                                            'CPI Change (%)': 'CPI Change (%)', 'Country': 'Country'},
                                        height=600, color='Currency-Code')  # Using 'Currency Code' for color
    country_cpi_chart_vertical.update_layout(title_x=0.5)

    return country_cpi_chart_vertical


def Top20LifeExp():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy'])
    # Sorting the df by 'Life Expectancy' in descending order
    df_sorted = WorldAtlasGraphs_filtered.sort_values(
        by='Life Expectancy', ascending=False)
    # Selecting the top 20 countries
    top_countries_life_expectancy = df_sorted.head(20)
    # Making a vertical bar chart
    Top20LifeExp_fig = px.bar(top_countries_life_expectancy, x='Country', y='Life Expectancy',
                              color='Life Expectancy',
                              title='Top 20 Countries by Highest Life Expectancy',
                              labels={'Life Expectancy': 'Life Expectancy',
                                      'Country': 'Country'},
                              height=600)
    Top20LifeExp_fig.update_layout(yaxis_range=[75, 86])
    Top20LifeExp_fig.update_layout(title_x=0.5)

    return Top20LifeExp_fig


def Top20LowestLifeExp():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy'])
    # Sorting the df by 'Life Expectancy' in descending order
    df_sorted = WorldAtlasGraphs_filtered.sort_values(
        by='Life Expectancy', ascending=False)
    # Selecting the top 20 countries
    top_countries_life_expectancy = df_sorted.tail(20)
    # Making a vertical bar chart
    Top20LowestLifeExp_fig = px.bar(top_countries_life_expectancy, x='Country', y='Life Expectancy',
                                    color='Life Expectancy',
                                    title='Top 20 Countries by Lowest Life Expectancy',
                                    labels={
                                        'Life Expectancy': 'Life Expectancy', 'Country': 'Country'},
                                    height=600)
    Top20LowestLifeExp_fig.update_layout(yaxis_range=[50, 65])
    Top20LowestLifeExp_fig.update_layout(title_x=0.5)

    return Top20LowestLifeExp_fig


def LifeExp80Club():

    # Filter out rows where 'Life Expectancy' or 'Continent' is NA
    filtered_df = WorldAtlasGraphs.dropna(
        subset=['Life Expectancy', 'Continent'])
    # Filter to include only countries with life expectancy above 80
    filtered_df = filtered_df[filtered_df['Life Expectancy'] > 80]
    # Creating a scatter plot
    EightyClub_fig = px.scatter(filtered_df, x='Country', y='Life Expectancy', color='Continent', height=500,
                                hover_data=['Country'], title='80 Club: The Only Countries With a Life Expectancy of 80+')
    # Rotate x-axis labels for better readability
    EightyClub_fig.update_xaxes(tickangle=45)
    EightyClub_fig.update_layout(title_x=0.5)

    return EightyClub_fig


def scatterGeoPop():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=['Population'])
    WorldAtlasGraphs_filtered = WorldAtlasGraphs_filtered.fillna("")
    ScatterGeo_Pop = px.scatter_geo(WorldAtlasGraphs_filtered, locations="Alpha-3 code", color="Continent",
                                    projection="orthographic", opacity=.8, # size="Population", 
                                    hover_name="Country", hover_data=["Official language", "Population", "Urban_population", "Population: Labor force participation (%)"],
                                    height=650, width=900,
                                    title="Global Population in 2023")
    ScatterGeo_Pop.update_layout(title_x=0.5)

    return ScatterGeo_Pop


def Top10GDP():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=['GDP'])
    # Sorting by GDP
    top_ten_GDP = WorldAtlasGraphs_filtered.sort_values(
        by='GDP', ascending=False).head(10)
    # Making an GDP bar chart
    highestGDPchart = px.bar(top_ten_GDP, x='Country', y='GDP',
                             title='Top 10 Countries with Highest GDP', height=600,
                             color="Country", template="simple_white")
    highestGDPchart.update_layout(title_x=0.5)

    return highestGDPchart


def Lowest10GDP():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=['GDP'])
    # Sorting by GDP
    lowest_ten_GDP = WorldAtlasGraphs_filtered.sort_values(
        by='GDP', ascending=False).tail(10)
    # Making an GDP bar chart
    lowestGDPchart = px.bar(lowest_ten_GDP, x='Country', y='GDP',
                            title='Top 10 Countries with Lowest GDP', height=600,
                            color="Country", template="simple_white")
    lowestGDPchart.update_layout(title_x=0.5)

    return lowestGDPchart


def EduLevels():

    EduFig = go.Figure()  # creating empty figure, adding graphs below
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)'])
    # Graphing Educational Enrollment Ratios of Top Economies
    GDPInfo = WorldAtlasGraphs_filtered.sort_values(
        by='GDP', ascending=False).head(10)  # getting top 10 GDP countries
    EduFig.add_trace(go.Bar(
        x=GDPInfo['Country'],
        y=GDPInfo["Gross primary education enrollment (%)"],
        name='Primary Education',
        marker_color='rgb(26, 118, 255)'
        # marker_color='indianred'
    ))
    EduFig.add_trace(go.Bar(
        x=GDPInfo["Country"],
        y=GDPInfo["Gross tertiary education enrollment (%)"],
        name='Higher Education',
        marker_color='rgb(55, 83, 109)'
        # marker_color='lightsalmon'
    ))
    # Modify tickangle of the xaxis, resulting in rotated labels:
    EduFig.update_layout(barmode='group', xaxis_tickangle=-45)
    EduFig.update_layout(template="simple_white", height=500)
    EduFig.update_layout(
        title="Educational Enrollment Ratios of Top Economies")
    EduFig.update_layout(xaxis={"title": "Country"}, yaxis={"title": "Enrollment Ratio %"})
    EduFig.update_layout(title_x=0.5)
    return EduFig


def UrbanPopCO2():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Urban_population', 'Co2-Emissions'])
    Urban_Pop_CO2 = px.scatter(WorldAtlasGraphs_filtered, x="Urban_population", y="Co2-Emissions", color="Region",
                               marginal_y="violin", trendline="ols", height=600, hover_name="Country", range_y=[-45000, 1500000], range_x=[100000, 120000000], log_x=True,
                               title="Urban Population Impact on Climate Change", template="simple_white")
    Urban_Pop_CO2.update_layout(xaxis={"title": "Urban Population"})
    Urban_Pop_CO2.update_layout(title_x=0.5)

    return Urban_Pop_CO2


def FoodSecurity():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Urban_population', 'Life Expectancy', 'Agricultural Land(%)'])
    foodsecurityfig = px.scatter(WorldAtlasGraphs_filtered, x="Agricultural Land(%)", y="Life Expectancy",
                                 color="Continent", hover_name="Country", template="simple_white", size="Urban_population", size_max=35,
                                 # log_x=True,
                                 range_x=[1, 85], range_y=[52, 90], height=500, width=900,
                                 title="Global Overview: Agricultural Land %, Life Expectancy, and Urban Populations")
    foodsecurityfig.update_layout(font_family="Rockwell",
                                  legend=dict(orientation="h", title="", y=1.0, x=1, xanchor="right", yanchor="bottom"))
    # foodsecurityfig.update_xaxes(tickprefix="$", range=[.1,4.6], dtick=1)
    foodsecurityfig.update_layout(title_x=0.5)

    return foodsecurityfig


def EduHealth():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Gross tertiary education enrollment (%)', 'Physicians per thousand'])
    HigherEducationHealth = px.scatter(WorldAtlasGraphs_filtered, x="Gross tertiary education enrollment (%)", y="Physicians per thousand", color="Region",
                                       marginal_y="violin", trendline="ols", height=600, hover_name="Country",
                                       title="Higher Education's Correlation to Number of Physicians", template="simple_white")
    HigherEducationHealth.update_layout(title_x=0.5)

    return HigherEducationHealth


def BabyHealth():
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Infant mortality', 'Physicians per thousand'])
    HigherEducationHealth = px.scatter(WorldAtlasGraphs_filtered, x="Infant mortality", y="Physicians per thousand", color="Continent",
                                       height=600, hover_name="Country", range_y=[-.5, 9], trendline="ols",
                                       title="Physicians Impact on Healthy Newborns", template="simple_white")
    HigherEducationHealth.update_layout(title_x=0.5)

    return HigherEducationHealth


def TopCurrencies():

    # Specifying top 10 count
    top_currency_count = 10
    # Counting the occurrences of each official language
    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(
        subset=['Currency-Code'])
    currency_count = WorldAtlasGraphs_filtered['Currency-Code'].value_counts(
    ).nlargest(top_currency_count)
    # Creating a bar chart with Plotly
    top10_currencies = px.bar(currency_count, x=currency_count.values, y=currency_count.index,
                              orientation='h', title='Most Commonly Used Currencies', height=600,
                              color=currency_count.index, template="simple_white")
    top10_currencies.update_layout(title_x=0.5)

    return top10_currencies

def outofpocket():

    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=['Out of pocket health expenditure'])
    # Sorting by GDP
    top_ten_healthexpense = WorldAtlasGraphs_filtered.sort_values(
        by='Out of pocket health expenditure', ascending=False).head(20)
    # Making an GDP bar chart
    highesthealthexpense = px.bar(top_ten_healthexpense, x='Country', y='Out of pocket health expenditure',
                             title='Countries with the Highest Out of Pocket Health Expenditure %', height=600,
                             color="Country", template="simple_white")
    highesthealthexpense.update_layout(yaxis={"title": "% Paid out of pocket"})
    highesthealthexpense.update_layout(title_x=0.5)

    return highesthealthexpense

def UrbanPop():

    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=['Urban_population'])
    # Sorting by GDP
    top_ten_urban = WorldAtlasGraphs_filtered.sort_values(
        by='Urban_population', ascending=False).head(20)
    # Making an GDP bar chart
    highesturbanpop = px.bar(top_ten_urban, x='Country', y='Urban_population',
                             title='Countries with the Highest Urban Population', height=600,
                             color="Country", template="simple_white")
    highesturbanpop.update_layout(yaxis={"title": "Urban Population"})
    highesturbanpop.update_layout(title_x=0.5)

    return highesturbanpop

def HigherEd():

    WorldAtlasGraphs_filtered = WorldAtlasGraphs.dropna(subset=['Gross tertiary education enrollment (%)'])
    top_higher_ed = WorldAtlasGraphs_filtered.sort_values(
        by='Gross tertiary education enrollment (%)', ascending=False).head(20)
    top_tertiary_ed = px.bar(top_higher_ed, x='Country', y='Gross tertiary education enrollment (%)',
                             title='Top Countries in Higher Education Enrollment Rate', height=600,
                             color="Country", template="simple_white")
    top_tertiary_ed.update_layout(xaxis={"title": "Country"}, yaxis={"title": "Higher Ed Enrollment %"})
    top_tertiary_ed.update_layout(title_x=0.5)

    return top_tertiary_ed