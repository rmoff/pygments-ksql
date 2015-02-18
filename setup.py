# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.1'

setup(name='pygments-sql-pl-lexer',
    version=version,
    description='Pygments lexer for SQL PL (SQL Procedural Language), a DB2 implementation of ANSI SQL/PSM',
    long_description=open('README.md').read(),
    keywords='pygments sql lexer',
    author='Dimitar Dimitrov',
    author_email='admin@mitakas.com',
    url='',
    license='GPL',
    packages=find_packages(),
    install_requires=[
        'pygments >= 1.4',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        [pygments.lexers]
        sqlpl=sql_pl_lexer:SqlPlLexer
    """,
)
