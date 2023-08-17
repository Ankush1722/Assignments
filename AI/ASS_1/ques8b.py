class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initializes the User class with user profile information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        """prints a summary of the user's information."""
        print("User Profile:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age})")
        print(f"Location: {self.location}")
        print(f"occupation: {self.occupation}")

    def greet_user(self):
        """prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

# Creating instances representing different users
user1 = User("John", "Doe", 25, "New York", "Engineer")
user2 = User("Emma", "smith", 30, "London", "Teacher")
user3 = User("Michael", "Johnson", 40, "Los Angeles", "Business Owner")

# Calling the describe_user() and greet_user() methods for each user
user1.describe_user()
user1.greet_user()

user2. describe_user()
user2. greet_user()

user3. describe_user()
user3. greet_user()

