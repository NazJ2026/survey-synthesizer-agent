import os
import pandas as pd
from anthropic import Anthropic
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()

# Initialize the Claude client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def synthesise_surveys(responses_text):
    """
    Sends survey responses to Claude and returns the synthesised analysis.
    """
    # Your system prompt from the README
    system_prompt = """You are an AI Survey Analyst. Your role is to synthesise open-ended survey responses and produce insight-led summaries.

For each batch of survey responses provided:

1. KEY THEMES – Identify 3-5 recurring themes across responses
2. PAIN POINTS – List the most frequently mentioned challenges
3. QUICK WINS – Identify 3-5 actionable improvements that could be implemented quickly
4. LONG-TERM OPPORTUNITIES – Identify 2-3 strategic recommendations
5. EXECUTIVE SUMMARY – 2-3 sentences summarising the overall sentiment

Be specific. Use frequency scoring (e.g., "mentioned by 42% of respondents") where possible.
Format your response as a clear, structured summary suitable for a senior decision-maker."""

    # The user message containing the data
    user_prompt = f"Here are the survey responses to analyse:\n\n{responses_text}"

    # Send the request to Claude
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    return message.content[0].text

# --- Main execution ---
if __name__ == "__main__":
    # Load your survey data (ensure this file exists)
    try:
        # Assuming you have a CSV with a column called 'response'
        df = pd.read_csv("responses.csv")
        all_responses = "\n".join(df['response'].astype(str).tolist())
    except FileNotFoundError:
        # If you don't have a CSV file, run the dummy data below
        print("No responses.csv found. Using built-in dummy data...")
        # Your 50 dummy responses here (trimmed for space)
        all_responses = """
        Customer 1: "Love the product quality but delivery took 5 days longer..."
        Customer 2: "Great customer service when I called..."
        Customer 3: "The checkout process was confusing..."
        # ... (paste all 50 responses here)
        """

    # Get the analysis
    summary = synthesise_surveys(all_responses)
    print(summary)
