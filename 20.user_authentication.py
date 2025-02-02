'''20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, 
and it is implemented by `GoogleAuth` and `FacebookAuth` classes.'''

from abc import ABC, abstractmethod
import time
import getpass

class AuthSystem(ABC):
    @abstractmethod
    def login(self, email, password):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(AuthSystem):
    def login(self, email, password):
        print(f"\nAuthenticating Google account: {email}...")
        time.sleep(1)
        
        valid_email = "user@google.com"
        valid_password = "googlepass"

        if email.lower() == valid_email and password == valid_password:
            print("Google login successful.")
        else:
            print("Google login failed. Please check your details.")

    def logout(self):
        print("Logged out from Google.\n")

class FacebookAuth(AuthSystem):
    def login(self, email, password):
        print(f"\nAuthenticating Facebook account: {email}...")
        time.sleep(1)

        valid_email = "user@facebook.com"
        valid_password = "facebookpass"

        if email.lower() == valid_email and password == valid_password:
            print("Facebook login successful.")
        else:
            print("Facebook login failed. Please check your details.")

    def logout(self):
        print("Logged out from Facebook.\n")

def authenticate(auth_method):
    print("\nEnter login credentials:")
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ").strip()

    auth_method.login(email, password)
    auth_method.logout()

def main():
    while True:
        print("\nSelect a login method:")
        print("1. Google")
        print("2. Facebook")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            authenticate(GoogleAuth())
        elif choice == "2":
            authenticate(FacebookAuth())
        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
