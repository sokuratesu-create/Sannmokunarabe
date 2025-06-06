from flask import Flask, render_template, request

app = Flask(__name__)

# 空のボード（3x3）
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "〇"

@app.route("/", methods=["GET", "POST"])
def index():
    global board, current_player
    if request.method == "POST":
        row = int(request.form["row"])
        col = int(request.form["col"])
        if board[row][col] == "":
            board[row][col] = current_player
            current_player = "×" if current_player == "〇" else "〇"
    return render_template("index.html", board=board)

if __name__ == "__main__":
    app.run(debug=True)