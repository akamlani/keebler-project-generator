#!/bin/sh
PROJECT_REPO_DIR={{cookiecutter.repo.name}}
PACKAGE_DIR={{cookiecutter.package.name}}

# hooks represents pre and post hooks for cookiecutter
echo "GENERATE: directories for project"
mkdir -p hooks

# for repo directory
echo "GENERATE: Project Root Structure for ${PROJECT_REPO_DIR}"
mkdir -p ${PROJECT_REPO_DIR}/.github/workflows
mkdir -p ${PROJECT_REPO_DIR}/.vscode
mkdir -p ${PROJECT_REPO_DIR}/apps/{demos,nbs,programs}
mkdir -p ${PROJECT_REPO_DIR}/assets
mkdir -p ${PROJECT_REPO_DIR}/config/credentials/providers
mkdir -p ${PROJECT_REPO_DIR}/data
mkdir -p ${PROJECT_REPO_DIR}/docker
mkdir -p ${PROJECT_REPO_DIR}/docs
mkdir -p ${PROJECT_REPO_DIR}/environment/dependencies
mkdir -p ${PROJECT_REPO_DIR}/examples/providers
mkdir -p ${PROJECT_REPO_DIR}/scripts/commands
mkdir -p ${PROJECT_REPO_DIR}/templates
mkdir -p ${PROJECT_REPO_DIR}/tests

# add specific directories for a given use case or submodule
#mkdir -p ${PROJECT_REPO_DIR}/config/{dataops,models,training,evaluation,serving,monitoring}

# for given package directory structure
# add __init__.py to each top level and .gitkeep for each child directory
echo "GENERATE: Package Structure for ${PROJECT_REPO_DIR}/${PACKAGE_DIR}"
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/cards
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/contrib
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/core/io
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/datasets/{config,loaders}
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/infra
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/integrations/{providers,dataops,ml,mlops}
mkdir -p ${PROJECT_REPO_DIR}/${PACKAGE_DIR}/ui/layouts
