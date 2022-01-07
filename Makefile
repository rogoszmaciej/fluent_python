######################
# Utilities
######################
update-requirements:
	pip install -U pip pip-tools
	pip-compile -U requirements.in
	pip-compile -U requirements-test.in

black:
	python3 -m black ./

######################
# Services
######################
docker-build:
	docker build ./

docker-test: docker-build
	docker-compose run --rm python sh -c "pip install -q -r requirement.txt ; py.test --maxfail=1 -vv"

docker-stop::
	docker-compose down
