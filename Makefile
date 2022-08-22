SOURCE_PATH=./src

.PHONY: install_generate_mkdocs isort black flake8 reformat

install_generate_mkdocs:
	pip install mkdocs
	pip install mkdocs-git-revision-date-plugin
	pip install mkdocs-material
	pip install mkdocs-minify-plugin
	mkdocs build -d ./docs

isort:
	isort --verbose ${SOURCE_PATH}

black:
	black --verbose ${SOURCE_PATH}

flake8:
	flake8 --verbose ${SOURCE_PATH}

reformat: isort black flake8
