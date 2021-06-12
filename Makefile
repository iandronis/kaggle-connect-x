SOURCE_PATH=./src

.PHONY: isort black flake8 reformat

isort:
	isort --verbose ${SOURCE_PATH}/

black:
	black --verbose ${SOURCE_PATH}

flake8:
	flake8 --verbose ${SOURCE_PATH}

reformat: isort black flake8

gitlint:
	gitlint -d
