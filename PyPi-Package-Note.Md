📦 PyPI-তে Django App Publish করার সম্পূর্ণ Process

## 1. প্রথমে Project Structure সঠিকভাবে সাজান
```bash
my_django_app/
├── my_django_app/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
├── README.md
├── LICENSE
├── setup.py
├── setup.cfg
├── pyproject.toml
└── MANIFEST.in
```

## 2. Required Files তৈরি করুন

### setup.py (মূল ফাইল)
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rakib-django-core",
    version="0.1.1",  # Version change করুন
    author="Md. Rakib Hassan",
    author_email="rakib1515hassan@gmail.com",
    description="This is a Django-based web application for managing core functionalities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rakib1515hassan/django-core-app",
    packages=find_packages(exclude=['*.pyc', '__pycache__']),  # exclude add করুন
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Django>=3.2",
    ],
    include_package_data=True,
    exclude_package_data={
        '': ['*.pyc', '__pycache__/*'],  # pycache files exclude করুন
    },
)
```


### pyproject.toml (প্যাকেজিং এর জন্য)
```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "rakib-django-core"
version = "0.1.1"
authors = [
    {name = "Md. Rakib Hassan", email = "rakib1515hassan@gmail.com"},
]
description = "This is a Django-based web application for managing core functionalities."
readme = {file = "README.md", content-type = "text/markdown"}
requires-python = ">=3.7"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Framework :: Django",
    "Framework :: Django :: 3.2",
    "Framework :: Django :: 4.0",
]
dependencies = [
    "Django>=3.2",
]

[project.urls]
Homepage = "https://github.com/rakib1515hassan/django-core-app"
```


### MANIFEST.in (অতিরিক্ত ফাইল অন্তর্ভুক্ত করার জন্য)
```plaintext
include LICENSE
include README.md
recursive-include core/templates *
recursive-include core/static *
recursive-include core/locale *
recursive-include core/migrations *.py
prune core/migrations/__pycache__
prune */__pycache__
global-exclude *.pyc
global-exclude __pycache__
global-exclude *.pyo
```


### README.md (ডকুমেন্টেশন)
# My Django App

A reusable Django app for [your app's purpose].

## Installation

```bash
pip install rakib-django-core
``` 


## 3. Configuration [Add configuration details]

### **Package তৈরি করুন**

#### Required tools install করুন
```python
pip install setuptools wheel twine
```

#### Distribution packages তৈরি করুন
```python
python setup.py sdist bdist_wheel
```

এটি dist/ folder-এ দুইটি file তৈরি করবে:

- rakib-django-core-0.1.0.tar.gz
- rakib-django-core-0.1.0-py3-none-any.whl


## 4. PyPI-তে Upload করুন

### Test:-
- Test PyPI-তে প্রথমে test করুন
```python
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
or,
```python
twine upload --repository testpypi dist/* --verbose
``` 

- Test install
```python
pip install -i https://test.pypi.org/simple/ rakib-django-core==0.1.1
```

### Production:-
- PyPI-তে upload করুন
```python
twine upload dist/*
``` 
- PyPI থেকে install করুন
```python
pip install rakib-django-core
```



## 5. Users কীভাবে Install করবে

- সরাসরি install
```python
pip install rakib-django-core
```

- অথবা requirements.txt ফাইলে যোগ করে
``` plaintext
rakib-django-core
```





## Complete Cleanup of Build Files

```bash
# 1. Clean everything
rm -rf dist/ build/ rakib_app.egg-info/

# 2. Update setup.py with version 0.1.1 and exclude patterns

# 3. Update MANIFEST.in

# 4. Build new package
python setup.py sdist bdist_wheel

# 5. Upload with verbose
twine upload --repository testpypi dist/* --verbose
```
Or,
- Complete cleanup
```bash
git clean -fdx
```

- Then rebuild
```python
python setup.py sdist bdist_wheel
``` 
```bash
twine upload --repository testpypi dist/* --verbose
```