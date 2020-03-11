# Write a class to hold player information
# Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a Room


# name
# location
# inventory
# on_drop
# on_take
# score

import room


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.location = starting_room
        self.inventory = []

        def on_drop(self, item):
            if item in inventory:
                self.inventory.remove(item)
                print(f"You have dropped {item}")

        def on_take(self, item):
            if item in location:
                self.inventory.append(item)
                print(f"You now have {item} in your inventory")
