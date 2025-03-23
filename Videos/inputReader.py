import json

def load_math_problems(filename):
    """
    Reads the math problems from a JSON file.
    
    The JSON file should be structured as an array of objects. For example:
    [
        {
            "problem": "Solve for x in 2x+3=7",
            "solution": "x = 2"
        },
        {
            "problem": "Simplify (3+5)*2",
            "solution": "16"
        }
    ]
    
    Parameters:
        filename (str): The path to the JSON file.
        
    Returns:
        list: A list of dictionaries, where each dictionary represents a math problem.
    """
    try:
        with open(filename, 'r') as file:
            problems = json.load(file)
        return problems
    except json.decoder.JSONDecodeError as e:
        print("JSON decode error:", e)
        return []
    except FileNotFoundError as e:
        print("File not found:", e)
        return []
    except Exception as e:
        print("An unexpected error occurred:", e)
        return []

def generate_prompt(problem_entry):
    """
    Generates a detailed prompt for inVideo AI using the given math problem.
    
    The prompt instructs inVideo AI to create an engaging animated video that 
    explains the math problem step by step. The prompt includes both the problem 
    statement and the solution.
    
    Parameters:
        problem_entry (dict): A dictionary with 'problem' and 'solution' keys.
        
    Returns:
        str: A formatted string that serves as the prompt.
    """
    template = (
        "Create an engaging animation video that explains the following math problem step by step:\n"
        "Problem: {problem}\n"
        "Solution: {solution}\n"
        "Please include clear visual highlights for each step, animated text explanations, "
        "and conclude with the final answer."
    )
    return template.format(problem=problem_entry["problem"], solution=problem_entry["solution"])

if __name__ == "__main__":
    # Load math problems from the JSON file.
    problems = load_math_problems('problems.json')
    
    if not problems:
        print("No math problems loaded. Please check your problems.json file.")
    else:
        # For demonstration, generate a prompt for the first problem.
        prompt = generate_prompt(problems[0])
        
        # Print out the generated prompt.
        # Next Steps:
        # 1. Copy the printed prompt.
        # 2. Go to inVideo AI in your browser.
        # 3. Paste the prompt into the tool and generate the video.
        # 4. Download the video and store it in your designated temporary folder.
        print("Generated Prompt for inVideo AI:")
        print("---------------------------------")
        print(prompt)
        print("---------------------------------")
        print("Instructions:")
        print("1. Copy the above prompt.")
        print("2. Go to inVideo AI, paste the prompt, and generate the video (max 10 minutes/week, 4 watermarked exports).")
        print("3. Download the video and save it to your 'temp_videos' folder for uploading to YouTube later.")
