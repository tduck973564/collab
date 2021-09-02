# THIS MUST BE TYPE HINTED
# INSTALL MYPY

from types import *
import cmdparser
import database

if __name__ == "__main__":
    print("Initializing the Greatest ToDo app ever created...")
    db = database.Database(input("Type the name of the todo list to open or create >> "))
    while True:
        a = input(">> ")
        cmdparser.parse(a, db)
 