import sqlite3

def connect():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor TEXT NOT NULL, conteudo TEXT NOT NULL)")        
    conn.commit()
    conn.close()

def check_table():
    connect()
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notes';")
    exists = cursor.fetchone()
    conn.close()
    return exists is not None

if check_table():
    print("A tabela 'notes' existe.")
else:
    print("A tabela 'notes' não existe.")
#Inserir nota

def insert(titulo, autor, conteudo):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes VALUES(NULL,?,?,?)",
                   (titulo, autor, conteudo))
    conn.commit()
    conn.close()

def search(titulo="", autor="", conteudo=""):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor
    cursor.execute("SELECT * FROM notes WHERE titulo=? OR autor=? OR conteudo=?",(titulo,autor,conteudo))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, titulo, autor, conteudo):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET titulo=?, autor=?, conteudo=? WHERE id=?",
                   (titulo, autor, conteudo, id))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("notes.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes")
    rows = cur.fetchall()
    conn.close()
    return rows