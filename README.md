Dashboard Link - https://india-s-electricity-transition-study.streamlit.app/

# India's Electricity Transition Study

A data-driven study of India's transition toward renewable energy, combining historical electricity-generation analysis with trend-based forecasting and an interactive Streamlit dashboard.

## Overview

India's electricity generation is gradually shifting toward renewable sources such as solar, wind, hydro and biomass.

This project analyzes historical electricity data and explores how renewable energy could contribute to India's future electricity demand.

The project has two main components:

1. **Historical analysis** — understanding electricity-generation and renewable-energy trends.
2. **Scenario-based forecasting** — estimating future electricity demand and renewable generation based on historical trends and user-defined renewable capacities.

## Key Features

* Historical analysis of India's electricity generation
* Analysis of renewable generation from:

  * Solar
  * Wind
  * Hydro
  * Biomass
* Calculation of Capacity Utilization Factor (CUF) for each renewable source
* Trend-based forecasting of total electricity generation
* Separate CUF trend models for each renewable source
* Future renewable-generation estimation based on assumed installed capacities
* Renewable share of total electricity demand/generation
* Interactive Streamlit dashboard
* Model statistics and visualization of historical and projected trends

## Methodology

### 1. Data Preparation

Historical electricity-generation and renewable-capacity data are collected and structured using Python and Pandas.

The data contains approximately a decade of annual observations.

### 2. Capacity Utilization Factor

For each renewable source, CUF is calculated as:

$$
CUF = \frac{Generation}{Capacity \times 8.76}
$$

where:

* Generation is measured in Billion Units (BU)
* Capacity is measured in GW
* 8.76 converts GW of continuous generation over one year into BU

CUF helps estimate how much electricity can realistically be generated from a given installed capacity.

### 3. Demand Trend Model

A Linear Regression model is used to capture the historical relationship between year and total electricity generation:

$$
Generation = m(Year) + c
$$

The model is then extrapolated to future years.

### 4. CUF Trend Models

Separate Linear Regression models are trained for:

* Solar CUF
* Wind CUF
* Hydro CUF
* Biomass CUF

The projected CUF is constrained within reasonable source-specific bounds to avoid unrealistic extrapolated values.

### 5. Future Scenario Calculation

For a selected future year and user-defined renewable capacities:

$$
Generation = Capacity \times CUF \times 8.76
$$

Generation is calculated separately for solar, wind, hydro and biomass.

The renewable contribution is then calculated as:

$$
Renewable\ Share =
\frac{Renewable\ Generation}{Total\ Generation}
\times 100
$$

This allows the dashboard to explore different renewable-capacity scenarios.

## Technology Stack

* **Python**
* **Pandas** — data manipulation and processing
* **NumPy** — numerical calculations
* **Matplotlib / Seaborn** — visualization
* **Scikit-learn** — Linear Regression and model evaluation
* **Streamlit** — interactive dashboard

## Data Sources

The project uses publicly available electricity and renewable-energy information from sources including:

* Central Electricity Authority (CEA)
* Ministry of New and Renewable Energy (MNRE)

## Project Structure

```text
India-s-Electricity-Transition-Study/
│
├── pages/
│   └── 3_Prediction.py
│
├── data/
│   └── ...
│
├── notebooks/
│   └── ...
│
├── app.py
└── README.md
```

## Limitations

The forecasting component is intended as a **trend and scenario-analysis tool**, not as a high-accuracy long-term forecasting system.

The main limitations are:

* The dataset contains a relatively small number of annual observations.
* Linear regression captures broad trends but does not model seasonality or complex nonlinear relationships.
* Future projections can be affected by policy changes, weather conditions, economic growth, technology changes and changes in electricity demand.
* Forecast uncertainty increases as the prediction moves further beyond the historical period.

A future version could use higher-frequency monthly data and additional variables such as historical demand, seasonal patterns, capacity additions and economic indicators, followed by time-series or nonlinear model comparison.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/PoojaSDange/India-s-Electricity-Transition-Study.git
cd India-s-Electricity-Transition-Study
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## Project Goal

The goal of this project is to combine **data analysis, machine learning and interactive visualization** to understand India's electricity transition and explore how different renewable-capacity scenarios could affect future electricity generation.
