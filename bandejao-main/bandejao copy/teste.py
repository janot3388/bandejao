import db, sqlite3

def admprint():
    db = sqlite3.connect('db.sqlite') 
    c = db.cursor()
    c.execute("SELECT * FROM alocados")  

    for row in c:
    
        print(row)

admprint()


from control import Fila
