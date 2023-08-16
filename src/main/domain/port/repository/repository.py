from abc import ABC, abstractmethod

from src.main.domain.schema.account import Account, ListAccounts
from src.main.domain.schema.category import Category, ListCategories
from src.main.domain.schema.transaction import ListTransactions, Transaction
from src.main.domain.schema.user import User


class Repository(ABC):
    @abstractmethod
    def user_exist(user: User) -> bool:
        """devuelve booleano sobre si existe un usuario o no"""
        pass

    @abstractmethod
    def create_user(user: User) -> None:
        """creo una persona con un phone"""
        pass

    @abstractmethod
    def update_user(user: User) -> None:
        """actualizo una persona con phone y un user con email o name"""
        pass

    @abstractmethod
    def delete_user(user: User) -> None:
        """borro una persona con phone y un user con email o name"""
        pass

    @abstractmethod
    def create_category(phone: str, category: Category) -> None:
        """creo una categoria teniendo el numero de telefono"""
        pass

    @abstractmethod
    def delete_category(phone: str, category: Category) -> None:
        """borro una categoria teniendo el numero de telefono"""
        pass

    @abstractmethod
    def create_account(phone: str, account: Account) -> None:
        """creo una cuenta teniendo el numero de telefono"""
        pass

    @abstractmethod
    def delete_account(phone: str, account: Account) -> None:
        """borro una cuenta teniendo el numero de telefono"""
        pass

    @abstractmethod
    def create_transaction(phone: str, transaction: Transaction) -> None:
        """creo una transaction con el numero de telefono, nombre categoria y nombre account"""
        pass

    @abstractmethod
    def delete_transaction(phone: str, transaction_id: int) -> None:
        """borro una transaccion teniendo el numero de telefono"""
        pass

    @abstractmethod
    def list_accounts_with_phone(phone: str) -> ListAccounts:
        """listo todos los valores de las cuentas asociadas a un numero de telefono"""
        pass

    @abstractmethod
    def list_categories_with_phone(phone: str) -> ListCategories:
        """listo todos los valores de las categorias asociadas a un numero de telefono"""
        pass

    @abstractmethod
    def list_transaction_with_phone(phone: str) -> ListTransactions:
        """listo todas las transacciones con un numero de telefono"""
        pass

    @abstractmethod
    def list_transaction_with_phone_and_category(
        phone: str, category: Category
    ) -> ListTransactions:
        """listo todas las transacciones con un numero de telefono y un nombre de categoria"""
        pass

    @abstractmethod
    def list_transaction_with_phone_and_account(
        phone: str, account: Account
    ) -> ListTransactions:
        """listo todas las transacciones con un numero de telefono y un nombre de cuenta"""
        pass
