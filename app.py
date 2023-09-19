import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GerenciadorBancoDados:
    def __init__(self):
        self.conn = sqlite3.connect('senhas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                cpf TEXT,
                rg TEXT,
                pais TEXT,
                cidade TEXT,
                bairro TEXT,
                numero_casa TEXT,
                senha TEXT
            )
        ''')
        self.conn.commit()

    def salvar_usuario(self, nome, cpf, rg, pais, cidade, bairro, numero_casa, senha):
        self.cursor.execute('INSERT INTO usuarios (nome, cpf, rg, pais, cidade, bairro, numero_casa, senha) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                            (nome, cpf, rg, pais, cidade, bairro, numero_casa, senha))
        self.conn.commit()

    def fechar(self):
        self.conn.close()

class GerenciadorSenhasApp(App):
    def build(self):
        self.db_manager = GerenciadorBancoDados()

        layout = BoxLayout(orientation='vertical', padding=20)

        titulo = Label(text='Gerenciador de Senhas', font_size=24)
        layout.add_widget(titulo)

        nome_input = TextInput(hint_text='Nome')
        cpf_input = TextInput(hint_text='CPF')
        rg_input = TextInput(hint_text='RG')
        pais_input = TextInput(hint_text='País')
        cidade_input = TextInput(hint_text='Cidade')
        bairro_input = TextInput(hint_text='Bairro')
        numero_casa_input = TextInput(hint_text='Número de Casa')
        senha_input = TextInput(hint_text='Digite sua senha', password=True)

        layout.add_widget(nome_input)
        layout.add_widget(cpf_input)
        layout.add_widget(rg_input)
        layout.add_widget(pais_input)
        layout.add_widget(cidade_input)
        layout.add_widget(bairro_input)
        layout.add_widget(numero_casa_input)
        layout.add_widget(senha_input)

        botao_cadastrar = Button(text='Cadastrar')
        botao_cadastrar.bind(on_press=lambda instance: self.cadastrar_usuario(nome_input.text))
        layout.add_widget(botao_cadastrar)

        self.confirmacao_label = Label(text='', font_size=18)
        layout.add_widget(self.confirmacao_label)

        return layout

    def cadastrar_usuario(self, nome):
        self.db_manager.salvar_usuario(nome, '', '', '', '', '', '', '')
        self.confirmacao_label.text = f'Cadastro de "{nome}" feito com sucesso'

    def on_stop(self):
        self.db_manager.fechar()

if __name__ == '__main__':
    GerenciadorSenhasApp().run()



              