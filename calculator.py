def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

operations = {
    '1': ('Add', add),
    '2': ('Subtract', sub),
    '3': ('Multiply', mul),
    '4': ('Divide', div)
}

def get_numbers():
    while True:
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            return n1, n2
        except ValueError:
            print("Invalid value. Please use numbers only.")

def display_menu():
    print("\n Select a Calculation ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an operation 1 to 5: ")

        if choice == '5':
            print("You have exited the calculator.")
            break

        if choice in operations:
            n1, n2 = get_numbers()
            op_name, op_func = operations[choice]
            result = op_func(n1, n2)

            if isinstance(result, float):
                print(f"\n{op_name} Result: {result:.2f}")
            else:
                print(f"\n{result}")
        else:
            print("Invalid choice. Please select between 1 and 5.")

#Run unit tests
def test_calculator():
    assert add(3, 2) == 5
    assert sub(5, 3) == 2
    assert mul(2, 4) == 8
    assert div(10, 2) == 5
    assert div(5, 0) == "Error: Cannot divide by zero."
    print("All unit tests passed.")

if __name__ == "__main__":
    test_calculator()
    main()
