# Write a class to hold player information, e.g. what room they are in
# currently.

class player:
    def __init__(self, id, current_loc):
        self.id = id
        self.current_loc = current_loc
        
    def getCurrentLocation(self):
        print(f'\n***** Current Room: {self.current_room.name} *****\n')
        print(f'\n***** Current Description: {self.current_room.description} *****\n')
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
        if (direction in ['n', 's', 'e', 'w'] and self.current_loc.['%d_to' % direction]):
            self.current_room = self.current_room.n_to
            self.getCurrentRoom()
        else: print("There are no rooms that way!")
