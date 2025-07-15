HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found!")
            else:
                print("Calculation History:")
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found yet.")

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print('History cleared.')

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (e.g. 8 + 8)')
        return
    
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return

    if op == "+":
        result = num1 + num2 
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot divide by zero.')
            return
        result = num1 / num2
    else:    
        print('Invalid operator. Use only + - * /.')
        return

    equation = f"{num1} {op} {num2}"
    print(f"Result: {result}")
    save_to_history(equation, result)

# Main loop
while True:
    print("\n--- Calculator Menu ---")
    print("1. Calculate")
    print("2. Show History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        user_input = input("Enter expression (e.g. 5 + 3): ")
        calculator(user_input)
    elif choice == "2":
        show_history()
    elif choice == "3":
        clear_history()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
