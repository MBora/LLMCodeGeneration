import os

def extract_data_from(base_path, language):
    data = []

    # Get a list of all problem IDs in the directory
    problem_ids = [folder for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))]

    for problem_id in problem_ids:
        description_path = os.path.join(base_path, problem_id, "description", "description.txt")

        # Check if solutions folder exists for the language
        solution_folder_path = os.path.join(base_path, problem_id, f"solutions_{language}")
        if os.path.exists(solution_folder_path):
            solution_files = os.listdir(solution_folder_path)

            for solution_file in solution_files:
                # Looping over all solution files for each problem
                solution_path = os.path.join(solution_folder_path, solution_file)

                with open(description_path, 'r', encoding="utf-8", errors='ignore') as desc_file, \
                     open(solution_path, 'r', encoding="utf-8", errors='ignore') as sol_file:

                    description = desc_file.read()
                    solution = sol_file.read()

                    # Append to the data list
                    data.append({
                        "description": description,
                        "solution": solution
                    })

    return data

base_path = "/home/valgrant/Desktop/3-1/NLP/description2code_current/description2code_current/hackerearth/problems_college"
data_python = extract_data_from(base_path, "python")
data_cpp = extract_data_from(base_path, "c++")

# Structuring the data
structured_data_python = [{"prompt": problem["description"], "output": problem["solution"]} for problem in data_python]
structured_data_cpp = [{"prompt": problem["description"], "output": problem["solution"]} for problem in data_cpp]

# Displaying samples (optional)
print("Python  Dataset Samples:")
for i, entry in enumerate(structured_data_python[:5]):
    print(f"Sample {i+1}:")
    print("Prompt (Description):\n", entry["prompt"])
    print("Output (Solution):\n", entry["output"])
    print("---------------------------------------------------------")

print("\nC++  Dataset Samples:")
for i, entry in enumerate(structured_data_cpp[:5]):
    print(f"Sample {i+1}:")
    print("Prompt (Description):\n", entry["prompt"])
    print("Output (Solution):\n", entry["output"])
    print("---------------------------------------------------------")

# Printing out the total number of entries
print(f"\nTotal entries in Python dataset: {len(structured_data_python)}")
print(f"Total entries in C++ dataset: {len(structured_data_cpp)}")