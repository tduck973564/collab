# Kinetic's stuff

from database import Database

def parse(cmdstr: str, db: Database):
    arr = cmdstr.split()
    if len(arr) < 1: 
        print("Invalid command.")
        return
    cmd = arr.pop(0)
    if cmd == "add":
        todoitem = " ".join(arr)
        print("Adding todo item " + todoitem)
        db.addTask(todoitem)
    elif cmd == "ls":
        print(db.listTasks())
    elif cmd == "rm":
        todoitem = " ".join(arr)
        print("Removing todo item " + todoitem) 
        db.removeTask(todoitem) 
    elif cmd == "exit":
        exit()
    elif cmd == "clear":
        db.clearDb()
        print("Database cleared!")
    elif cmd == "help":
        print("""add\tAdds an entry to the list.
rm\tRemoves an entry from the list.
ls\tLists all entries in the list.
clear\tRemoves all entries from the list.
help\tPrints this message.
exit\tCloses the app.""")
    else:
        print("Invalid command.")
