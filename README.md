# Clarity 🔍

Clarity is a command-line interface (CLI) tool designed to generate **engaging narrative stories** and **insightful code analyses** 📝 any topic, with a special focus on 💸 financial insights and 🐍 programming-related queries. Built for the Perplexity Hackathon 🏆, Clarity leverages the power of Perplexity AI's Sonar API 🚀 to deliver real-time, data-driven responses in either a 😄 fun or 😐 serious tone, with options for 🔍 deep research. Whether you're exploring financial trends like "Apple earning report 2025" 📊, analyzing code errors 🐛, or diving into topics like "climate change" 🌍, Clarity transforms complex information into accessible, story-driven narratives or detailed technical reviews.

## Features ✨

- **Narrative Stories** 📖: Generate stories for any topic, emphasizing financial insights when relevant, in 😄 fun or 😐 serious tones.
- **Code Analysis** 💻: Debug code by providing code snippets and error messages, with 😄 humorous or 😐 professional explanations and improvement suggestions.
- **Deep Research Mode** 🔍: Use Perplexity’s Deep Research for in-depth analysis, incorporating detailed real-time data.
- **Interactive Multiline Input** ⌨️: Enter multiline code snippets for debugging directly in the terminal.
- **Loading Animation** ⏳: Visual feedback with a spinner during API calls, powered by the `rich` library.
- **Customizable Output** 🎨: Choose between 😄 fun or 😐 serious tones, with clean, formatted output using `rich` panels.

## Integration with Perplexity AI 🤖

Clarity integrates Perplexity AI’s Sonar API to deliver real-time, data-driven responses. The Sonar API powers:
- **Real-Time Data** ⏱️: Fetches up-to-date information for narrative stories, ensuring accuracy for topics like financial reports or market trends.
- **Deep Research** 🔬: Provides in-depth analysis for complex queries, enhancing the detail in stories or code reviews.
- **Trusted Citations** 📚: Includes source citations in responses, aligning with Perplexity’s commitment to transparency.
- **Flexible Tones** 🎭: Supports 😄 fun or 😐 serious narrative styles, making outputs suitable for general or business audiences.

The API is accessed via the `openai` client, configured with a Perplexity API key 🔑, and used in two main functions:
- `sonar_query` 🔍: Generates stories for any topic, with a financial focus when applicable.
- `sonar_code_query` 💻: Analyzes code and error messages, offering fixes and improvements.

## Installation 🛠️

### Prerequisites 📋
- 🐍 Python 3.8+
- 🔑 A Perplexity API key (sign up at [Perplexity AI](https://www.perplexity.ai/))
- 📦 `uv` or `pip` package manager

### Steps 🚶‍♂️
1. **Clone the Repository** 
  ```bash
  git clone https://github.com/Marvellous111/clarity.git
  cd clarity
  ```

2. **Install Dependencies**
  ```bash
  uv pip install rich openai python-dotenv
  ```

3. **Set Up Environment Variable**
  ```bash
  echo "PERPLEXITY_API_KEY=your_api_key" > .env
  ```
