import sys
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO  # Import StringIO from io

# Read CSV data from stdin
input_data = sys.stdin.read()

# Convert the CSV data to a pandas DataFrame
data = pd.read_csv(StringIO(input_data))  # Use StringIO directly
data.columns = data.columns.str.strip()

# Group by 'Model' and calculate the mean score
mean_scores = data.groupby('Model')['Score'].mean().reset_index()

# Plot the scores by model
plt.figure(figsize=(10, 6))
plt.bar(mean_scores['Model'], mean_scores['Score'], color='skyblue')
plt.xlabel('Model')
plt.ylabel('Mean Score')
plt.title('Mean Scores by Model')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
