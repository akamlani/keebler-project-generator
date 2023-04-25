[![Testing {ci}](https://github.com/{{ cookiecutter.author.username }}/{{ cookiecutter.repo.name }}/actions/workflows/testing-ci.yml/badge.svg)](https://github.com/{{ cookiecutter.author.username }}/{{ cookiecutter.repo.name }}/actions/workflows/testing-ci.yml)


[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=492249131&machine=standardLinux32gb&location=EastUs)

# {{ cookiecutter.repo.name }}
Template for executing domain or use case specific projects



## Installation
Install Libraries, Documentation, and Dependencies
```sh
# installs the library in 'edit' mode for development into prior installed environment
# show be installed as: `{*-template}` in listing the packages (pip list | less ) as mentioned in setup.py
cd '{*-template}'
rm -r $(find . -name '*.egg-info')
pip uninstall <package_name>
pip install -e .
pip install -e ".[all]"
pip install -e ".[data]"
```
