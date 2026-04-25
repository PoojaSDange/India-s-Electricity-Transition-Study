
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# from style_loader import load_light_theme

st.set_page_config(page_title="Renewable Energy Dashboard", layout="wide")

st.set_page_config(layout="wide", page_title="India Energy Pulse")

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


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(244, 201, 93, 0.12), transparent 28%),
        radial-gradient(circle at top right, rgba(134, 199, 122, 0.12), transparent 30%),
        linear-gradient(180deg, #fffdf8 0%, #f8fbf6 100%);
    color: #233123;
}

.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-bottom: 2rem;
}

.hero-box {
    background: rgba(255, 255, 255, 0.90);
    border: 1px solid rgba(134, 199, 122, 0.22);
    border-radius: 26px;
    padding: 26px 28px;
    box-shadow: 0 14px 34px rgba(60, 80, 50, 0.08);
    margin-bottom: 1.2rem;
}

.hero-box h1 {
    margin: 0;
    font-size: 2.25rem;
    font-weight: 800;
    background: linear-gradient(90deg, #d9a441, #6fb58f, #8bbd62);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-box p {
    margin: 10px 0 0 0;
    color: #5d6b5d;
    font-size: 1rem;
}

.metric-card {
    background: rgba(255, 255, 255, 0.93);
    border: 1px solid rgba(134, 199, 122, 0.18);
    border-radius: 18px;
    padding: 18px 20px;
    box-shadow: 0 10px 22px rgba(60, 80, 50, 0.06);
}

.metric-title {
    color: #6a7a69;
    font-size: 0.85rem;
    margin-bottom: 6px;
}

.metric-value {
    font-size: 1.65rem;
    font-weight: 800;
    margin: 0;
}

.panel-card {
    background: rgba(255, 255, 255, 0.93);
    border: 1px solid rgba(134, 199, 122, 0.16);
    border-radius: 22px;
    padding: 18px 18px 10px 18px;
    box-shadow: 0 10px 22px rgba(60, 80, 50, 0.06);
}

.insight-box {
    background: linear-gradient(180deg, rgba(244, 201, 93, 0.14), rgba(134, 199, 122, 0.10));
    border: 1px solid rgba(134, 199, 122, 0.22);
    border-radius: 18px;
    padding: 18px 20px;
    color: #334433;
    box-shadow: 0 10px 22px rgba(60, 80, 50, 0.06);
}

.small-note {
    color: #6a7a69;
    font-size: 0.88rem;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Dashboard")
    st.markdown("Renewable capacity vs actual generation")
    st.markdown("---")
    st.markdown("**Key view**")
    st.markdown("- Actual RE generation")
    st.markdown("- Expected maximum output")
    st.markdown("- Gap between them")
    st.markdown("---")
    st.markdown("**Note**")
    st.caption("The plot uses your Excel file and compares actual output with theoretical output from installed capacity.")

st.markdown("""
<div class="hero-box">
    <h1>Renewable Energy: Actual vs Expected Generation</h1>
    <p>Installed capacity shows what India can produce. Actual generation shows what the system truly delivers.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# CAPACITY DATA
# -----------------------------
capacity_data = {
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
}

capacity_df = pd.DataFrame(capacity_data)
years = ['2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23','2023-24','2024-25','2025-26']

total_row = capacity_df[capacity_df['Sector'] == 'Total'].iloc[0]
cumulative_capacity = total_row['Cum_2014'] + total_row[years].cumsum()
expected_generation = (cumulative_capacity * 8760) / 1e6

expected_df = pd.DataFrame({
    'Year': years,
    'Expected_RE_Generation_BU': expected_generation.values
})

# -----------------------------
# ACTUAL RE GENERATION
# -----------------------------
power_df = pd.read_excel(r"pages/power.xlsx")

power_df['Generation (BU)'] = (
    power_df['Generation (BU)']
    .astype(str)
    .str.replace(',', '.', regex=False)
)
power_df['Generation (BU)'] = pd.to_numeric(power_df['Generation (BU)'], errors='coerce')

re_sources = ['Wind', 'Solar', 'Bio Power', 'Small-Hydro']
actual_re_df = (
    power_df[power_df['Source'].isin(re_sources)]
    .groupby('Year', as_index=False)['Generation (BU)']
    .sum()
    .rename(columns={'Generation (BU)': 'Actual_RE_Generation_BU'})
)

plot_df = pd.merge(expected_df, actual_re_df, on='Year', how='inner')
plot_df = plot_df.sort_values("Year").reset_index(drop=True)
plot_df["Gap_BU"] = plot_df["Expected_RE_Generation_BU"] - plot_df["Actual_RE_Generation_BU"]
plot_df["Gap_Pct"] = (plot_df["Gap_BU"] / plot_df["Expected_RE_Generation_BU"]) * 100

# -----------------------------
# KPI ROW
# -----------------------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Years shown</div>
        <p class="metric-value">{len(plot_df)}</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Latest actual</div>
        <p class="metric-value" style="color:#2f4f3a;">{plot_df['Actual_RE_Generation_BU'].iloc[-1]:.2f} BU</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Latest expected</div>
        <p class="metric-value" style="color:#8c6b1f;">{plot_df['Expected_RE_Generation_BU'].iloc[-1]:.2f} BU</p>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Latest gap</div>
        <p class="metric-value" style="color:#6b3d3d;">{plot_df['Gap_BU'].iloc[-1]:.2f} BU</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# CHART + INSIGHT LAYOUT
# -----------------------------
left, right = st.columns([2.2, 1])
with left:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)

    plot_df = plot_df.sort_values("Year").reset_index(drop=True)
    x = np.arange(len(plot_df))
    actual = pd.to_numeric(plot_df["Actual_RE_Generation_BU"], errors="coerce").fillna(0).values
    expected = pd.to_numeric(plot_df["Expected_RE_Generation_BU"], errors="coerce").fillna(0).values

    # Setting up a high-quality figure
    fig, ax = plt.subplots(figsize=(13.5, 6.8), dpi=100)
    fig.patch.set_facecolor("#FFFFFF")  # Clean white background
    ax.set_facecolor("#FFFFFF")

    # 1. ACTUAL GENERATION: Rounded bars with a soft Sage color
    bars = ax.bar(
        x, actual,
        color="#4F7942",  # Deep Sage
        alpha=0.85,
        width=0.6,
        label="Actual RE Generation",
        edgecolor="#3E5F34",
        linewidth=0.8,
        zorder=3
    )

    # 2. EXPECTED OUTPUT: Elegant Golden line
    ax.plot(
        x, expected,
        marker="o",
        markersize=8,
        linewidth=3,
        color="#C5A059",  # Sophisticated Gold
        markerfacecolor="#FFFFFF",
        markeredgecolor="#C5A059",
        markeredgewidth=2,
        label="Expected Maximum RE Output",
        zorder=5
    )

    # 3. GENERATION GAP: Subtle shaded region with a custom hatch
    ax.fill_between(
        x, actual, expected,
        where=expected >= actual,
        facecolor="#F9F1E1",  # Very light cream-gold
        alpha=0.5,
        interpolate=True,
        hatch='///',          # Subtle pattern for texture
        edgecolor="#C5A059",
        linewidth=0,
        label="Efficiency Gap",
        zorder=2
    )

    # 4. TYPOGRAPHY & AXES
    ax.set_xticks(x)
    ax.set_xticklabels(plot_df["Year"], fontsize=11, fontweight="medium", color="#4A5A49")
    
    ax.set_title(
        "Renewable Energy Generation Performance",
        fontsize=22,
        fontweight="bold",
        pad=25,
        y=1.02,
        color="#1E2F1E",
        loc="left" # Modern left-aligned title
    )
    
    ax.set_ylabel("Generation (Billion Units)", fontsize=12, fontweight="medium", labelpad=15, color="#4A5A49")

    # 5. CLEANING THE VISUAL (Spines & Grid)
    ax.grid(axis="y", linestyle=(0, (5, 10)), alpha=0.4, color="#A8B2A7")
    ax.set_axisbelow(True)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#D8E2D5")
    ax.spines["bottom"].set_linewidth(1.2)

    ax.tick_params(axis='both', which='major', labelsize=11, colors="#4A5A49")

    # 6. ENHANCED LEGEND
    ax.legend(
        frameon=False, 
        ncol=3, 
        loc="upper left", 
        bbox_to_anchor=(0, 1.08), 
        fontsize=10.5,
        labelcolor="#2E3B2E"
    )

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)
with right:
   st.markdown("""
    <div class="insight-box">
        <h3 style="margin-top:0;">Interpretation</h3>
        <p>
            At first glance, it looks like renewable energy should be producing much more power — the capacity is there, after all. But reality doesn’t quite follow the ideal line. Sunlight fades, winds slow down, seasons shift, and sometimes the grid just can’t handle everything being produced.
        </p>
        <p>
            What’s interesting is that this gap isn’t constant. Some years, we get closer to that potential; other times, we drift away. It shows that simply adding more capacity doesn’t automatically translate into more electricity.
        </p>
        <p style="margin-bottom:0;">
            So the real story is not only how much capacity was built, but how effectively that capacity is converted into electricity.
        </p>
    </div>
    """, unsafe_allow_html=True)







import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
 
st.set_page_config(page_title="Generation Mix Dashboard", layout="wide")
 
# ─── GLOBAL STYLES (mirror your existing dashboard) ───────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
 
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
 
.stApp {
    background:
        radial-gradient(circle at top left,  rgba(244,201,93,0.12),  transparent 28%),
        radial-gradient(circle at top right, rgba(134,199,122,0.12), transparent 30%),
        linear-gradient(180deg, #fffdf8 0%, #f8fbf6 100%);
    color: #233123;
}
 
.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-bottom: 2rem;
}
 
/* ── shared card shells ── */
.hero-box {
    background: rgba(255,255,255,0.90);
    border: 1px solid rgba(134,199,122,0.22);
    border-radius: 26px;
    padding: 26px 28px;
    box-shadow: 0 14px 34px rgba(60,80,50,0.08);
    margin-bottom: 1.2rem;
}
.hero-box h1 {
    margin: 0;
    font-size: 2.1rem;
    font-weight: 800;
    background: linear-gradient(90deg, #d9a441, #6fb58f, #8bbd62);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-box p {
    margin: 10px 0 0 0;
    color: #5d6b5d;
    font-size: 1rem;
}
 
.metric-card {
    background: rgba(255,255,255,0.93);
    border: 1px solid rgba(134,199,122,0.18);
    border-radius: 18px;
    padding: 18px 20px;
    box-shadow: 0 10px 22px rgba(60,80,50,0.06);
}
.metric-title { color: #6a7a69; font-size: 0.85rem; margin-bottom: 6px; }
.metric-value { font-size: 1.65rem; font-weight: 800; margin: 0; }
 
.panel-card {
    background: rgba(255,255,255,0.93);
    border: 1px solid rgba(134,199,122,0.16);
    border-radius: 22px;
    padding: 20px 18px 12px 18px;
    box-shadow: 0 10px 22px rgba(60,80,50,0.06);
    margin-bottom: 1.2rem;
}
.panel-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #1E2F1E;
    margin-bottom: 4px;
}
.panel-sub {
    font-size: 0.87rem;
    color: #6a7a69;
    margin-bottom: 12px;
}
 
.insight-box {
    background: linear-gradient(180deg, rgba(244,201,93,0.14), rgba(134,199,122,0.10));
    border: 1px solid rgba(134,199,122,0.22);
    border-radius: 18px;
    padding: 18px 20px;
    color: #334433;
    box-shadow: 0 10px 22px rgba(60,80,50,0.06);
}
.insight-box h3 { margin-top: 0; font-size: 1rem; color: #2a3b2a; }
.insight-box p  { font-size: 0.92rem; line-height: 1.65; }
 
.section-divider {
    border: none;
    border-top: 1px solid rgba(134,199,122,0.20);
    margin: 1.6rem 0 1.2rem 0;
}
</style>
""", unsafe_allow_html=True)
 
# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Dashboard")
    st.markdown("India's electricity generation mix analysis")
    st.markdown("---")
    st.markdown("**Plots on this page**")
    st.markdown("- Generation transition (area chart)")
    st.markdown("- Electricity composition (Sankey)")
    st.markdown("- Source-by-source growth (heatmap)")
    st.markdown("- Renewable share radial chart")
    st.markdown("---")
    st.caption("All generation values are in Billion Units (BU). Renewable sources include Hydro, Wind, Solar, Bio Power and Small-Hydro.")
 
# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-box">
    <h1>India's Electricity Generation Mix</h1>
    <p>Tracking how the energy basket has evolved — from fossil-heavy to a growing renewable share — across a decade of data.</p>
</div>
""", unsafe_allow_html=True)
 
# ─── DATA ─────────────────────────────────────────────────────────────────────
df = pd.DataFrame({
    "Year":      ["2015-16","2016-17","2017-18","2018-19","2019-20",
                  "2020-21","2021-22","2022-23","2023-24","2024-25","2025-26"],
    "Coal":      [896.3, 944, 986.6, 1022.3, 994.2, 981.44, 1078.58, 1182.1, 1294.85, 1331.87, 1162.11],
    "Oil & Gas": [47.5, 49.5, 50.6, 50, 48.61, 51.07, 36.13, 24.11, 31.7, 32.02, 24.83],
    "Nuclear":   [37.4, 37.9, 38.3, 37.8, 46.38, 43.03, 47.11, 45.86, 47.94, 56.68, 50.07],
    "Hydro":     [121.4, 122.4, 126.1, 134.9, 155.97, 150.3, 151.63, 162.1, 134.05, 148.63, 157.69],
    "Wind":      [33, 46, 52.7, 62, 64.64, 60.15, 68.64, 71.81, 83.39, 83.35, 100.21],
    "Solar":     [7.4, 13.5, 25.9, 39.3, 50.1, 60.4, 73.48, 102.01, 115.98, 144.15, 153.91],
    "Bio Power": [16.95, 14.44, 15.61, 16.75, 14.21, 16.44, 18.32, 18.55, 16.99, 15.94, 14.06],
    "Small-Hydro":[8.4, 7.9, 7.7, 8.7, 9.37, 10.26, 10.46, 11.17, 9.49, 11.57, 11.02],
    "Total":     [1168, 1236, 1304, 1372, 1383, 1373, 1484, 1618, 1734, 1824, 1674],
})
 
renewable     = ["Hydro", "Wind", "Solar", "Bio Power", "Small-Hydro"]
nonrenewable  = ["Coal", "Oil & Gas", "Nuclear"]
 
df["Renewable"]     = df[renewable].sum(axis=1)
df["Non-Renewable"] = df[nonrenewable].sum(axis=1)
df["RE %"]          = df["Renewable"] / df["Total"] * 100
 
# ─── KPI ROW ──────────────────────────────────────────────────────────────────
latest = df.iloc[-1]   # 2024-25 (last full year)
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-title">Total generation (2025-26)</div>
        <p class="metric-value" style="color:#2f4f3a;">{latest['Total']:.0f} BU</p>
    </div>""", unsafe_allow_html=True)
with k2:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-title">Renewable share (2025-26)</div>
        <p class="metric-value" style="color:#4f7942;">{latest['RE %']:.1f}%</p>
    </div>""", unsafe_allow_html=True)
with k3:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-title">Solar generation (2025-26)</div>
        <p class="metric-value" style="color:#8c6b1f;">{latest['Solar']:.0f} BU</p>
    </div>""", unsafe_allow_html=True)
with k4:
    re_growth = ((latest['Renewable'] - df.iloc[0]['Renewable']) / df.iloc[0]['Renewable']) * 100
    st.markdown(f"""<div class="metric-card">
        <div class="metric-title">RE growth since 2015-16</div>
        <p class="metric-value" style="color:#5a6b5a;">+{re_growth:.0f}%</p>
    </div>""", unsafe_allow_html=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════════════════════
# PLOT 1 — Generation Transition Area Chart
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
p1_left, p1_right = st.columns([2.2, 1])
 
with p1_left:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Electricity Generation Transition Over Years</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel-sub">Renewable vs Non-Renewable generation (BU) and total demand</div>', unsafe_allow_html=True)
 
    PLOTLY_LAYOUT = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color="#334433"),
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.05,
            xanchor="center", x=0.5,
            bgcolor="rgba(255,255,255,0.7)",
            bordercolor="rgba(134,199,122,0.3)",
            borderwidth=1,
        ),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=11, color="#4A5A49"),
            title=dict(text="Year", font=dict(size=12, color="#4A5A49")),
            linecolor="#D8E2D5",
        ),
        yaxis=dict(
            gridcolor="rgba(168,178,167,0.25)",
            gridwidth=1,
            tickfont=dict(size=11, color="#4A5A49"),
            title=dict(text="Generation (BU)", font=dict(size=12, color="#4A5A49")),
            zeroline=False,
        ),
    )
 
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df["Year"], y=df["Renewable"],
        mode="lines", name="Renewable",
        line=dict(color="#4F7942", width=3),
        fill="tozeroy", fillcolor="rgba(79,121,66,0.20)",
        hovertemplate="Year=%{x}<br>Renewable=%{y:.1f} BU<extra></extra>",
    ))
    fig1.add_trace(go.Scatter(
        x=df["Year"], y=df["Non-Renewable"],
        mode="lines", name="Non-Renewable",
        line=dict(color="#C5A059", width=3),
        fill="tozeroy", fillcolor="rgba(197,160,89,0.18)",
        hovertemplate="Year=%{x}<br>Non-Renewable=%{y:.1f} BU<extra></extra>",
    ))
    fig1.add_trace(go.Scatter(
        x=df["Year"], y=df["Total"],
        mode="lines+markers", name="Total Demand",
        line=dict(color="#1E2F1E", width=3, dash="dot"),
        marker=dict(size=7, symbol="diamond",
                    color="#ffffff", line=dict(color="#1E2F1E", width=2)),
        hovertemplate="Year=%{x}<br>Total=%{y:.1f} BU<extra></extra>",
    ))
    fig1.add_annotation(
        x="2022-23",
        y=float(df.loc[df["Year"] == "2022-23", "Renewable"].iloc[0]),
        text="RE rising fast ↑",
        showarrow=True, arrowhead=2, ax=30, ay=-38,
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor="rgba(79,121,66,0.4)", borderwidth=1,
        font=dict(size=11, color="#4F7942", family="Inter"),
    )
    fig1.add_annotation(
        x="2024-25",
        y=float(df.loc[df["Year"] == "2024-25", "Non-Renewable"].iloc[0]),
        text="Non-RE still climbs",
        showarrow=True, arrowhead=2, ax=-50, ay=38,
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor="rgba(197,160,89,0.4)", borderwidth=1,
        font=dict(size=11, color="#8c6b1f", family="Inter"),
    )
    fig1.update_layout(**PLOTLY_LAYOUT, height=360)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
 
with p1_right:
    st.markdown("""
    <div class="insight-box">
        <h3>Interpretation</h3>
        <p>
            Even as renewable generation has grown steadily, non-renewable output keeps climbing in absolute terms — driven by relentless demand growth.
        </p>
        <p>
            The reason shows up in the demand line. Overall energy demand is rising so quickly that both sources end up growing together.
        <p style="margin-bottom:0;">
            The real transition story is therefore about <strong>share</strong>, not absolute numbers — renewables must outpace demand growth to meaningfully shift the mix.
        </p>
    </div>
    """, unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════════════════════
# PLOT 2 — Sankey Composition Diagram
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
    <style>
    /* Hard‑override Plotly Sankey node label shadow */
    .sankey .node-label-text-path {
        text-shadow: none !important;
        stroke: none !important;
    }
    .sankey .node-labels {
        text-shadow: none !important;
    }
    .node-label-text-path {
        text-shadow: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
p2_left, p2_right = st.columns([1, 2.2])
 
with p2_right:
    # Use the beautified title group from before for consistency
    st.markdown('''
        <style>
            .radial-title-group { text-align: left; margin-bottom: -10px; }
            .panel-title-fixed {
                font-size: 1.05rem; font-weight: 850; color: #1E3018; margin: 0 !important;
            }
            .panel-sub-fixed {
                font-size: 0.78rem; font-weight: 600; color: #667766; margin: 0 !important;
            }
        </style>
        <div class="radial-title-group">
            <p class="panel-title-fixed">Electricity Composition — Flow Diagram</p>
            <p class="panel-sub-fixed">LATEST DATA (2025-26) </p>
        </div>
    ''', unsafe_allow_html=True)

    last = df[df["Year"] == "2025-26"].iloc[0]
    sources_list = ["Coal", "Oil & Gas", "Nuclear", "Hydro", "Wind", "Solar", "Bio Power", "Small-Hydro"]
    vals = [float(last[s]) for s in sources_list]
    labels = ["Total Electricity"] + sources_list # Removed \n for cleaner horizontal alignment
 
    node_colors = ["#1E2F1E", "#C5A059","#C5A059","#C5A059","#4F7942","#4F7942","#4F7942","#4F7942","#4F7942"]
    link_colors = ["rgba(197,160,89,0.15)"] * 3 + ["rgba(79,121,66,0.15)"] * 5
 
    fig2 = go.Figure(go.Sankey(
        arrangement="snap",
        node=dict(
            pad=25, thickness=15,
            line=dict(color="rgba(0,0,0,0)", width=0), # Removed node borders
            label=labels,
            color=node_colors,
        ),
        link=dict(
            source=[0] * len(sources_list),
            target=list(range(1, len(sources_list) + 1)),
            value=vals,
            color=link_colors,
        ),
    ))

    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        # FIX FOR THE TEXT SHADE:
        font=dict(family="Inter, sans-serif", size=11, color="#2a4f22"),
        margin=dict(l=5, r=60, t=40, b=10), # Added right margin to stop labels cutting off
        height=320,
    )

    # CRITICAL: This removes the "halo/shade" from the text
    fig2.update_traces(
        textfont=dict(color="#2a4f22"),
        # Setting the font style here prevents Plotly from adding an outline
        textfont_family="Inter",
        selector=dict(type='sankey')
    )

    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False}) 
with p2_left:
    st.markdown("""
    <div class="insight-box">
        <h3>Interpretation</h3>
        <p>
            Coal still dominates the picture by a wide margin — it makes up most of the total generation in 2025–26, far ahead of every other source.
        </p>
        <p>
            Among the non-coal sources, Solar and Hydro are now quite close, with Solar catching up fast and becoming one of the major contributors.
        </p>
        <p style="margin-bottom:0;">
            The rest — Wind, Nuclear, Oil & Gas, and others — add to the mix, but each of them is much smaller on its own compared to Coal.
        </p>
    </div>
    """, unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════════════════════
# PLOT 3 — Growth Heatmap
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
p3_left, p3_right = st.columns([2.2, 1])
 
with p3_left:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Source-by-Source Year-on-Year Growth (%)</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel-sub">Green = high growth · White = flat · Blue = decline</div>', unsafe_allow_html=True)
 
    all_sources = ["Hydro", "Wind", "Solar", "Bio Power", "Small-Hydro", "Coal", "Oil & Gas", "Nuclear"]
    pivot = df.set_index("Year")[all_sources]
    heat  = (pivot.pct_change() * 100).iloc[1:].round(1)
 
    fig3 = go.Figure(data=go.Heatmap(
        z=heat.values,
        x=heat.columns.tolist(),
        y=heat.index.tolist(),
        colorscale=[
            [0.0,  "#2A6099"],
            [0.35, "#A8C8E0"],
            [0.5,  "#F5F5F0"],
            [0.65, "#B8D4A8"],
            [1.0,  "#3E5F34"],
        ],
        zmid=0,
        colorbar=dict(
            title=dict(text="YoY %", font=dict(size=11, family="Inter", color="#4A5A49")),
            tickfont=dict(size=10, family="Inter", color="#4A5A49"),
            len=0.8,
        ),
        hovertemplate="Source: %{x}<br>Year: %{y}<br>Growth: %{z:.1f}%<extra></extra>",
        xgap=3, ygap=3,
    ))
    fig3.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color="#334433"),
        margin=dict(l=10, r=10, t=10, b=10),
        height=360,
        xaxis=dict(
            title=dict(text="Source", font=dict(size=12, color="#4A5A49")),
            tickfont=dict(size=11, color="#4A5A49"),
            side="bottom",
        ),
        yaxis=dict(
            title=dict(text="Year", font=dict(size=12, color="#4A5A49")),
            tickfont=dict(size=11, color="#4A5A49"),
            autorange="reversed",
        ),
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
 
with p3_right:
    st.markdown("""
    <div class="insight-box">
        <h3>Interpretation</h3>
        <p>
            Solar stands out as the most consistently strong performer — it shows steady positive growth across most years, even if the pace varies.
        </p>
        <p>
            Wind and Hydro don’t follow that same smooth pattern. Their growth goes up and down, with some weaker years, likely reflecting weather and seasonal dependence.
        </p>
        <p>
            Oil & Gas clearly struggles the most, with repeated negative phases, while Bio Power and Small Hydro remain inconsistent.
        </p>
        <p style="margin-bottom:0;">
            Coal, on the other hand, stays relatively stable — not high growth, but rarely dropping sharply, which shows its continued role as a steady base source.
        </p>
    </div>
    """, unsafe_allow_html=True)
 
# ══════════════════════════════════════════════════════════════════════════════
# PLOT 4 — Radial Renewable Share Chart
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
p4_left, p4_right = st.columns([1, 2.2])
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# 1. Change the ratio to [1, 1.5] to bring the two sides closer together
p4_left, p4_right = st.columns([1, 1.5])

with p4_left:
    latest_re = df["RE %"].iloc[-2]
    earliest_re = df["RE %"].iloc[0]
    st.markdown(f"""
    <div class="insight-box">
        <h3>Interpretation</h3>
        <p>
            The renewable share increases over the observed period, but the rate of change remains moderate.
        </p>
    </div>
    """, unsafe_allow_html=True)

with p4_right:
    # 2. CSS: Create a tight bundle that moves as one unit
    st.markdown("""
        <style>
            .radial-bundle {
                display: flex;
                flex-direction: column;
                align-items: flex-end; /* Shoves everything to the right edge */
                margin-top: -150px;    /* Pulls the whole group up */
                width: 100%;
            }
            .radial-title-group {
                text-align: right;    /* Aligns text to the right */
                margin-bottom: -20px; /* Pulls the chart closer to the text */
                padding-right: 20px;  /* Slight tweak for perfect alignment */
            }
            .panel-title-fixed { font-size: 1rem; font-weight: 800; color: #2a4f22; margin: 0; }
            .panel-sub-fixed { font-size: 0.75rem; color: #666; margin: 0; }
        </style>
    """, unsafe_allow_html=True)

    # 3. Wrap everything together
    st.markdown('<div class="radial-bundle">', unsafe_allow_html=True)
    
    st.markdown('''
        <style>
            .radial-title-group {
                text-align: right;
                padding-right: 10px;
                margin-bottom: -10px;
                font-family: sans-serif;
            }
            .panel-title-fixed {
                font-size: 1.1rem;
                font-weight: 850;
                background: linear-gradient(90deg, #4F7942, #2a4f22);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 0 !important;
                letter-spacing: -0.5px;
            }
            .panel-sub-fixed {
                font-size: 0.78rem;
                font-weight: 600;
                color: #667766;
                margin: 0 !important;
                opacity: 0.8;
                letter-spacing: 0.2px;
            }
        </style>
        <div class="radial-title-group">
            <p class="panel-title-fixed">Progressive Renewable Share</p>
            <p class="panel-sub-fixed">RADIAL VIEW • YEAR-ON-YEAR RE %</p>
        </div>
    ''', unsafe_allow_html=True)

    # Smaller figsize keeps it sharp and manageable
    fig4, ax4 = plt.subplots(figsize=(2.6, 2.5), dpi=140, subplot_kw=dict(polar=True))
    fig4.patch.set_facecolor("none")
    ax4.set_facecolor("none")
    ax4.axis("off")

    # [Data mapping remains same]
    labels_r = df["Year"].tolist()
    values_r = df["RE %"].tolist()
    n = len(labels_r)
    angles_r = np.linspace(0, 2 * np.pi, n, endpoint=False)
    lower = 14 
    norm = plt.Normalize(vmin=min(values_r) - 2, vmax=max(values_r) + 2)
    cmap = mcolors.LinearSegmentedColormap.from_list("sage_ramp", ["#a8c89a", "#4F7942", "#2a4f22"])
    
    ax4.bar(angles_r, values_r, width=(2*np.pi/n)*0.85, bottom=lower, 
            color=[cmap(norm(v)) for v in values_r], edgecolor="white", linewidth=0.8)
 
    for angle, height, label, value in zip(angles_r, values_r, labels_r, values_r):
        rotation = np.rad2deg(angle)
        alignment = "right" if 90 < rotation < 270 else "left"
        display_rot = rotation + 180 if 90 < rotation < 270 else rotation
        ax4.text(angle, lower + height + 2.5, f"{label}\n{value:.1f}%", 
                 ha=alignment, va="center", rotation=display_rot, 
                 rotation_mode="anchor", fontsize=5.5, fontweight="bold", color="#2a4f22")
 
    ax4.text(0, 0, "RE\nSHARE", ha="center", va="center", fontsize=8, fontweight="900", color="#2a4f22")
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9)
    
    st.pyplot(fig4, use_container_width=False) 
    st.markdown("</div>", unsafe_allow_html=True)
with p4_left:
    latest_re = df["RE %"].iloc[-1]
    earliest_re = df["RE %"].iloc[0]
    st.markdown(f"""
    <div class="insight-box">
        <p>
            The outer rings gradually extend further out, showing that the share of renewables has been increasing over time.
        </p>
        <p>
            It rises from <strong>{earliest_re:.1f}%</strong> in 2015-16 to <strong>{latest_re:.1f}%</strong> in 2025-26 — a steady shift rather than a sudden jump.
        </p>
        <p style="margin-bottom:0;">
            So even though total electricity demand is growing, renewables are slowly taking up a larger portion of the mix.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════════════════
# FINAL SECTION: REPORT & EXECUTIVE SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

st.markdown("""
<div class="hero-box" style="background: linear-gradient(135deg, #ffffff 0%, #f0f7ee 100%);">
    <h2 style="color: #1E2F1E; margin-top:0;">The Energy Pulse Analysis</h2>
</div>
""", unsafe_allow_html=True)

# Three-column "Key Takeaways"
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="panel-card" style="height: 100%;">
        <h4 style="color: #d9a441; margin-top:0;">1. The "Ambition Gap"</h4>
        <p style="font-size: 0.9rem;">
            Our <b>Actual vs. Expected</b> analysis reveals that installed capacity is growing faster than our ability to utilize it. 
            The persistent gap highlights that adding "Giga-Watts" on paper doesn't immediately solve the energy crisis without 
            better grid storage and transmission infrastructure.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="panel-card" style="height: 100%;">
        <h4 style="color: #4F7942; margin-top:0;">2. The Solar Surge</h4>
        <p style="font-size: 0.9rem;">
            The <b>Heatmap</b> and <b>Sankey</b> confirm Solar is no longer a "minority stakeholder." 
            It has moved from a negligible 7.4 BU in 2015 to nearly 154 BU in 2025-26. 
            It is the engine driving the RE % upward, even as Wind and Hydro remain volatile.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="panel-card" style="height: 100%;">
        <h4 style="color: #1E2F1E; margin-top:0;">3. The Coal Paradox</h4>
        <p style="font-size: 0.9rem;">
            Despite the <b>RE rising fast</b> annotations, Coal remains the titan of the mix. 
            While the <i>percentage</i> share of Renewables is improving, the <i>absolute</i> amount of 
            Coal generation hasn't dropped because total demand is rising so aggressively.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Final Conclusion Box
st.markdown(f"""
<div class="insight-box" style="border-left: 6px solid #4F7942; padding: 25px;">
    <h3 style="font-size: 1.3rem;">Conclusion: Moving from Mix to Mastery</h3>
    <p style="font-size: 1rem;">
        The data suggests that India is successfully diversifying its basket, with <b>Renewable growth since 2015-16 hitting +{re_growth:.0f}%</b>. 
        However, the "Transition" is not yet a "Replacement." For the next decade, the challenge shifts from 
        simply <i>building</i> more solar and wind to <i>optimizing</i> them—closing the efficiency gap 
        and ensuring that green energy can eventually handle the "Total Demand" line without the coal safety net.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)