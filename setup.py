# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.3'

setup(name='pygments-ksql-lexer',
    version=version,
    description='Pygments lexer for KSQL, a SQL Streaming engine for Apache Kafka',
    long_description=open('README.rst').read(),
    keywords='pygments sql lexer apache kafka ksql streaming',
    author='Robin Moffatt',
    author_email='robin@rmoff.net',
    url='https://github.com/rmoff/pygments-ksql',
    license='GPL',
    packages=find_packages(),
    install_requires=[
        'pygments >= 1.4',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        [pygments.lexers]
        ksql=ksql_lexer:KSQLLexer
    """,
)
