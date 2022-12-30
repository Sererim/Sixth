# from binary to decimal
# and from decimal to binary

class Convert():
    
    @staticmethod
    def dec_to_binary(num: int) -> str:
        binary: str = ""
        
        while len(binary) < 8:
            if num == 1:
                binary += "1"
                break
            
            if num % 2 == 1:
                num = (num - 1) / 2
                binary += "1"
            else:
                num /= 2
                binary += "0"
        if len(binary) < 8:
            for i in range(len(binary), 8):
                binary += "0"
        binary = binary[::-1]
        return binary
            
    @staticmethod
    def binary_to_dec(bnum: str) -> int:
        foo = list(map(int, bnum))
        bar: int = 0
        p: int = 7
        for i in range(0, 8, 1):
            bar += int(foo[i]) * (2**(p - i))
        return bar
    

def main() -> int:
    char: str = ""
    while True:
        char = input("Enter a number to convert into binary and back to decimal.\n")
        char = (Convert.dec_to_binary(int(char)))
        print(char)
        print(Convert.binary_to_dec(char))
        
        char = input("Enter Y or y to terminate the program.\n")
        if char in ['Y', 'y']:
            break
    return 0


if __name__ == "__main__":
    main()
