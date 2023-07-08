# Resume-Filtering
It Divide the candidate into 2 parts - 1. Top 10 Candidate 2. All eligible candidate

The provided script performs the following tasks:

1. Imports the necessary libraries, in this case, pandas.
2. Loads a dataset from a Google Sheets URL into a pandas DataFrame using the `read_csv` function.
3. Defines the criteria weights for different skills.
4. Calculates a score for each intern based on their skills and the criteria weights using vectorized multiplication and summation.
5. Ranks the interns based on their scores in descending order.
6. Selects the top 10 candidates with the highest scores.
7. Writes the top candidates to a CSV file named "top_candidates.csv".
8. Sets a minimum score threshold.
9. Filters the interns who meet the minimum score threshold and are available for a 3-month full-time work from home internship.
10. Writes the shortlisted candidates to a CSV file named "shortlisted_candidates.csv".
11. Prints messages indicating where the output files are saved.

The script takes into account the specified criteria weights to calculate scores, ranks the candidates based on these scores, and filters the candidates based on the minimum score threshold and availability for the internship. The selected candidates are then saved to separate CSV files.

If you have received a screening task today, you can submit the script provided along with your approach to solving the task.
