# * Create a file called `item.py` and add an `Item` class in there.

#   * The item should have `name` and `description` attributes.

#      * Hint: the name should be one word for ease in parsing later.

#   * This will be the _base class_ for specialized item types to be declared
#     later.

# * Add the ability to add items to rooms.

#      * Add an `on_take` method to `Item`.

#         * Call this method when the `Item` is picked up by the player.

#         * `on_take` should print out "You have picked up [NAME]" when you pick up an item.

#         * The `Item` can use this to run additional code when it is picked up.

#      * Add an `on_drop` method to `Item`. Implement it similar to `on_take`.

# * Implement support for the verb `drop` followed by an `Item` name. This is the
#   opposite of `get`/`take`.

        # def on_drop(self, item):
        #     if item in self.inventory:
        #         self.inventory.remove(item)
        #         print(f"You have dropped {item}")

        # def on_take(self, item):
        #     if item in self.current_room:
        #         self.inventory.append(item)
        #         print(f"You now have {item} in your inventory")
 class Item:
     def __init__(self, name, desc, starting_room):
         self.name = name
         self.desc = desc
         self.location = starting_room
    def 
