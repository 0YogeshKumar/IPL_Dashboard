# pip install -r requirements.txt

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE SETUP
st.set_page_config(page_title="IPL Analytics", page_icon="🏏", layout="wide")
st.title("🏏 IPL Big Data Analytics (Mini-Project)")

# 2. SIDEBAR
st.sidebar.header("About This Project")
st.sidebar.info("This project was created for the 'Big Data Analytics' (BCS714D) course.")

st.sidebar.markdown("**Technologies Used:**")
st.sidebar.markdown("- **Google Colab** (Environment)")
st.sidebar.markdown("- **PySpark** (Cleaning & Analytics)")
st.sidebar.markdown("- **Streamlit** (Dashboard)")
st.sidebar.markdown("- **Plotly** (Visualization)")

# 3. LOAD DATA
try:
    df_winners = pd.read_csv("data/top_winners.csv")
    df_scorers = pd.read_csv("data/top_scorers.csv")
    df_wickets = pd.read_csv("data/top_wickets.csv")
    df_pom = pd.read_csv("data/top_pom.csv")
    df_season = pd.read_csv("data/matches_per_season.csv")
except FileNotFoundError:
    st.error("❌ CSV files not found. Please download the 5 files from Colab and place them in this folder.")
    st.stop()

# 4. ROW 1: TEAMS & BATTING
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Most Successful Teams")
    fig = px.bar(df_winners, x="winner", y="matches_won", color="winner", 
                 title="Matches Won by Team")
    # FIX: replaced use_container_width with width="stretch"
    st.plotly_chart(fig, width="stretch")

with col2:
    st.subheader("🏏 Top Run Scorers")
    fig = px.pie(df_scorers, names="batter", values="total_runs", hole=0.4,
                 title="Career Runs (Top 10)")
    # FIX: replaced use_container_width with width="stretch"
    st.plotly_chart(fig, width="stretch")

# 5. ROW 2: BOWLING & AWARDS (New!)
col3, col4 = st.columns(2)

with col3:
    st.subheader("🎯 Top Wicket Takers")
    fig = px.bar(df_wickets, x="bowler", y="total_wickets", color="bowler",
                 title="Career Wickets", color_discrete_sequence=px.colors.qualitative.Bold)
    # FIX: replaced use_container_width with width="stretch"
    st.plotly_chart(fig, width="stretch")

with col4:
    st.subheader("🎖️ Player of the Match Awards")
    fig = px.bar(df_pom, x="player_of_match", y="awards_won", color="player_of_match",
                 title="Most POM Awards", color_discrete_sequence=px.colors.qualitative.Vivid)
    # FIX: replaced use_container_width with width="stretch"
    st.plotly_chart(fig, width="stretch")

# 6. ROW 3: SEASON TREND
st.subheader("📅 Matches Played Per Season")
fig_season = px.line(df_season, x="season_year", y="matches_played", markers=True)
# FIX: replaced use_container_width with width="stretch"
st.plotly_chart(fig_season, width="stretch")

# 7. RAW DATA TOGGLE
with st.expander("View Raw Data Tables"):
    st.write("Top Scorers", df_scorers)
    st.write("Top Wickets", df_wickets)