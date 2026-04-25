# from pydoc import text

import streamlit as st
import pandas as pd
import plotly.express as px





st.set_page_config(layout="wide", page_title="India Energy Pulse")

# st.markdown("""
# <style>
# /* Force all Plotly SVG text to dark */
# .js-plotly-plot .plotly text {
#     fill: #1A1A1A !important;
# }
# </style>
# """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* 1. Target the main app container and all text elements */
    .stApp, .stMarkdown, p, span, label, .stMetric div {
        color: #1A1A1A !important;
    }

    /* 2. Target all header levels */
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }

    /* 3. Ensure links don't become invisible */
    a {
        color: #0000EE !important;
    }
    
    /* 4. Fix for sidebar text if you use it */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #1A1A1A !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. THE "VISIBLE NAVBAR" CSS
st.markdown("""
    <style>
    /* 1. Remove the huge gap at the top */
    .stAppHeader {
        background-color: rgba(0,0,0,0);
        height: 0px;
    }
    
    .block-container {
        padding-top: 2rem !important; /* Adjust this to move the buttons up or down */
        padding-bottom: 0rem !important;
    }

    /* 2. Make buttons stand out against the background */
    div.stButton > button {
        width: 100%;
        height: 42px;
        border-radius: 10px;
        border: 1px solid #d1d5db;
        background-color: white; /* Solid white so they are visible */
        color: #1f2937;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s;
    }

    div.stButton > button:hover {
        border-color: #2ecc71;
        color: #2ecc71;
        background-color: #f9fafb;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)
import streamlit as st

# 1. THE BEAUTIFICATION (CSS)
st.markdown("""
    <style>
    /* Style the button containers */
    [data-testid="stColumn"] {
        display: flex;
        justify-content: center;
    }

    /* Style the buttons themselves */
    div.stButton > button {
        border-radius: 20px;
        border: 1px solid #e0e0e0;
        background-color: white;
        color: #31333F;
        padding: 10px 24px;
        width: 100%;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Hover effects */
    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
        background-color: #fffafa;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* Active/Focus state */
    div.stButton > button:active {
        transform: translateY(0px);
    }
    </style>
""", unsafe_allow_html=True)
import streamlit as st

# 1. CSS FOR THE NAV BAR & TITLE ALIGNMENT
st.markdown("""
    <style>
    /* Align the title and buttons vertically */
    [data-testid="column"] {
        display: flex;
        align-items: center;
    }
    
    /* Clean button styling */
    div.stButton > button {
        border-radius: 15px;
        border: 1px solid #f0f2f6;
        background-color: #f8f9fb;
        transition: all 0.2s;
        width: 100%;
    }

    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 2. THE NAVIGATION BAR
# We use a larger weight for the title (3) and smaller for buttons (1.2)
title_col, n1, n2, n3 = st.columns([3, 1.2, 1.2, 1.2])

with title_col:
    st.markdown("<h3 style='margin:0; padding-bottom:10px;'>🚀 Navigation</h3>", unsafe_allow_html=True)

with n1:
    if st.button("📈 Capacity"):
        st.switch_page("pages/1_Growth.py")

with n2:
    if st.button("⚡ Generation"):
        st.switch_page("pages/2_Generation.py")

with n3:
    if st.button("📊 Prediction"):
        st.switch_page("pages/3_Prediction.py")

st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px; opacity: 0.2;'>", unsafe_allow_html=True)
# 3. YOUR CONTENT
st.markdown("### India's Electricity Transition")

# ---------------------------
# LIGHT NATURE THEME (Beige, Green, Yellow)
# ---------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #FDFBF0; /* Soft Beige/Cream */
        text-color: #2D3A2D;
    }

    .stApp {
        background-color: #FDFBF0;
    }

    /* Elegant Green Header Card */
    .header-card {
        background-color: #F2F5EB; /* Light Sage Green */
        border-radius: 20px;
        padding: 40px;
        border: 1px solid #E2E8D5;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    h1 { color: #2D3A2D !important; font-weight: 800 !important; }
    h2, h3 { color: #3E4D3E !important; }

    /* KPI / Metric Cards */
    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #E2E8D5;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* Subtext styling */
    .subtext {
        color: #6B7280;
        font-size: 18px;
    }

    /* Horizontal Rule */
    hr { border-top: 1px solid #E2E8D5; }

</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("""
<div class="header-card">
    <h1 style='margin:0;'>🌿 India's Electricity Transition</h1>
    <p class="subtext">
        Tracking the shift toward a greener future: Renewable infrastructure growth (2014 - 2026).
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# DATA (STAYS EXACTLY THE SAME)
# ---------------------------
data = {
    'Sector': ['Wind Power', 'Solar Power', 'Small Hydro Power', 'Biomass (Bagasse) Cogeneration', 
               'Biomass(Non-bagasse) Cogeneration', 'Waste to Energy', 'Waste to Energy (Off-grid)', 'Total'],
    'Cum_2014': [21042.58, 2821.91, 3803.68, 7419.23, 531.82, 90.58, 139.79, 35849.59],
    '2014-15': [2311.77, 1171.62, 251.68, 295.67, 60.05, 0.00, 9.71, 4100.50],
    '2015-16': [3423.05, 3130.36, 218.11, 304.85, 59.24, 0.00, 5.69, 7141.30],
    '2016-17': [5502.37, 5658.63, 106.38, 161.95, 2.20, 23.50, 11.77, 11466.81],
    '2017-18': [1865.23, 9563.69, 105.95, 519.10, 9.50, 24.22, 5.55, 12093.24],
    '2018-19': [1480.97, 6750.97, 107.34, 402.70, 12.00, 0.00, 6.58, 8760.56],
    '2019-20': [2117.79, 6510.06, 90.01, 97.00, 0.00, 9.34, 19.11, 8843.31],
    '2020-21': [1503.30, 5628.80, 103.65, 173.37, 97.24, 21.00, 20.75, 7548.11],
    '2021-22': [1110.53, 12760.50, 62.09, 59.69, 0.00, 54.50, 34.66, 14081.97],
    '2022-23': [2275.55, 12783.80, 95.40, 0.00, 42.40, 25.00, 52.28, 15274.43],
    '2023-24': [3253.38, 15033.24, 58.95, 0.00, 107.34, 1.60, 30.17, 18484.68],
    '2024-25': [4151.31, 23832.87, 97.30, 387.76, 0.00, 59.60, 194.81, 28723.65],
    '2025-26': [5094.68, 37957.90, 70.81, 0.00, 14.20, 0.00, 17.45, 43155.04],
    'Cum_2026': [56094.84, 150260.72, 5171.36, 9821.32, 1047.85, 324.24, 553.12, 223273.45]
}

df = pd.DataFrame(data)
years = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026']

def calculate_cumulative(row):
    cum = row['Cum_2014']
    cumulatives = [cum]
    addition_cols = ['2014-15','2015-16','2016-17','2017-18','2018-19',
                     '2019-20','2020-21','2021-22','2022-23','2023-24','2024-25','2025-26']
    for col in addition_cols:
        cum += row[col]
        cumulatives.append(cum)
    return cumulatives

key_sectors = ['Wind Power', 'Solar Power', 'Total']
df_key = df[df['Sector'].isin(key_sectors)].copy()
df_key['cumulatives'] = df_key.apply(calculate_cumulative, axis=1)

plot_data = []
for _, row in df_key.iterrows():
    for i, cap in enumerate(row['cumulatives']):
        plot_data.append({'Year': years[i], 'Capacity_GW': cap/1000, 'Sector': row['Sector']})

df_plot = pd.DataFrame(plot_data)

# ---------------------------
# KPI SECTION
# ---------------------------
st.write("### 🍃 Summary Stats")
k1, k2, k3 = st.columns(3)

k1.metric("Solar Total", "150 GW", "↑ Solar Focus")
k2.metric("Wind Total", "56 GW", "Steady Growth")
k3.metric("Total RE", "223 GW", "Green Target")
st.write("---")

# ---------------------------
# MAIN CHART (UNCHANGED LOGIC)
# ---------------------------
st.write("## 📈 Capacity Growth Trend")
col1, col2 = st.columns([2,1])

# Your exact chart setup
fig = px.line(
    df_plot,
    x="Year",
    y="Capacity_GW",
    color="Sector",
    markers=True,
    color_discrete_map={
        "Solar Power": "#EAB308",   # Golden Yellow
        "Wind Power": "#10B981",    # Emerald Green
        "Total": "#15803D"          # Dark Forest Green
    }
)

fig.update_layout(
    template="plotly_white", # Light template for your new theme
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_family="Plus Jakarta Sans",
    hovermode="x unified"
)
# fig.update_layout(
#     font=dict(color="#000000"),
#     legend=dict(font=dict(color="#000000"))
# )
fig.update_layout(template="plotly_white")

with col1:
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    ### 🔍 Key Findings
    - **Solar Dominance:** Massive surge specifically in the 2024-2026 forecast.
    - **Diversification:** While Wind is growing, Solar is clearly the primary engine.
                <div style="margin-top:20px; padding:20px; background:#FEFCE8; border: 1px solid #FEF08A; border-radius: 12px; color: #854D0E;">
        <b>Transition Note:</b> Capacity represents the peak power infrastructure, but infrastructure must be matched by storage technology.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    
    ### 📊Insight
       - **Solar grew** ~2 → ~145 GW (2014–2026) vs wind ~21 → ~55 GW → solar drives >70–80% of incremental capacity post-2020.
       - The inflection after ~2018 and steeper rise post-2021 aligns with:
            - **Solar Park Scheme** → reduced land & infra bottlenecks → faster commissioning
            - **PLI (2021)** → improved domestic supply → accelerated deployments
            - **Transmission charge waivers + 100% FDI** → lower project cost, higher capital inflow
       - **Cost effect** is decisive: solar tariffs fell below wind → higher auction wins and capacity addition.
       - **Wind remains linear** (~2.5× growth) due to:
            - resource/geographic constraints (limited high-wind sites)
            - longer project cycles + lower policy push vs solar
       - By 2024–2026, total capacity slope ≈ solar slope → system growth is solar-dependent.
    
   
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------
# PIE CHART (UNCHANGED LOGIC)
# ---------------------------
st.write("## ⚡ Capacity Composition (2026)")

pie_data = df[df['Sector'] != 'Total'][['Sector','Cum_2026']].copy()

fig2 = px.pie(
    pie_data,
    values='Cum_2026',
    names='Sector',
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.GnBu_r
)
fig.update_layout(template="plotly_white")

fig2.update_traces(textposition='inside', textinfo='percent+label')
fig2.update_layout(
    # textfont_color="#EFEFEF",
    template="plotly_white",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig2.update_layout(
    width=600,
    height=600
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# FINAL INSIGHT
# ---------------------------
st.success("India has rapidly expanded its renewable infrastructure, driven primarily by solar energy. Solar power, wind power, and biomass cogeneration together constitute the major share of India’s renewable energy capacity.")





st.write("---")
st.write("## 🗺️ State-wise Renewable Capacity")


import re

raw_text = """1 28 Andhra Pradesh 164.51 4415.78 378.10 134.57 53.16 49.19 615.02 6382.54 774.5 249.42 88.34 7494.80 3290.00 15980.11
2 12 Arunachal Pradesh 140.61 0 0 0 0 0 0.00 1.27 6.68 0 7.49 15.44 1865.00 2021.05
3 18 Assam 34.11 0 0 8.00 0 0 8.00 216.26 344.2 0 9.71 570.17 346.00 958.28
4 10 Bihar 70.70 0 112.50 31.40 0 1.32 145.22 196.06 218 0 21.28 435.34 0 651.26
5 22 Chhattisgarh 100.90 0 272.09 7.00 0 10.83 289.92 1254.41 167.6 0 390.73 1812.74 120.00 2323.56
6 30 Goa 0.05 0 0 0 1.94 0 1.94 8.51 71.5 0 1.49 81.50 0 83.49
7 24 Gujarat 113.30 15642.26 65.30 12.00 7.50 45.05 129.85 20974.68 6881.8 1273.43 173.01 29302.92 1990.00 47178.33
8 6 Haryana 73.50 0 151.40 125.46 11.20 41.78 329.84 267.76 1188.3 0 1152.32 2608.38 0 3011.72
9 2 Himachal Pradesh 1013.46 0 0 9.20 0 1.00 10.20 257 66.7 0 34.58 358.28 11421.02 12802.96
10 1 Jammu & Kashmir 189.93 0 0 5.00 0 0 5.00 2.49 42.2 0 34.79 79.48 3360.00 3634.41
11 20 Jharkhand 4.05 0 0 19.10 0 1.04 20.14 21 94.9 0 139.5 255.40 210.00 489.59
12 29 Karnataka 1284.73 8730.14 1868.91 20.20 1.00 26.94 1917.05 9855.78 842.9 358.85 44.11 11101.64 3689.20 26722.76
13 32 Kerala 276.52 71.52 0 2.27 0 0.23 2.50 340.26 1850.4 0 24.93 2215.59 2008.15 4574.28
15 23 Madhya Pradesh 123.71 3679.15 92.50 18.85 15.40 32.71 159.46 4990.18 893.1 0 102.04 5985.32 2235.00 12182.64
16 27 Maharashtra 384.28 5927.21 2907.30 16.40 12.59 63.68 2999.97 12171.3 5442.3 0 2008.57 19622.17 3047.00 31980.63
17 14 Manipur 5.45 0 0 0 0 0 0.00 0.6 10.6 0 6.32 17.52 105.00 127.97
18 17 Meghalaya 55.03 0 0 13.80 0 0 13.80 0 0.21 0 4.07 4.28 322.00 395.11
19 15 Mizoram 45.47 0 0 0 0 0 0.00 22 5.3 0 6.39 33.69 60.00 139.16
20 13 Nagaland 32.67 0 0 0 0 0 0.00 0 1 0 2.34 3.34 75.00 111.01
21 21 Odisha 140.63 0 50.40 8.82 0 5.00 64.22 662.52 156.3 0 64.62 883.44 2154.55 3242.84
22 3 Punjab 176.10 0 299.50 237.79 10.75 34.55 582.59 886.77 581.2 0 116.97 1584.94 1096.30 3439.93
23 8 Rajasthan 23.85 5349.15 134.15 2.00 74.50 11.77 222.42 36125.95 2090.4 1980 816.27 41012.62 412.50 47020.54
24 11 Sikkim 55.11 0 0 0 0 0 0.00 0.52 5.12 0 1.92 7.56 2282.00 2344.67
25 33 Tamil Nadu 123.05 12147.23 969.10 52.05 6.40 27.57 1055.12 11972.82 1532.3 0 74.55 13579.67 2203.20 29108.27
26 36 Telangana 89.67 128.10 158.10 23.74 45.80 14.47 242.11 4360.49 695.9 0 8.71 5065.10 2405.60 7930.58
27 16 Tripura 16.01 0 0 0 0 0 0.00 7.09 12.2 0 16.25 35.54 0 51.55
28 9 Uttar Pradesh 50.60 0 1985.50 184.76 0 159.63 2329.89 3048.33 715.3 0 359.51 4123.14 501.60 7005.23
29 5 Uttarakhand 233.82 0 72.72 71.92 0 16.85 161.49 541.05 273.71 0 23.13 837.89 4785.35 6018.55
30 19 West Bengal 98.50 0 300.00 43.52 0 8.34 351.86 240.35 67.13 0 13.14 320.62 1341.20 2112.18"""

# CLEAN LINES
lines = raw_text.split("\n")
clean_lines = []
buffer = ""

for line in lines:
    line = line.strip()
    if not line:
        continue

    if re.match(r"^\d+", line):
        if buffer:
            clean_lines.append(buffer)
        buffer = line
    else:
        buffer += " " + line

if buffer:
    clean_lines.append(buffer)

# PARSE
data = []
for line in clean_lines:
    parts = line.split()
    idx = parts[0]
    state_parts = []
    numeric_parts = []

    for p in parts[1:]:
        if re.match(r"^\d+(\.\d+)?$", p):
            numeric_parts.append(float(p))
        else:
            state_parts.append(p)

    state = " ".join(state_parts)
    data.append([idx,state] + numeric_parts)

df_state = pd.DataFrame(data)
df_state = df_state.drop(df_state.columns[[0, 2]], axis=1)
# COLUMN NAMES
cols = [
    "State",
    "Small Hydro",
    "Wind",
    "Biomass Bagasse",
    "Biomass Non-Bagasse",
    "Waste",
    "Waste Offgrid",
    "Bio Total",
    "Solar Ground",
    "Solar RTS",
    "Solar Hybrid",
    "Solar Offgrid",
    "Solar Total",
    "Large Hydro",
    "Total Capacity"
]

df_state.columns = cols

# KEEP IMPORTANT COLUMNS
df_state = df_state[
    ["State", "Solar Total", "Wind", "Small Hydro", "Bio Total", "Large Hydro", "Total Capacity"]
]

# NUMERIC
for col in df_state.columns:
    if col != "State":
        df_state[col] = pd.to_numeric(df_state[col], errors="coerce")


fig_bar = px.bar(
    df_state.sort_values("Total Capacity", ascending=False),
    x="State",
    y="Total Capacity",
    color="Total Capacity",
    color_continuous_scale="YlGn",
    title="State-wise Total Renewable Capacity"
)

fig_bar.update_layout(
    xaxis_tickangle=45,
    template="plotly_white"
)
fig_bar.update_layout(
    xaxis_tickangle=45,
    template="plotly_white",
    paper_bgcolor="#FDFBF0",  # match your page background
    plot_bgcolor="#FDFBF0",
)
fig.update_layout(template="plotly_white")

st.plotly_chart(fig_bar, use_container_width=True)


st.markdown("""
<div style="padding:20px; background:#ECFDF5; border-radius:12px; border:1px solid #A7F3D0;">

### 🔍 Insight

- Capacity is highly concentrated in a few states due to stronger resource potential, larger land availability, supportive policies, and better grid connectivity.
- Gujarat, Rajasthan, Tamil Nadu dominate renewable infrastructure  
- Smaller states contribute very little  

👉 Transition is **not uniform across India**

</div>
""", unsafe_allow_html=True)


# import json

# import os


# with open("pages/india_telengana.geojson") as f:
#     geojson = json.load(f)

# ndf = df_state.copy()
# ndf["State"] = ndf["State"].str.strip()
# ndf["State"] = ndf["State"].str.strip()

# ndf["State"] = ndf["State"].replace({
#     "Jammu & Kashmir": "Jammu and Kashmir"
# })


# fig_map = px.choropleth(
#     ndf,
#     geojson=geojson,
#     featureidkey="properties.NAME_1",
#     locations="State",
#     color="Total Capacity",
#     color_continuous_scale="YlGn",
# )

# fig_map.update_geos(fitbounds="locations", visible=False)

# fig_map.update_layout(
#     margin={"r":0,"t":30,"l":0,"b":0},
#     title="State-wise Renewable Capacity"
# )

# st.plotly_chart(fig_map, use_container_width=True)



import plotly.express as px
import streamlit as st

source_cols = [
    "Solar Total",
    "Wind",
    "Small Hydro",
    "Bio Total",
    "Large Hydro"
]

source_labels = {
    "Solar Total": "Solar",
    "Wind": "Wind",
    "Small Hydro": "Small Hydro",
    "Bio Total": "Biomass",
    "Large Hydro": "Large Hydro"
}

source_colors = {
    "Solar Total": "#F4C95D",
    "Wind": "#7FB8D4",
    "Small Hydro": "#C8B6E2",
    "Bio Total": "#86C77A",
    "Large Hydro": "#8FD3C8"
}

st.markdown("## Top 3 States by Renewable Source")

insights = {
    "Wind": """
#### Wind Power Insights
* Gujarat, Tamil Nadu, and Karnataka have strong wind zones with steady high-speed winds (Kutch coast, Kanyakumari–Tirunelveli belt, and Western Ghats foothills), plus open terrain that supports large wind farms.
* Total wind capacity reached ~51.7 GW by 2025, with a big rise in 2025, and these three states together contribute more than half of it.
""",
    "Solar Total": """
#### Solar Power Insights
* Rajasthan (Thar) and Gujarat (Kutch) have India’s highest solar irradiation, high sunshine hours, and flat desert land enabling mega solar parks like Bhadla and Pokhran at low land cost.
* Maharashtra has flat, low-density regions suited for utility-scale solar, with strong industrial demand nearby.

""",
    "Small Hydro": """
### Small Hydro Insights
* Karnataka leads because the Western Ghats provide many suitable river sites, and policy support has encouraged small hydro development.
* Himachal Pradesh is high due to steep Himalayan rivers that naturally support hydropower projects.
* Maharashtra ranks third because parts of the Western Ghats offer potential sites, and strong grid access plus industrial demand improves viability.""",
    "Bio Total": """
### Biomass Insights
* Maharashtra leads biomass due to its large sugar industry and steady supply of bagasse.
* Uttar Pradesh ranks second because of extensive agricultural residues (sugarcane, rice) and high rural energy demand.
* Karnataka is third due to available agricultural waste and policy-supported biomass power development in rural areas.
.""",
    "Large Hydro": """
### Large Hydro Insights
* Himachal Pradesh leads due to steep Himalayan rivers (Sutlej, Beas, Chenab) with high elevation drop and snowmelt-fed flow, ideal for hydropower.
* Uttarakhand ranks second because the Ganga and its tributaries provide strong river flow and terrain suited for large hydro projects.
* Karnataka is third with major hydro stations on rivers like Sharavathi, Cauvery, and Tungabhadra, built through early dam development.
""",
}

for i in range(0, len(source_cols), 2):
    c1, c2 = st.columns(2)

    for col_box, source in zip([c1, c2], source_cols[i:i+2]):
        top3 = df_state.nlargest(3, source)[["State", source]].sort_values(source, ascending=True)

        fig = px.bar(
            
            top3,
            x=source,
            y="State",
            orientation="h",
            text=source,
            color_discrete_sequence=[source_colors[source]],
            title=f"Top 3 States in {source_labels[source]}"
        )

        fig.update_traces(
              # increase top space
            texttemplate="%{text:.1f}",
            textposition="inside",
            
            marker_line_color="white",
            marker_line_width=1.5
        )

        fig.update_layout(
            title_x=0.5 ,
            template="plotly_white",
            height=320,
            margin=dict(l=10, r=10, t=80, b=10),
            title_font=dict(size=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Capacity",
            yaxis_title="",
            font=dict(color="#2e3a2f")
        )

        fig.update_xaxes(gridcolor="rgba(168,213,186,0.20)")
        fig.update_yaxes(categoryorder="total ascending")
        fig.update_layout(template="plotly_white")

        with col_box:
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown(f"""
            <div style="
                background: rgba(244, 201, 93, 0.12);
                padding: 10px 12px;
                border-radius: 5px;
                margin-top: 6px;
                margin-left: 50px;
                margin-right: 100px;
                color: #2e3a2f;
                font-size: 0.9rem;
            ">
            {insights.get(source, "No insight available for this plot.")}
            """, unsafe_allow_html=True)


st.markdown("""
<div style="padding:20px; background:#F2F5EB; border-radius:12px; border:1px solid #A7F3D0;">

<h3>📊 Insight</h3>

<ul>
<li>Solar: Highly concentrated — Rajasthan (~41 GW) leads, followed by Gujarat and Maharashtra → high irradiance + land availability</li>
<li>Wind: Dominated by Gujarat, Tamil Nadu, Karnataka → coastal/high wind-speed corridors</li>
<li>Small Hydro: Karnataka and Himachal Pradesh → terrain-driven</li>
<li>Biomass: Maharashtra and Uttar Pradesh → agricultural base</li>
<li>Large Hydro: Himachal Pradesh and Uttarakhand → Himalayan rivers</li>
</ul>

</div>
""", unsafe_allow_html=True)