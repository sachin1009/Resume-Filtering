
#CODE INPUT 
import pandas as pd




# Load the dataset
url = "https://docs.google.com/spreadsheets/d/1-ASvJPaCKl_t4eN8LxJL-MrtI62PMvz5/export?format=csv"
df = pd.read_csv(url)




criteria_weights = {
    "Python (out of 3)": 1,
    "Machine Learning (out of 3)": 2,
    "Natural Language Processing (NLP) (out of 3)": 1.5,
    "Deep Learning (out of 3)": 2,
    # Add more criteria with respective weights
}


# Calculate intern scores
df["Score"] = df[list(criteria_weights.keys())].mul(list(criteria_weights.values())).sum(axis=1)


# Rank the interns based on their scores
df = df.sort_values(by="Score", ascending=False)


# Select the top 10 candidates
top_candidates = df.head(10)


# Write top candidates to a file
top_candidates.to_csv("top_candidates.csv", index=False)


minimum_score = 8  # Set the desired minimum score threshold


shortlisted_candidates = df[(df["Score"] >= minimum_score) & (df["Are you available for 3 months, starting immediately, for a full-time work from home internship? "] == "Yes, I am available for 3 months starting immediately for a full-time internship.")]


# Write shortlisted candidates to a file
shortlisted_candidates.to_csv("shortlisted_candidates.csv", index=False)


print("Top Candidates saved to top_candidates.csv")
print("Shortlisted Candidates saved to shortlisted_candidates.csv")
