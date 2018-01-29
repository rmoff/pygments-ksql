# -*- coding: utf-8 -*-

from pygments.lexers.sql import SqlLexer
from pygments.token import Name, Keyword

class KSQLLexer(SqlLexer):
    name = 'KSQL'
    aliases = ['ksql']

    EXTRA_KEYWORDS = ['STREAM', 'WINDOW', 'TUMBLING', 'HOPPING', 'STRINGTOTIMESTAMP','KAFKA_TOPIC','VALUE_FORMAT','LIMIT','SELECT', 'WITH', 'VALUES', 'CREATE', 'REGISTER', 'TABLE', 'DESCRIBE', 'PRINT', 'EXPLAIN', 'SHOW', 'LIST', 'TERMINATE', 'LOAD', 'DROP', 'SET', 'EXPORT', 'UNSET', 'RUN', 'ADD', 'APPROXIMATE', 'AT', 'CONFIDENCE', 'NO', 'SUBSTRING', 'POSITION', 'TINYINT', 'SMALLINT', 'INTEGER', 'DATE', 'TIME', 'TIMESTAMP', 'INTERVAL', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'ZONE', 'OVER', 'PARTITION', 'RANGE', 'ROWS', 'PRECEDING', 'FOLLOWING', 'CURRENT', 'ROW', 'VIEW', 'REPLACE', 'GRANT', 'REVOKE', 'PRIVILEGES', 'PUBLIC', 'OPTION', 'EXPLAIN', 'ANALYZE', 'FORMAT', 'TYPE', 'TEXT', 'GRAPHVIZ', 'LOGICAL', 'DISTRIBUTED', 'TRY', 'SHOW', 'TABLES', 'SCHEMAS', 'CATALOGS', 'COLUMNS', 'COLUMN', 'USE', 'PARTITIONS', 'FUNCTIONS', 'TO', 'SYSTEM', 'BERNOULLI', 'POISSONIZED', 'TABLESAMPLE', 'RESCALED', 'UNNEST', 'ARRAY', 'MAP', 'SET', 'RESET', 'SESSION', 'DATA', 'START', 'TRANSACTION', 'COMMIT', 'ROLLBACK', 'WORK', 'ISOLATION', 'LEVEL', 'SERIALIZABLE', 'REPEATABLE', 'COMMITTED', 'UNCOMMITTED', 'READ', 'WRITE', 'ONLY', 'CALL', 'NFD', 'NFC', 'NFKD', 'NFKC', 'IF', 'NULLIF', 'COALESCE']

    def get_tokens_unprocessed(self, text):
        for index, token, value in SqlLexer.get_tokens_unprocessed(self, text):
            if token in Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value
