import unittest
from unittest.mock import Mock

from user_registration import RegisterUser
from user_registration.user import User
from user_registration.user_id_generator import UserIdGenerator
from user_registration.user_repository import UserRepository


class RegisterUserTest(unittest.TestCase):

    def test_the_user_is_persisted_with_the_id(self):
        user_repository = Mock(UserRepository)
        user_id_generator = Mock(UserIdGenerator)
        user_id_generator.generate = Mock(return_value="anId")
        register_user = RegisterUser(user_repository, user_id_generator)

        register_user.register("an@email", "valid_password")

        expected_user = User("anId", "an@email", "valid_password")
        user_repository.save.assert_called_with(expected_user)
