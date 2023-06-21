from user_registration.user import User


class UserRepository:
    def save(self, user: User) -> None:
        pass

    def find_by_email(self, email: str) -> User:
        pass
