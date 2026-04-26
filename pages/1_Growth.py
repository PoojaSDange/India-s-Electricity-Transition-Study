# from pydoc import text

import streamlit as st
import pandas as pd
import plotly.express as px





st.set_page_config(layout="wide", page_title="India's Electricity Transition", initial_sidebar_state="collapsed", page_icon="⚡")

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
import pandas as pd
import requests
from io import StringIO

url = "https://mnre.gov.in/en/year-wise-achievement/"
response = requests.get(url)
response.raise_for_status()

tables = pd.read_html(StringIO(response.text))
df = tables[0]   # that main table

new_cols = [
    "Sector",
    "Cum_2014",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
    "Cum_2026"
]
df.columns = new_cols

# Make sure the last row is "Total"
df.iloc[-1, 0] = "Total"

#Convert all numeric columns to float
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Convert to your exact dict format
sector_order = [
    'Wind Power',
    'Solar Power',
    'Small Hydro Power',
    'Biomass (Bagasse) Cogeneration',
    'Biomass(Non-bagasse) Cogeneration',
    'Waste to Energy',
    'Waste to Energy (Off-grid)',
    'Total'
]

data = {'Sector': sector_order}
for year in df.columns[1:]:
    data[year] = [float(df.loc[df["Sector"] == s, year].iloc[0]) for s in sector_order]

# # Now `data` looks exactly like your example
# print(data)

df = pd.DataFrame(data)
years = ['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026']
# 

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

large_hydro_cap_gw = [40, 42, 42.78, 44.48, 45.29, 45.40, 45.70, 46.21, 46.72, 46.85, 46.93, 47.73, 48.00]
# 2026 Large‑Hydro capacity (GW → MW)
large_hydro_2026_mw = large_hydro_cap_gw[12] * 1000   # 48 GW → 48,000 MW

# Append a new row for Large‑Hydro
new_row = {
    'Sector': 'Large Hydro',
    **{col: 0.0 for col in df.columns if col != 'Sector'},  # all addition cols = 0
    'Cum_2026': large_hydro_2026_mw
}

df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

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
st.success("India has rapidly expanded its renewable infrastructure, driven primarily by solar energy. Solar power, wind power, and  Large Hydro together constitute the major share of India’s renewable energy capacity.")





st.write("---")
st.write("## 🗺️ State-wise Renewable Capacity")


import re

""

import io
import re
import requests
import pdfplumber
import pandas as pd

# ── Config ─────
PDF_URL = (
    "https://cdnbbsr.s3waas.gov.in/"
    "s3716e1b8c6cd17b771da77391355749f3/uploads/2026/04/20260415955675604.pdf"
)

# PDF column order (what pdfplumber sees left-to-right):
PDF_COLS = [
    "small_hydro", "wind",
    "bagasse", "nonbagasse", "wte", "wte_offgrid", "bio_total",
    "gm_solar", "rts", "hybrid", "offgrid_solar", "solar_total",
    "large_hydro", "total",
]

# Output column order for raw_text (matches the format you want):
OUT_COLS = PDF_COLS

# Regex: <int>  <int>  <state name (words/&/spaces)>  <numbers...>
ROW_RE = re.compile(
    r"^(\d+)\s+(\d+)\s+([A-Za-z &]+?)\s+([\d.][0-9. ]+)$"
)


# ── Step 1: Download ───

def download_pdf(url: str) -> io.BytesIO:
    print(f"[1] Downloading PDF …")
    resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    print(f"    {len(resp.content)/1024:.1f} KB received")
    return io.BytesIO(resp.content)


# ── Step 2: Extract raw text ────

def extract_text(pdf_bytes: io.BytesIO) -> str:
    print("[2] Extracting text with pdfplumber …")
    with pdfplumber.open(pdf_bytes) as pdf:
        text = pdf.pages[0].extract_text(x_tolerance=3, y_tolerance=3)
    print(f"    {len(text.splitlines())} lines extracted")
    return text


# ── Step 3: Constraint-based token alignment ──

def align_tokens(tokens: list[str], s_no: int, state: str) -> list[float] | None:
    t = [float(x) for x in tokens]
    tot = t[-1]

    for lh_present in [True, False]:
        # Set right_used inside the loop (not before it)
        if lh_present:
            if len(t) < 3:
                continue
            lh = t[-2]
            st = t[-3]
            right_used = 3
        else:
            if len(t) < 2:
                continue
            lh = 0.0
            st = t[-2]
            right_used = 2

        # Now use right_used safely
        if len(t) < right_used + 1:
            continue

        left = t[:len(t) - right_used]
        rem  = tot - lh - st
        if rem < -0.02:
            continue

        # --- rest of the function remains unchanged ---
        # (solar block, bio block, etc.)

        for sol_size in [4, 3, 2]:
            if len(left) < sol_size:
                continue
            sol_block = left[-sol_size:]
            pre_sol   = left[:-sol_size]
            if abs(sum(sol_block) - st) > 0.02:
                continue
            if not pre_sol:
                continue

            bio_total_val = pre_sol[-1]
            pre_bio       = pre_sol[:-1]

            for bio_sub_size in [4, 3, 2, 1, 0]:
                if len(pre_bio) < bio_sub_size:
                    continue
                bio_sub  = pre_bio[-bio_sub_size:] if bio_sub_size > 0 else []
                pre_bio2 = pre_bio[:-bio_sub_size] if bio_sub_size > 0 else pre_bio

                if bio_sub_size > 0 and abs(sum(bio_sub) - bio_total_val) > 0.02:
                    continue
                if bio_sub_size == 0 and abs(bio_total_val) > 0.02:
                    continue

                if   len(pre_bio2) == 0: sh, wind = 0.0, 0.0
                elif len(pre_bio2) == 1: sh, wind = pre_bio2[0], 0.0
                elif len(pre_bio2) == 2: sh, wind = pre_bio2[0], pre_bio2[1]
                else: continue

                if abs(sh + wind + bio_total_val - rem) > 0.02:
                    continue

                # Expand bio block → [bagasse, nonbagasse, wte, wte_offgrid]
                b4 = [0.0] * 4
                for i, v in enumerate(bio_sub):
                    b4[i + (4 - bio_sub_size)] = v

                # Expand solar block → [gm_solar, rts, hybrid, offgrid_solar]
                # hybrid (index 2) is the column most often absent
                s4 = [0.0] * 4
                if   sol_size == 4: s4 = list(sol_block)
                elif sol_size == 3: s4[0], s4[1], s4[3] = sol_block[0], sol_block[1], sol_block[2]
                elif sol_size == 2: s4[0], s4[3]         = sol_block[0], sol_block[1]

                # Return in PDF column order
                return [sh, wind] + b4 + [bio_total_val] + s4 + [st, lh, tot]

    return None   # alignment failed


# ── Step 4: Parse text → DataFrame ───────────────────────────────────────────

def parse(raw_text: str) -> pd.DataFrame:
    print("[3] Parsing and aligning rows …")
    records  = []
    failed   = []

    for line in raw_text.splitlines():
        line = line.strip()
        m    = ROW_RE.match(line)
        if not m:
            continue

        s_no     = int(m.group(1))
        lgd_code = int(m.group(2))
        state    = m.group(3).strip()
        tokens   = m.group(4).strip().split()

        aligned = align_tokens(tokens, s_no, state)
        if aligned is None:
            failed.append(f"  ✗ Row {s_no} ({state}): could not align {tokens}")
            continue

        records.append([s_no, lgd_code, state] + aligned)

    if failed:
        print("  Alignment failures:")
        print("\n".join(failed))

    print(f"    {len(records)} rows aligned successfully  |  {len(failed)} failures")
    return pd.DataFrame(records, columns=["s_no", "lgd_code", "state"] + PDF_COLS)


# ── Step 5: Build raw_text string ─────────────────────────────────────────────

def to_raw_text(df: pd.DataFrame) -> str:
    """
    Format the DataFrame as the raw_text string:
        s_no  lgd_code  state  large_hydro  small_hydro  wind  ...  total
    Whole numbers are emitted without decimals (218 not 218.0).
    """
    def fmt(v: float) -> str:
        if v == 0:          return "0"
        if v == int(v):     return str(int(v))
        return str(v)

    lines = []
    for _, row in df.sort_values("s_no").iterrows():
        parts = (
            [str(int(row["s_no"])), str(int(row["lgd_code"])), row["state"]]
            + [fmt(row[c]) for c in OUT_COLS]
        )
        lines.append(" ".join(parts))
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

    
def maini():
    # pdf_bytes = download_pdf(PDF_URL)
    raw_text_pdf = extract_text("state_wise.pdf")
    df = parse(raw_text_pdf)

    raw_text = to_raw_text(df)
    return raw_text



raw_text = maini()

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

fig_bar.update_traces(
    marker_line_color="lightgreen",   # outline color
    marker_line_width=1                # thickness of the outline
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