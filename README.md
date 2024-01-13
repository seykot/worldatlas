
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
   - 2021 data from the historical dataset was skewed.
   - Solution: data omitted for 2021, will check back to see if it is updated on Kaggle or request custom data from Gapminder.

4. **Correlation Analysis**
   – Correlation analysis with matplotlib didn't yield any insights or patterns in the data. 
   – Solution: Extensive exploratory analysis done using plotly graphs to unearth insights visually.

## Technical Challenges in Python Shiny App Development
Developing with Python's Shiny framework, recently out of Alpha testing, posed several challenges:

1. Limited community resources and documentation.
2. Pyleaflet maps had little documentation and some versions were discontinued in October 2023.
3. Navigating deprecated UI code and learning new UI coding practices in Python Shiny.
4. Managing environment setups in VSCode and Jupyter Notebook for different aspects of development.
5. Ensuring correct package versions in `requirements.txt` for smooth user experience.

## Benefits for Stakeholders as this App improves

- **Policy Makers and Strategists:**
  - Data-Driven Decisions: Access to a broad range of indicators for informed decision-making.
  - Strategic Planning: Identifying urgent intervention areas for targeted policies and programs.

- **Researchers and Analysts:**
  - Comprehensive Data Analysis: Central repository for in-depth analysis and research.
  - Trend Identification: Tracking long-term trends for forecasting and modeling.

- **Program and Project Managers:**
  - Program Design and Implementation: Designing effective programs based on regional data.
  - Impact Assessment: Assessing the impact of initiatives to adjust strategies.

- **Field Workers and Local Offices:**
  - Localized Information: Understanding specific regional challenges and resources.
  - Community Engagement: Using data to educate and engage local communities.

- **Educators and Advocacy Groups:**
  - Awareness and Education: Utilizing the app for educational purposes and awareness.
  - Advocacy and Campaigns: Creating data-backed advocacy campaigns.

- **Donors and Funders:**
  - Funding Allocation: Insight into the most impactful funding areas.
  - Accountability and Transparency: Tracking the effectiveness of funded projects.

  ## Ideal Users

- **Data-Driven Leaders:** Decision-makers who rely on data analysis and visualization.
- **Innovative Educators and Advocates:** Using technology and data for education and advocacy.
- **Global Health Specialists:** Professionals needing up-to-date health and environmental data.
- **Economic Analysts and Environmentalists:** Experts requiring data on economic and environmental trends.

## Future Works of this World Atlas App
Add to the app the following features:

1. Write a function to calculate a Socioeconomic Score that measures a society's overall quality of life, weighted in areas: economic, educational, environmental, demographic, and health. 
2. Create navigation tab for predictive analytics with future projections in areas of Population, CO2 Emissions, GDP, and other socioeconomic metric.
3. Create navigation tab using APIs with real time data on all types of metrics (i.e. current world flight data, freight shipping data, top economy's stock markets, songs topping the charts country-by-country on Spotify)
4. Allow users to export data or graphs for further analysis or reporting.
5. Add Gapminder datasets with annual data for deeper historical analysis. Swap out data on historical data page that is missing some years. 
6. Add Plotly Dash functionality. This opens the door for increased interactive features for users.
7. Add Correlation Analysis to homepage, allowing users to select variables to see if and how they are correlated from different countries (i.e. education and income levels).
8. Enable users to create custom queries or filter data based on their criteria.
9. Make the project Open Source for anybody who wants to contribute to creating a more useful.
10. Create more utility in the app for more stakeholders.
   – Develop a more comprehensive economic dashboard with key economic metrics for every country.
   – Helping users can understand the environmental and educational challenges and resources of different countries.
   – Allow users to better explore demographic structures and trends.
   – Further develop health indicator data into it's own public health part of the app. 
   – New navigation tab with data concerning Developing Nations.
   
Thank you for using the World Atlas App. Hopefully it enhances your understanding of the world and inspires curiosity about our global society.
