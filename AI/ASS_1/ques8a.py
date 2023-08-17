class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the Restaurant class with a restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type of the restaurant."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is now open."""
        print(f"The restaurant {self.restaurant_name} is now open!")

# Creating an instance of the Restaurant class
restaurant = Restaurant("Taj Hotel", "Indian")

# printing the attributes individually
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

# Calling both methodas
restaurant.describe_restaurant()
restaurant.open_restaurant ()

