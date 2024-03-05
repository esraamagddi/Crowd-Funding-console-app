from Authentication import Authentication
from projects import ProjectManager

auth = Authentication()
project_manager = ProjectManager()

def main():
    while True:
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if auth.login(email, password):
                print("Login successful")
                create_project(email)  
            else:
                print("Login failed")

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice")


def create_project(email):
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    total_target = input("Enter total target amount: ")
    start_time = input("Enter start time (YYYY-MM-DD): ")
    end_time = input("Enter end time (YYYY-MM-DD): ")

    project_manager.create_project(email, title, details, total_target, start_time, end_time)


if __name__ == "__main__":
    main()
