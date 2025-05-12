import datetime
import os

FILE_NAME = "attendance.csv"

def mark_attendance():
    name = input("Enter student name: ").title()
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{date},{time}\n")
    
    print(f"✅ Attendance marked for {name} on {date} at {time}")
    view_latest_entry()

def view_latest_entry():
    print("\n📌 Latest Attendance Entry:")
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            if lines:
                name, date, time = lines[-1].strip().split(",")
                print(f"{name}\t\t{date}\t{time}")
            else:
                print("📭 No entries yet.")
    except FileNotFoundError:
        print("❌ No attendance file found.")

def view_attendance():
    print("\n🧾 Full Attendance Records:")
    try:
        if not os.path.exists(FILE_NAME):
            print("📭 No records to display.")
            return
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
            if not data:
                print("📭 File is empty.")
                return
            print("Name\t\tDate\t\tTime")
            print("------------------------------------------------")
            for line in data:
                name, date, time = line.strip().split(",")
                print(f"{name}\t\t{date}\t{time}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

def attendance_menu():
    print("🎓 Welcome to Attendance Management System")
    while True:
        print("\nMenu:")
        print("1. Mark Attendance 🖊️")
        print("2. View Full Attendance 📄")
        print("3. Exit 🚪")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("👋 Exiting... See you again, Teacher Pooja!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    attendance_menu()
