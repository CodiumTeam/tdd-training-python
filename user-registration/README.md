# User Registration kata

## Goal
Create the functionality using Unit tests and test doubles.

## Requirements
Part 1
- Validate that the user is persisted
- A userId is randomly generated

Part 2
- It cannot exist two users with the same email
- The password should meet security requirements
  - Have more than 8 characters
  - Contains an underscore
- Sends a confirmation email when the user is registered

## Remember
- Write a failing test.
- Write the minimum amount of code to make it pass.
- Do not forget to refactor the code.

## Tools
[Unittest](https://docs.python.org/3/library/unittest.mock.html)
### Example of spy

    def test_should_send_an_email(self):
        email_sender = Mock()
        user_registration = UserRegistration(email_sender)
    
        user_registration.register()
    
        email_sender.send.assert_called()

	
### Example of stub

    def test_should_success_when_password_is_valid(self):
        password_validator = Mock()
        password_validator.is_valid = Mock(return_value=true)
        user_registration = UserRegistration(password_validator)

        success = user_registration.register()

        assertTrue(success)

## Authors
Luis Rovirosa [@luisrovirosa](https://www.twitter.com/luisrovirosa)

Jordi Anguela [@jordianguela](https://www.twitter.com/jordianguela)
