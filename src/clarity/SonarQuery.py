from dotenv import load_dotenv
import os
import httpx
from openai import OpenAI


load_dotenv()

pplx_api_key = os.getenv("PERPLEXITY_API_KEY")


def sonarquery(query: str, tone: str, research_mode: str):
  returned_response = ""
  citations_response = {}
  message_prompt: list = []
  client = OpenAI(api_key=pplx_api_key, base_url="https://api.perplexity.ai")
  
  if tone == "fun" and research_mode == "standard":
    message_prompt = [
      {
          "role": "system",
          "content": (
            f"""Generate a humorous and engaging story based on the topic '{query}'. 
            Use real-time data to inform the narrative, keeping the tone light-hearted and fun, suitable for a general audience.
            If the topic has financial implications, emphasize key financial insights in a creative, storytelling format.
            Provide citations for all sources used."""
          ),
      },
      {   
          "role": "user",
          "content": (
            f"""Tell a humorous and engaging story about {query}.
            Use real-time data to inform the narrative, keeping the tone light-hearted and fun for a general audience.
            If the topic has financial implications, highlight key financial insights in a creative, storytelling format.
            Include citations for all sources."""
          ),
      },
    ]
    # chat completion without streaming
    response = client.chat.completions.create(
      model="sonar-pro",
      messages=message_prompt,
    )
    returned_response = response.choices[0].message.content
    citations_response = response
  elif tone == "serious" and research_mode == "standard":
    message_prompt = [
      {
          "role": "system",
          "content": (
            f"""Generate a professional and concise story based on the topic '{query}'. 
            Use real-time data to inform the narrative, maintaining a serious and factual tone suitable for a business audience. 
            If the topic has financial implications, focus on key financial insights in a clear, narrative format. 
            Provide citations for all sources used."""
          ),
      },
      {   
          "role": "user",
          "content": (
            f"""Tell a professional and concise story about {query}. 
            Use real-time data to inform the narrative, maintaining a serious and factual tone for a business audience. 
            If the topic has financial implications, focus on key financial insights in a clear, narrative format. 
            Include citations for all sources."""
          ),
      },
    ]
    # chat completion without streaming
    response = client.chat.completions.create(
      model="sonar-pro",
      messages=message_prompt,
    )
    returned_response = response.choices[0].message.content
    citations_response = response
  elif tone == "fun" and research_mode == "deep":
    message_prompt = [
      {
          "role": "system",
          "content": (
            f"""Generate a humorous and engaging story based on the topic '{query}'. 
            Use Deep Research to perform an in-depth analysis, incorporating detailed insights from real-time data.
            Keep the tone light-hearted and fun, suitable for a general audience, and weave financial implications, if relevant, into a creative, storytelling format. 
            Provide citations for all sources used."""
          ),
      },
      {   
          "role": "user",
          "content": (
            f"""Tell a humorous and engaging story about {query}.
            Use Deep Research to perform an in-depth analysis with real-time data, keeping the tone light-hearted and fun for a general audience.
            If the topic has financial implications, weave detailed financial insights into a creative, storytelling format.
            Include citations for all sources."""
          ),
      },
    ]
    # chat completion without streaming
    response = client.chat.completions.create(
      model="sonar-deep-research",
      messages=message_prompt,
    )
    returned_response = response.choices[0].message.content
    citations_response = response
  elif tone == "serious" and research_mode == "deep":
    message_prompt = [
      {
          "role": "system",
          "content": (
            f"""Generate a professional and concise story based on the topic '{query}'.
            Use Deep Research to perform an in-depth analysis, incorporating detailed insights from real-time data.
            Maintain a serious and factual tone suitable for a business audience, emphasizing financial implications, if relevant, in a clear, narrative format. 
            Provide citations for all sources used."""
          ),
      },
      {   
          "role": "user",
          "content": (
            f"""Tell a professional and concise story about {query}.
            Use Deep Research to perform an in-depth analysis with real-time data, maintaining a serious and factual tone for a business audience.
            If the topic has financial implications, emphasize detailed financial insights in a clear, narrative format.
            Include citations for all sources."""
          ),
      },
    ]
     # chat completion without streaming
    response = client.chat.completions.create(
      model="sonar-deep-research",
      messages=message_prompt,
    )
    returned_response = response.choices[0].message.content
    citations_response = response
  
  return {
    "text": returned_response or "No results found",
    "citations": citations_response
  }
  