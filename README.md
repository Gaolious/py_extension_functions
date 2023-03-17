# 시작하기
 
Django를 이용한 프로젝트에 공통적으로 쓰이는 module 모음 입니다.

## 설치
```
$ pip install ajava_pyext_functions
```

## 설정
설치 이후 Django Project의 settings `INSTALLED_APPS` 에 추가 해야 합니다.

```text
INSTALLED_APPS = (
    ...
    'gpp',
)
```


# Tests
- [https://tox.wiki/en/latest/](https://tox.wiki/en/latest/)
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
