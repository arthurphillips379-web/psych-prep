# psych-prep

A lightweight Python library for cleaning survey data.

## Features
* **Triple-Header Ingestion:** Automatically handles Qualtrics metadata.
* **Method Chaining:** Clean datasets in a single, readable pipeline.
* **Auto-Reverser:** Invert negatively phrased items.
* **Subscale Aggregator:** Generate composite scores with validation.

## Quick Start
```python
from psych_prep.core import Survey

df = (Survey("data.csv")
      .filter_attention("Check_Q1", 1)
      .reverse_score(["Q2", "Q4"], scale_min=1, scale_max=5)
      .calculate_subscale("Anxiety_Total", ["Q1", "Q2", "Q3", "Q4"])
      .get_df())
```
