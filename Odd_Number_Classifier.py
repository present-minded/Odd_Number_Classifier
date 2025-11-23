def check_even_odd():
    print("--- Even/Odd Number Classifier ---")
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            
            number = int(user_input)
            
            if number % 2 == 0:
                print(f"Result: {number} is an EVEN number.")
            else:
                print(f"Result: {number} is an ODD number.")
                
        except ValueError:
            print("Error: Please enter a valid whole number.")
        print("-" * 30) 

if __name__ == "__main__":
    check_even_odd()