import streamlit as st
import pandas as pd
import swehockey.swehockey_scraper as swe

st.set_page_config(page_title="Swehockey Game Viewer", layout="wide")
st.title("📅 Swehockey Game Schedule")

# Load schedule IDs
@st.cache_data
def load_schedule_ids():
    try:
        # Load from GitHub as fallback
        #return pd.read_csv("https://raw.githubusercontent.com/msjoelin/swehockey_scraper/master/data/scheduleid.csv", dtype=str)
        return pd.read_csv("./scheduleid.csv",
                               dtype=str)
    except:
        st.error("Failed to load schedule IDs.")
        return pd.DataFrame()

df_swehockey = load_schedule_ids()

if df_swehockey.empty:
    st.stop()

# Dropdown to choose a league/season
schedule_id = st.selectbox("Select a schedule (league/season):",
                           options=df_swehockey,
                           format_func=lambda x: df_swehockey.loc[df_swehockey['schedule_id'] == x, 'league'].values[0] + " " + df_swehockey.loc[df_swehockey['schedule_id'] == x, 'season'].values[0] if 'season' in df_swehockey.columns else x)

st.text("schedule ID: " + schedule_id)
# Fetch games for the selected schedule
if schedule_id:
    with st.spinner("Fetching games..."):
        #games_df = swe.getGames(df_swehockey['schedule_id'])
        df = df_swehockey['schedule_id'][df_swehockey['schedule_id'] == schedule_id]
        games_df = swe.getGames(df)

    if games_df is not None and not games_df.empty:
        st.success(f"Showing {len(games_df)} games.")
        st.dataframe(games_df)
    else:
        st.warning("No games found or invalid schedule ID.")