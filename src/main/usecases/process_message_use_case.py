from datetime import datetime

from src.main.usecases.account_use_case import AccountUseCase
from src.main.usecases.category_use_case import CategoryUseCase
from src.main.usecases.transaction_use_case import TransactionUseCase
from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.whatsapp.whatsapp import send_message
from src.main.domain.schema.account import Account
from src.main.domain.schema.category import Category
from src.main.domain.schema.transaction import Transaction
from src.main.domain.schema.user import User


class ProcessMessageUseCase:
    def execute(self, phone: str, message: str, date: datetime = datetime.now()):
        words_spend = ["gaste"]
        words_configuration = ["configurar"]
        words_create = ["crear", "definir"]
        words_ingreso = ["ingreso"]
        words_delete = ["borrar"]
        words_transfer = ["transferi", "retire"]
        words_list = ["listar", "traer", "mostrar"]
        message = message.lower()
        if self._words_in_message(words_configuration, message):
            message_to_send = self._proccess_configuration(phone, message)
        elif self._words_in_message(words_create, message):
            message_to_send = self._proccess_create(phone, message)
        elif self._words_in_message(words_ingreso, message):
            message_to_send = self._proccess_ingreso(phone, message, date)
        elif self._words_in_message(words_transfer, message):
            message_to_send = self._proccess_transfer(phone, message, date)
        elif self._words_in_message(words_spend, message):
            message_to_send = self._proccess_spend(phone, message, date)
        elif self._words_in_message(words_list, message):
            message_to_send = self._proccess_list(phone, message)
        elif self._words_in_message(words_delete, message):
            message_to_send = self._proccess_delete(phone, message)
        else:
            message_to_send = self._proccess_help()
        if message_to_send is not None:
            send_message(phone, message_to_send)
        return message_to_send

    def _proccess_help(self):
        message = """Hola, si no sabes que quieres pedirme, prueba con:
    - Crear/Definir cuenta 'cuenta'
    - Crear/Definir categoria 'categoria'
    - Gaste 300 por 'categoria' en 'cuenta'
    - Ingreso 300 por 'categoria' en 'cuenta'
    - Transferi/Retire 300 desde 'cuenta_origen' hacia 'cuenta_destino'
    - Configurar email 'email@example.com'
    - Configurar nombre 'nombre_de_usuario'
    - Listar/Traer/Mostrar categorias
    - Listar/Traer/Mostrar cuentas
    - Listar/Traer/Mostrar transacciones
    - Listar/Traer/Mostrar transacciones con categoria 'categoria'
    - Listar/Traer/Mostrar transacciones con cuenta 'cuenta'

Recuerda que las *Cuentas* son donde tenes tu dinero, sea el nombre de un banco o tu misma billetera.
Las *Categorias* son como vos queres organizar tus gastos como alquiler, comida, etc.
"""
        return message

    def _proccess_spend(self, phone: str, message: str, date: datetime):
        spend, amount, forr, category, inn, account = message.split(" ")
        amount = int(amount)
        category = Category(name=category)
        account = Account(name=account)
        transaction = Transaction(
            amount=-amount, created_at=date, category=category, account=account
        )
        return TransactionUseCase().create(phone=phone, transaction=transaction)

    def _proccess_delete(self, phone, message: str):
        delete, attr, name = message.split(" ")
        if attr == "transaccion":
            return TransactionUseCase().delete_with_id(phone, name)
        elif attr == "cuenta":
            account = Account(name=name)
            return AccountUseCase().delete(phone, account)
        elif attr == "categoria":
            category = Category(name=name)
            return CategoryUseCase().delete(phone, category)
        elif attr == "usuario":
            user = User(name=name)
            return UserUseCase().delete(user)

    def _proccess_list(self, phone: str, message: str):
        list, *attr = message.split(" ")
        if attr[0] == "transacciones":
            if "categoria" in attr:  # list transactions with category xxx
                return TransactionUseCase().get_filtered_by_category(phone, attr[3])
            elif "cuenta" in attr:
                return TransactionUseCase().get_filtered_by_account(phone, attr[3])
            else:
                return TransactionUseCase().get_all(phone)
        elif attr[0] == "cuentas":
            return AccountUseCase().get_all(phone)
        elif attr[0] == "categorias":
            return CategoryUseCase().get_all(phone)

    def _proccess_configuration(self, phone: str, message: str):
        if "email" in message:
            configure, email, address = message.split(" ")
            user = User(phone=phone, email=address)
        elif "nombre" in message:
            configure, name, user_name = message.split(" ")
            user = User(phone=phone, name=user_name)
        else:
            return
        return UserUseCase().update(user=user)

    def _proccess_create(self, phone: str, message: str):
        create, attr, name = message.split(" ")
        if attr == "cuenta":
            account = Account(name=name)
            return AccountUseCase().create(phone=phone, account=account)
        elif attr == "categoria":
            category = Category(name=name)
            return CategoryUseCase().create(phone=phone, category=category)

    def _proccess_ingreso(self, phone: str, message: str, date: datetime):
        ingreso, amount, forr, category, inn, account = message.split(" ")
        account = Account(name=account)
        category = Category(name=category)
        transaction = Transaction(
            amount=amount, created_at=date, category=category, account=account
        )
        return TransactionUseCase().create(phone=phone, transaction=transaction)

    def _proccess_transfer(self, phone: str, message: str, date: datetime):
        transfer, amount, fromm, account_origin, to, account_destiny = message.split(
            " "
        )
        account_origin = Account(name=account_origin)
        account_destiny = Account(name=account_destiny)
        category = Category(name="transfer")
        transaction_origin = Transaction(
            amount=-amount,
            created_at=date,
            description=f"Transfer from {account_origin} to {account_destiny}",
            account=account_origin,
            category=category,
        )
        transaction_destiny = Transaction(
            amount=amount,
            created_at=date,
            description=f"Transfer from {account_origin} to {account_destiny}",
            account=account_destiny,
            category=category,
        )
        TransactionUseCase().create(
            phone=phone,
            transaction=transaction_origin,
        )
        TransactionUseCase().create(
            phone=phone,
            transaction=transaction_destiny,
        )

    def _words_in_message(self, words: list[str], message: str):
        for word in words:
            if word in message:
                return True
        return False
