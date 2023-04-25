import re
import sys


REGEX_CHECK  = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
package_name = '{{ cookiecutter.package.name}}'

if not re.match(REGEX_CHECK, package_name):
    print(f"ERROR: The package {package_name} is not a valid Python Repo name. Please do not use a - and use _ instead")
    #Exit to cancel project
    sys.exit(1)

