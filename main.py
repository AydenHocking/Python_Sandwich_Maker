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

def main():
    machine = SandwichMachine(resources)
    while True:
        selection = input("What would you like? (small/medium/large/off/report/add): ").lower()     ##Input selections formatted.
        if selection in recipes:                                                                    ##Checks if the input is small/medium/large.
            sandwich = recipes[selection]                                                           ##selects sandwich with selection name.
            if machine.check_resources(sandwich["ingredients"]):                                    ##Runs check_resources for true value.
                payment = machine.process_coins()                                                   ##Assigns payment to coins from running process_coins.
                if machine.transaction_result(payment, sandwich["cost"]):                           ##Runs transaction_result for true value.
                    machine.make_sandwich(selection, sandwich["ingredients"])                       ##Runs make_sandwich.
        elif selection == "report":                                                                 ##Checks if input is "report".
            for item, amount in resources.items():                                                  ##Iterates through the resource items.
                if item == "bread" or item == "ham":                                                ##Checks if item is "bread" or "ham".
                    print(str(item) + ": " + str(amount) + " slices")                               ##Prints slices.
                else:
                    print(str(item) + ": " + str(amount) + " ounces")                               ##Prints ounces(cheese).
        elif selection == "off":                                                                    ##Checks if input is "off".
            print("Turning off the sandwich machine.")
            break                                                                                   ##End program with code 0.
        elif selection == "add":                                                                    ##Checks if input is "add". Added to maintain steady resource amount without program re-execution.
            add_bread = int(input("How many bread slices would you like to add? "))                 ##Input bread to add.
            add_ham = int(input("How many ham slices would you like to add? "))                     ##Input ham to add.
            add_cheese = int(input("How many cheese ounces would you like to add? "))               ##Input cheese to add.
            machine.add_resources({"bread": add_bread, "ham": add_ham, "cheese": add_cheese})       ##Runs add_resources with amounts.
        else:
            print("Sorry, that's not a valid option.")                                              ##Error check.

if __name__ == "__main__":
    main()