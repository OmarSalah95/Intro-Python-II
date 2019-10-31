from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#  Drop Items in Rooms
room['outside'].items = [Item("Bat", "This is for my own protection, and homeruns"),Item("Cubbard", "It is the best way to keep those valuable dishes safe."),Item("Table", "-"),Item("Dog Food", "Gotta feed the DOggos"),Item("Garbage", "The trash can is too far away, you know in the driveway and all.")]
room['foyer'].items = [Item("Car", "You see what had happened was... I was trying to park and it was dark, and well I missed the garage."),Item("TV", "How I spend all my free time"),Item("Chair", "These chairs actually suck, they have no padding"),Item("Speakers", "I like my music real loud"),Item("Expired Cheese", "Dang this stuff stinks!")]
room['narrow'].items = [Item("Axe", "I will leave this one to your imagination"),Item("Sofa", "Also known as the best napping location in the place"),Item("Refrigerator", "How else could I keep my food cold? BTW is your fridge running???? If it is you should go catch it!"),Item("Battery", "I can use this to turn my car on!"),Item("Box", "The second best method of transporting stuff/things")]
room['treasure'].items = [Item("Grandma", "She is always loitering around somewhere."),Item("Computer", "This is where the magic happens... Literally I am a software engineer and have no idea how this thing works."),Item("My Patience", "I lost this a long long time ago.... Don't judge me."),Item("Gold", "Keep It Secret"),Item("Platinum", "keep it safe")]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(1, room['outside'])
player1.getCurrentLocation()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

game_active = True
while game_active:
    directions = ['n', 's', 'e', 'w']
    userInput = input("\n\nWhat is your next Play? ")
    print(100*"~")
    if (userInput == 'q'):
        conf = input("Are you sure you want to quit?(Y/N) ")
        if (conf.upper() == 'Y'):
            print("Game is being quit...")
            game_active = False
        else:
            print("Good choice lets go again!")
            continue
    elif (userInput.lower() =='loot'):
        if player1.current_loc.items:
            itemNames = {item.name.lower() for item in player1.current_loc.items}
            for item in player1.current_loc.items:
                item.getItem() 
            item = input("\n\nWhat is it we will be plundering from this room? ").lower()
            if item.lower() in itemNames:
                player1.loot(item)
            else:
                print("That item is actually not in this room!")
        else:
            print("It Seems this room has nothing worth taking")
            continue
    elif (userInput.lower() =='store'):
        if player1.bag:
            itemNames = {item.name.lower() for item in player1.bag}
            for item in player1.bag:
                item.getItem() 
            item = input("\n\nWhat is it we will storing in this room? ")
            if item.lower() in itemNames:
                player1.store(item)
            else:
                print("That item is actually not in your bag!")
        else:
            print("It Seems your bag is Empty, let's go fill it!")
            continue
    elif (userInput in directions):
        player1.move(userInput)
    else:
        print('That Command was invalid.')