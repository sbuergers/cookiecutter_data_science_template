## Version: 0.1.0

Feel free to adapt this Readme scaffolding as needed for your project!

# cookiecutter_template_old (cto) description

fill in you project description!

_Authors:_ Someone

_Emails:_ someone@example.com

_Reviewers:_ Sometwo

_Emails:_ sometwo@example.com

# Run options

How can you run your package, use your code?

``` 
```

# Configuration

If you have a configuration file, explain it here.

```
```

# Testing

How to test your package / code?

```
```

# Package installation

This is done by going to the root folder of this package, and running `pip install -e .` This will install a development version of the package locally. That means that if you make local changes, the package will automatically reflect them. It is recommended to do this in a virtual environment such as `venv` or `conda`.

If you want to develop in a notebook, you will also need to reload the cto package whenever you run from cto import x. This can be achieved by putting the following lines at the top of every notebook:

```
%load_ext autoreload
%autoreload 2
%aimport cto
```

This will reload cto everytime you run a new cell. The third line is optional: if you leave it out, you will reload every import every cell, instead of only those from cto.

# Documentation

Documentation is very important. The cookiecutter template offers support for creating docs with sphinx, but feel free to use whatever suits your needs.

Building the documentation can be done through the following command within the main directory:

```
sphinx-build -b html ./docs/source/ ./docs/build/
```

You will need to have the following packages:
```
pip install Sphinx==1.8.5
pip install sphinx_rtd_theme
pip install recommonmark
pip install numpydoc
```

Sphinx 2.0 is currently still broken when used together with numpydoc.

# Project Organization

    ├── cto                <- Source code for use in this project, replace name with package name
    │   ├── __init__.py    <- Makes cto a Python module
    │   │
    │   ├── data_sources   <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make predictions
    │   │   ├── predict.py
    │   │   └── train.py
    │   │
    │   ├── preprocessing  <- Scripts to preprocess data from `data_sources` to obtain features for ML
    │   │   └── build_features.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    |
    ├── data               <- Hidden from source control
    │   └── raw_immutable  <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project to create web pages with docs; 
    |                         see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    |
    ├── output             <- Any generated output data or files by the ML model (hidden from source control).
    │   ├── data           <- Output data relevant for the end user.
    │   ├── models         <- Trained and serialized models, model predictions, or model summaries.
    │   ├── reports        <- Project report(s).
    │   └── visualizations <- Final visualizations (e.g. used in project report).
    │
    ├── pipelines          <- .yaml files for azure devops pipelines or github actions.
    │   ├── build-python-package.yaml
    │   ├── lint-python.yaml
    │   └── test-python.yaml
    |
    ├── references         <- All useful documents, manuals and meta-files related to the project.
    |
    ├── run                <- Contains script to run the model and create final output.
    │   └── configs        <- Various config files, e.g. one used for production, one for testing.
    |
    ├── tests              <- Include all unit and integration tests here.
    |
    ├── conftest.py        <- Necessary for smooth integration of coverage reports
    │
    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt` (if in a hurry)
    |
    ├── setup.cfg          <- sets standard linting options of RHDHV Data Solutions (called by setup.py)
    |
    ├── setup.py           <- makes project pip installable (pip install -e .) so cto package can be imported
                              Add the necessary dependencies here as well!

# Code of Conduct

Contributors to this project agree to adhere to the following [code of conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html).

# References

The data science cookiecutter is inspired and adapted from [https://github.com/drivendata/cookiecutter-data-science/blob/master/README.md](https://github.com/drivendata/cookiecutter-data-science/blob/master/README.md).
