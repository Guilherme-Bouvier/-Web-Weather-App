# 🌤️ Web Weather App

Aplicação web desenvolvida com **Flask + Python + Jinja2 + Bootstrap**, que consome a API do OpenWeatherMap para exibir informações climáticas em tempo real de qualquer cidade do mundo.

---

## 🚀 Demonstração

O usuário pode:
- Pesquisar qualquer cidade
- Ver temperatura atual
- Ver descrição do clima
- Ver umidade e velocidade do vento

---

## 🧠 Tecnologias utilizadas

- Python 🐍
- Flask 🌐
- Requests 🔗
- HTML5 🧱
- CSS3 🎨
- Bootstrap 5 💙
- Jinja2 (templates dinâmicos)

---
# 📁 Estrutura do Projeto

```
Web Weather App/
├── app.py
│   
└── templates/
│   └── index.html
│
└── requirements.txt   
│   
└── license
│    
└── readme.md
│    
└── .gitignore
│    
└── Video Explicação 

```

## ⚙️ Como funciona

### 1. Usuário acessa o site
A rota principal `/` abre a página inicial com um campo de busca.

---

### 2. Usuário pesquisa uma cidade
O formulário envia uma requisição:

- Método: `POST`
- Campo: `cidade`

---

### 3. Backend consulta API
O Flask:

- Recebe o nome da cidade
- Monta URL da OpenWeatherMap
- Usa `requests.get()`
- Retorna JSON com dados climáticos

---

### 4. Dados exibidos na tela

São mostrados:

- 🌡 Temperatura (°C)
- 🌤 Descrição do clima
- 💧 Umidade
- 🌬 Velocidade do vento
- 🏙 Nome da cidade e país

---

## 🌐 API utilizada

OpenWeatherMap:


https://openweathermap.org/api


Você precisa de uma API Key gratuita para funcionamento.

## 🔑 Configuração da API

No arquivo app.py:

API_KEY = "SUA_CHAVE_AQUI"

## ▶️ Como executar o projeto
1. Instalar dependências
python -m pip install flask requests

2. Executar servidor
python app.py

3. Acessar no navegador
http://127.0.0.1:5000

## 📦 Funcionalidades
✔ Busca de clima em tempo real
✔ Integração com API externa
✔ Interface responsiva (Bootstrap 5)
✔ Tratamento de erros (cidade não encontrada)
✔ Design dark moderno

## ⚠️ Possíveis erros
Cidade não encontrada
Verifique ortografia
Tente nomes internacionais
Erro de conexão
Verifique internet
Verifique API Key

## 📈 Melhorias futuras

🌡 Sensação térmica (feels_like)
🌅 Nascer e pôr do sol
📊 Previsão de 5 dias
🎨 Fundo dinâmico conforme clima
🔘 Botões clicáveis no histórico
⭐ Sistema de favoritos

## 👨‍💻 Autor

Guilhrme Bouvier. Projeto desenvolvido para estudo de:

Flask
Consumo de APIs
Desenvolvimento web full stack básico

##🏁 Status

✔ Projeto funcional
✔ Pronto para evolução
✔ Base sólida para portfólio
---
