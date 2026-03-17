import pandas as pd
from psych_prep.core import Survey
import os

# 1. GENERATE A MESSY QUALTRICS CSV
data = {
    "ResponseID": ["R_1", "R_2", "R_3"],
    "Attention_Check": ["Pass", "Fail", "Pass"],
    "Anxiety_Q1": [5, 3, 1], # Let's say 5 is High Anxiety
    "Anxiety_Q2_Rev": [1, 2, 5] # This one needs reversing!
}

# Qualtrics has 2 extra rows of metadata
metadata_row1 = ["Response ID", "Check", "Question 1", "Question 2 (Reverse)"]
metadata_row2 = ["ID", "Logic", "Numeric", "Numeric"]

df_messy = pd.DataFrame(data)
# Add the metadata rows to the top
df_final = pd.DataFrame([metadata_row1, metadata_row2], columns=df_messy.columns)
df_final = pd.concat([df_final, df_messy], ignore_index=True)

# Save it
df_final.to_csv("qualtrics_mock.csv", index=False)
print("--- Messy CSV Created ---")

# 2. USE YOUR PACKAGE TO CLEAN IT
try:
    # Initialize the survey (skips those 2 metadata rows automatically!)
    study = Survey("qualtrics_mock.csv")
    
    # Filter out the person who failed the attention check
    study.filter_attention("Attention_Check", "Pass")
    
    # Reverse score Q2 (Assume it's a 1-5 scale)
    study.reverse_score(["Anxiety_Q2_Rev"], scale_min=1, scale_max=5)
    
    # Get the result
    clean_df = study.get_df()
    
    print("\n--- Cleaned Data ---")
    print(clean_df)
    
    # Cleanup the file
    os.remove("qualtrics_mock.csv")

except Exception as e:
    print(f"Error: {e}")