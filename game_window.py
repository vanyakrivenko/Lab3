from PySide6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox

class GameWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("X-0")
    self.setGeometry(100, 100, 400, 400)
    self.current_player = "X"
    self.board = [[None for _ in range(3)] for _ in range(3)]
    self.initUI()

  def initUI(self):
    self.central_widget = QWidget()
    self.setCentralWidget(self.central_widget)
    
    self.layout = QGridLayout()
    self.central_widget.setLayout(self.layout)

    self.buttons = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
      for j in range(3):
        button = QPushButton()
        button.setFixedSize(100, 100)
        button.setStyleSheet("font-size: 24 px;")
        button.clicked.connect(lambda _, row = i, col = j: self.make_move(row, col))
        self.layout.addWidget(button, i ,j)
        self.buttons[i][j] = button

  def make_move(self, row,col):
    if self.board[row][col] is None:
      self.board[row][col] = self.current_player
      self.buttons[row][col].setText(self.current_player)
      self.buttons[row][col].setEnabled(False)

      if self.check_winner():
        QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
        self.reset_game()
      elif self.check_draw():
        QMessageBox.information(self, "Game Over", "It is a draw!")
        self.reset_game()
      else:
        self.current_player = "0" if self.current_player == "X" else "X"

  def check_winner(self):
    for i in range(3):
      if self.board[i][0] == self.board[i][1] == self.board[i][2] != None:
        return True
      if self.board[0][i] == self.board[1][i] == self.board[2][i] != None:
        return True
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
        return True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
        return True

    return False

  def check_draw(self):
    for row in self.board:
      if None in row:
        return False
    return True

  def reset_game(self):
    self.current_player = "X"
    self.board = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
      for j in range(3):
        self.buttons[i][j].setText("")
        self.buttons[i][j].setEnabled(True)
      
      
        
        
        
