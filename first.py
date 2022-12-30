
class Calculator:
    
    @staticmethod
    def mainloop() -> None:
        formula: str = ""
        answer: int = 0
        char: str = ""
        
        while True:
            formula = input("Enter an equation.\n")
            try:
                answer = eval(formula)
                print(f"Entered equation is: {formula}\nSolution is: {answer}")                
                
                char = input("Enter Y or y to terminate the program.\n")
                if char in ['Y', 'y']:
                    break
            except SyntaxError:
                print("Syntax error!")
                pass
            
        
def main() -> int:
    
    print("Program is running.")
    Calculator.mainloop()
    return 0


if __name__ == "__main__":
    main()
