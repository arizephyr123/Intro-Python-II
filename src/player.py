# Write a class to hold player information
# Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a

# Add a new type of sentence the parser can understand: two words.

#   * Until now, the parser could just understand one sentence form:

#      `verb`

#     such as "n" or "q".

#   * But now we want to add the form:

#     `verb` `object`

#     such as "take coins" or "drop sword".

#   * Split the entered command and see if it has 1 or 2 words in it to determine
#     if it's the first or second form.

# * Implement support for the verb `get` followed by an `Item` name. This will be
#   used to pick up `Item`s.

#   * If the user enters `get` or `take` followed by an `Item` name, look at the
#     contents of the current `Room` to see if the item is there.

#      * If it is there, remove it from the `Room` contents, and add it to the
#        `Player` contents.

#      * If it's not there, print an error message telling the user so.


#      * Add an `on_take` method to `Item`.

#         * Call this method when the `Item` is picked up by the player.

#         * `on_take` should print out "You have picked up [NAME]" when you pick up an item.

#         * The `Item` can use this to run additional code when it is picked up.

#      * Add an `on_drop` method to `Item`. Implement it similar to `on_take`.

# * Implement support for the verb `drop` followed by an `Item` name. This is the
#   opposite of `get`/`take`.

# * Add the `i` and `inventory` commands that both show a list of items currently
#   carried by the player.

# name
# location
# inventory
# on_drop
# on_take
# score

class Player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

        def on_drop(self, item):
            if item in inventory:
                inventory.remove(item)
                print(f"You have dropped {item}")
        
        def on_take(self, item):
            if item in location:
                inventory.append(item)
                print(f"You now have {item} in your inventory")
