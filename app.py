# Importa a classe Flask da biblioteca flask
# Sem essa linha, o Python não sabe o que é "Flask"
from flask import Flask, render_template

# Cria a instância da aplicação Flask
# __name__ é uma variável especial do Python que contém o nome do módulo atual
# O Flask usa isso para saber onde procurar os templates e arquivos estáticos
app = Flask(__name__)


# O decorador @app.route define qual URL aciona esta função
# '/' é a rota raiz — o endereço principal do site (ex: http://localhost:5000/)
@app.route('/')
def home():
    # Esta função retorna o que o navegador vai receber como resposta
    # Por enquanto, retornamos uma string HTML simples
    return render_template('index.html')

@app.route('/revisao')
def revisao():
    return '''
    <h1>Revisão</h1>
    <p>Conteúdo da página de revisão.</p>
    <p style="color: red;">Esta é uma mensagem de revisão importante!</p>
    '''

@app.route('/revisao/<nome>/<int:idade>')
def parametros(nome, idade):
    ano_nascimento = 2026 - idade
    return f'''
    <h1>Revisão</h1>
    <p style="color: blue;">Olá, {nome}! Você tem {idade} anos.</p>
    <p>Seu ano de nascimento é {ano_nascimento}.</p>
    '''

# Bloco de execução: só roda quando o arquivo é executado diretamente
if __name__ == '__main__':
    # debug=True ativa o recarregamento automático ao salvar o arquivo
    # NUNCA use debug=True em produção (servidor público)
    app.run(debug=True)