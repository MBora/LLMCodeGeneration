import os
from datasets import Dataset

def extract_data(base_path, language):
    difficulties = ["easy", "external", "hard", "harder", "hardest", "medium"]
    data = []
    
    # Define a mapping for the language to the folder name
    language_folder_map = {
        "python": "solutions_python",
        "cpp": "solutions_c++"
    }
    solution_folder_name = language_folder_map.get(language, f"solutions_{language}")

    for difficulty in difficulties:
        difficulty_path = os.path.join(base_path, "codechef", difficulty)
        if os.path.exists(difficulty_path):  # Checking if the difficulty folder exists
            problem_folders = os.listdir(difficulty_path)
            
            for problem in problem_folders:
                # Skip system files or folders starting with dot
                if problem.startswith('.'):
                    continue
                description_path = os.path.join(difficulty_path, problem, "description", "description.txt")

                with open(description_path, 'r', encoding="utf-8", errors='ignore') as desc_file:
                    description = desc_file.read()

                    # Check if solutions folder exists for the language
                    solution_folder_path = os.path.join(difficulty_path, problem, solution_folder_name)
                    if os.path.exists(solution_folder_path):
                        solution_files = os.listdir(solution_folder_path)

                        # Loop over all solution files for the problem
                        for solution_file in solution_files:
                            solution_path = os.path.join(solution_folder_path, solution_file)

                            with open(solution_path, 'r', encoding="utf-8", errors='ignore') as sol_file:
                                solution = sol_file.read()

                                # Append to the data list
                                data.append({
                                    "description": description,
                                    "solution": solution
                                })

    return data



# Extracting data for Python and C++
data_python = extract_data("/home/valgrant/Desktop/3-1/NLP/description2code_current/description2code_current/", "python")
data_cpp = extract_data("/home/valgrant/Desktop/3-1/NLP/description2code_current/description2code_current/", "cpp")

# Structuring the data
structured_data_python = [{"prompt": problem["description"], "output": problem["solution"]} for problem in data_python]
structured_data_cpp = [{"prompt": problem["description"], "output": problem["solution"]} for problem in data_cpp]

# You can now save these structured datasets to files or use them directly
# Assuming the data structuring script was executed and the 
# structured_data_python and structured_data_cpp lists are available

# Display the first few entries of the Python dataset
# print("Python Dataset Samples:")
# for i, entry in enumerate(structured_data_python[:5]):
#     print(f"Sample {i+1}:")
#     print("Prompt (Description):\n", entry["prompt"])
#     print("Output (Solution):\n", entry["output"])
#     print("---------------------------------------------------------")

# # Display the first few entries of the C++ dataset
# print("\nC++ Dataset Samples:")
# for i, entry in enumerate(structured_data_cpp[:5]):
#     print(f"Sample {i+1}:")
#     print("Prompt (Description):\n", entry["prompt"])
#     print("Output (Solution):\n", entry["output"])
#     print("---------------------------------------------------------")

# Printing out the total number of entries
print(f"\nTotal entries in Python dataset: {len(structured_data_python)}")
print(f"Total entries in C++ dataset: {len(structured_data_cpp)}")

def list_of_dicts_to_dict_of_lists(list_of_dicts):
    """Convert a list of dictionaries to a dictionary of lists."""
    return {key: [d[key] for d in list_of_dicts] for key in list_of_dicts[0].keys()}

data_dict_python = list_of_dicts_to_dict_of_lists(structured_data_python)
dataset = Dataset.from_dict(data_dict_python)
print(dataset)
split_data = dataset.train_test_split(train_size=0.8, test_size=0.2)
train_data = split_data["train"]
test_and_eval_data = split_data["test"]
split_test_eval = test_and_eval_data.train_test_split(train_size=0.5, test_size=0.5)
test_data = split_test_eval["train"]
eval_data = split_test_eval["test"]
print(f"Number of training examples: {len(train_data)}")
print(f"Number of testing examples: {len(test_data)}")
print(f"Number of validation examples: {len(eval_data)}")
dataset = dataset.map(lambda example: {'text': "<Question>: " + example['prompt'] + " <CODE> \n" + example['output'] + " </CODE>"})
print(dataset.column_names)

# print a sample
print(dataset[0])
# import json

# # Saving Python dataset
# with open('structured_data_python.json', 'w', encoding='utf-8') as f:
#     json.dump(structured_data_python, f, ensure_ascii=False, indent=4)
# # Saving C++ dataset
# with open('structured_data_cpp.json', 'w', encoding='utf-8') as f:
#     json.dump(structured_data_cpp, f, ensure_ascii=False, indent=4)

import json

# Convert the Datasets into dictionaries or lists of dictionaries
train_data_dict = train_data.to_dict()
test_data_dict = test_data.to_dict()
eval_data_dict = eval_data.to_dict()

# Combine them into a single dictionary
combined_data = {
    "train": train_data_dict,
    "test": test_data_dict,
    "eval": eval_data_dict
}

# # Write the combined dictionary into a JSON file
# with open('combined_data.json', 'w', encoding='utf-8') as f:
#     json.dump(combined_data, f, ensure_ascii=False, indent=4)

