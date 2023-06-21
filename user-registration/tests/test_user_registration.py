import unittest
from unittest.mock import Mock

from user_registration import RegisterUser
from user_registration.user import User
from user_registration.user_already_exists_exception import UserAlreadyExistsException
from user_registration.user_id_generator import UserIdGenerator
from user_registration.user_repository import UserRepository


class RegisterUserTest(unittest.TestCase):

    def setUp(self):
        self.user_id_generator = Mock(UserIdGenerator)
        self.user_repository = Mock(UserRepository)
        self.user_repository.find_by_email = Mock(return_value=None)

    def test_the_user_is_persisted_with_the_id(self):
        self.user_id_generator.generate = Mock(return_value="anId")
        register_user = RegisterUser(self.user_repository, self.user_id_generator)

        register_user.register("an@email", "valid_password")

        expected_user = User("anId", "an@email", "valid_password")
        self.user_repository.save.assert_called_with(expected_user)

    def test_cannot_exists_two_user_with_the_same_email(self):
        existing_user = User("anId", "an@email", "a_password")
        self.user_repository.find_by_email = Mock(return_value=existing_user)
        register_user = RegisterUser(self.user_repository, self.user_id_generator)

        register = lambda: register_user.register("an@email", "valid_password")

        self.assertRaises(UserAlreadyExistsException, register)
        self.user_repository.save.assert_not_called()
