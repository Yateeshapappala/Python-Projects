class game():
    def __init__(self):
        self.game={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
        def set_items(self,user,position,game):
            game [position]=user
            return game
        def gameboard(self):
            return self.game
        def clear(self):
            self.game={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
        def is_place_taken(self,game,index):
            if game[index]!='':
                return True
            
        def is_board_full
        