from flask import Flask, render_template, request, jsonify
import requests
import uuid

app = Flask(__name__)

BASE_URL = "https://sandbox-api.staq.io/api/v1/partner"
HEADERS = {
    "Content-Type": "application/json",
    "Idempotency-key": "65d16950-1355-486e-8322-6002b713e0a6"
}

def criar_cartao_prepago(customer_id, nome_titular, numero_celular, codigo_moeda="JOD"):
    url = f"{BASE_URL}/prepaid-cards/customers/{customer_id}/cards"
    
    payload = {
        "CurrencyCode": codigo_moeda,
        "CardholderName": nome_titular,
        "MobileNumber": numero_celular
    }
    
    response = requests.post(url, json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro: {response.status_code} - {response.text}"


# Exemplo de uso
if __name__ == "__main__":
    customer_id = "#012345678"  # Substitua por um ID de cliente válido
    nome_titular = "João Silva"
    numero_celular = "0123456789"

    resultado = criar_cartao_prepago(customer_id, nome_titular, numero_celular)
    print(resultado)
