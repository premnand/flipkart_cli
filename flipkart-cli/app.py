import sys
from dbhelper import DBhelper

class Flipkart:

    def __init__(self):
        self.db = DBhelper()
        self.current_user = None
        self.menu()

    def menu(self):
        user_input = input("""
  ================================
          FLIPKART CLI APP
  ================================
  1. Register
  2. Login
  3. Exit
  > """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            print("Goodbye!")
            sys.exit(0)

    def login_menu(self):
        user_input = input(f"""
  --------------------------------
  Logged in as: {self.current_user[1]}
  --------------------------------
  1. View profile
  2. Edit profile
  3. Delete account
  4. Logout
  > """)

        if user_input == "1":
            self.view_profile()
        elif user_input == "2":
            self.edit_profile()
        elif user_input == "3":
            self.delete_profile()
        elif user_input == "4":
            self.current_user = None
            print("Logged out successfully.")
            self.menu()
        else:
            print("Invalid option.")
            self.login_menu()

    def register(self):
        print("\n  -- Register --")
        name = input("  Name     : ")
        email = input("  Email    : ")
        password = input("  Password : ")

        response = self.db.register(name, email, password)

        if response == 1:
            print("  Registration successful! Please login.\n")
        else:
            print("  Registration failed. Email may already exist.\n")

        self.menu()

    def login(self):
        print("\n  -- Login --")
        email = input("  Email    : ")
        password = input("  Password : ")

        data = self.db.search(email, password)

        if len(data) == 0:
            print("  Incorrect email or password. Try again.\n")
            self.login()
        else:
            self.current_user = data[0]
            print(f"\n  Welcome back, {self.current_user[1]}!")
            self.login_menu()

    def view_profile(self):
        u = self.current_user
        print(f"""
  ---- Your Profile ----
  ID       : {u[0]}
  Name     : {u[1]}
  Email    : {u[2]}
  Password : {'*' * len(u[3])}
  ----------------------""")
        self.login_menu()

    def edit_profile(self):
        print("\n  -- Edit Profile (leave blank to keep current value) --")
        name = input(f"  Name [{self.current_user[1]}]: ").strip() or self.current_user[1]
        email = input(f"  Email [{self.current_user[2]}]: ").strip() or self.current_user[2]
        new_pass = input(f"  New password (blank = keep current): ").strip() or self.current_user[3]

        result = self.db.update_user(self.current_user[0], name, email, new_pass)

        if result == 1:
            self.current_user = self.db.get_user(self.current_user[0])
            print("  Profile updated successfully!")
        else:
            print("  Update failed.")

        self.login_menu()

    def delete_profile(self):
        confirm = input("  Type YES to confirm account deletion: ").strip()
        if confirm == "YES":
            self.db.delete_user(self.current_user[0])
            self.current_user = None
            print("  Account deleted.")
            self.menu()
        else:
            print("  Cancelled.")
            self.login_menu()


obj = Flipkart()
