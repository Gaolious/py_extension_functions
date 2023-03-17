Django를 이용한 프로젝트에 공통적으로 쓰이는 module 모음 입니다.

## 시작하기
### 문서
- https://py-extension-functions.readthedocs.io/

### 설치
- pypi : https://pypi.org/project/ajava-pyext-functions/
- github : https://github.com/Gaolious/py_extension_functions
```shell
$ pip install ajava_pyext_functions
```

### 설정
설치 이후 Django Project의 settings `INSTALLED_APPS` 에 추가 해야 합니다.

```text
INSTALLED_APPS = (
    ...
    'gpp',
)
```


## Build
### Tests
- [https://tox.wiki/en/latest/](https://tox.wiki/en/latest/)
```shell
$ python -m pip install tox 
$ tox
``` 

### Docs
- [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/)

#### Sphinx
```shell
# Install
$ python -m pip install sphinx sphinx_rtd_theme

# Initialize
$ sphinx-quickstart docs 

# Generate documents from source
$ sphinx-apidoc -e -F -o ./docs/source ./gpp

# Generate html
$ make -C ./docs html
```
