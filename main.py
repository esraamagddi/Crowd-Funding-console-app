from Authentication import Authentication
from projects import ProjectManager

auth = Authentication()
project_manager = ProjectManager()

def main():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if auth.login(email, password):
                print("Login successful")
                logged_in_menu(email)
            else:
                print("Login failed")

        elif choice == '2':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")
            mobile_phone = input("Enter your mobile phone: ")
            if auth.register(first_name, last_name, email, password, confirm_password, mobile_phone):
                print("Registration successful")
                logged_in_menu(email)
            else:
                print("Registration failed")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

def logged_in_menu(email):
    while True:
        print("1. Search Projects by Email")
        print("2. Search Projects by Date")
        print("3. Create Project")
        print("4. Edit Project")
        print("5. Delete Project")
        print("6. Logout")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            search_email = input("Enter email to search projects: ")
            projects = auth.search_projects_by_email(search_email)
            if projects:
                print("Projects found:", projects)
            else:
                print("No projects found for this email")

        elif choice == '2':
            date = input("Enter date to search projects (YYYY-MM-DD): ")
            projects = project_manager.search_projects_by_date(date)
            if projects:
                print("Projects found:", projects)
            else:
                print("No projects found for this date")

        elif choice == '3':
            title = input("Enter project title: ")
            details = input("Enter project details: ")
            total_target = input("Enter total target amount: ")
            start_time = input("Enter start time (YYYY-MM-DD): ")
            end_time = input("Enter end time (YYYY-MM-DD): ")
            project_manager.create_project(email, title, details, total_target, start_time, end_time)

        elif choice == '4':
            project_id = input("Enter project ID to edit: ")
            title = input("Enter updated title: ")
            details = input("Enter updated details: ")
            total_target = input("Enter updated total target amount: ")
            start_time = input("Enter updated start time (YYYY-MM-DD): ")
            end_time = input("Enter updated end time (YYYY-MM-DD): ")
            project_manager.edit_project(email, project_id, title, details, total_target, start_time, end_time)

        elif choice == '5':
            project_id = input("Enter project ID to delete: ")
            project_manager.delete_project(email, project_id)

        elif choice == '6':
            print("Logging out...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
