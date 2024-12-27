import sys
from Pyside6.QtWidgets import QApplication
from game_window  import GameWindow

if __name == "__main__":
  app = QApplication(sys.argv)
  window = GameWindow()
  window.show()
  sys.exit(app.exec())
  
