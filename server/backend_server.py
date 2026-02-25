from fastapi import FastAPI
from server.weather import  fetch_report, forecast

app=FastAPI()

@app.get("/alerts/{state}")
async def get_alerts(state:str)->dict:
    """Endpoint of weather reports to fetch data with State name as input"""
    result=await fetch_report(state)
    return {"alerts":result}

@app.get("/forecast")
async def weath_forecast(lat:float, long:float)->dict:
    """Endpoint where user can get the forecast by entering his latitude and longitude"""
    result= await forecast(lat, long)
    return {"forecast":result}

