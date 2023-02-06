import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

@st.cache
def load_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    return df

def main():
    st.title("Football Player Analytics Dashboard")
    
    player = st.text_input("Enter a player name")
    position = st.selectbox("Select a position", ["Forward", "Midfielder", "Defender", "Goalkeeper"])
    
    if player and position:
        fbref_url = f"https://fbref.com/en/players/{player.lower().replace(' ', '-')}/comps"
        markstat_url = f"https://markstats.club/player/{player.lower().replace(' ', '-')}/{position.lower()}"
        
        fbref_data = load_data(fbref_url)
        markstat_data = load_data(markstat_url)
        
        st.write("Fbref Data")
        st.write(fbref_data)
        
        st.write("Markstats Data")
        st.write(markstat_data)

if __name__ == "__main__":
    main()
