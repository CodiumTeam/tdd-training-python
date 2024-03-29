# Goal
Unit test the printCurrentDate function.

1. Test the code with doubles from a library.
2. Test the code with doubles created by you.
# Code to test
    class PrintDate:
        def __init__(self, calendar, printer):
            self.printer = printer
            self.calendar = calendar
    
        def print_current_date(self):
            self.printer.print_line(self.calendar.today())

# Learnings
How to build a Mock and Stub manually.

How to use Unittest Mock to generate the doubles.

## Tools
[Unittest](https://docs.python.org/3/library/unittest.mock.html)
### Example of spy

    from unittest.mock import Mock
    from my_example_app import UserRegistration, EmailSender

    def test_should_send_an_email(self):
        emailSender = Mock(spec=EmailSender)
        user_registration = UserRegistration(email_sender)
    
        user_registration.register()
    
        email_sender.send.assert_called()

	
### Example of stub
    
    from unittest.mock import Mock
    from my_example_app import UserRegistration, PasswordValidator

    def test_should_success_when_password_is_valid(self):
        password_validator = Mock(spec=PasswordValidator)
        password_validator.is_valid = Mock(return_value=true)
        user_registration = UserRegistration(password_validator)

        success = user_registration.register()

        assertTrue(success)

## How to run and see the result
## Locally
### on Linux and Mac
Run the tests

    make run

Run the code coverage

    make coverage
    
### on Windows
Run the tests
    
    python -m unittest tests/weather_test.py
    
Run the code coverage

    pytest --cov=weather tests
	coverage html
	
## Docker

### on Linux and Mac
Generate the image

    make docker-build

Run the tests
    
    make docker-run

Run the code coverage
    
    make docker-coverage

### on Windows
Generate the image

    docker build . -t python-coverage

Run the tests
    
    docker run -v %cd%:/kata python-coverage make run

Run the code coverage

    docker run -v %cd%:/kata python-coverage make coverage


## Authors
Luis Rovirosa [@luisrovirosa](https://www.twitter.com/luisrovirosa)

Jordi Anguela [@jordianguela](https://www.twitter.com/jordianguela)
