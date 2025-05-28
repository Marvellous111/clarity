from dotenv import load_dotenv
import os
import httpx
from openai import OpenAI


load_dotenv()

pplx_api_key = os.getenv("PERPLEXITY_API_KEY")


def sonarquery(query: str, tone: str, research_mode: str):
  if tone == "fun":
    messages = [
      {
          "role": "system",
          "content": (
            """Generate a humorous and engaging story based on the topic '{query}'.
            Use real-time data to inform the narrative, keeping the tone light-hearted and fun, suitable for a general audience.
            Include key financial insights in a creative, storytelling format, and provide citations for all sources used."""
          ),
      },
      {   
          "role": "user",
          "content": (
            "How many stars are in the universe?"
          ),
      },
    ]