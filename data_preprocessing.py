import os
import re

# Define input and output directories
input_folder = 'event_logs_raw'
output_folder = 'event_logs'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    input_filepath = os.path.join(input_folder, filename)
    output_filepath = os.path.join(output_folder, filename)

    # Read the content of the input file
    with open(input_filepath, 'r') as file:
        content = file.read()

    # Perform find and replace
    modified_content = re.sub(r'<date key="timestamp"', r'<date key="time:timestamp"', content)

    # Write the modified content to the output file
    with open(output_filepath, 'w') as file:
        file.write(modified_content)

    print(f"Processed: {filename}")

print("Processing complete.")