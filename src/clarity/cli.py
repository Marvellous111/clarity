import argparse
import json
import os
import sys
import textwrap
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
import httpx
from openai import OpenAI
from utils.SonarQuery import sonarquery

def sonar_query(word: str, tone: str, research_mode: str) -> str:
  """Fetches"""
  
  
  
  return f"{word}: {tone}, {research_mode}"

def sonar_code_query(code_review: str, research_mode: str, tone: str, error_message: str, code_message: str = "") -> str:
  return f"""
{code_review}: {tone}, {research_mode}\n
{error_message}: {code_message}
"""


def get_multiline_input(console):
  lines = []
  while True:
    line = console.input()
    if line == "":  # Empty line signals end of input
      if lines and lines[-1] == "":  # Two empty lines
        break
      lines.append("")
    else:
      lines.append(line)
  return "\n".join(lines).strip()

def main():
  """Fetches and prints according to the query and tags"""
  parser = argparse.ArgumentParser(description="Clarity: Ask clarity for anything and also debug your code with it.")
  parser.add_argument("query", type=str, help="Write what you want to search")
  parser.add_argument("--fun-mode", action="store_true", help="[green]Generate a humorous, engaging story[/green]")
  parser.add_argument("--serious-mode", action="store_true", help="[green]Generate a professional, serious story[/green]")
  parser.add_argument("--deep-research", action="store_true", help="[green]Use Deep Research for in-depth analysis[/green]")
  parser.add_argument("--code-review", action="store_true", help="[green]Check your code for errors when coding[/green]")
  args = parser.parse_args()
  
  tone = "serious" if args.serious_mode else "fun" if args.fun_mode else "serious"
  research_mode = "deep" if args.deep_research else "standard"
  code_review = "code-review" if args.code_review else ""
  
  console = Console()
  
  error_message: str = ""
  wrong_code: str = ""
  
  if args.code_review:
    console.print("Input the error you are facing here(press Enter twice to submit)")
    error_message = get_multiline_input(console)
    console.print("Input the code causing the errors(press Enter twice to submit)")
    wrong_code = get_multiline_input(console)
  
  try:
    if args.code_review:
      source = sonar_code_query(code_review, research_mode, tone, error_message, wrong_code)
    else:
      source = sonar_query(args.query, tone, research_mode)
    console.print(Panel(source, title="Clarity: Financial Story", border_style="blue" if tone == "serious" else "green"))
    console.print("\n[bold]Sources:[/bold]")
  except:
    console.print("Error")


if __name__ == "__main__":
    sys.exit(main())
