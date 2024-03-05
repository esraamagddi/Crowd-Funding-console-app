import os

class ProjectManager:
    def __init__(self):
        self.projects_dir = "projects/"

    def create_project(self, title, details, total_target, start_time, end_time):
        project_id = len(os.listdir(self.projects_dir)) + 1

        with open(self.projects_dir + f"project_{project_id}.txt", "w") as project_file:
            project_file.write(f"Title: {title}\n")
            project_file.write(f"Details: {details}\n")
            project_file.write(f"Total target: {total_target}\n")
            project_file.write(f"Start time: {start_time}\n")
            project_file.write(f"End time: {end_time}\n")

        print("Project created successfully")

    def edit_project(self, project_id, title, details, total_target, start_time, end_time):
        if os.path.exists(self.projects_dir + f"project_{project_id}.txt"):
            with open(self.projects_dir + f"project_{project_id}.txt", "w") as project_file:
                project_file.write(f"Title: {title}\n")
                project_file.write(f"Details: {details}\n")
                project_file.write(f"Total target: {total_target}\n")
                project_file.write(f"Start time: {start_time}\n")
                project_file.write(f"End time: {end_time}\n")
            
            print("Project edited successfully")
        else:
            print("Project does not exist")

    def delete_project(self, project_id):
        project_file_path = self.projects_dir + f"project_{project_id}.txt"
        if os.path.exists(project_file_path):
            os.remove(project_file_path)
            print("Project deleted successfully")
        else:
            print("Project does not exist")

    def search_projects_by_date(self, date):
        found_projects = []
        for project_file in os.listdir(self.projects_dir):
            with open(self.projects_dir + project_file, "r") as f:
                lines = f.readlines()
                start_time = lines[3].split(":")[1].strip()
                end_time = lines[4].split(":")[1].strip()
                if start_time <= date <= end_time:
                    found_projects.append(project_file)
        return found_projects
