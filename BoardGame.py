
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize board for checkers

def initial_board():
    board = [['' for _ in range(8)] for _ in range(8)]
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = 'P2'
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = 'P1'
    return board

board_state = initial_board()

@app.route('/')
def index():
    return render_template('index.html', board=board_state)

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    from_pos = data['from']
    to_pos = data['to']
    fr = 8 - int(from_pos[1])
    fc = ord(from_pos[0]) - ord('a')
    tr = 8 - int(to_pos[1])
    tc = ord(to_pos[0]) - ord('a')
    piece = board_state[fr][fc]
    board_state[fr][fc] = ''
    board_state[tr][tc] = piece
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
