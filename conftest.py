from unittest.mock import patch

import pytest
from django.db import connections, transaction

import sys


# global fixture
def pytest_sessionstart(session):
    """
    to avoid
    https://pytest-django.readthedocs.io/en/latest/database.html#multi-db

    Args:
        session:

    Returns:

    """
    from django.test import TestCase
    TestCase.multi_db = True
    TestCase.databases = '__all__'


@pytest.fixture(scope='function')
def multidb():
    atomics = {}
    db_names = [k for k in connections]  # for multi db

    for db in db_names:
        atomics[db] = transaction.atomic(using=db)
        atomics[db].__enter__()

    yield atomics

    for db in reversed(db_names):
        transaction.set_rollback(True, using=db)
        atomics[db].__exit__(None, None, None)


if 'celery' in sys.modules:
    @pytest.fixture(scope='function', autouse=True)
    def celery_app_trap():
        with patch('celery.app.task.Task.delay') as mock:
            mock.side_effect = Exception('You should be mock the async task.')
            yield mock

if 'urllib3' in sys.modules:
    @pytest.fixture(scope='function', autouse=True)
    def http_connection_pool():
        with patch('urllib3.connectionpool.HTTPConnectionPool.urlopen') as mock:
            mock.side_effect = Exception('You should be mock the async task.')
            yield mock
