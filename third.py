# [1, 2, 3, 4] -> [4, 6]


class Pairs:
    
    
    @staticmethod 
    def get_pairs(num_1, num_2) -> int:
        return num_1 * num_2
        
    
def main() -> int:
    foo: list[int] = []
    bar: list[int] = []
    
    size: int = 0
    num: int = 0
    char:str = ""
    
    while True:
        size = int(input("Enter the size of a list.\n"))
        for i in range(size):
            num = int(input(f"Enter {i + 1} number of the list.\n"))
            foo.append(num)
        bar = foo[::-1]
        s = list(dict.fromkeys(map(Pairs.get_pairs, foo, bar)))
        print(s)
        char = input("To terminate the program enter Y or y.\n")
        
        if char in ['Y', 'y']:
            break
    return 0


if __name__ == "__main__":
    main()
