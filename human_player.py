class HumanPlayer:
    
    def __init__(self,value):
        self.value=value


    def get_move(self):
        print("hello {}, please type your move (row, col)".format(self.value))
        row=input("row: ")
        column=input("column: ")
        return (row, column)

