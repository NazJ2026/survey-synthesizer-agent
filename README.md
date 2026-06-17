# Survey Synthesizer Agent

## Problem Statement
Consultants and business analysts spend hours manually synthesising open-ended survey responses. This tool automates that process – reducing analysis time from hours to minutes.

**The Business Problem:**
- Manual synthesis is time-consuming and inconsistent
- Insights are often buried in unstructured text
- Senior decision-makers need rapid, actionable summaries

**My Solution:**
An AI agent that takes open-ended survey responses and produces executive-ready summaries with key themes, pain points, quick wins, and strategic recommendations.

---

## Technical Approach

### Agent Architecture (4-Step Pipeline)

1. **Data Ingestion:** Parse and clean text responses (CSV/JSON input)
2. **Theme Extraction:** Multi-turn Claude API call to identify recurring themes
3. **Frequency Weighting:** Score themes based on mention frequency
4. **Executive Summary Generation:** Produce structured output with confidence scores

### Tools & Frameworks

| Tool | Purpose |
|------|---------|
| **Claude API (Sonnet 3.5)** | Core LLM for theme extraction and summary generation |
| **Python** | Data processing, API orchestration |
| **Pandas** | Response parsing and frequency analysis |
| **Google Colab** | Rapid prototyping environment |
| **Jupyter Notebook** | Iterative development and testing |

### Prompt Engineering Iterations

| Version | Approach | Outcome |
|---------|----------|---------|
| **v1** | Basic prompt: "Find themes in these responses" | Outputs too broad and generic |
| **v2** | Added structure: "Identify 3-5 themes with example quotes" | Better, but no prioritisation |
| **v3** | Added confidence scoring and sub-themes | Outputs specific and actionable |
| **v4** | Added executive summary + quick wins | Outputs ready for senior stakeholders |

**Key Learning:** The most effective prompts explicitly ask for *frequency weighting* and *actionable recommendations* – not just themes.

---

## Sample Output

**Input:** 50 customer survey responses about their shopping experience


**Output:**
Customers are broadly satisfied with product quality and price, and many cite fast delivery and easy checkout as genuine strengths. However, recurring friction across website performance, delivery reliability, and post-purchase support is undermining loyalty — particularly on mobile. Addressing checkout and returns UX as quick wins, alongside a longer-term investment in mobile experience and logistics accountability, would meaningfully improve NPS and repeat purchase rate.

Here's the synthesised analysis across all 50 responses, formatted as a slide-ready brief.
A few standout signals worth flagging for any debrief:
The positive core is strong — product quality, competitive pricing, and fast delivery (when it works) generate genuine advocacy. Customers 9, 24, 30, 38, and 44 are effectively promoters.
The biggest reputational risk sits in post-purchase: stolen packages, wrong items, slow refunds, and rude agents are the types of experiences that drive public reviews. Customers 19, 21, 25, and 31 are all at churn or complaint risk.
The highest-effort, highest-return structural investment is the website — it's mentioned negatively by at least 7 customers across different symptoms (crashing, slow, confusing navigation, not mobile-friendly, cluttered checkout). That volume suggests a systemic issue rather than isolated edge cases.

### Prerequisites
- Python 3.9+
- Claude API key (get from Anthropic)
- Git (for cloning)

### Step-by-Step

1. **Clone the repository**
   ```bash
   git clone https://github.com/NazJ2026/survey-synthesizer-agent.git
   cd survey-synthesizer-agent
   pip install -r requirements.txt
