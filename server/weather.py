from mcp.server.fastmcp import FastMCP
from server.utils import make_req, format_output
from typing import Any

# A MCP server comprises of 3 things - Resources, Tools, Prompts

#01. Initialize the MCP server
mcp=FastMCP('weather')

#02. Resources
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

#03. Tools
@mcp.tool()
async def fetch_report(state:str)->str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url=f"{NWS_API_BASE}/alerts/active/area/{state}"
    result=await make_req(url,USER_AGENT)

    if not result or "features" not in result:
        return "Unable to fetch alerts or no alerts found."
    
    if not result['features']:
        return "No active alerts for this state."
    
    alerts=[format_output(feature) for feature in result['features']]
    return "\n---\n".join(alerts)

@mcp.tool()
async def forecast(lat:float, long:float):
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    points_url = f"{NWS_API_BASE}/points/{lat},{long}"
    points_data = await make_req(points_url, USER_AGENT)

    if not points_data:
        return "Unable to fetch forecast data for this location."
    
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_req(forecast_url, USER_AGENT)

    if not forecast_data:
        return "Unable to fetch detailed forecast."
    
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
        {period["name"]}:
        Temperature: {period["temperature"]}°{period["temperatureUnit"]}
        Wind: {period["windSpeed"]} {period["windDirection"]}
        Forecast: {period["detailedForecast"]}
        """
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)