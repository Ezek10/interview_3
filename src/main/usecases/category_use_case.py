from src.main.usecases.user_use_case import UserUseCase
from src.main.adapter.repository.repository_impl import Database
from src.main.domain.schema.category import Category
from src.main.domain.schema.user import User


class CategoryUseCase:
    def create(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        Database.create_category(phone=phone, category=category)

    def delete(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        Database.delete_category(phone=phone, category=category)

    def get_all(self, phone: str):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        return Database.list_categories_with_phone(phone=phone)

    def get_one(self, phone: str, category: Category):
        user = User(phone=phone)
        if Database.user_exist(user=user) is False:
            UserUseCase().create(user=user)
        return Database.list_categories_with_phone(phone=phone)
