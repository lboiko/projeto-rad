from itertools import tee
import sqlite3
import tkinter as tk
from tkinter import END, Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button, ttk, Toplevel, messagebox, Frame
import back as back

id=None
nota_selecionada = None
janela_alterar = None
janela_incluir = None

root = Tk()
root.title("─────•「  Your notes!  」 •─────")
treeview = ttk.Treeview()
width = 900
height = 400

def get_linha_selecionada(event):
    global nota_selecionada
    index = list1.curselection()[0]
    nota_selecionada = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, nota_selecionada[1])
    e2.delete(0, END)
    e2.insert(END, nota_selecionada[2])
    e3.delete(0, END)
    e3.insert(END, nota_selecionada[3])
        
def visualizar_nota():
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)

def procurar_nota():
    list1.delete(0, END)
    for row in back.search(titulo.get(), autor.get(), conteudo.get()):
        list1.insert(END, row)

def adicionar_nota():
    back.insert(titulo.get(), autor.get(),
                   conteudo.get())
    list1.delete(0, END)
    list1.insert(END, (titulo.get(), autor.get(),
                       conteudo.get()))
    
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    visualizar_nota()

def apagar_nota():
    if nota_selecionada:
        back.delete(nota_selecionada[0])
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        visualizar_nota()
    else:
        print("Nenhuma nota selecionada para apagar.")
        
def atualizar_nota():
    back.update(nota_selecionada[0], titulo.get(
    ), autor.get(), conteudo.get())
    
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    visualizar_nota()

def abrir_treeview():
    
    janela_treeview = Toplevel(root)
    janela_treeview.title("Notas")
    
    tree = ttk.Treeview(janela_treeview, columns=("Título", "Autor", "Conteúdo"), show="headings")
    tree.heading("Título", text="Título")
    tree.heading("Autor", text="Autor")
    tree.heading("Conteúdo", text="Conteúdo")
    tree.column("Título", anchor="w", width=200)
    tree.column("Autor", anchor="w", width=150)
    tree.column("Conteúdo", anchor="w", width=250)
    tree.pack(fill='both', expand=True)
    
    for row in back.view(): 
        tree.insert("", END, values=row)

def load_data():    
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()    
    try:        
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()        
        list1.delete(0, tk.END)
        for row in rows:
                list1.insert(tk.END, f"{row[0]} - {row[1]}")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {e}")
    finally:
        conn.close()

frame_listbox = tk.Frame(root)
frame_listbox.grid(row=7, column=0, columnspan=4, pady=10)

list1 = tk.Listbox(frame_listbox, height=8, width=100)
list1.pack(side='left', fill='both', expand=True)

sb1 = tk.Scrollbar(frame_listbox)
sb1.pack(side='right', fill='y')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_linha_selecionada)

load_data()

# Menu
menu_principal = tk.Menu(root)

def sair():
    root.quit()
    
menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)
menu_arquivo.add_separator()

menu_principal.add_cascade(label="Menu", menu=menu_arquivo)

root.config(menu=menu_principal)


# Estilo janela principal e das labels
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

root.config(bg='#a2999e')

l1 = Label(root, font=("Roboto", 16), text="Título", fg='#000000', bg='#a2999e')
l1.grid(row=0, column=0, columnspan=2)

l2 = Label(root, font=("Roboto", 16),text="Autor", fg='#000000',bg='#a2999e')
l2.grid(row=1, column=0, columnspan=2) 

l3 = Label(root, font=("Roboto", 16), text="Digite aqui sua nota:", fg='#000000', bg='#a2999e')
l3.grid(row=2, column=1, columnspan=2)


# Entrys
titulo = StringVar()
e1 = Entry(root, textvariable=titulo, width=30)
e1.grid(row=0, column=1, columnspan=2)  

autor = StringVar()
e2 = Entry(root, textvariable=autor, width=30)
e2.grid(row=1, column=1, columnspan=2)  

conteudo = StringVar()
e3 = Entry(root, textvariable=conteudo, width=80)
e3.grid(row=3, column=1, columnspan=2)  

# Botões
b3 = Button(root, font=("Roboto", 9),text="Incluir", width=22, bg="#846a6a", command=adicionar_nota)
b3.grid(row=1, column=3, padx=10, pady=5)  

b1 = Button(root, font=("Roboto", 8),text="Exibir todos", width=22, bg="snow", command=abrir_treeview)
b1.grid(row=5, column=0, padx=20, pady=5)  

b4 = Button(root, font=("Roboto", 10),text="Atualizar Selecionado", width=22, bg="#f3e2d6", command=atualizar_nota)
b4.grid(row=8, column=1, padx=20, pady=5)  

b5 = Button(root, font=("Roboto", 10),text="Deletar Selecionado", bg="#757283", width=22, command=apagar_nota)
b5.grid(row=8, column=2, padx=20, pady=5) 

b6 = Button(root, font=("Roboto", 8),text="Fechar", width=22, bg="#f5ebe7", command=root.destroy)
b6.grid(row=9, column=3, padx=5, pady=5) 

root.mainloop()