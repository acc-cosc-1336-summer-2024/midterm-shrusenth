import question_c
from src.question_c.question_c import is_prime

def main():
    while True:
        num_str = input("Enter a positive integer (or 'q' to quit): ")
        if num_str.lower() == 'q':  
            break
        
        if num_str.isdigit() and int(num_str) > 0:
            num = int(num_str)
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        else:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()#add import
