""" File: connect_n_state.py
    Author: Aiden Foster
    Class: CSC 120
    Purpose: To run in connection with a given file that will play
             the game connect n in the background to finish the file.
"""
class Connect_N_State:
    """ This class resprsents the logistical processing behind the 
        connect n game.

       The constructor creates the variables that we can use to make 
       the grid and the variables we will use to manipulate whos turn 
       it is on the board.

       The class defines several helpful methods and fields:
           get_size()        - get the size of the board.
           get_target()      - get the target length.
           get_player_list() - get the player list.
           is_game_ovevr()   - check if someone has won or the board is full.
           get_winner()      - return the winner of the game.
           is_board_full()   - check if the board is full.
           is_column_full()  - check if the comlumn is full.
           get_cell()        - if there is a piece at the spot return it.
           get_cur_player()  - return the current players turn.
           move()            - define how to make a move and if it is possible.
           did_someone_win() - check if someone has won the game.
           north()  - check to the north if target length has been met.
           south()  - check to the south if target length has been met.
           west()   - check to the west if target length has been met.
           east()     - check to the east if target length has been met.
           northwest() - check to the northwest if target length has been met.
           southwest() - check to the southwest if target length has been met.
           northeast() - check to the northeast if target length has been met.
           southeast() - check to the southeast if target length has been met.

    """
    def __init__(self, wid, hei, target, players):
        self._wid = wid
        self._hei = hei
        self._target = target
        self._players = players
        self._cur_player = 0

        
        self._grid = []
        for i in range(self._hei):
            height = []
            for k in range(self._wid):
                height.append('.')
            self._grid.append(height)

        
    def get_size(self):
        return (self._wid, self._hei)

    
    def get_target(self):
        return self._target

    
    def get_player_list(self):
        return self._players

    
    def is_game_over(self):
        if self.did_someone_win():
            return True
        elif self.is_board_full():
            return True
        else:
            return False

    
    def get_winner(self):
        if self.did_someone_win():
            self.get_cur_player()
            try:
                return self._players[self._cur_player + 1]
            except IndexError:
                return self._players[0]
        else:
            return None


    def is_board_full(self):
        for i in range(self._hei):
            for k in range(self._wid):
                if self._grid[i][k] == '.':
                    return False
        return True


    def is_column_full(self, col):
        if self._grid[0][col] != '.':
            return True
        else: 
            return False 


    def get_cell(self, x, y):
        counter = self._grid[- 1 - y][x]
        if counter != '.':
            for people in self._players:
                if people[0] == counter:
                    return people
        else:
            return None



    def get_cur_player(self):
        try:
            self._players[self._cur_player]
        except IndexError:
            self._cur_player = 0
        return self._players[self._cur_player]


    def move(self, col):
        if self.is_column_full(col):
            return False
        else: 
            height = -1
            while height < self._hei - 1:
                height += 1
                if self._grid[height][col] != '.':
                    new = self._players[self._cur_player][0]
                    self._grid[height - 1].pop(col)
                    self._grid[height - 1].insert(col, new)
                    height = self._hei
                elif height == self._hei - 1 and \
                self._grid[height][col] == '.':
                    new = self._players[self._cur_player][0]
                    self._grid[height].pop(col)
                    self._grid[height].insert(col, new)
                    height = self._hei
                    
            self.is_game_over()
            self._cur_player += 1
            self.get_cur_player()
            return True
        


    def did_someone_win(self):
        for row in range(self._hei):
            for col in range(self._wid):
                current_piece = self._grid[row][col]
                if current_piece != '.':
                    if self.north(col,row,current_piece):
                        return True 
                    elif self.south(col,row,current_piece):
                        return True
                    elif self.southwest(col,row,current_piece):
                        return True
                    elif self.southeast(col,row,current_piece):
                        return True
                    elif self.northwest(col,row,current_piece):
                        return True
                    elif self.northeast(col,row,current_piece):
                        return True
                    elif self.west(col,row,current_piece):
                        return True
                    elif self.east(col,row,current_piece):
                        return True



    def north(self,col,row,current_piece):
        try:
            if self._grid[row + 1][col] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if self._grid[row + next][col] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False
            

    def south(self,col,row,current_piece):
        try:
            if self._grid[row - 1][col] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if row - next < 0:
                        return False
                    if self._grid[row - next][col] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False

    def northeast(self,col,row,current_piece):
        try:
            if self._grid[row + 1][col + 1] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if self._grid[row + next][col + next] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False

    def southwest(self,col,row,current_piece):
        try:
            if self._grid[row - 1][col - 1] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if row - next < 0 or col - next < 0:
                        return False
                    if self._grid[row - next][col - next] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False

    def northwest(self,col,row,current_piece):
        try:
            if self._grid[row + 1][col - 1] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if col - next < 0:
                        return False
                    if self._grid[row + next][col - next] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False

    def southeast(self,col,row,current_piece):
        try:
            if self._grid[row - 1][col + 1] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if row - next < 0:
                        return False
                    if self._grid[row - next][col + next] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False

    def east(self,col,row,current_piece):
        try:
            if self._grid[row][col + 1] == current_piece:
                total = 2
                next = 2
                while (col + next) <= self._wid:
                    if total == self._target:
                        return True
                    if self._grid[row][col + next] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False
        
    def west(self,col,row,current_piece):
        try:
            if self._grid[row][col - 1] == current_piece:
                total = 2
                next = 2
                while (row + next) <= self._hei:
                    if total == self._target:
                        return True
                    if col - next < 0:
                        return False
                    if self._grid[row][col - next] == current_piece:
                        total += 1
                        next += 1
                    else:
                        return False
        except IndexError:
            return False

    def print(self):
        for y in range(len(self._grid)):
            f = ''.join(self._grid[y])
            # print each line
            print(f)
    

    
