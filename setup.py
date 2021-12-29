from setuptools import setup

setup(
    name='snooki-api',
    version='0.0.1',
    description='REST API for pi (pet project).',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'requests'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)