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
from .SonarQuery import sonarquery
from .SonarCodeQuery import sonarcodequery



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
  
  console = Console()
  
  error_message: str = ""
  wrong_code: str = ""
  
  if args.code_review:
    console.print("Input the error you are facing here(press Enter twice to submit)")
    error_message = get_multiline_input(console)
    console.print("Input the code causing the errors(press Enter twice to submit)")
    wrong_code = get_multiline_input(console)
    if not error_message.strip():
      return "Error: An error message must be provided."
  source_text: str = "";
  citations: list = []
  try:
    if args.code_review:
      with console.status(f"[green]Checking for fix to errors pasted...[/green]", spinner="dots"):
        source = sonarcodequery(research_mode, tone, error_message, wrong_code)
        source_text = source["text"]
        citations = source["citations"].citations
    else:
      with console.status(f"[green]Loading your query: {args.query}...[/green]", spinner="dots"):
        source = sonarquery(args.query, tone, research_mode)
        source_text = source["text"]
        citations = source["citations"].citations
    console.print(Panel(source_text, title="Clarity: Never leave your terminal", border_style="blue" if tone == "serious" else "green"))
    console.print("\n[bold]Sources:[/bold]")
    for sites in range(len(citations)):
      console.print(f"{sites+1} - {citations[sites]}")
  except Exception as e:
    console.print(f"[red]Error:[/red] {str(e)}")


if __name__ == "__main__":
    sys.exit(main())
