# App.py txt

HOME_MSG = """Inspired by the viral Ted Talk by Hans Rosling, \
                    The Best Stats You've Ever Seen, this World Atlas app was created to help users \
                    learn about the world visually. By using this app, beliefs and stories about \
                    the nature of the world gradually begin to coalesce into a worldview. \
                    It is designed for users to select and learn about the countries and socioeconomic indicators \
                    they're most interested in from two stand points: \
                    an interactive world map and a variety of graphs that show how the world has changed over time. \
                    To get started, try selecting a country and an indicator below. \
                    For more parameters, check out the Maps and Graphs pages."""

DATASET_INFO = """This app was created to provide a high level look at every country's socioeconomic data from the year 2023 \
                    and to provide a recent historical look at various socioeconomic datapoints from every country. \
                    The first dataset is comprised of 2023 Global Country Information encompassing demographic statistics, \
                    economic indicators, environmental factors, healthcare metrics, and education statistics. \
                    With every country represented, this dataset offers a complete global perspective on various aspects of nations, \
                    enabling comprehensive analyses and cross-country comparisons. To add depth, a second dataset was created to incorporate \
                    20 years of historical insights including CO2 Emissions, GDP, Life Expectancy, and Population."""

INFO_HEADER = """The main ways to explore World Atlas data:"""
INFO_BUTTON_1 = """– View the world’s information country-by-country with geo-visualizations"""
INFO_BUTTON_2 = """– Research insights found in the 2023 data through interactive data visualizations"""
INFO_BUTTON_3 = """– Research insights, trends, and patterns in the historical data that led us to  2023"""

INSIGHTS_2023  =  {
    "Economic Indicators": {"Most Commonly Used Currencies": "Most Commonly Used Currencies",
                            "Top 10 Countries with Highest GDP": "Top 10 Countries with Highest GDP",
                            "Top 10 Countries with Lowest GDP": "Top 10 Countries with Lowest GDP",
                            "Top 15 Countries with Lowest Unemployment Rates": "Top 15 Countries with Lowest Unemployment Rates",
                            "Top 15 Countries with Highest Unemployment Rates": "Top 15 Countries with Highest Unemployment Rates",
                            "Top 20 Countries by CPI Change %": "Top 20 Countries by CPI Change %"},
    "Education Statistics": {"Educational Enrollment Ratios of Top Economies": "Educational Enrollment Ratios of Top Economies",
                            "Top Countries in Higher Education Enrollment Rate":"Top Countries in Higher Education Enrollment Rate",
                            "Higher Education's Correlation to Number of Physicians": "Higher Education's Correlation to Number of Physicians",
                            "Higher Education's Impact on Birth Rate": "Higher Education's Impact on Birth Rate",
                            "Higher Education's Impact on Life Expectancy": "Higher Education's Impact on Life Expectancy"},
    "Environmental Factors": {"Distribution of Agricultural Land and Forested Area": "Distribution of Agricultural Land and Forested Area",
                                "Urban Population Impact on Climate Change": "Urban Population Impact on Climate Change",
                                "Countries with Highest Agricultural Land %": "Countries with Highest Agricultural Land %",
                                "Countries with Lowest Agricultural Land %": "Countries with Lowest Agricultural Land %",
                                "Global Overview: Agricultural Land %, Life Expectancy, and Urban Populations": "Global Overview: Agricultural Land %, Life Expectancy, and Urban Populations"
                                },
    "Demographic Factors": {"Global Population in 2023": "Global Population in 2023",
                            "Countries with the Highest Urban Population":"Countries with the Highest Urban Population",
                            "Most Commonly Spoken Official Languages": "Most Commonly Spoken Official Languages",
                            },
    "Health Indicators": {"Countries with the Highest Out of Pocket Health Expenditure":"Countries with the Highest Out of Pocket Health Expenditure",
                            "Physicians Impact on a Society's Well-being": "Physicians Impact on a Society's Well-being",
                            "Physicians Impact on Healthy Newborns": "Physicians Impact on Healthy Newborns", "Infant Mortality Rates": "Infant Mortality Rates",
                            "Birth and Mortality Trends Across Continents": "Birth and Mortality Trends Across Continents",
                            "Health Indicator 3D Scatterplot": "Health Indicator 3D Scatterplot"
                            },
    "Life Expectancy": {"Life Expectancy Histogram": "Life Expectancy Histogram", "Life Expectancy Tree Map": "Life Expectancy Tree Map",
                        "Top 20 Countries by Highest Life Expectancy": "Top 20 Countries by Highest Life Expectancy",
                        "Top 20 Countries by Lowest Life Expectancy": "Top 20 Countries by Lowest Life Expectancy",
                        "Regional Life Expectancy Sunburst Chart": "Regional Life Expectancy Sunburst Chart", "Regional Life Expectancy Violin Plot": "Regional Life Expectancy Violin Plot",
                        "80 Club: The Only Countries With a Life Expectancy of 80+": "80 Club: The Only Countries With a Life Expectancy of 80+"
                        }
}

NOTE = """Note: these interactive data visualizations illustrate the 2023 Global Country Information dataset encompassing \
        demographic statistics, economic indicators, environmental factors, health indicators, and education statistics."""

