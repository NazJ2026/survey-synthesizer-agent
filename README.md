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

