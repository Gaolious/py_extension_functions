help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "install - install the package to the active Python's site-packages"
	@echo "docs - generate documents"

clean: clean-test clean-build clean-pyc clean-docs

clean-build:
	rm -rf ./build
	rm -rf ./dist
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-docs:
	rm -rf ./docs/build

docs: clean-docs
	sphinx-apidoc -e -F -o ./docs/source ./gpp
	make -C ./docs html

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .cache/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache/

test:
	pytest gpp tests

coverage: test
	coverage report -i -m
	coverage html

install: clean
	python setup.py install