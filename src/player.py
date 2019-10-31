# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, id, current_loc):
        self.id = id
        self.current_loc = current_loc
        self.bag = []
        
    def getCurrentLocation(self):
        print(f'***************\n*** Current Room: {self.current_loc.name}\n*** Current Room Description: {self.current_loc.desc}\n***************')
        if self.bag:
            print('***** Items in your bag: ',{item.name for item in self.bag})
        if self.current_loc.items:
            print('***** Items in this room: ',{item.name for item in self.current_loc.items})
            
    #  Break Glass incase of emergency, I don't like that legit almost everyline is a repetition Working on lower solution instead  
    # def noRooms(self):
    #     print("There are no more rooms in that directions. Try a different direction.")
        
    # def move(self, direction):
    #     if (direction == 'n'):
    #         if (self.current_room.n_to):
    #             self.current_room = self.current_room.n_to
    #             self.getCurrentRoom()
    #         else:
    #             self.noRooms()
    #     elif (direction == 's'):
    #         if (self.current_room.s_to):
    #             self.current_room = self.current_room.s_to
    #             self.getCurrentRoom()
    #         else:
    #             self.noRooms()
    #     elif (direction == 'e'):
    #         if (self.current_room.e_to):
    #             self.current_room = self.current_room.e_to
    #             self.getCurrentRoom()
    #         else:
    #             self.noRooms()
    #     elif (direction == 'w'):
    #         if (self.current_room.w_to):
    #             self.current_room = self.current_room.w_to
    #             self.getCurrentRoom()
    #         else:
    #             self.noRooms()
        
    def move(self, direction):
        if (getattr(self.current_loc, f'{direction}_to')):
            self.current_loc = getattr(self.current_loc, f'{direction}_to')
            self.getCurrentLocation()
        else: print("There are no rooms that way!")
        
    def loot(self, item):
        for itemObj in self.current_loc.items:
            if itemObj.name.lower() == item:
                self.current_loc.items.remove(itemObj)
                self.bag.append(itemObj)
                print(f'You have picked up {item}.')
        
    def store(self, item):
        for itemObj in self.bag:
            if itemObj.name.lower() == item.lower():
                self.bag.remove(itemObj)
                self.current_loc.items.append(itemObj)
                print(f'You have dropped up {item}.')

