# psych-prep 🧠🐍

**psych-prep** is a lightweight Python library designed to bridge the gap between behavioral research and data science. It automates the "Qualtrics Headache"—the tedious process of cleaning messy survey exports.

## Key Features
* **Triple-Header Ingestion:** Automatically skips Qualtrics metadata rows.
* **Method Chaining:** Clean your entire dataset in a single, readable block of code.
* **Auto-Reverser:** Effortlessly invert negatively phrased items.
* **Subscale Aggregator:** Generate composite scores (means/sums) with built-in validation.

## Quick Start
```python
from psych_prep.core import Survey

# Clean a survey in seconds
df = (Survey("qualtrics_data.csv")
      .filter_attention("Check_Q1", 1)
      .reverse_score(["Q2", "Q4"], scale_min=1, scale_max=5)
      .calculate_subscale("Anxiety_Total", ["Q1", "Q2", "Q3", "Q4"])
      .get_df())