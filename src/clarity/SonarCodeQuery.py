from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

pplx_api_key = os.getenv("PERPLEXITY_API_KEY")

def sonarcodequery(research_mode: str, tone: str, error_message: str, code_message: str = ""):
  # if code_message and not code_review:
  #     return code_message or "Error: Code message provided but no code to review."

  message_prompt: list = []
  citations_response = []
  returned_response = ""
  client = OpenAI(api_key=pplx_api_key, base_url="https://api.perplexity.ai")

  code_section = f"Code (if any):\n```\n{code_message}\n```\n" if code_message.strip() else "No code provided.\n"

  if tone == "fun" and research_mode == "standard":
      message_prompt = [
        {
          "role": "system",
          "content": (
            f"""Analyze the provided error message and, if available, the code. Generate a humorous and engaging explanation of the error's cause, potential fixes, and any relevant code improvements. 
            Use real-time data or programming knowledge to inform the narrative, keeping the tone light-hearted and fun, suitable for a general audience. 
            Include citations for any external sources used. GO STRAIGHT TO THE POINT"""
          ),
        },
        {
          "role": "user",
          "content": (
            f"""{code_section}
            Error message: {error_message}\n
            Provide a humorous and engaging explanation of the error, its cause, and suggest fixes. If code is provided, analyze it for bugs or inefficiencies and suggest improvements. 
            Use real-time data or programming knowledge, keeping the tone light-hearted and fun for a general audience. 
            Include citations for any sources. GO STRAIGHT TO THE POINT"""
          ),
        },
      ]
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
          f"""Analyze the provided error message and, if available, the code. Generate a professional and concise explanation of the error's cause, potential fixes, and any relevant code improvements. 
          Use real-time data or programming knowledge to inform the narrative, maintaining a serious and factual tone suitable for a technical audience. 
          Include citations for any external sources used. GO STRAIGHT TO THE POINT"""
        ),
      },
      {
        "role": "user",
        "content": (
          f"""{code_section}
          Error message: {error_message}\n
          Provide a professional and concise explanation of the error, its cause, and suggest fixes. If code is provided, analyze it for bugs or inefficiencies and suggest improvements. 
          Use real-time data or programming knowledge, maintaining a serious and factual tone for a technical audience. 
          Include citations for any sources. GO STRAIGHT TO THE POINT"""
        ),
      },
    ]
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
          f"""Analyze the provided error message and, if available, the code. Generate a humorous and engaging explanation of the error's cause, potential fixes, and any relevant code improvements. 
          Use Deep Research to perform an in-depth analysis, incorporating detailed insights from real-time data or programming knowledge. 
          Keep the tone light-hearted and fun, suitable for a general audience. 
          Include citations for any external sources used. GO STRAIGHT TO THE POINT"""
        ),
      },
      {
        "role": "user",
        "content": (
          f"""{code_section}
          Error message: {error_message}\n
          Provide a humorous and engaging explanation of the error, its cause, and suggest fixes. If code is provided, analyze it for bugs or inefficiencies and suggest improvements. 
          Use Deep Research for an in-depth analysis with real-time data or programming knowledge, keeping the tone light-hearted and fun for a general audience. 
          Include citations for any sources. GO STRAIGHT TO THE POINT"""
        ),
      },
    ]
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
          f"""Analyze the provided error message and, if available, the code. Generate a professional and concise explanation of the error's cause, potential fixes, and any relevant code improvements. 
          Use Deep Research to perform an in-depth analysis, incorporating detailed insights from real-time data or programming knowledge. 
          Maintain a serious and factual tone suitable for a technical audience. 
          Include citations for any external sources used. GO STRAIGHT TO THE POINT"""
        ),
      },
      {
        "role": "user",
        "content": (
          f"""{code_section}
          Error message: {error_message}\n
          Provide a professional and concise explanation of the error, its cause, and suggest fixes. If code is provided, analyze it for bugs or inefficiencies and suggest improvements. 
          Use Deep Research for an in-depth analysis with real-time data or programming knowledge, maintaining a serious and factual tone for a technical audience. 
          Include citations for any sources. GO STRAIGHT TO THE POINT"""
        ),
      },
    ]
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