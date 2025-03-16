import random  

# Core components for combinatorial generation  
domains = [  
    "Healthcare diagnostics", "Autonomous weapons systems", "Climate modeling",  
    "Financial markets", "Neuroprosthetics", "Quantum computing",  
    "Space exploration", "Educational systems", "Criminal justice"  
]  

question_types = [  
    "Discuss the implications of", "Analyze the potential impacts and provide a detailed framework for",  
    "Evaluate the effectiveness and propose improvements in", "Compare various methodologies in",  
    "Explore the long-term consequences of", "Design a comprehensive study on",  
    "Assess the ethical considerations related to", "Predict future trends and outcomes in",  
    "Debate the advantages and drawbacks of", "Formulate a detailed strategy to enhance"  
]  

technical_components = [  
    "neural architecture search", "multi-modal transformers", "reinforcement learning with human feedback",  
    "differential privacy mechanisms", "neuromorphic computing", "federated learning systems",  
    "adversarial robustness", "causal inference models", "embodied AI systems",  
    "swarm intelligence algorithms", "neurosymbolic integration", "self-supervised learning paradigms"  
]  

# Generation engine  
def generate_questions(num_questions):  
    with open("keywords.txt", "w") as f:  
        for _ in range(num_questions):  
            combo = (  
                f"{random.choice(question_types)} {random.choice(technical_components)} "  
                f"within the context of {random.choice(domains)}. "  
                "Include specific examples, potential challenges, and evaluative criteria."  
            )  
            question = combo[0].upper() + combo[1:] + "?"  
            f.write(question + "\n")  # Write each question immediately  
            f.flush()  # Ensure the content is written to the file immediately  
            print(f"Generated: {question}")  # Log the generated question  

# Generate unique questions based on user input  
if __name__ == "__main__":  
    try:  
        num_questions = int(input("Enter the number of questions you want to generate: "))  # Prompt user input  
        if num_questions <= 0:  
            print("Please enter a positive number.")  
        else:  
            print(f"Starting to generate {num_questions} questions...")  
            generate_questions(num_questions)  # Generate questions  
            print("Question generation completed.")  
    except ValueError:  
        print("Invalid input. Please enter a valid integer.")  
