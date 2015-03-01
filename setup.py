from setuptools import setup, find_packages


install_requires = [
  'flask == 0.10.1', 'sqlalchemy == 0.9.8',
  'alembic == 0.7.4'
]

test_require = [
    'pytest == 2.6.4',
]

docs_require = [
    'sphinx == 1.2.3',
]

setup(
    name='simple_python_project',
    version='0.0.1',
    author='Kang hyojun',
    author_email='hyojun@admire.kr',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=test_require,
    extras_require={
        'docs': docs_require,
        'tests': test_require
    }
)
