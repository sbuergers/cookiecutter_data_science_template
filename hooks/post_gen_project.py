import os
import shutil

print(os.getcwd())

# https://github.com/audreyr/cookiecutter/issues/723


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


pkg_name = '{{cookiecutter.pkg_name}}'
language = '{{cookiecutter.language}}'


if (pkg_name == 'not applicable') | (language != 'python'):
    print("Removing package files...")
    remove(os.path.join(os.getcwd(), '{{cookiecutter.pkg_name}}'))
    remove(os.path.join(os.getcwd(),  'setup.py'))

else:
    print("Removing src files...")
    remove(os.path.join(os.getcwd(), 'src'))


if language.lower() == 'r':
    print("Removing python linting...")
    remove(os.path.join(os.getcwd(), '.arclint'))
    remove(os.path.join(os.getcwd(),  'setup.cfg'))

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



