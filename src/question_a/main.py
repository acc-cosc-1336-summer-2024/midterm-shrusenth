import question_a
from src.question_a.question_a import get_sum_of_evens

def main():
    while True:
        num_str = input()
        if num_str.lower() == 'quit':
            break
        
        if num_str.isdigit():
            num = int(num_str)
            if num <= 0:
                print("Enter a positive integer greater than 0.")
                continue
            
            result = get_sum_of_evens(num)
            print({result})
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()#add import
