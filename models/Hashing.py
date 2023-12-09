import csv

class Hashing:
    def __init__(self):
        self.data = []

    def add_user(self, email, password, contact, address):
        updated_password = self.hashPassword(password)
        self.data.append({'email': email, 'password': updated_password, 'contact': contact, 'address': address})

    def hashPassword(self, password):
        hashed_value = 0
        for char in password:
            hashed_value ^= ord(char)
            hashed_value = (hashed_value << 3) | (hashed_value >> (32 - 3))  # Rotate left by 3 bits
        return hashed_value

    def save_to_csv(self, filename='user_data.csv'):
        try:
            with open(filename, 'r') as checkfile:
                first_char = checkfile.read(1)
        except FileNotFoundError:
            first_char = ""

        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['email', 'password', 'contact', 'address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not first_char:
                writer.writeheader()

            for data in self.data:
                writer.writerow(data)

    def load_from_csv(self, filename='user_data.csv'):
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = list(reader)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")

    def verify_credentials(self, email, password):
        for user in self.data:
            if user['email'] == email:
                stored_hashed_password = user['password']
                input_hashed_password = self.hashPassword(password)
                if stored_hashed_password == input_hashed_password:
                    return True
        return False


# Example usage:
custom_hash = Hashing()

# Load user data from CSV file (if the file exists)
custom_hash.load_from_csv()

# Get user input for signup
signup_email = input("Enter your email: ")
signup_password = input("Enter your password: ")
signup_contact = input("Enter your contact: ")
signup_address = input("Enter your address: ")

# Add user data to the custom hash instance
custom_hash.add_user(signup_email, signup_password, signup_contact, signup_address)

# Save user data to a CSV file
custom_hash.save_to_csv()

# Get login credentials
login_email = input("Enter your email: ")
login_password = input("Enter your password: ")

# Verify login credentials
if custom_hash.verify_credentials(login_email, login_password):
    print("Login successful!")
else:
    print("Login failed. Please check your email and password.")
