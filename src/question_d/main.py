from src.question_d.question_d import get_day_of_week
def main():

    while True:
        try:
            day_number = int(input("Enter a number between 1 and 7 : "))
        except ValueError:
            print("Invalid Input")
            continue

        if 1 <= day_number <= 7:
            day_name = get_day_of_week(day_number)
            print("The corresponding day of the week is:", day_name)
            break
        else:
            print("Not in range.")


if __name__ == "__main__":
    main()#add import
