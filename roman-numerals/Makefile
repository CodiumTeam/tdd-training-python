.PHONY: default test coverage docker-build docker-test docker-coverage
default: docker-test

test:
	python3 -m unittest

coverage:
	coverage run --source=roman_numerals -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

docker-build:
	@docker build .. -t codium-tdd-training

docker-test:
	docker run --rm -v ${PWD}:/opt/project -w /opt/project codium-tdd-training make test

docker-coverage:
	@docker run --rm -v ${PWD}:/opt/project -w /opt/project codium-tdd-training make coverage