from questions import questions

def display_welcome():
    """Display welcome message with the game instructions to the player"""
    print("\n=== Welcome to the Quiz Game! ===")
    print("Answer the questions by entering the number of your choice (1-4)")

def play_game():
    """Main game loop handling questions and scoring"""
    score = 0
    display_welcome()
    
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j+1}. {option}")
            
        while True:
            try:
                answer = int(input("\nYour answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
                
        if answer - 1 == q['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['options'][q['correct']]}")
            
    print(f"\nGame Over! Your score: {score}/{len(questions)}"))

if __name__ == "__main__":
    play_game()
