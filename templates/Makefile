VENV_PATH=".venv"
OPTIONS=--no-input --overwrite-if-exists -v -f 
BUILD_DIR=BUILD/GENERATED 
PROJECT_DIR=projects/project_default
CONFIG_FILE=

.PHONY: help build install clean setup all 

help:
	@echo "Commands  : "  
	@echo "install   : installs a minimal virtual environment"
	@echo "clean     : cleans necessary files and virtual environment"
	@echo "build     : generates a project using defaults or a config file with CONFIG_FILE=path/to/config/file"

# make build BUILD_DIR=custom_build_path
# make build BUILD_DIR=custom_build_path CONFIG_FILE=projects/project_default/user-custom-config.yaml
.PHONY: build
build:
ifeq ($(CONFIG_FILE),)
	cookiecutter $(OPTIONS) --output-dir=$(BUILD_DIR) $(PROJECT_DIR)
else 
	cookiecutter $(OPTIONS) --output-dir=$(BUILD_DIR) --config-file=$(CONFIG_FILE) $(PROJECT_DIR)
endif

.ONESHELL: 
install:
	python -m venv $(VENV_PATH) &&								\
	. $(VENV_PATH)/bin/activate &&								\
	pip install -U pip pip-tools setuptools wheel &&			\
	pip install -r requirements.txt

clean:
	find . -type f -name "*.DS_Store" -ls -delete
	find . -name "*~" -delete             
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	rm -rf $(VENV_PATH)


setup: install
all:   install clean