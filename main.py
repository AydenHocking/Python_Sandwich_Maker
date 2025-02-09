### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():                                                    ##Searches through the Items in Ingredients.
            if self.machine_resources[item] < amount:                                               ##Checks if there is enough of Item for making sandwich.
                print("Sorry, there is not enough " + str(item) + ".")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert coins:")                                                                      ##Collection of inputs for coins.
        dollars = int(input("How many dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickles = int(input("How many nickles?: "))
        coins = round(float(dollars * 1 + half_dollars * 0.5 + quarters * 0.25 + nickles * 0.05),2) ##Adds all coin amounts * their worth. Then rounds to two digits to prevent error.
        return coins

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost > coins:                                                                            ##Checks if the user paid enough for sandwich cost.
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost                                                                   ##Determine change.
            print("Here is $%.2f in change." % change)                                              ##Formats change to 2 decimal places.
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():                                              ##Iterates through the items in the selected sandwich order.
            self.machine_resources[item] -= amount                                                  ##Remove Ingredients.
        print(str(sandwich_size) + " sandwich is ready. Bon appetit!")

    def add_resources(self, ingredients):
        for item, amount in ingredients.items():                                                    ##Iterates through the ingredients
            self.machine_resources[item] += amount                                                  ##Adds the item amount input to the resources

### Make an instance of SandwichMachine class and write the rest of the codes ###
