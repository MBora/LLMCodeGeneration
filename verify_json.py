import json

# Verification: Load and print some records to ensure data integrity
with open('combined_data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

# Print some records for verification
keys = list(loaded_data['train'].keys())[:5]  # Get the first 5 keys
subset = {key: loaded_data['train'][key] for key in keys}  # Create a subset of the dictionary
print(json.dumps(subset, ensure_ascii=False, indent=4))

