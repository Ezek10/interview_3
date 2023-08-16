from sqlalchemy import delete, func, select

from src.main.adapter.repository.config import SessionLocal
from src.main.adapter.repository.model.account import AccountDB
from src.main.adapter.repository.model.category import CategoryDB
from src.main.adapter.repository.model.transaction import TransactionDB
from src.main.adapter.repository.model.user import UserDB
from src.main.domain.exceptions.account_not_found import AccountNotFound
from src.main.domain.exceptions.category_not_found import CategoryNotFound
from src.main.domain.port.repository.repository import Repository
from src.main.domain.schema.account import Account, ListAccounts
from src.main.domain.schema.category import Category, ListCategories
from src.main.domain.schema.transaction import ListTransactions, Transaction
from src.main.domain.schema.user import User

db = SessionLocal()


class Database(Repository):
    def user_exist(user: User) -> bool:
        """devuelve booleano sobre si existe un usuario o no"""
        user_db = db.scalars(select(UserDB).where(UserDB.id == user.phone)).first()
        return user_db is not None

    def create_user(user: User) -> None:
        """creo una persona con un phone"""
        db.add(UserDB(email=user.email, id=user.phone, name=user.name))
        db.commit()
        db.add(CategoryDB(name="transfer", user_id=user.phone))
        db.add(CategoryDB(name="saldo_inicial", user_id=user.phone))
        db.commit()

    def update_user(user: User) -> None:
        """actualizo una persona con phone y un user con email o name"""
        user_db = db.scalars(select(UserDB).where(UserDB.id == user.phone)).first()
        if user_db is not None:
            if user.name is not None:
                user_db.name = user.name
            if user.email is not None:
                user_db.email = user.email
            db.commit()

    def delete_user(user: User) -> None:
        """borro una persona con phone y un user con email o name"""
        db.execute(delete(UserDB).where(UserDB.id == user.phone)).first()
        db.commit()

    def create_category(phone: str, category: Category) -> None:
        """creo una categoria teniendo el numero de telefono"""
        category_db = db.scalars(
            select(CategoryDB)
            .where(CategoryDB.user_id == phone)
            .where(CategoryDB.name == category.name)
        ).first()
        if category_db is None:
            db.add(CategoryDB(name=category.name, user_id=phone))
            db.commit()

    def delete_category(phone: str, category: Category) -> None:
        """borro una categoria teniendo el numero de telefono"""
        category_db = db.scalars(
            select(CategoryDB)
            .where(CategoryDB.user_id == phone)
            .where(CategoryDB.name == category.name)
        ).first()
        if category_db is not None:
            db.execute(delete(category_db))
            db.commit()

    def create_account(phone: str, account: Account) -> None:
        """creo una cuenta teniendo el numero de telefono"""
        account_db = db.scalars(
            select(AccountDB)
            .where(AccountDB.user_id == phone)
            .where(AccountDB.name == account.name)
        ).first()
        if account_db is None:
            db.add(AccountDB(name=account.name, user_id=phone))
            db.commit()

    def delete_account(phone: str, account: Account) -> None:
        """borro una cuenta teniendo el numero de telefono"""
        account_db = db.scalars(
            select(AccountDB)
            .where(AccountDB.user_id == phone)
            .where(AccountDB.name == account.name)
        ).first()
        if account_db is not None:
            db.execute(delete(account_db))
            db.commit()

    def create_transaction(phone: str, transaction: Transaction) -> None:
        """creo una transaction con el numero de telefono, nombre categoria y nombre account"""
        category_db: CategoryDB = db.scalars(
            select(CategoryDB)
            .where(CategoryDB.user_id == phone)
            .where(CategoryDB.name == transaction.category.name)
        ).first()
        if category_db is None:
            raise CategoryNotFound(transaction.category.name)

        account_db: AccountDB = db.scalars(
            select(AccountDB)
            .where(AccountDB.user_id == phone)
            .where(AccountDB.name == transaction.account.name)
        ).first()
        if account_db is None:
            raise AccountNotFound(transaction.account.name)

        db.add(
            TransactionDB(
                amount=transaction.amount,
                category_id=category_db.id,
                account_id=account_db.id,
                user_id=phone,
                description=transaction.description,
            )
        )
        db.commit()

    def delete_transaction(phone: str, transaction_id: int) -> None:
        """borro una transaccion teniendo el numero de telefono"""
        transaction_db = db.scalars(
            select(TransactionDB)
            .where(TransactionDB.user_id == phone)
            .where(TransactionDB.id == transaction_id)
        ).first()
        if transaction_db is not None:
            db.execute(delete(transaction_db))
            db.commit()

    def list_accounts_with_phone(phone: str) -> ListAccounts:
        """listo todos los valores de las cuentas asociadas a un numero de telefono"""
        response = db.execute(
            select(
                AccountDB.name,
                AccountDB.currency,
                func.sum(TransactionDB.amount).label("resume_value"),
            )
            .where(AccountDB.user_id == phone)
            .group_by(AccountDB.name, AccountDB.id)
        ).all()
        accounts = list(map(Account.model_validate, response))
        return ListAccounts(accounts=accounts)

    def list_categories_with_phone(phone: str) -> ListCategories:
        """listo todos los valores de las categorias asociadas a un numero de telefono"""
        response = db.execute(
            select(
                CategoryDB.name, func.sum(TransactionDB.amount).label("resume_value")
            )
            .join(TransactionDB)
            .where(CategoryDB.user_id == phone)
            .group_by(CategoryDB.name, CategoryDB.id)
        ).all()
        categories = list(map(Category.model_validate, response))
        return ListCategories(categories=categories)

    def list_transaction_with_phone(phone: str) -> ListTransactions:
        """listo todas las transacciones con un numero de telefono"""
        result = db.scalars(
            select(TransactionDB).where(TransactionDB.user_id == phone)
        ).all()
        transactions = list(map(Transaction.model_validate, result))
        return ListTransactions(transactions=transactions)

    def list_transaction_with_phone_and_category(
        phone: str, category: Category
    ) -> ListTransactions:
        """listo todas las transacciones con un numero de telefono y un nombre de categoria"""
        result = db.scalars(
            select(TransactionDB)
            .where(TransactionDB.user_id == phone)
            .where(CategoryDB.name == category.name)
        ).all()
        transactions = list(map(Transaction.model_validate, result))
        return ListTransactions(transactions=transactions)

    def list_transaction_with_phone_and_account(
        phone: str, account: Account
    ) -> ListTransactions:
        """listo todas las transacciones con un numero de telefono y un nombre de cuenta"""
        result = db.scalars(
            select(TransactionDB)
            .where(TransactionDB.user_id == phone)
            .where(AccountDB.name == account.name)
        ).all()
        transactions = list(map(Transaction.model_validate, result))
        return ListTransactions(transactions=transactions)
