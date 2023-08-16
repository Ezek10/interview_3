from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.repository.repository_impl import Database
from src.main.domain.schema.account import Account
from src.main.domain.schema.user import User


class AccountUseCase:
    def create(self, phone: str, account: Account):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        Database.create_account(phone=phone, account=account)

    def delete(self, phone: str, account: Account):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        Database.delete_account(phone=phone, account=account)

    def get_all(self, phone: str):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        return Database.list_accounts_with_phone(phone)
