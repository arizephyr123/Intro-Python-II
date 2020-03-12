# Write a class to hold player information
# Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a Room


# name
# current_room
# inventory
# on_drop
# on_take


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(
                self.current_room, f"{direction}_to")
        else:
            print("You cannot move in that direction.")

    def player_inventory(self):
        if len(self.inventory) == 0:
            print(f"\n\n{self.name}'s inventory is empty.\n")

    def on_drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You have dropped {item}")

    def on_take(self, item):
        if item in self.current_room:
            self.inventory.append(item)
            print(f"You now have {item} in your inventory")
