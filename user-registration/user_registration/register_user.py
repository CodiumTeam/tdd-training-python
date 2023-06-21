from user_registration.email import Email
from user_registration.email_sender import EmailSender
from user_registration.invalid_password_exception import InvalidPasswordException
from user_registration.user import User
from user_registration.user_already_exists_exception import UserAlreadyExistsException
from user_registration.user_id_generator import UserIdGenerator
from user_registration.user_repository import UserRepository


class RegisterUser:

    def __init__(self, repository: UserRepository, generator: UserIdGenerator, email_sender: EmailSender) -> None:
        super().__init__()
        self.generator = generator
        self.repository = repository
        self.email_sender = email_sender

    def register(self, email: str, password: str) -> None:
        if len(password) <= 8 or "_" not in password:
            raise InvalidPasswordException()
        if self.repository.find_by_email(email):
            raise UserAlreadyExistsException
        id = self.generator.generate()
        user = User(id, email, password)
        self.repository.save(user)
        email = Email("info@codium.team", email, "Welcome to Codium")
        self.email_sender.send(email)
