# ===================== BIBLIOTECAS
import urllib3
import tkinter as tk
from tkinter import messagebox
from with_selenium import login_with_selenium
from with_requests import login_with_requests

# ===================== SCRIPT
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def centralizar_janela():
    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (w // 2)
    y = (screen_height // 2) - (h // 2)
    root.geometry(f'+{x}+{y}')

usuario = None
senha = None

# Coleta informações de acesso
def submit():
    global usuario, senha
    usuario_input = entry_usuario.get()
    senha_input = entry_senha.get()

    if usuario_input == '1':
        usuario = 'tomsmith'
    else: usuario = usuario_input

    if senha_input == '1':
        senha = 'SuperSecretPassword!'
    else: senha = senha_input

    root.destroy()  # closes the window

root = tk.Tk()
root.title('Login')
root.resizable(False, False)
root.attributes('-topmost', True)
root.deiconify()
root.lift()
root.focus_force() 

root.after(10, centralizar_janela)

tk.Label(root, text='Digite o usuário (ou 1 para utlizar o padrão de teste):').grid(row=0, column=0, sticky='w', padx=10, pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text='Digite a senha (ou 1 para utlizar o padrão de teste):').grid(row=1, column=0, sticky='w', padx=10, pady=5)
entry_senha = tk.Entry(root, show='*')
entry_senha.grid(row=1, column=1, padx=10, pady=5)

btn_submit = tk.Button(root, text='Enviar', command=submit)
btn_submit.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()


alert_class = []
def usar_selenium():
    root.destroy()
    response = login_with_selenium(usuario,senha)
    response = response.replace('flash ','')
    alert_class.clear()
    alert_class.append(response)

def usar_requests():
    root.destroy()
    response = login_with_requests(usuario,senha)
    alert_class.clear()
    alert_class.append(response)

# Cria a interface gráfica para escolha do método
root = tk.Tk()
root.title('Escolha o método de automação')
root.geometry('300x150')
root.resizable(False, False)
root.attributes('-topmost', True)
root.deiconify()
root.lift()
root.focus_force() 

root.after(10, centralizar_janela)

titulo = tk.Label(root, text='Como você quer fazer o login?', font=('Trebuchet MS', 12))
titulo.pack(pady=20)

# Botões
btn_selenium = tk.Button(root, text='Usar Selenium', width=15, command=usar_selenium)
btn_selenium.pack(pady=5)

btn_requests = tk.Button(root, text='Usar Requests', width=15, command=usar_requests)
btn_requests.pack()

root.mainloop()


if 'success' in alert_class:
    print('\n✅ Login bem sucedido!')
elif 'error' in alert_class or alert_class is None:
    print('\n❌ Login falhou, verifique os dados de acesso e tente novamente.')
else:
    print('\n⚠️ Classe de alerta inesperada:', alert_class)