import os

class ProjectManager:
    def __init__(self):
        self.projects_dir = "projects/"

    def create_project(self, email, title, details, total_target, start_time, end_time):
        project_files = os.listdir(self.projects_dir)
        if project_files:
            last_project_id = int(project_files[-1].split("_")[1].split(".")[0])
            project_id = last_project_id + 1
        else:
            project_id = 1

        with open(self.projects_dir + f"project_{project_id}.txt", "w") as project_file:
            project_file.write(f"Title: {title}\n")
            project_file.write(f"Details: {details}\n")
            project_file.write(f"Total target: {total_target}\n")
            project_file.write(f"Start time: {start_time}\n")
            project_file.write(f"End time: {end_time}\n")
            project_file.write(f"Owner email: {email}\n")

        print("Project created successfully")

    def edit_project(self, email, project_id, title, details, total_target, start_time, end_time):
            project_file_path = self.projects_dir + f"project_{project_id}.txt"
            if os.path.exists(project_file_path):
                with open(project_file_path, "r") as project_file:
                    lines = project_file.readlines()
                    # print(lines)  
                
                owner_email = lines[5].split(":")[1].strip() 
                # print(owner_email)
                # print(email)
                if owner_email == email:
                    with open(project_file_path, "w") as project_file:
                        project_file.write(f"Title: {title}\n")
                        project_file.write(f"Details: {details}\n")
                        project_file.write(f"Total target: {total_target}\n")
                        project_file.write(f"Start time: {start_time}\n")
                        project_file.write(f"End time: {end_time}\n")
                    print("Project edited successfully")
                else:
                    print("You are not authorized to edit this project")
            else:
                print("Project does not exist")


    def search_projects_by_date(self, date):
        found_projects = []
        for project_file in os.listdir(self.projects_dir):
            with open(os.path.join(self.projects_dir, project_file), "r") as f:
                lines = f.readlines()
                start_time = lines[3].split(":")[1].strip()
                end_time = lines[4].split(":")[1].strip()
                if start_time <= date <= end_time:
                    found_projects.append(project_file)
        return found_projects

    def delete_project(self, email, project_id):
        project_file_path = self.projects_dir + f"project_{project_id}.txt"
        if os.path.exists(project_file_path):
            with open(project_file_path, "r") as project_file:
                lines = project_file.readlines()
                if len(lines) >= 6:
                    owner_email = lines[5].split(":")[1].strip()
                    if owner_email == email:
                        os.remove(project_file_path)
                        print("Project deleted successfully")
                    else:
                        print("You are not authorized to delete this project")
                else:
                    print("Invalid project file format")
        else:
            print("Project does not exist")

    



