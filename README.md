
# Tests
- [https://tox.wiki/en/latest/](https://tox.wiki/en/latest/)
## Installation

```shell
$ python -m pip install tox 
```
## pytest
```shell
$ tox
``` 

# Docs
- [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/)

## Sphinx
### Installation
```shell
$ python -m pip install sphinx sphinx_rtd_theme
```

### Initialize
```shell
$ sphinx-quickstart docs 
```
### Generate documents from source
```shell
$ sphinx-apidoc -e -F -o ./docs/source ./gpp
```
### Generate html
```shell
$ make -C ./docs html
```
