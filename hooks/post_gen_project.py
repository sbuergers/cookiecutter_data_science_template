import os


if '{{cookiecutter.language}}' != 'python':
    raise ValueError('Only python is currently supported by this cookiecutter template')


print(f"COOKIECUTTER Created the project in: {os.getcwd()}")


if '{{cookiecutter.repo_name}}' == 'template_repo':
    print('We highly encourage you to change the default repository name!')


if '{{cookiecutter.pkg_name}}' == 'template_pkg':
    print('We highly encourage you to change the default package name!')
    

print("Please create new 'Pipelines' in Azure Devops, and use the existing pipeline files "
      "found in the pipeline folder. A pipeline for each .yaml.")


if '{{cookiecutter.documentation}}' != 'y':
    print("Removing documentation files...")
    os.rmdir(os.path.join(os.getcwd(), 'docs'))
else:
    print('For information on how to create documentation, please see the DDC wiki:')
    print('https://wikiddc.corporateroot.net/doku.php?id=python_styleguide#documentation')
