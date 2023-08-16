from src.main.adapter.repository.repository_impl import Database
from src.main.adapter.whatsapp.whatsapp import send_message
from src.main.domain.schema.user import User


class UserUseCase:
    def create(self, user: User):
        Database.create_user(user=user)
        message = """Hola!, veo que eres nuevo por aqui.
La idea es que me puedas hablar para anotar tus gastos y manejar tus finanzas
Para que sepas, lo que me puedes pedir actualmente es:
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

Las *Cuentas* son donde tenes tu dinero, sea el nombre de un banco o tu misma billetera.
Las *Categorias* son como vos queres organizar tus gastos como alquiler, comida, etc.
"""
        send_message(phone=user.phone, message=message)

    def update(self, user: User):
        if Database.user_exist(user) is False:
            UserUseCase().create(user=user)
        Database.update_user(user=user)

    def delete(self, user: User):
        if Database.user_exist(user) is True:
            Database.delete_user(user=user)
