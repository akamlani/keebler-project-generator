from pathlib import Path

from setuptools import find_namespace_packages, setup

# read description for long-form description
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# read requirements for core development installation
# ignore those with commments at beginning of line
with open(
    Path("{{ cookiecutter.interpreter.dependencies.path }}").joinpath(
        "requirements.txt"
    ),
    encoding="utf-8",
) as f:
    requirements = [
        line.strip() for line in f if len(line) > 1 and "#" not in line[0:3]
    ]

# read requirements for core development installation
extra = {}
files = [
    *Path("{{ cookiecutter.interpreter.dependencies.path }}").glob("**/requirements_*")
]
etypes = [f.stem.split("_")[-1] for f in files]
for etype, filepath in zip(etypes, files):
    with open(filepath, encoding="utf-8") as f:
        # ignore those with commments at beginning of line
        extra[etype] = [
            line.strip() for line in f if len(line) > 1 and "#" not in line[0:3]
        ]

# repackage information
extra["default"] = [item for sublist in extra.values() for item in sublist]
extra["all"] = [item for sublist in extra.values() for item in sublist]

# install the module
setup(
    name="{{ cookiecutter.package.installer }}",
    version="{{ cookiecutter.module.version }}",
    # author information
    author="{{ cookiecutter.author.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.author.email }}",
    # descriptions
    description="{{ cookiecutter.properties.description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="{{ cookiecutter.module.license }}",
    keywords="{{ cookiecutter.properties.keywords }}",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
    ],
    # URIs
    url="{{ cookiecutter.repo.host }}/{{ cookiecutter.author.username }}/{{ cookiecutter.repo.name }}",
    project_urls={
        "Bug Tracker": "{{ cookiecutter.repo.host }}//{{ cookiecutter.repo.username }}/{{ cookiecutter.repo.name }}/issues",
        "Repository": "{{ cookiecutter.repo.host }}/{{ cookiecutter.repo.username }}/{{ cookiecutter.repo.name }}",
        "Homepage": "{{ cookiecutter.author.homepage }}",
    },
    # what is packaged here
    python_requires=">={{cookiecutter.interpreter.version}}",
    install_requires=requirements,
    packages=find_namespace_packages(
        include=[
            "{{ cookiecutter.package.name }}",
            "{{ cookiecutter.package.name }}.*",
        ],
        exclude=["docs", "tests"],
    ),
    extras_require=extra,
    # testing packages
    test_suite="tests",
    tests_require=extra["test"],
    # include perspective data
    include_package_data=True,
    package_data={
        "{{ cookiecutter.package.name }}": [
            "*.txt",
            "*.rst",
            "*.md",
            "*.json",
            "*.yaml",
        ]
    },
    zip_safe=False,
)
