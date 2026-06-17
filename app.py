# =====================================================
# IMPORTAÇÕES
# =====================================================

# Importa a classe Flask para criar o servidor web.
# Importa render_template para enviar páginas HTML.
# Importa request para acessar dados enviados pelo usuário.
from flask import Flask, render_template, request

# Importa a biblioteca requests.
# Ela permite fazer requisições para APIs na internet.
import requests


# =====================================================
# CRIAÇÃO DA APLICAÇÃO FLASK
# =====================================================

# Cria uma instância da aplicação Flask.
#
# __name__ informa ao Flask qual arquivo está sendo executado.
#
# A partir deste objeto "app" criaremos rotas,
# páginas e funcionalidades do sistema.
app = Flask(__name__)


# =====================================================
# CHAVE DA API
# =====================================================

# Chave fornecida pelo OpenWeatherMap.
#
# Ela funciona como uma identificação da sua aplicação.
#
# Sempre que sua aplicação consultar a API,
# esta chave será enviada.
API_KEY = "89e33f84a3addad4b2fbe12b61e2842d"


# =====================================================
# ROTA PRINCIPAL
# =====================================================

# Define a rota principal do sistema.
#
# Quando alguém acessar:
#
# http://127.0.0.1:5000
#
# esta função será executada.
#
# methods=["GET", "POST"]
#
# GET  -> abrir a página
# POST -> enviar uma busca
@app.route("/", methods=["GET", "POST"])


# =====================================================
# FUNÇÃO PRINCIPAL
# =====================================================

def index():

    # Variável que armazenará os dados do clima.
    #
    # Inicialmente não existe clima.
    clima = None

    # Variável que armazenará mensagens de erro.
    #
    # Inicialmente não existe erro.
    erro = None


    # ==============================================
    # VERIFICA SE O USUÁRIO ENVIOU O FORMULÁRIO
    # ==============================================

    if request.method == "POST":

        # Obtém o valor digitado no campo:
        #
        # <input name="cidade">
        #
        # Se o usuário digitou:
        #
        # Porto Alegre
        #
        # cidade receberá:
        #
        # "Porto Alegre"
        cidade = request.form.get("cidade")


        # ==========================================
        # VERIFICA SE A CIDADE FOI INFORMADA
        # ==========================================

        if cidade:

            # Monta a URL da API.
            #
            # Exemplo final:
            #
            # https://api.openweathermap.org/data/2.5/weather?q=Porto Alegre&appid=CHAVE
            #
            # q = cidade pesquisada
            # appid = chave da API
            # units=metric = Celsius
            # lang=pt_br = português
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={cidade}"
                f"&appid={API_KEY}"
                f"&units=metric"
                f"&lang=pt_br"
            )


            # ======================================
            # TENTA CONSULTAR A API
            # ======================================

            try:

                # Faz uma requisição GET para a API.
                #
                # A resposta será armazenada em "resposta".
                resposta = requests.get(url)


                # ==================================
                # VERIFICA SE A API RESPONDEU OK
                # ==================================

                if resposta.status_code == 200:

                    # Converte o JSON retornado pela API
                    # para um dicionário Python.
                    #
                    # Exemplo:
                    #
                    # {
                    #     "name":"Porto Alegre",
                    #     "main":{"temp":18}
                    # }
                    #
                    clima = resposta.json()

                else:

                    # Se o código não for 200,
                    # normalmente significa que a cidade
                    # não foi encontrada.
                    erro = "Cidade não encontrada."


            # ======================================
            # ERROS DE CONEXÃO
            # ======================================

            except requests.exceptions.RequestException:

                # Caso a internet esteja indisponível
                # ou a API esteja fora do ar.
                erro = "Erro ao conectar à API de clima."


    # =================================================
    # ENVIA DADOS PARA O HTML
    # =================================================

    # Renderiza o arquivo:
    #
    # templates/index.html
    #
    # E envia duas variáveis:
    #
    # clima
    # erro
    #
    return render_template(
        "index.html",
        clima=clima,
        erro=erro
    )


# =====================================================
# INÍCIO DA EXECUÇÃO
# =====================================================

# Executa somente se este arquivo
# estiver sendo iniciado diretamente.
if __name__ == "__main__":

    # Inicia o servidor Flask.
    #
    # debug=True:
    #
    # - reinicia automaticamente ao salvar
    # - mostra erros detalhados
    app.run(debug=True)