from itertools import tee
from tkinter import END, Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button
import back as back

id=None
nota_selecionada = None
janela_alterar = None
janela_incluir = None

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
    

root = Tk()
root.title("**** SUAS NOTAS *****")
width = 900
height = 400

sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#Cor da janela principal
root.config(bg='#addf98')

l1 = Label(root, font=("Roboto", 16), text="Título", fg='#000000', bg='#addf98')
l1.grid(row=0, column=0, columnspan=2)

l2 = Label(root, font=("Roboto", 16),text="Autor", fg='#000000',bg='#addf98')
l2.grid(row=1, column=0, columnspan=2) 


l3 = Label(root, font=("Roboto", 16), text="Conteúdo", fg='#000000', bg='#addf98')
l3.grid(row=2, column=1, columnspan=2)  

# Entradas
titulo = StringVar()
e1 = Entry(root, textvariable=titulo, width=30)
e1.grid(row=0, column=1, columnspan=2)  

autor = StringVar()
e2 = Entry(root, textvariable=autor, width=30)
e2.grid(row=1, column=1, columnspan=2)  

conteudo = StringVar()
e3 = Entry(root, textvariable=conteudo, width=80)
e3.grid(row=3, column=1, columnspan=2)  

# Listbox
list1 = Listbox(root, height=8, width=100)
list1.grid(row=6, column=0, columnspan=4)  



list1.bind('<<ListboxSelect>>', get_linha_selecionada)

# Botões
b3 = Button(root, font=("Roboto", 8),text="Incluir", width=22, bg="#81be6f", command=adicionar_nota)
b3.grid(row=1, column=3, padx=10, pady=5)  

b1 = Button(root, font=("Roboto", 10),text="Exibir todos", width=22, bg="snow", command=visualizar_nota)
b1.grid(row=5, column=0, padx=20, pady=5)  

b4 = Button(root, font=("Roboto", 10),text="Atualizar Selecionado", width=22, bg="snow", command=atualizar_nota)
b4.grid(row=7, column=0, padx=20, pady=5)  

b5 = Button(root, font=("Roboto", 8),text="Deletar Selecionado", bg="firebrick4", width=22, command=apagar_nota)
b5.grid(row=7, column=2, padx=20, pady=5) 

b6 = Button(root, font=("Roboto", 8),text="Fechar", width=22, bg="#a8a8a8", command=root.destroy)
b6.grid(row=8, column=3, padx=5, pady=5) 



root.mainloop()

































# root = Tk()
# root.title("Bloco de Notas")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# root.mainloop()


#Cria uma janela
#root = tk.Tk()
#root.title("Bloco de Notas")
#Cria um rótulo
#label = tk.Label(root, text="Olá, bem vindo(a) ao bloco de notas!")
#label.pack()



#botao = tk.Button(root, text="Adicionar")
#botao.pack()
#Inicia o loop principal da aplicação
#root.mainloop()

#def inserir_note():
#    label.config(text="Botão clicado!")