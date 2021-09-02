# My stuff

import sqlite3

class Database:
    def __init__(self, path: str):
        self.db = sqlite3.connect(path)
        self.db.cursor().execute("CREATE TABLE IF NOT EXISTS todo (task TEXT NOT NULL)")
        self.db.commit()

    def addTask(self, task: str):
        self.db.cursor().execute(f"INSERT INTO todo (task) VALUES (?)", (task,))
        self.db.commit()

    def removeTask(self, task: str): 
        self.db.cursor().execute(f"DELETE FROM todo WHERE task = ?", (task,))
        self.db.commit()

    def listTasks(self) -> str:
        out = ""
        for task in self.db.cursor().execute("SELECT * FROM todo"):
            out += str(task[0]) + "\n"
        return out
    
    def clearDb(self):
        cur = self.db.cursor()
        cur.execute("DROP TABLE todo") 
        cur.execute("CREATE TABLE IF NOT EXISTS todo (task TEXT NOT NULL)")
        self.db.commit()
