[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=492249131&machine=standardLinux32gb&location=EastUs)

# Project Repository Skeleton
Project Template for executing domain or use case specific projects

## Create Project Structure

Thd default project directory structure was created with:
```bash
# note this does not include any underlying files
 > cd templates/projects/project_default
 > ./create_structure.h
```

Execute Locally after cloning git repo
```bash
# Locally within cloned directory 
> cd templates
# setup local venv environment
> make install 
> . .venv/bin/activate
# Execute with default parameters: output path is BUILD/GENERATED/...
> make build
# override default output build directory
> make build BUILD_DIR=custom_build_path
# override default output build directory and provide user config file 
> make build BUILD_DIR=custom_build_path CONFIG_FILE=projects/project_default/user-custom-config.yaml
```

Execute Remote Repository
```bash
# directory only works with remote rempository 
> cookiecutter --no-input --overwrite-if-exists --output-dir=BUILD/GENERATOR
  https://github.com/akamlani/project-repository-skeleton.git 
  --directory='templates/projects/project_default'
```

