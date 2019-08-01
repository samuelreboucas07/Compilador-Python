#coding: utf-8
import ply.lex as lex

keywords = {
            'if': 'IF', 
            'while': 'WHILE', 
            'for': 'FOR', 
            'do': 'DO', 
            'continue': 'CONTINUE', 
            'break': 'BREAK', 
            'main': 'MAIN', 
            'void': 'VOID', 
            'return': 'RETURN', 
            'else': 'ELSE',
            'float': 'FLOAT',
            'int': 'INT',
            'boolean': 'BOOLEAN',
            'char': 'CHAR',
            'printf': 'PRINTF',
            'scanf': 'SCANF'
            }
tokens = list(keywords.values()) + [
   'ID',
   'const_float',
   'asterisco',
   'const_int',
   'mais',
   'menos',
   'barra_n',
   'barra_i',
   'atribuicao',
   'l_parentese',
   'r_parentese',
   'l_chave',
   'r_chave',
   'l_cochete',
   'r_cochete',
   'ou',
   'e',
   'ponto_virgula',
   'const_char_min',
   'const_char_mai',   
   'const_string',
   'aspas_simples',
   'aspas_duplas',
   'maior',
   'menor',
   'maior_igual',
   'menor_igual',
   'mod',
   'igual',
   'negacao',
   'diferente',
   'virgula',
   'ponto',
]

t_asterisco = r'\*'
t_mais  = r'\+'
t_menos  = r'-'
t_barra_n  = r'/'
t_barra_i  = r'\\'
t_l_parentese  = r'\('
t_r_parentese  = r'\)'
t_l_chave  = r'\{'
t_r_chave  = r'\}'
t_l_cochete  = r'\['
t_r_cochete  = r'\]'
t_ou = r'\|\|'
t_e = r'&&'
t_ponto_virgula = r';'
t_const_char_min = r'\'[a-z]?\''
t_const_char_mai = r'\'[A-Z]?\''
t_const_string = r'\"(\n|.)*?\"'
t_aspas_simples = r'\''
t_aspas_duplas = r'\"'
t_maior = r'>'
t_menor = r'<'
t_maior_igual = r'>='
t_menor_igual = r'<='
t_mod = r'%'
t_atribuicao = r'='
t_igual = r'=='
t_diferente = r'!='
t_negacao = r'!'
t_virgula = r','
t_ponto = r'\.'



def t_const_float(t):
   # r'\d+\.\d+'
   r'\-?\d+\.\d+'   
   t.value = float(t.value)
   return(t)

def t_const_int(t):
   r'\d+'
   t.value = int(t.value)    
   return t

def t_comment_multiline(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    pass
 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t
 
lexer = lex.lex()

def test():
  data = '''
              int main(void)
               { 
                  /* Comentário em linha
                  */
                  int a;            // declara a variável "a"
                  a = 3 + 2;        // soma 3 com 2
               }
                  "teste_String&98"
      '''
      

  lexer.input(data)

  while True:
     tok = lexer.token()
     if not tok: 
          break     
     print(tok)


test()

