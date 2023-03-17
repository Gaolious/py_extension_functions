설치하기
==================

Installation
--------------------
pip를 이용한 설치::

 $ pip install gaolious_utils

setup.py를 이용한 설치::

 $ git clone git://github.com/Gaoilious/gaolious-utils.git
 $ cd gaolious-utils
 $ python setup.py install


Development
--------------------

::

 from gpp import texts


Configuration
--------------------

setting of your Django project *settings.py* file.::

  INSTALLED_APPS = (
      ...
      'gpp',
  )
