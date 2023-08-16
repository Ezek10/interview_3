import os

from requests import request

from src.main.domain.schema.account import ListAccounts
from src.main.domain.schema.category import ListCategories
from src.main.domain.schema.transaction import ListTransactions


def send_message(
    phone, message: str | ListTransactions | ListAccounts | ListCategories
):
    auth = os.environ["AUTH"]
    message = message_to_whatsapp_view(message)
    model = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "text",
        "text": {"body": message},
    }
    url = "https://graph.facebook.com/v17.0/117706181376555/messages"
    header = {
        "Authorization": auth
    }
    response = request(method="post", url=url, headers=header, json=model)
    print(response, response.content)


def message_to_whatsapp_view(message):
    if type(message) == ListAccounts:
        whatsapp_view = "Cuentas:\n"
        iterable = message.accounts
    elif type(message) == ListCategories:
        whatsapp_view = "Categorias:\n"
        iterable = message.categories
    elif type(message) == ListTransactions:
        whatsapp_view = "Transacciones:\n"
        iterable = message.transactions
    elif type(message) == str:
        return message
    for attr in iterable:
        whatsapp_view += attr.model_dump() + "\n"
    return whatsapp_view
