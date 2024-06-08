.PHONY: qa quality pylint pyroma

quality:
	isort sopel_slap
	flake8 sopel_slap

pylint:
	pylint sopel_slap

pyroma:
	pyroma .

qa: quality pylint pyroma

.PHONY: develop build

develop:
	python -m pip install -U -r dev-requirements.txt
	python -m pip install -e .

build:
	rm -rf build/ dist/
	python -m build --sdist --wheel --outdir dist/ .
