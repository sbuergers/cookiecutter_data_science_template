from setuptools import setup

setup(name='{{cookiecutter.pkg_name}}',
      version='{{cookiecutter.version}}',
      description='{{cookiecutter.project_short_description}}',
      url='',
      author='{{cookiecutter.full_name}}',
      author_email='{{cookiecutter.email}}',
      license='',
      packages=['{{cookiecutter.pkg_name}}'],
      zip_safe=False,
      install_requires=[]
      )