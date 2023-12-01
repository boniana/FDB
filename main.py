from database.db import Session
from gui.Home.Home import Application
from database.dados import create_dados

if __name__ == "__main__":
    s = Session()
    if s.createNewDados:
        create_dados()
    app = Application()
    app.mainloop()
    