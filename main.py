import os
from Authentication import Authentication
from projects import ProjectManager

def print_menu():
    print("\n======= Main Menu =======")
    print("1. Register")
    print("2. Login")
    print("3. Create Project")
    print("4. Edit Project")
    print("5. Delete Project")
    print("6. Search Projects by Date")
    print("0. Exit")
    print("=========================")

def main():
    if not os.path.exists("users"):
        os.makedirs("users")
    if not os.path.exists("projects"):
        os.makedirs("projects")

    auth = Authentication()
    project_manager = ProjectManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")
            mobile_phone = input("Enter your mobile phone: ")
            auth.register(first_name, last_name, email, password, confirm_password, mobile_phone)

        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            auth.login(email, password)

        elif choice == '3':
            title = input("Enter project title: ")
            details = input("Enter project details: ")
            total_target = input("Enter total target amount: ")
            start_time = input("Enter start time (YYYY-MM-DD): ")
            end_time = input("Enter end time (YYYY-MM-DD): ")
            project_manager.create_project(title, details, total_target, start_time, end_time)

        elif choice == '4':
            project_id = input("Enter project ID: ")
            title = input("Enter updated title: ")
            details = input("Enter updated details: ")
            total_target = input("Enter updated total target amount: ")
            start_time = input("Enter updated start time (YYYY-MM-DD): ")
            end_time = input("Enter updated end time (YYYY-MM-DD): ")
            project_manager.edit_project(project_id, title, details, total_target, start_time, end_time)

        elif choice == '5':
            project_id = input("Enter project ID to delete: ")
            project_manager.delete_project(project_id)

        elif choice == '6':
            date = input("Enter date to search projects (YYYY-MM-DD): ")
            found_projects = project_manager.search_projects_by_date(date)
            print("Projects found:", found_projects)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
