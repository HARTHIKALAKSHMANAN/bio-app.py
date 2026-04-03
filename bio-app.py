import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="AI Smart Bioreactor",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Look
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #00ff88; text-align: center;}
    .sub-header {font-size: 1.3rem; color: #a0a0a0;}
    .stMetric {background-color: #1e1e1e; padding: 15px; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("🧪 AI-Integrated Smart Bioreactor System")
st.markdown('<p class="sub-header">Waste-to-Biopolymer (PHA) Conversion Platform</p>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 System Overview",
    "📊 Live Dashboard",
    "🤖 AI Optimization",
    "⚙️ Process Simulation",
    "📈 Performance Analytics"
])

# ====================== SYSTEM OVERVIEW ======================
if page == "🏠 System Overview":
    st.header("System Architecture")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Our Proposed Solution
        An AI-integrated smart bioreactor that converts organic waste into biodegradable biopolymers (PHA) using microbial fermentation.
        """)
        
        st.subheader("Key Modules")
        modules = {
            "Waste Pre-processing Unit": "Segregates, shreds & forms slurry from food scraps and agricultural residues",
            "Smart Bioreactor Unit": "Controlled fermentation chamber with multiple sensors",
            "AI Control System": "Machine learning for real-time parameter optimization",
            "IoT & Cloud Platform": "Real-time monitoring and user dashboard"
        }
        
        for title, desc in modules.items():
            st.markdown(f"**{title}** — {desc}")
    
    with col2:
        st.image("https://via.placeholder.com/400x300/00ff88/000000?text=Smart+Bioreactor", use_column_width=True)
        st.caption("Conceptual Design of Smart Bioreactor")

    st.subheader("Working Principle")
    steps = [
        "1. Organic waste collection & pre-processing",
        "2. Slurry fed into the bioreactor",
        "3. Microbial digestion begins",
        "4. Sensors monitor temperature, pH, DO & gas levels",
        "5. AI analyzes data and auto-adjusts parameters",
        "6. PHA biopolymer is produced and extracted"
    ]
    for step in steps:
        st.markdown(f"✅ {step}")

    st.success("This system promotes circular economy by turning waste into valuable biodegradable plastic.")

# ====================== LIVE DASHBOARD ======================
elif page == "📊 Live Dashboard":
    st.header("Real-time Bioreactor Monitoring")
    
    col1, col2, col3, col4 = st.columns(4)
    
    temp = st.sidebar.slider("Temperature (°C)", 25, 45, 36)
    ph = st.sidebar.slider("pH Level", 5.0, 9.0, 7.0)
    feed_rate = st.sidebar.slider("Waste Feed Rate (g/h)", 0.0, 12.0, 4.0)
    oxygen = st.sidebar.slider("Dissolved Oxygen (%)", 0, 100, 65)
    
    # Simulated values
    biomass = 8.5 + (temp - 36) * 0.2 + (7 - ph) * 0.3
    pha_yield = 3.8 + (feed_rate * 0.6) * (oxygen / 80)
    
    with col1:
        st.metric("Temperature", f"{temp}°C", "Optimal")
    with col2:
        st.metric("pH", f"{ph:.1f}", "Neutral")
    with col3:
        st.metric("PHA Yield", f"{pha_yield:.2f} g/L", "↑ 12%")
    with col4:
        st.metric("Biomass", f"{biomass:.1f} g/L")
    
    # Production Graph
    hours = np.linspace(0, 72, 200)
    pha = 0.45 * feed_rate * (1 - np.exp(-0.055 * hours)) * (temp/37) * (1 - abs(ph-7)/8)
    biomass_data = 0.8 * (1 - np.exp(-0.07 * hours))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hours, y=pha, name="PHA Biopolymer", line=dict(color="#00ff88", width=4)))
    fig.add_trace(go.Scatter(x=hours, y=biomass_data, name="Biomass", line=dict(color="#4488ff")))
    
    fig.update_layout(
        title="Biopolymer Production Over Time (72 Hours)",
        xaxis_title="Time (hours)",
        yaxis_title="Concentration (g/L)",
        template="plotly_dark",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

# ====================== AI OPTIMIZATION ======================
elif page == "🤖 AI Optimization":
    st.header("🤖 AI Control & Optimization")
    st.markdown("The AI system continuously analyzes sensor data and suggests optimal conditions for maximum PHA yield.")
    
    if st.button("Run AI Optimization", type="primary"):
        with st.spinner("AI analyzing microbial kinetics..."):
            st.success("✅ AI Recommendation:")
            st.info("""
            **Optimal Settings for Maximum PHA Yield:**
            - Temperature: **36.2°C**
            - pH: **7.0**
            - Feed Rate: **4.5 g/h**
            - Dissolved Oxygen: **70%**
            
            Predicted PHA Yield: **4.85 g/L** (+28% improvement)
            """)
    
    st.subheader("Why these parameters?")
    st.markdown("""
    - Temperature 36.2°C → Optimal microbial growth rate  
    - Neutral pH → Best conditions for PHA accumulation  
    - Controlled feed rate → Prevents substrate inhibition  
    """)

# ====================== PROCESS SIMULATION ======================
elif page == "⚙️ Process Simulation":
    st.header("Process Flow Simulation")
    st.markdown("Step-by-step working of the smart bioreactor system")
    
    cols = st.columns(3)
    with cols[0]:
        st.subheader("Input")
        waste_type = st.selectbox("Waste Type", ["Food Scraps", "Agricultural Residues", "Mixed Organic Waste"])
        quantity = st.slider("Waste Quantity (kg)", 1, 100, 25)
        st.metric("Pre-processed Slurry", f"{quantity*0.85:.1f} kg")
    
    with cols[1]:
        st.subheader("Bioreactor")
        st.write("Microbial Digestion Active")
        st.progress(75)
    
    with cols[2]:
        st.subheader("Output")
        st.metric("PHA Produced", "4.2 kg", "per batch")
        st.metric("Conversion Efficiency", "68%", "↑")

# ====================== PERFORMANCE ANALYTICS ======================
elif page == "📈 Performance Analytics":
    st.header("Performance Analytics & Expected Outcomes")
    
    metrics = {
        "Waste Reduction": "85%",
        "PHA Conversion Efficiency": "62-75%",
        "CO₂ Emission Reduction": "92%",
        "Cost Savings (long term)": "40-55%"
    }
    
    cols = st.columns(2)
    for i, (k, v) in enumerate(metrics.items()):
        with cols[i % 2]:
            st.metric(k, v)

    st.success("This system contributes to a circular economy by transforming waste into valuable biodegradable plastics.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("AI-Integrated Smart Bioreactor\nDeveloped as Academic Project")
st.caption(f"Last updated: {datetime.now().strftime('%d %B %Y')} | Professional Dashboard")
