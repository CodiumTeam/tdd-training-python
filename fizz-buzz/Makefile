.PHONY: default test docker-build docker-test
default: docker-test

test:
	python3 -m unittest tests/fizz_buzz_test.py

docker-build:
	@docker build .. -t codium-tdd-training

docker-test:
	docker run -v ${PWD}:/opt/project -w /opt/project codium-tdd-training make test
