# World Atlas app navigation tab layouts

from shiny import ui
from shiny.ui import modal_show, modal, modal_button
from htmltools import tags
from shinywidgets import output_widget
from txt_files.text import (
    HOME_MSG, DATASET_INFO, INFO_HEADER, 
    INFO_BUTTON_1, INFO_BUTTON_2, INFO_BUTTON_3, 
    INSIGHTS_2023, NOTE
)

# -----------------------------------------------------

def info_button():
    modal_show(
        modal(
            tags.strong(tags.h3("World Atlas App")),
            tags.p(
                "Exploring the World's Socioeconomic Data"
            ),
            tags.hr(),
            tags.strong(tags.h4("How to Gain Insights from this App")),
            tags.p(
                INFO_HEADER, ui.br(),
                INFO_BUTTON_1, ui.br(),
                INFO_BUTTON_2, ui.br(),
                INFO_BUTTON_3,
                style="""
            text-align: justify;
            word-break:break-word;
            hyphens: auto;
            """,
            ),
            size="l",
            easy_close=True,
            footer=modal_button("Close"),
        )
    )

# -----------------------------------------------------

# Homepage

def get_homepage(dropdown_options_countries, dropdown_options_indicators):

    return ui.layout_sidebar(
        ui.panel_sidebar
        (
            # Sidebar CSS
            {"style": "background-color: rgba(0, 128, 255, 0.1); \
                font-family: Times; \
                color: black; \
                height: inherit;"
            },
            ui.div(
                ui.h1("Welcome to the World Atlas App!"),
                ui.div(
                    ui.h3("About this App"),
                    ui.p(HOME_MSG,
                        style="""
                        text-align: justify;
                        word-break:break-word;
                        hyphens: auto;
                        """,)
                )
            ),
            ui.div(
                ui.input_select("country_dropdown_homepage_map", "Select a Country",
                                choices=dropdown_options_countries, selected="United States"),
                ui.input_select("indicator_dropdown_homepage", "Select a Socioeconomic Indicator",
                                choices=dropdown_options_indicators, selected=None),
                {"style": "margin: 10px; "
                },
            ),

            ui.div(
                ui.h3(" \
                        Dataset Information"),
                ui.p(DATASET_INFO,
                    style="""
                        text-align: justify;
                        word-break:break-word;
                        hyphens: auto;
                        """,
                )
            )
        ),
        # Main content area
        ui.panel_main(

            output_widget("satellite_map", width="auto", height="auto"),
            # Main panel color
            {"style": "background-color: rgba(153, 204, 153, 0.1);"},
        )
    )

# MAP Page

def get_map_layout(dropdown_options_countries):

    return ui.layout_sidebar(
    ui.panel_sidebar(
        # Sidebar CSS
        {"style": "background-color: rgba(0, 128, 255, 0.1); \
            font-family: Times; \
            color: black; \
            height: inherit;"
         },
        ui.input_select("country_dropdown_map", "Select Country",
                        choices=dropdown_options_countries, selected="United States"),
        ui.input_select("economic_dropdown", "Economic Indicators", ["GDP", "CPI", "CPI Change (%)",
                                                                     "Tax revenue (%)", "Total tax rate", "Minimum wage", "Unemployment rate"], selected=None),
        ui.input_select("education_dropdown", "Education Statistics", [
                        "Gross primary education enrollment (%)", "Gross tertiary education enrollment (%)"], selected=None),
        ui.input_select("environmental_dropdown", "Environmental Factors", [
                        "Agricultural Land(%)", "Land Area(Km2)", "Co2-Emissions", "Forested Area (%)"], selected=None),
        ui.input_select("demographic_dropdown", "Demographic Factors", [
                        "Population", "Urban_population", "Population: Labor force participation (%)"], selected=None),
        ui.input_select("health_dropdown", "Health Indicators", ["Birth Rate", "Fertility Rate", "Infant mortality", "Life Expectancy",
                                                                 "Maternal mortality ratio", "Out of pocket health expenditure", "Physicians per thousand"], selected=None),
        # ui.input_select("map_dropdown", "Select a Map")
    ),

    # Main content area
    ui.panel_main(

        output_widget("render_map_widget", width="auto", height="auto"),
        # Main panel color
        {"style": "background-color: rgba(153, 204, 153, 0.1);"},
    )
)

# 2023 Data 

def get_2023_layout():
    return ui.layout_sidebar(
        ui.panel_sidebar(
            {"style": "background-color: rgba(0, 128, 255, 0.1); \
            height:inherit;"},
            ui.div(
                # Sidebar CSS
                {"style":
                "font-family: Times; \
                color: black; \
                height: inherit; \
                margin-bottom: 150px;"},
                ui.input_selectize("current_year_graphs",
                                "Choose An Insight",
                                INSIGHTS_2023,
                                multiple=False,
                                )
            ),
            ui.div(
                {"style": "font-family: Times; \
                    color: black; \
                    height: inherit;"
                },
                ui.em(NOTE)
            )
        ),
        # Main content area
        ui.panel_main(

            output_widget("current_year_widget", width="auto", height="auto"),
            # Main panel color
            {"style": "background-color: rgba(153, 204, 153, 0.1);"},
        )
    )

# Historical Data Graphs Page

def get_historical_layout(dropdown_options_continents, dropdown_options_countries):
    return ui.layout_sidebar(
        ui.panel_sidebar(
            # Sidebar CSS
            {"style": "background-color: rgba(0, 128, 255, 0.1); \
                font-family: Times; \
                color: black; \
                height: inherit;"
            },
            ui.input_selectize("scatter_plot", "Select a Graph", ["Health and Wealth", "GDP and CO2 Emissions", "Regional GDP Growth",
                                                                "Regional Population Growth", "CO2 Scatter Geo Map",
                                                                "CO2 Choropleth Map", "Life Expectancy Choropleth",
                                                                "Life Expectancy Strip Bar"], multiple=False),
            ui.panel_conditional("input.scatter_plot === 'Health and Wealth' || input.scatter_plot === 'GDP and CO2 Emissions' ",

                                ui.input_select("continent_dropdown", "Select Continent",
                                                choices=dropdown_options_continents, selected=None),
                                ui.input_select("country_dropdown", "Select Country", choices=dropdown_options_countries, selected=None)),

            ui.input_slider("year_slider", "Choose a Year", 1999, 2018,
                            value=1999, ticks=False, animate=True, drag_range=False, sep="")
        ),
        # Main content area
        ui.panel_main(
            output_widget("scatterplot_widget", width="auto", height="auto"),
            # Main panel color
            {"style": "background-color: rgba(153, 204, 153, 0.1);"},
        )
    )