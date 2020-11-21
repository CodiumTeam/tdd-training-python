.PHONY: default test coverage docker-test docker-coverage
default: docker-test

test:
	python3 -m unittest

coverage:
	coverage run --source=password_validator -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

docker-test:
	docker run --rm -v ${PWD}:/kata codiumteam/tdd-training-python make test

docker-coverage:
	@docker run --rm -v ${PWD}:/kata codiumteam/tdd-training-python make coverage