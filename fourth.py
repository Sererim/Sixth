# Difference between decimals of max and min numbers in a sequence

from decimal import Decimal as dec, getcontext as point

class Difference:

    @staticmethod
    def decimal_part(num: float) -> dec:
        point().prec = 4
        num = dec(num) % 1
        return num



def main() -> int:
    foo: list[float] = []
    delta: dec = '0.0'
    size: int = 0
    num: float = 0.0
    char: str = ""
    
    while True:
        
        size = int(input("Enter the size of a list.\n"))
        for i in range(size):
            num = float(input(f"Enter {i + 1} number of the list.\n"))
            foo.append(num)
        
        foo = list(map(str, foo))
        foo = (list(map(Difference.decimal_part, foo)))
        delta = max(foo) - min(foo)
        print(delta)
            
        char = input("To terminate the program enter Y or y.\n")
        if char in ['Y', 'y']:
            break
    
    return 0


if __name__ == "__main__":
    main()
