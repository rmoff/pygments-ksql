Contents
========

KSQL is a streaming SQL engine for Apache Kafka. 

This module extends the *SqlLexer* lexer of `Pygments`_ to support more
keywords of KSQL.

Installation
============

Use the following commands to install the package::

    $ cd pygments-ksql-lexer
    $ [sudo] python setup.py install

Check if the lexer is present
=============================

Simply grep the output of the following command for **ksql**.::

    $ pygmentize -L lexers | grep ksql

Acknowledgements
================

Forked and completely based on `https://github.com/mitakas/pygments-sql-pl-lexer` !
