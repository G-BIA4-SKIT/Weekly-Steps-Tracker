def main():

    def set_steps_goal():
        goal = int(input("Enter your daily steps goal: "))
        return goal

    def record_daily_steps():
        total_steps = 0

        for day in range(1, 8):
            steps = int(input(f"Enter steps for day {day}: "))
            total_steps = total_steps + steps

        return total_steps

    def evaluate_weekly_performance(total_steps, goal):
        average_steps = total_steps / 7

        print(f"Your average daily steps for the week is {average_steps:.2f}.")

        if average_steps > goal:
            print(f"You exceeded your daily steps goal on average.")
        elif average_steps == goal:
            print(f"You met your daily steps goal on average.")
        else:
            print(f"You did not meet your daily steps goal on average.")

    goal = set_steps_goal()
    total_steps = record_daily_steps()
    evaluate_weekly_performance(total_steps, goal)


main()