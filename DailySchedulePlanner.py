import os
import pickle

def display_schedule(schedule):
    print("Hour\tTask")
    print("----\t----")
    for hour, task in sorted(schedule.items()):
        print(f"{hour:02d}\t{task}")

def save_schedule(schedule):
    with open("schedule.pkl", "wb") as file:
        pickle.dump(schedule, file)

def load_schedule():
    if os.path.exists("schedule.pkl"):
        with open("schedule.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return {}

def main():
    schedule = load_schedule()

    while True:
        print("\n1. Display Schedule")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_schedule(schedule)
        elif choice == "2":
            hour = int(input("Enter the hour (0-23): "))
            task = input("Enter the task: ")
            schedule[hour] = task
        elif choice == "3":
            hour = int(input("Enter the hour to remove task from (0-23): "))
            if hour in schedule:
                del schedule[hour]
                print("Task removed successfully.")
            else:
                print("No task found for the specified hour.")
        elif choice == "4":
            save_schedule(schedule)
            print("Schedule saved. Quitting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

