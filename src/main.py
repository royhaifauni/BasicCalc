import calculator

def main():
    print("Welcome to the Basic Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    
    while True:
        try:
            op = input("Enter operation (add, subtract, multiply, divide) or 'exit': ").lower()
            if op == 'exit':
                break
            
            if op not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation.")
                continue
                
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if op == 'add':
                print(f"Result: {calculator.add(a, b)}")
            elif op == 'subtract':
                print(f"Result: {calculator.subtract(a, b)}")
            elif op == 'multiply':
                print(f"Result: {calculator.multiply(a, b)}")
            elif op == 'divide':
                try:
                    print(f"Result: {calculator.divide(a, b)}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
