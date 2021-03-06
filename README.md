# packgenmypy - Python package builder

This package adds type checking with `mypy`to the original **packgenlite** package by krokrob (https://github.com/krokrob/packgenlite.git)

It is a meta-package that provide python libs for projects
and mainly `packgenmypy` script.

`packgenmypy` create a Python package template.

## Install `packgenmypy`
```bash
pip install git+https://github.com/alexisgourdol/packgenlite-mypy.git
```

## Create a `newpkgname` package

Use `packgenmypy` to create a new python package:

```bash
packgenmypy newpkgname
```

Check that the package has been created:

```bash
cd newpkgname
tree
.
├── MANIFEST.in
├── Makefile
├── README.md
├── newpkgname
│   ├── __init__.py
│   └── data
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   └── newpkgname-run
├── setup.py
└── tests
    └── __init__.py

6 directories, 8 files
```
