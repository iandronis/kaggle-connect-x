SOURCE_PATH=./src

.PHONY: install_mkdocs_depend isort black flake8 reformat

install_mkdocs_depend:
	pip install mkdocs
	pip install mkdocs-git-revision-date-plugin
	pip install mkdocs-material
	pip install mkdocs-minify-plugin

isort:
	isort --verbose ${SOURCE_PATH}

black:
	black --verbose ${SOURCE_PATH}

flake8:
	flake8 --verbose ${SOURCE_PATH}

reformat: isort black flake8
