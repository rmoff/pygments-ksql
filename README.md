# Pygments lexer for SQL PL (SQL Procedural Language)

## Installation

    $ cd pygments-sql-pl-lexer
    $ [sudo] python setup.py install

## Check if the lexer is present

Simply grep the output of

    $ pygmentize -L lexers

for `sqlpl`

## Use the lexer in LaTeX

Use **sqlpl** as <language>.

    \begin{minted}{<language>}
        <code>
    \end{minted}

For example:

    \begin{minted}{sqlpl}
        CREATE MODULE project
    \end{minted}
