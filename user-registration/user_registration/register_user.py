from user_registration.invalid_password_exception import InvalidPasswordException
from user_registration.user import User
from user_registration.user_already_exists_exception import UserAlreadyExistsException
from user_registration.user_id_generator import UserIdGenerator
from user_registration.user_repository import UserRepository


class RegisterUser:

    def __init__(self, repository: UserRepository, generator: UserIdGenerator) -> None:
        super().__init__()
        self.generator = generator
        self.repository = repository

    def register(self, email: str, password: str) -> None:
        if len(password) <= 8:
            raise InvalidPasswordException()
        if self.repository.find_by_email(email):
            raise UserAlreadyExistsException
        id = self.generator.generate()
        user = User(id, email, password)
        self.repository.save(user)
