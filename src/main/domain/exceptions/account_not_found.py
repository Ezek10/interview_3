class AccountNotFound(Exception):
    """Exception to use when an account is not found in database"""

    def __init__(self, account: str) -> None:
        message = f"Account {account} not found"
        super().__init__(message)
