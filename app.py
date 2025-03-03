from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_player = 'X'
        self.wining_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
            (0, 4, 8), (2, 4, 6) # Diagonal
        ]

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] == self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self):
        for combination in self.wining_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None
    
    def get_winning_combinations(self):
        for combination in self.wining_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return combination
        return None
    
    def reset_game(self):
        self.board = [' ']*9
        
game = TicTacToe()


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)