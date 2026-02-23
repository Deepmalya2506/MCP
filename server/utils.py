# Helper functions or utilities to send request

import httpx
from typing import Any


async def make_req(url:str, USER_AGENT:str) -> dict[str,Any]|None:
    """Make a request to the NWS API with proper error handling."""
    headers={"User-Agent":USER_AGENT, "Accept":'application/geo+json'}
    async with httpx.AsyncClient() as client:
        try:
            reponse=await client.get(url,headers=headers, timeout=30.0)
            reponse.raise_for_status()
            return reponse.json()
        except Exception as e:
            print(f"Error: {e}")
            return None

def format_output(response:dict) -> str:
    """Format an alert feature into a readable string."""
    prop=response["properties"]
    return f"""
        Event: {prop.get("event", "Unknown")}   
        Area:{prop.get("areaDesc","Unknown")}
        Severity: {prop.get("severity", "Unknown")}
        Description: {prop.get("description", "No description available")}
        Instructions: {prop.get("instruction", "No specific instructions provided")}
    """

