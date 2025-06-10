from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()

    user_input = input("Enter the number of days to add to the current date: ")

    if user_input.isdigit():
        days = int(user_input)
        calculate_future_date(days)
    else:
        print("Invalid input. Please enter an integer number of days.")

