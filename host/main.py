import streamlit as st
import requests

st.title("Weather MCP Client 🌦️")

option = st.selectbox("Choose query type:", ["Alerts by State", "Forecast by Coordinates"])

if option == "Alerts by State":
    state = st.text_input("Enter state code (e.g., CA, NY)")
    if st.button("Get Alerts"):
        resp = requests.get(f"http://localhost:8000/alerts/{state}")
        st.write(resp.json()["alerts"])

elif option == "Forecast by Coordinates":
    lat = st.number_input("Latitude", value=37.7749)
    lon = st.number_input("Longitude", value=-122.4194)
    if st.button("Get Forecast"):
        resp = requests.get(f"http://localhost:8000/forecast", params={"lat": lat, "lon": lon})
        st.write(resp.json()["forecast"])
