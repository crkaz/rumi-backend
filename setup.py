from setuptools import setup

setup(
    name='snooki-server',
    version='0.0.1',
    description='Microserver REST API for pi.',
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