
# Read Me: World Atlas App

## Introduction
Thanks for checking out the World Atlas App, inspired by Hans Rosling's enlightening Ted Talk, "The Best Stats You've Ever Seen." The goal is to present the world's information in a simplified, visually engaging manner. This application allows users to explore various socioeconomic indicators across countries, offering insights into how our world has evolved over time.

## About the App
The World Atlas App is a tool for discovery and learning. It invites users to engage with the world's socioeconomic data through an interactive map and various graphs. By selecting countries and indicators of interest, users can visualize how different regions and aspects of global society have changed over time. 

### Getting Started
- Select a country and an indicator on the main page.
- Explore more parameters and detailed analyses on the Maps and Graphs pages.

## Research Questions
The World Atlas app aims to answer these key questions:

1. How can geo-visualization simplify the understanding of global information?
2. What insights emerge from the 2023 data through interactive visualizations?
3. What patterns and trends in historical data have shaped our current world status?

## Datasets Overview
The app integrates multiple comprehensive datasets to provide both current and historical perspectives on global socioeconomic factors:

1. **Global Country Information Dataset 2023**
   - Content: Demographic statistics, economic indicators, environmental factors, healthcare metrics, and education statistics.
   - Scope: Current year data for a global overview.

2. **20 Year Global Country Historical Dataset**
   - Content: Data from the past 20 years on CO2 Emissions, GDP, Life Expectancy, Population for each country.
   - Purpose: To analyze trends and changes over time.

3. **Additional Data Sources**
   - GDP (1999-2022) from Kaggle.
   - World Bank Population Data.
   - Total Emissions Per Country.
   - Life Expectancy Data from Gapminder.
   - All datasets include APAC/AMER/EMEA Regions, Continents, and ISO Codes.

## Dataset Challenges and Solutions
In making the app, several challenges arose while integrating datasets:

1. **2023 Dataset Updates**
   - Issue: Incomplete data for the full scope of 2023.
   - Solution: Awaiting an update from the author on Kaggle for comprehensive coverage.

2. **20-Year Historical Dataset Gaps**
   - Issue: Missing data for certain years (2011, 2016-2017).
   - Solution: Use data from the previous year to prevent app glitches. Alternative options include imputing the mean, using 4-5 year increments, or substituing with Gapminder data.

3. **Data Quality Concerns**
   - 2021 data from the historical dataset was skewed and omitted.
   - Solution: data omitted for 2021, will check back to see if it is updated on Kaggle or request custom data from Gapminder.

## Technical Challenges in Python Shiny App Development
Developing with Python's Shiny framework, recently out of Alpha testing, posed several challenges:

1. Limited community resources and documentation.
2. Pyleaflet maps had little documentation and some versions were discontinued in October 2023.
3. Navigating deprecated UI code and learning new UI coding practices in Python Shiny.
4. Managing environment setups in VSCode and Jupyter Notebook for different aspects of development.
5. Ensuring correct package versions in `requirements.txt` for smooth user experience.

Thank you for using the World Atlas App. Hopefully it enhances your understanding of the world and inspires curiosity about our global society.
