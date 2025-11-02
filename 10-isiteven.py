def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    num = int(input("Enter a number: "))
    print(check_even_odd(num))

if __name__ == "__main__":
    main()