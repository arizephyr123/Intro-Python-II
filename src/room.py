# Implement a class to hold room information. This should have name and
# description attributes.
# Put the Room class in `room.py` based on what you see in `adv.py`.

#   * The room should have `name` and `description` attributes.

#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.

# * The `Room` class should be extended with a `list` that holds the `Item`s
# that are currently in that room.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None


def __str__(self):
    return f"{self.name}/n{self.desc}"
