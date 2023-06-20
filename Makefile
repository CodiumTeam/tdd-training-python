.PHONY: docker-build
docker-build:
	docker build -t codiumteam/tdd-training-python .

.PHONY: docker-push
docker-push:
	docker push codiumteam/tdd-training-python