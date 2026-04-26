
"""
India Renewable Energy Share Prediction Model
Streamlit App — full page layout, no sidebar
Run: streamlit run app.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import streamlit as st


st.markdown("""
<style>
/* Force all Plotly SVG text to dark */
.js-plotly-plot .plotly text {
    fill: #1A1A1A !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="India's Electricity Transition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

# ─────────────────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* Main App Background - Pale Beige/Cream */
.stApp {
    background-color: #F9F7F2;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #2D3436;
}

/* Hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 3rem 3rem; max-width: 1400px; }

/* Hero banner - Lush Earthy Gradient */
.hero {
    background: linear-gradient(135deg, #2D5A27 0%, #4A773C 60%, #76A36D 100%);
    border-radius: 20px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 10px 25px rgba(45, 90, 39, 0.2);
}
.hero h1 { font-size: 2.2rem; font-weight: 600; margin: 0 0 0.4rem 0; letter-spacing: -0.5px; }
.hero p  { font-size: 1rem; opacity: 0.9; margin: 0; font-weight: 300; }
.hero-badges { display: flex; gap: 10px; margin-top: 1.2rem; flex-wrap: wrap; }
.badge {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    color: white;
}

/* Section headers - Sage Green Border */
.section-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2D5A27;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    border-left: 5px solid #A2AD91;
    padding-left: 12px;
    margin: 2.5rem 0 1.2rem 0;
}

/* Metric cards - Clean White with Soft Shadows */
.metric-card {
    background: white;
    border: 1px solid #E0DCD3;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    transition: transform 0.2s ease;
}
.metric-card:hover { 
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.06); 
}
.metric-label { font-size: 0.8rem; color: #7F8C8D; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.4rem; }
.metric-value { font-size: 2.1rem; font-weight: 600; color: #2D3436; line-height: 1.1; }
.metric-accent { color: #2D5A27; }

/* Input Section - Pale Yellow/Sand */
.input-card {
    background: #FEF9E7;
    border: 1px solid #F1E5BC;
    border-radius: 12px;
    padding: 1.5rem;
}

/* Sliders - Forest Green */
.stSlider > div > div > div > div { background: #2D5A27 !important; }

/* Tab styling - Natural tones */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #E9E4D9;
    border-radius: 12px;
    padding: 6px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    font-size: 0.9rem;
    color: #5D6D7E;
    background: transparent;
    padding: 10px 24px;
}
.stTabs [aria-selected="true"] {
    background: white !important;
    color: #2D5A27 !important;
    font-weight: 600;
}

/* Stat Pill */
.stat-pill {
    background: #E9E4D9;
    border-radius: 10px;
    padding: 10px 18px;
    font-size: 0.85rem;
    color: #2D3436;
    border: 1px solid #D0C9B8;
}
.stat-pill span { font-weight: 600; color: #2D5A27; }

/* Divider */
.divider { height: 1px; background: #D0C9B8; margin: 2rem 0; }
</style>
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# DATA & MODELS
# ─────────────────────────────────────────────────────────────
@st.cache_data
def load_and_train():
    data = {
        'year':      [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
        'fiscal':    ['2015-16','2016-17','2017-18','2018-19','2019-20',
                      '2020-21','2021-22','2022-23','2023-24','2024-25','2025-26'],
        'total':     [1168,1236,1304,1372,1383,1373,1484,1618,1734,1824,1674],
        'solar':     [7.4,13.5,25.9,39.3,50.1,60.4,73.48,102.01,115.98,144.15,153.91],
        'wind':      [33.0,46.0,52.7,62.0,60.15,68.64,71.81,83.39,83.35,83.35,100.21],
        'hydro':     [129.8,130.3,133.8,165.34,160.56,162.09,173.27,171.59,143.54,160.20,157.69],
        'bio':       [16.95,14.44,15.61,16.75,14.21,16.44,18.32,16.99,15.94,14.06,14.06],
    }
    df = pd.DataFrame(data)
    # Capacity additions are in MW — convert to GW
    capacity_additions_MW = {
    'Wind':  [3423.05, 5502.37, 1865.23, 1480.97, 2117.79, 1503.30, 1110.53, 2275.55, 3253.38,4151.31,6057.02],
    'Solar': [3130.36, 5658.63, 9563.69, 6750.97, 6510.06, 5628.80, 12760.50, 12783.80, 15033.24,23832.87,44614.25],
    'SHP':   [218.11,  106.38,  105.95,  107.34,  90.01,  103.65,  62.09,  95.40,  58.95,97.30	,70.81],
    'Bio':   [364.09,  164.15,  528.60,  414.70,  97.00,  270.61, 59.69,  42.40,  107.34, 387.76 ,126.06],
    }

    # Cumulative capacity as of 2014 base (MW)
    base_MW = {'Wind': 23354.55, 'Solar':3993.53, 'SHP': 4055.36, 'Bio': 8306.77}

    # Build cumulative GW per year
    import numpy as np
    years = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
    cap_gw = {}
    for src in ['Wind','Solar','SHP','Bio']:
        cum_mw = base_MW[src]
        gw_list = []
        for addition in capacity_additions_MW[src]:
            cum_mw += addition
            gw_list.append(round(cum_mw / 1000, 2))   # ← MW to GW here
        cap_gw[src] = gw_list

    df['cap_solar'] = cap_gw['Solar']
    df['cap_wind']  = cap_gw['Wind']
    df['cap_hydro'] = cap_gw['SHP']
    df['cap_bio']   = cap_gw['Bio']
    # 2025-26 estimated as ~48.0 GW
    large_hydro_cap_gw = [42.78, 44.48, 45.29, 45.40, 45.70,46.21, 46.72, 46.85, 46.93, 47.73, 48.00]
    df['cap_hydro'] = large_hydro_cap_gw

    # NOW compute CUF — cap is already in GW, generation is in BU (billion kWh = GWh×1000)
    # BU = GWh/1000, so: CUF = BU / (GW × 8.76)  ← units are consistent
    df['cuf_solar'] = df['solar'] / (df['cap_solar'] * 8.76)
    df['cuf_wind']  = df['wind']  / (df['cap_wind']  * 8.76)
    df['cuf_hydro'] = df['hydro'] / (df['cap_hydro'] * 8.76)
    df['cuf_bio']   = df['bio']   / (df['cap_bio']   * 8.76)
    

    
    for src, cap in [('solar','cap_solar'),('wind','cap_wind'),
                     ('hydro','cap_hydro'),('bio','cap_bio')]:
        df[f'cuf_{src}'] = df[src] / (df[cap] * 8.76)

    X = df[['year']].values
    dem_m   = LinearRegression().fit(X, df['total'].values)
    dem_r2  = r2_score(df['total'].values, dem_m.predict(X))
    dem_rmse= np.sqrt(mean_squared_error(df['total'].values, dem_m.predict(X)))

    CUF_CAPS   = {'solar':0.30,'wind':0.40,'hydro':0.55,'bio':0.30}
    CUF_FLOORS = {'solar':0.10,'wind':0.15,'hydro':0.25,'bio':0.10}
    cuf_models, cuf_stats = {}, {}
    for src in ['solar','wind','hydro','bio']:
        y_c = df[f'cuf_{src}'].values
        m   = LinearRegression().fit(X, y_c)
        cuf_models[src] = m
        cuf_stats[src]  = {
            'r2':    round(r2_score(y_c, m.predict(X)), 3),
            'slope': round(m.coef_[0]*100, 3),
            'rmse':  round(np.sqrt(mean_squared_error(y_c, m.predict(X)))*100, 3),
        }
    return df, dem_m, dem_r2, dem_rmse, cuf_models, cuf_stats, CUF_CAPS, CUF_FLOORS

df, dem_m, dem_r2, dem_rmse, cuf_models, cuf_stats, CUF_CAPS, CUF_FLOORS = load_and_train()

COLORS = {'solar':'#EF9F27','wind':'#1D9E75','hydro':'#378ADD','bio':'#D85A30'}
PLOTLY_LAYOUT = dict(
    font_family="DM Sans",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=50, b=40, l=50, r=20),
    xaxis=dict(showgrid=False, linecolor='#e8edf2'),
    yaxis=dict(gridcolor='#f0f4f8', linecolor='#e8edf2'),
)

def project_demand(year):
    return float(dem_m.predict([[year]])[0])

def project_cuf(src, year):
    raw = float(cuf_models[src].predict([[year]])[0])
    return float(np.clip(raw, CUF_FLOORS[src], CUF_CAPS[src]))

def predict(year, s_gw, w_gw, h_gw, b_gw):
    demand = project_demand(year)
    cuf    = {s: project_cuf(s, year) for s in ['solar','wind','hydro','bio']}
    gen    = {
        'solar': s_gw * cuf['solar'] * 8.76,
        'wind':  w_gw * cuf['wind']  * 8.76,
        'hydro': h_gw * cuf['hydro'] * 8.76,
        'bio':   b_gw * cuf['bio']   * 8.76,
    }
    re_total = sum(gen.values())
    return {'demand':demand,'cuf':cuf,'gen':gen,
            're_total':re_total,'re_pct':min(re_total/demand*100,100)}

# ─────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>⚡ India Renewable Energy Share Model</h1>
  <p>Demand forecast via linear regression · CUF projected per source · Data: CEA & MNRE (2015–16 to 2024–25)</p>
  <div class="hero-badges">
    <span class="badge">Linear Regression</span>
    <span class="badge">Trend-based CUF</span>
    <span class="badge">Solar · Wind · Hydro · Biomass</span>
    <span class="badge">10 years of data</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# INPUTS — full page, 5 columns
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Model Inputs</div>', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    year     = st.slider("📅 Target Year",    2026, 2035, 2030, step=1)
with c2:
    solar_gw = st.slider("☀️ Solar (GW)",      0,   600,  280,  step=5)
with c3:
    wind_gw  = st.slider("💨 Wind (GW)",       0,   250,  100,  step=5)
with c4:
    hydro_gw = st.slider("💧 Hydro (GW)", 44.0, 55.0, 48.0, step=0.5)
with c5:
    bio_gw   = st.slider("🌿 Biomass (GW)",    5,    20,   11,  step=1)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# PREDICT
# ─────────────────────────────────────────────────────────────
res = predict(year, solar_gw, wind_gw, hydro_gw, bio_gw)




# ─────────────────────────────────────────────────────────────
# KPI METRICS
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Prediction Results</div>', unsafe_allow_html=True)

m1, m2, m3, m4, m5, m6 = st.columns(6)
kpis = [
    (m1, "Predicted Demand",  f"{res['demand']:.0f}", "BU",  ""),
    (m2, "RE Generation",     f"{res['re_total']:.0f}","BU", ""),
    (m3, "RE Share",          f"{res['re_pct']:.1f}",  "%",  "metric-accent"),
    (m4, "Non-RE Generation", f"{res['demand']-res['re_total']:.0f}", "BU", ""),
    (m5, "Demand Model R²",   f"{dem_r2:.4f}",         "",   ""),
    (m6, "Demand Slope",      f"{dem_m.coef_[0]:.1f}", "BU/yr", ""),
]
for col, label, val, unit, extra_cls in kpis:
    with col:
        st.markdown(f"""
        <div class="metric-card">
          <div class="metric-label">{label}</div>
          <div class="metric-value {extra_cls}">{val}<span style="font-size:1rem;font-weight:400;color:#6b7c93"> {unit}</span></div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Projected CUF row
st.markdown('<div class="section-title">Projected CUF for {}</div>'.format(year), unsafe_allow_html=True)
cuf_cols = st.columns(4)
cuf_info = [
    ("☀️ Solar",   res['cuf']['solar'],  '#EF9F27', '#FFF8EC'),
    ("💨 Wind",    res['cuf']['wind'],   '#1D9E75', '#EDFAF4'),
    ("💧 Hydro",   res['cuf']['hydro'],  '#378ADD', '#EBF4FF'),
    ("🌿 Biomass", res['cuf']['bio'],    '#D85A30', '#FFF0EB'),
]
for col, (label, cuf_val, color, bg) in zip(cuf_cols, cuf_info):
    with col:
        src = label.split()[1]
        gen_key = "bio" if src == "Biomass" else src.lower()
        gen_val = res['gen'][gen_key]
        st.markdown(f"""
        <div class="metric-card" style="border-left: 4px solid {color}; background:{bg};">
          <div class="metric-label">{label}</div>
          <div class="metric-value" style="color:{color}">{cuf_val*100:.1f}%</div>
          <div class="metric-sub">{gen_val:.0f} BU generated · {gen_val/res['demand']*100:.1f}% of demand</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📈  Forecast Charts", "⚙️  CUF Trends", "📋  Historical Data", "🔢  Model Statistics"])

# ── TAB 1: FORECAST ──────────────────────────────────────────
with tab1:
    left, right = st.columns([3, 2])

    with left:
        # Main line chart
        hist_yrs  = list(df['year'])
        future_yrs= list(range(2016, year+1))
        hist_re   = (df['solar']+df['wind']+df['hydro']+df['bio']).round(1).tolist()

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=hist_yrs, y=list(df['total']),
            mode='lines+markers', name='Total generation (actual)',
            line=dict(color='#378ADD', width=2.5), marker=dict(size=7),
        ))
        fig.add_trace(go.Scatter(
            x=future_yrs, y=[round(project_demand(y),1) for y in future_yrs],
            mode='lines', name='Demand (regression)',
            line=dict(color='#185FA5', dash='dash', width=1.8),
        ))
        fig.add_trace(go.Scatter(
            x=hist_yrs, y=hist_re,
            mode='lines+markers', name='RE generation (actual)',
            line=dict(color='#1D9E75', width=2.5), marker=dict(size=7),
        ))
        proj_yrs = list(range(max(hist_yrs)+1, year+1))
        if proj_yrs:
            proj_re = [round(predict(y,solar_gw,wind_gw,hydro_gw,bio_gw)['re_total'],1)
                       for y in proj_yrs]
            fig.add_trace(go.Scatter(
                x=[max(hist_yrs)]+proj_yrs, y=[hist_re[-1]]+proj_re,
                mode='lines', name='RE generation (projected)',
                line=dict(color='#0F6E56', dash='dot', width=2),
            ))
        # Prediction point
        fig.add_trace(go.Scatter(
            x=[year], y=[round(res['re_total'],1)],
            mode='markers', name=f'{year} prediction',
            marker=dict(color='#D85A30', size=12, symbol='star'),
        ))
        fig.update_layout(
            **PLOTLY_LAYOUT,
            title=dict(text="Electricity Demand & RE Generation", font=dict(size=14, color='#0a2540')),
            xaxis_title="Year", yaxis_title="BU",
            legend=dict(orientation='h', y=-0.25, font=dict(size=11)),
            height=380,
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        # Donut
        fig_d = go.Figure(go.Pie(
            labels=['Solar','Wind','Hydro','Biomass','Non-RE'],
            values=[round(res['gen']['solar'],1), round(res['gen']['wind'],1),
                    round(res['gen']['hydro'],1), round(res['gen']['bio'],1),
                    round(res['demand']-res['re_total'],1)],
            hole=0.6,
            marker_colors=[COLORS['solar'],COLORS['wind'],COLORS['hydro'],COLORS['bio'],'#DDE3EA'],
            textinfo='label+percent', textfont_size=12,
        ))
        fig_d.update_layout(
            **PLOTLY_LAYOUT,
            title=dict(text=f"Generation Mix — {year-1}-{str(year)[2:]}", font=dict(size=14,color='#0a2540')),
            showlegend=False, height=380,
            annotations=[dict(text=f"<b>{res['re_pct']:.1f}%</b><br>RE", x=0.5, y=0.5,
                              font_size=16, showarrow=False, font_color='#0a2540')]
        )
        st.plotly_chart(fig_d, use_container_width=True)

    # Stacked bar breakdown
    src_keys = ['solar','wind','hydro','bio']
    fig_stack = go.Figure()
    for src in src_keys:
        fig_stack.add_trace(go.Bar(
            name=src.capitalize(), x=[f"{year-1}-{str(year)[2:]}"],
            y=[round(res['gen'][src],1)],
            marker_color=COLORS[src], text=[f"{res['gen'][src]:.0f} BU"],
            textposition='inside', insidetextfont=dict(color='white', size=12),
        ))
    fig_stack.add_trace(go.Bar(
        name='Non-RE', x=[f"{year-1}-{str(year)[2:]}"],
        y=[round(res['demand']-res['re_total'],1)],
        marker_color='#DDE3EA', text=[f"{res['demand']-res['re_total']:.0f} BU"],
        textposition='inside', insidetextfont=dict(color='#6b7c93', size=12),
    ))
    fig_stack.update_layout(
    **PLOTLY_LAYOUT,
    barmode='stack',
    title=dict(text="Generation Breakdown (BU)", font=dict(size=14,color='#0a2540')),
    height=280, showlegend=True,
    legend=dict(orientation='h', y=-0.25, font=dict(size=11)),
    yaxis_title="BU",
)
    st.plotly_chart(fig_stack, use_container_width=True)

# ── TAB 2: CUF TRENDS ────────────────────────────────────────
with tab2:
    future_range = list(range(2016, 2036))
    src_list = [
        ('solar','☀️ Solar'),('wind','💨 Wind'),
        ('hydro','💧 Hydro'),('bio','🌿 Biomass'),
    ]
    col_a, col_b = st.columns(2)
    for i, (src, label) in enumerate(src_list):
        col = col_a if i % 2 == 0 else col_b
        with col:
            actual = list(df[f'cuf_{src}'].values * 100)
            trend  = [np.clip(cuf_models[src].predict([[y]])[0],
                              CUF_FLOORS[src], CUF_CAPS[src])*100
                      for y in future_range]
            proj_y = project_cuf(src, year)*100

            fc = go.Figure()
            fc.add_trace(go.Scatter(
                x=list(df['year']), y=actual, mode='lines+markers',
                name='Actual', line=dict(color=COLORS[src], width=2.5),
                marker=dict(size=7),
            ))
            fc.add_trace(go.Scatter(
                x=future_range, y=trend, mode='lines', name='Trend (clipped)',
                line=dict(color=COLORS[src], dash='dash', width=1.5, ),
            ))
            fc.add_hline(y=CUF_CAPS[src]*100, line_dash='dot', line_color='#aaa',
                         annotation_text=f"Cap {CUF_CAPS[src]*100:.0f}%",
                         annotation_position="top right", annotation_font_size=10)
            fc.add_hline(y=CUF_FLOORS[src]*100, line_dash='dot', line_color='#aaa',
                         annotation_text=f"Floor {CUF_FLOORS[src]*100:.0f}%",
                         annotation_position="bottom right", annotation_font_size=10)
            fc.add_trace(go.Scatter(
                x=[year], y=[proj_y], mode='markers', name=f'{year}',
                marker=dict(color=COLORS[src], size=11, symbol='diamond',
                            line=dict(color='white', width=2)),
            ))
            fc.update_layout(
                **PLOTLY_LAYOUT,
                title=dict(
                    text=f"{label} CUF  |  R²={cuf_stats[src]['r2']:.3f}  "
                         f"slope={cuf_stats[src]['slope']:+.3f}%/yr",
                    font=dict(size=13, color='#0a2540')
                ),
                yaxis_title="CUF (%)", xaxis_title="Year",
                showlegend=False, height=290,
            )
            st.plotly_chart(fc, use_container_width=True)

    st.markdown("**CUF regression summary**")
    stats_df = pd.DataFrame([{
        'Source': s.capitalize(),
        'R²': cuf_stats[s]['r2'],
        'Slope (%/yr)': cuf_stats[s]['slope'],
        'RMSE (%)': cuf_stats[s]['rmse'],
        'Floor (%)': CUF_FLOORS[s]*100,
        'Cap (%)': CUF_CAPS[s]*100,
        f'Projected CUF {year} (%)': round(project_cuf(s, year)*100, 2),
    } for s in ['solar','wind','hydro','bio']])
    st.dataframe(stats_df, use_container_width=True, hide_index=True)

# ── TAB 3: HISTORICAL DATA ───────────────────────────────────
with tab3:
    hist_df = df[['fiscal','total','solar','wind','hydro','bio',
                  'cuf_solar','cuf_wind','cuf_hydro','cuf_bio']].copy()
    hist_df['RE Total (BU)'] = (hist_df['solar']+hist_df['wind']+hist_df['hydro']+hist_df['bio']).round(1)
    hist_df['RE Share (%)']  = (hist_df['RE Total (BU)']/hist_df['total']*100).round(2)
    for c in ['cuf_solar','cuf_wind','cuf_hydro','cuf_bio']:
        hist_df[c] = (hist_df[c]*100).round(2)
    hist_df.columns = ['Fiscal Year','Total BU','Solar BU','Wind BU','Hydro BU','Bio BU',
                        'CUF Solar %','CUF Wind %','CUF Hydro %','CUF Bio %',
                        'RE Total BU','RE Share %']
    st.dataframe(hist_df, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        fig_re = px.bar(hist_df, x='Fiscal Year', y='RE Share %',
                        text='RE Share %', color='RE Share %',
                        color_continuous_scale=['#9FE1CB','#1D9E75','#085041'])
        fig_re.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_re.update_layout(**PLOTLY_LAYOUT,
                             title=dict(text='Historical RE Share (%)', font=dict(size=13,color='#0a2540')),
                             showlegend=False, coloraxis_showscale=False,
                             height=320, xaxis_tickangle=45)
        st.plotly_chart(fig_re, use_container_width=True)

    with col2:
        fig_s = go.Figure()
        for src in ['solar','wind','hydro','bio']:
            fig_s.add_trace(go.Scatter(
                x=list(df['fiscal']), y=list(df[src]),
                mode='lines+markers', name=src.capitalize(),
                line=dict(color=COLORS[src], width=2), marker=dict(size=5),
            ))
        fig_s.update_layout(**PLOTLY_LAYOUT,
                            title=dict(text='Source-wise Generation (BU)', font=dict(size=13,color='#0a2540')),
                            height=320, xaxis_tickangle=45,
                            legend=dict(orientation='h', y=-0.3))
        st.plotly_chart(fig_s, use_container_width=True)

# ── TAB 4: MODEL STATS ───────────────────────────────────────
with tab4:
    st.markdown("**Demand Regression**")
    st.markdown(f"""
    <div class="stat-row">
      <div class="stat-pill">Equation: <span>Total = {dem_m.coef_[0]:.2f} × Year + ({dem_m.intercept_:.0f})</span></div>
      <div class="stat-pill">R²: <span>{dem_r2:.4f}</span></div>
      <div class="stat-pill">RMSE: <span>{dem_rmse:.1f} BU</span></div>
      <div class="stat-pill">Slope: <span>{dem_m.coef_[0]:.2f} BU/yr</span></div>
    </div>
    """, unsafe_allow_html=True)

    # Residuals chart
    resid_df = df[['fiscal','total']].copy()
    resid_df['predicted'] = dem_m.predict(df[['year']].values).round(1)
    resid_df['residual']  = (resid_df['total'] - resid_df['predicted']).round(1)
    fig_r = px.bar(resid_df, x='fiscal', y='residual',
                   color='residual',
                   color_continuous_scale=['#D85A30','#f5f5f5','#1D9E75'],
                   color_continuous_midpoint=0, text='residual',
                   labels={'fiscal':'Fiscal Year','residual':'Residual (BU)'})
    fig_r.update_traces(texttemplate='%{text:+.1f}', textposition='outside')
    fig_r.update_layout(**PLOTLY_LAYOUT,
                        title=dict(text='Demand Regression Residuals (Actual − Predicted)',
                                   font=dict(size=13,color='#0a2540')),
                        coloraxis_showscale=False, height=300, xaxis_tickangle=45)
    st.plotly_chart(fig_r, use_container_width=True)

    st.markdown("**CUF Trend Regressions**")
    for src in ['solar','wind','hydro','bio']:
        m = cuf_models[src]
        st.markdown(f"""
        <div class="stat-pill" style="margin-bottom:8px; display:inline-block; margin-right:8px;">
          <b>{src.capitalize()}</b>: CUF = <span>{m.coef_[0]*100:+.4f}%</span> × Year + ({m.intercept_*100:.2f}%)
          &nbsp;|&nbsp; R²: <span>{cuf_stats[src]['r2']}</span>
          &nbsp;|&nbsp; Slope: <span>{cuf_stats[src]['slope']:+.3f}%/yr</span>
        </div>
        """, unsafe_allow_html=True)