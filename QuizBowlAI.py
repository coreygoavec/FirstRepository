# Define the questions using a dictionary
questions = {
    "Q1": {"type": "True/False", "question": "Is the Earth flat?", "answer": False},
    "Q2": {"type": "Multiple Choice", "question": "What is the capital of France?", "options": ["A. Berlin", "B. Paris", "C. London"], "answer": "B"},
    "Q3": {"type": "Short Answer", "question": "What is the color of the sun?", "answer": "Yellow"},
    "Q4": {"type": "Number Input", "question": "How many continents are there?", "answer": 7},
    "Q5": {"type": "Multiple Choice", "question": "What is the largest planet in our solar system?", "options": ["A. Earth", "B. Jupiter", "C. Mars"], "answer": "B"}
}

# Display the game title
print("Are You Smarter Than a Fifth Grader")

# Initialize the counter for correct answers
correct_answers = 0

# Iterate through the questions
for key, question_info in questions.items():
    # Display a separator line between questions
    print("\n" + "="*40)
    
    print(f"{question_info['question']} ({question_info['type']})")
    
    # Ask user for input based on question type
    if question_info["type"] == "True/False":
        user_input = input("Enter True or False: ").lower()  # Convert to lowercase for case-insensitivity
        user_answer = user_input == "false"
    elif question_info["type"] == "Multiple Choice":
        print("\n".join(question_info["options"]))
        user_input = input("Enter the letter of your choice: ").upper()  # Convert to uppercase for case-insensitivity
        user_answer = user_input == question_info["answer"]
    elif question_info["type"] == "Short Answer":
        user_input = input("Your answer: ")
        user_answer = user_input.lower() == question_info["answer"].lower()  # Case-insensitive comparison
    elif question_info["type"] == "Number Input":
        user_input = input("Enter a number: ")
        user_answer = user_input.isdigit() and int(user_input) == question_info["answer"]
    else:
        print("Invalid question type")
        continue

    # Check if the user's answer is correct
    if user_answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is {question_info['answer']}.")
        
# Display a separator line at the end of the quiz
print("\n" + "="*40)

# Display the total number of correct answers
print(f"\nQuiz completed. You got {correct_answers} out of {len(questions)} questions correct.")
