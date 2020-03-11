# where the main logic for the game should live
# Add a REPL parser to `adv.py` that accepts directional commands to move the player
#   * After each move, the REPL should print the name and description of the player's current room
#   * Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
#   * The parser should print an error if the player tries to move where there is no room.
# Add functionality to the main loop that prints out all the items that are
# visible to the player when they are in that room.

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


# * Add the `i` and `inventory` commands that both show a list of items currently
#   carried by the player.


from room import Room
from player import Player
# from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together aka 'associations'

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player1 = Player("Steve", "outside")
player = Player(input("Enter player name: "), room['outside'])

# Write a loop that:
#
#

#

while True:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    print(f"{player.name} you are in the {player.location.name}.\n\n{player.location.desc}")
    cmd = input("\n\nWhich direction would you like to go next?")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
# if input == 'q' or 'quit'
