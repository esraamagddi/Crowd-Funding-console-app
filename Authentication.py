import os

class Authentication:
    def __init__(self):
        self.users_dir = "users/"

    def register(self, first_name, last_name, email, password, confirm_password, mobile_phone):
        if password != confirm_password:
            print("Passwords do not match")
            return False

        if self.user_exists(email):
            print("Email already exists")
            return False

        if not self.validate_email(email):
            print("Invalid email format")
            return False

        if not self.validate_phone(mobile_phone):
            print("Invalid mobile phone format")
            return False

        with open(self.users_dir + email + ".txt", "w") as user_file:
            user_file.write(f"First name: {first_name}\n")
            user_file.write(f"Last name: {last_name}\n")
            user_file.write(f"Password: {password}\n")
            user_file.write(f"Mobile phone: {mobile_phone}\n")

        print("Registration successful")
        return True

    def login(self, email, password):
        if not self.user_exists(email):
            print("User does not exist")
            return False

        with open(self.users_dir + email + ".txt", "r") as user_file:
            lines = user_file.readlines()

            stored_password = None

            for line in lines:
                if line.startswith("Password:"):
                    stored_password = line.split(":")[1].strip()
                    break

            if stored_password is not None:
                if stored_password == password:
                    print("Login successful")
                    return True
                else:
                    print("Invalid password")
                    return False
            else:
                print("Password not found in the user file")
                return False


    def user_exists(self, email):
        return os.path.exists(self.users_dir + email + ".txt")

    def validate_email(self, email):
        return '@' in email

    def validate_phone(self, phone):
        return phone.startswith('+20') and len(phone) == 13
