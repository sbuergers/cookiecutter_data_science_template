import os
import shutil

print(f"Created the project in: {os.getcwd()}")

# https://github.com/audreyr/cookiecutter/issues/723


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


pkg_name = '{{cookiecutter.pkg_name}}'
language = '{{cookiecutter.language}}'


if (pkg_name == 'not applicable') | (language != 'python'):
    remove(os.path.join(os.getcwd(), '{{cookiecutter.pkg_name}}'))
    remove(os.path.join(os.getcwd(),  'setup.py'))
    remove(os.path.join(os.getcwd(),  'pipelines/build-python-package.yaml'))
else:
    print("Please follow the instructions in 'pipelines/build-python-package.yaml' "
          "to set up an automatic package build")
    remove(os.path.join(os.getcwd(), 'src'))


if language.lower() == 'r':
    remove(os.path.join(os.getcwd(),  'setup.cfg'))
    remove(os.path.join(os.getcwd(),  'conftest.py'))
    remove(os.path.join(os.getcwd(),  'pipelines/lint-python.yaml'))
    remove(os.path.join(os.getcwd(),  'pipelines/test-python.yaml'))

if language.lower() == 'python':
    print("Please create new 'Pipelines' in Azure Devops, and use the existing pipeline files "
          "found in the pipeline folder. A pipeline for each .yaml.")

if ('{{cookiecutter.documentation}}' != 'y') | (language.lower() == 'r'):
    if language.lower() == "r":
        print('The RHDHV DDC cookiecutter part for automatic documentation in R is currently '
              'not supported.')
    print("Removing documentation files...")
    remove(os.path.join(os.getcwd(), 'docs', 'source'))
    remove(os.path.join(os.getcwd(), 'docs', 'build'))
else:
    print('For information on how to create documentation, please see the DDC wiki:')
    print('https://wikiddc.corporateroot.net/doku.php?id=python_styleguide#documentation')



