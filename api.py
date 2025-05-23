import pandas as pd
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, Response
from flask.json import jsonify
 
FILENAME = "lojinha-456714-a0206f7df291.json" 
SPREADSHEET_NAME = "Planilha de Testes - VenDASI"

scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename = FILENAME, 
    scopes = scopes
    )

client = gspread.authorize(creds)
pc = client.open(title = SPREADSHEET_NAME) 

planilhas_vendas  = pc.get_worksheet(0)
planilhas_produtos = pc.get_worksheet(1)

app = Flask(__name__)

def formatar_objeto(linha: int) -> dict:
    return {
        "produtos": [ {
            "nome": linha["PRODUTO"],
            "colecao": linha["Coleção"],
            "tamanho_disp": linha["TAMANHO"],
            "preco_cred": float(linha["PREÇO CARTÃO CRÉDITO"]),
            "preco_deb": float(linha["PREÇO CARTÃO DÉBITO"]),
            "preco_pix": float(linha["PREÇO PIX/DINHEIRO"])
        }
        ]
    }

@app.route("/products", methods=["GET"])
def get_products() -> Response:
    dados = planilhas_produtos.get_all_records()
    formatado = [formatar_objeto(linha) for linha in dados]
    return jsonify(formatado)

@app.route("/sell", methods=["POST"])
def post_sale() -> Response:
    nova_venda = request.json
    linha = [
        nova_venda["DATA"],
        nova_venda["PRODUTO"],
        nova_venda["TAMANHO"],
        nova_venda["FORMA DE PAGAMENTO"],
    ]
    planilhas_vendas.append_row(linha)
    return jsonify({"message": "Venda registrada"}), 201

if __name__ == "__main__":
    app.run()