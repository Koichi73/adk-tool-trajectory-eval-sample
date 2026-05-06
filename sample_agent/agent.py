from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    return {"status": "success", "message": f"Today is sunny in {city}."}

def get_current_time() -> dict:
    return {"status": "success", "message": "The current time is 2:00 PM."}

def get_current_date() -> dict:
    return {"status": "success", "message": "Today's date is June 1, 2024."}

root_agent = Agent(
    model='gemini-flash-latest',
    name='weather_agent',
    instruction="Use the provided tools to answer user queries.",
    tools=[get_weather, get_current_time, get_current_date],
)
