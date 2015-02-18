# -*- coding: utf-8 -*-

from pygments.lexers.sql import SqlLexer
from pygments.token import Name, Keyword

class SqlPlLexer(SqlLexer):
    name = 'SQL PL (SQL Procedural Language - DB2)'
    aliases = ['sqlpl']

    EXTRA_KEYWORDS = ['MODULE']

    def get_tokens_unprocessed(self, text):
        for index, token, value in SqlLexer.get_tokens_unprocessed(self, text):
            if token in Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value
