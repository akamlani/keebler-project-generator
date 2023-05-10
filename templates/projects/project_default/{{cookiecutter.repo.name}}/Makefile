PACKAGE_NAME={{cookiecutter.package.name}}
PACKAGE_INSTALL_NAME={{cookiecutter.package.installer}}

PYTHON_VERSION={{cookiecutter.interpreter.version}}
CONDA_URI={{cookiecutter.interpreter.conda.download.uri}}
CONDA_PREFIX={{cookiecutter.interpreter.conda.install.prefix}}
CONDA_BIN=$(CONDA_PREFIX)/bin/conda
ENV_NAME={{cookiecutter.interpreter.conda.env.name}}
ENV_FILE={{cookiecutter.interpreter.conda.env.file}}
ENV_DEP_PATH={{cookiecutter.interpreter.dependencies.path}}

VENV_PATH={{cookiecutter.interpreter.venv.dev}}


# e.g., Darwin for MacOS
PLATFORM_TYPE = $(shell uname)
# dynamically detect shell type as bash or zsh
ifeq ($(shell basename $(SHELL)), zsh)
	SHELL := zsh
else
	SHELL := bash
endif
# dynamically detect if conda is installed
ifeq ($(shell which conda),)
	HAS_CONDA=False
else
	HAS_CONDA=True
endif


.PHONY: help info
help:
	@echo "Commands  : "
	@echo "download  : downloads a new anaconda distribution"
	@echo "install   : create an anaconda and virtual environment based on project $(PACKAGE_INSTALL_NAME)"
	@echo "setup     : executes download and install based on project $(PACKAGE_INSTALL_NAME)"
	@echo "format    : formatting and linting of project $(PACKAGE_NAME)"
	@echo "clean     : cleans all files or project $(PACKAGE_INSTALL_NAME)"
	@echo "clean-all : executes clean and removes anaconda, and virtual environments"
	@echo "test      : execute unit testing"

info:
	@echo "Info      : "
	@echo "info      : platform=$(PLATFORM_TYPE), shell=$(SHELL)"
	@echo "Kernels:  : $$(jupyter kernelspec list)"

#################### Conda Setup
conda-download:
	curl $(CONDA_URI) > anaconda.sh
	chmod +x anaconda.sh
	mkdir -p $(CONDA_PREFIX)
# alternatively add -b -q options, but will require manually setting environment variables
	./anaconda.sh -u -p $(CONDA_PREFIX)

# even though executed in a subshell we will just activate it
.ONESHELL:
conda-env-install:
	conda create -n $(ENV_NAME) python=$(PYTHON_VERSION) && 			\
	source $$(conda info --base)/etc/profile.d/conda.sh  && 			\
	conda activate $(ENV_NAME) && 										\
	pip install -U pip &&												\
	pip install ipykernel==6.21.2 ipython\>=7.23.1,\<8.0.0

conda-env-create-from-file:
	conda env create -f $(ENV_FILE)

conda-env-remove:
	conda remove -n $(ENV_NAME) --all

#################### Create and Install Dependencies on Virtual Environment
.PHONY: build venv
build:
	python setup.py build

venv:
	source $$(conda info --base)/etc/profile.d/conda.sh && 					\
	conda activate $(ENV_NAME) &&											\
	python -m venv $(VENV_PATH) &&											\
	source $(VENV_PATH)/bin/activate

# pre-commmit to git hooks on execution of 'git commit'
# install module in appropriate venv directory
.PHONY: venv-install
.ONESHELL:
venv-install: venv
	source $$(conda info --base)/etc/profile.d/conda.sh && 					\
	conda activate $(ENV_NAME) &&											\
	source $(VENV_PATH)/bin/activate &&										\
	pip install --no-cache-dir -U pip pip-tools setuptools wheel &&			\
	pip install -r $(ENV_DEP_PATH)/requirements.txt && 						\
	pip install -r $(ENV_DEP_PATH)/requirements_nb.txt && 					\
	pip install -r $(ENV_DEP_PATH)/requirements_test.txt &&					\
	python -m ipykernel install --user --name=$(PACKAGE_NAME) &&			\
	pip install --no-cache-dir -e . &&										\
	pre-commit install && 													\
	pre-commit autoupdate


venv-remove:
	rm -rf $(VENV_PATH)

#################### Testing and Quality Checks
.PHONY: test
test:
	python -m pytest -vvv  --cov=$(PACKAGE_NAME) tests/

.PHONY: quality
quality:
	black --check *.py
	isort --check-only *.py

.PHONY: style
style:
	black   *.py
	isort   *.py
	flake8  --statistics *.py

.PHONY: lint
lint:
	pylint *.py

#################### Cleaning
.PHONY: clean
clean:
#	jupyter kernelspec remove $(PACKAGE_NAME)
	pip uninstall $(PACKAGE_INSTALL_NAME)
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E ".egg-info" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf

clean-all: clean
	rm -f ./anaconda.sh
	rm -rf $(CONDA_PREFIX)
	rm -rf $(VENV_PATH)
#	rm -rf ~/.conda

.PHONY: download install setup format
download:   conda-download
install:    conda-env-install venv-install
setup: 		conda-download conda-env-install venv-install
format:     quality style
