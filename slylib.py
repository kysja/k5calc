from sly import Lexer, Parser
import math


class CalcLexer(Lexer):
    tokens = { INT, FLOAT, PLUS, TIMES, MINUS, DIVIDE, LPAREN, RPAREN, POWER, POWER2, SQRT }
    ignore = ' \t'

    # Tokens
    # NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'



    # @_(r'\d+\.\d+')
    # def FLOAT(self, t):
    #     t.value = float(t.value)   # Convert to a numeric value
    #     return t

    # @_(r'\d+')
    # def INT(self, t):
    #     t.value = int(t.value)   # Convert to a numeric value
    #     return t

    FLOAT = r'\d+\.\d+'
    INT = r'\d+'

    # Special symbols
    SQRT = r'sqrt'
    PLUS = r'\+'
    MINUS = r'-'
    POWER = r'\^'
    POWER2 = r'\*\*'
    TIMES = r'\*'
    DIVIDE = r'/'
    # ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS),
        ('left', POWER, POWER2)
        )

    def __init__(self):
        self.names = { }

    

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('INT')
    def expr(self, p):
        return int(p.INT)

    @_('FLOAT')
    def expr(self, p):
        return float(p.FLOAT)

    @_('expr POWER expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    @_('expr POWER2 expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    @_('SQRT LPAREN expr RPAREN')
    def expr(self, p):
        return math.sqrt(p.expr)


