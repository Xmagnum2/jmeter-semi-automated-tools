import os
import pandas as pd

# Specify the root directory of the directory structure
root_dir = './{your-result-directory}'

# Create a list of DataFrames to store the results
dataframes = []

# Traverse all files and directories within the root directory
for subdir, _, files in os.walk(root_dir):
    for file in files:
        # When a statistics.json file is found
        if file == 'statistics.json':
            file_path = os.path.join(subdir, file)
            # Load the JSON file
            with open(file_path, 'r') as f:
                data = pd.read_json(f)["HTTP Request"]
                data["path"] = file_path
                data = pd.DataFrame(data).T
            # Add the DataFrame to the list
            dataframes.append(data)

# Concatenate the list of DataFrames
all_data = pd.concat(dataframes, ignore_index=True)
# Specify the order of the columns
columns_order = ["path", "sampleCount", "meanResTime", "medianResTime", "pct1ResTime", "pct2ResTime", "pct3ResTime", "minResTime", "maxResTime", "errorPct", "throughput"]
all_data = all_data[columns_order]

# Save the results to a CSV file
all_data.to_csv('combined_statistics.csv', sep='\t', index=False)
