class CategoryNotFound(Exception):
    """Exception to use when a category is not found in database"""

    def __init__(self, category: str) -> None:
        message = f"Category {category} not found"
        super().__init__(message)
