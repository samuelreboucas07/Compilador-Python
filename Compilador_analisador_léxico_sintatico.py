#coding: utf-8
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "./classes/")

from print_visitor import PrinterVisitor


from Main import initial
from assignment_value_const import Assignment_value_const
from const_values import const_values
# from condition_if import condition_if
# from condition_if_else import condition_if_else
from teste import teste
# from const_int import const_int
# if sys.version_info[0] >= 3:
#     raw_input = input

import ply.lex as lex
#SAMUEL REBOUÇAS DE JESUS

#PALAVRAS RESERVADAS
keywords = {
            'if'        : 'IF', 
            'while'     : 'WHILE', 
            'for'       : 'FOR', 
            'do'        : 'DO', 
            'continue'  : 'CONTINUE', 
            'break'     : 'BREAK', 
            'main'      : 'MAIN', 
            'void'      : 'VOID', 
            'return'    : 'RETURN', 
            'else'      : 'ELSE',
            'float'     : 'FLOAT',
            'int'       : 'INT',
            'boolean'   : 'BOOLEAN',
            'char'      : 'CHAR',
            'printf'    : 'PRINTF',
            'scanf'     : 'SCANF',
            'true'      : 'TRUE',
            'false'     : 'FALSE',
            'const'	  	: 'CONST'
            }

#SIMBOLOS POSSÍVEIS DE ACORDO COM A DESCRIÇÃO DO TRABALHO MAIS AS PALAVRAS RESERVADAS
tokens = list(keywords.values()) + [
   'ID',
   'const_float',
   'const_int',
   'mais',
   'menos',
   'barra_n',
   'atribuicao',
   'l_parentese',
   'r_parentese',
   'l_chave',
   'r_chave',
   'l_cochete',
   'r_cochete',
   'ou',
   'and',
   'ponto_virgula',
   'const_char',
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
   'e_comercial',
   'barra_v',
   'interrogacao',
   'dois_pontos',
   'mult',
]

# EXPRESSÕES REGULARES PARA CADA TOKEN DEFINIDO ACIMA.

# t_asterisco = r'\*'            # => *
t_mult = r'\*'                   # => *
t_mais  = r'\+'                  # => +
t_menos  = r'\-'                 # => -
t_barra_n  = r'/'                # => /
t_l_parentese  = r'\('           # => (
t_r_parentese  = r'\)'           # => )
t_l_chave  = r'\{'               # => {
t_r_chave  = r'\}'               # => }
t_l_cochete  = r'\['             # => [
t_r_cochete  = r'\]'             # => ]
t_ou = r'\|\|'                   # => \\
t_and = r'&&'                    # => &&
t_ponto_virgula = r';'           # => ;
t_aspas_simples = r'\''          # => '
t_aspas_duplas = r'\"'           # => "
t_maior = r'>'                   # => >
t_menor = r'<'                   # => <
t_maior_igual = r'>='            # => >=
t_menor_igual = r'<='            # => <=
t_mod = r'%'                     # => %
t_atribuicao = r'='              # => =
t_igual = r'=='                  # => ==
t_negacao = r'!'                 # => !
t_diferente = r'!='              # => !=
t_virgula = r','                 # => ,
t_ponto = r'\.'                  # => .
t_e_comercial = r'&'             # => &
t_barra_v = r'\|'
t_interrogacao = r'\?'
t_dois_pontos = r'\:'
# FUNÇÕES RESPONSÁVEIS POR DEFINIR AS EXPRESSÕES REGULARES E RETORNAR O TOKEN DAS ENTRADAS 
# QUE POSSUEM DIFERENTES POSSIBILIDADES QUE RESPEITEM UM ÚNICO PADRÃO. 

# FUNÇÃO QUE VERIFICA SE A ENTRADA É EQUIVALENTE A UM CARACTERE : 'C'
def t_const_char(t):
   r'\'(\n|.)?\''
   return (t)

# FUNÇÃO QUE VERIFICA SE A ENTRADA É EQUIVALENTE A UMA STRING : "STRING123 212"
def t_const_string(t):
   r'\"(\n|.)*?\"'
   return(t)
   
# FUNÇÃO QUE VERIFICA SE A ENTRADA É EQUIVALENTE A UM NÚMERO REAL : 1.2       
def t_const_float(t):
   r'([0-9]*[.][0-9]+((E|e)[+|-]?[0-9]+)?) | ([0-9]+([.][0-9]+)?(E|e)[+|-]?[0-9]+)'
   # r'(([0-9]*[.]?[0-9]+([ed|Ed][-+]?[0-9]+)?)|(inf)|(nan))'
   t.value = float(t.value)
   return(t)


# FUNÇÃO QUE VERIFICA SE A ENTRADA É EQUIVALENTE A UM NÚMERO INTEIRO : 10       
def t_const_int(t):
   r'\d+'
   t.value = int(t.value)    
   return t


# FUNÇÃO QUE IGNORA UMA LINHA IDENTIFICADA COMO COMENTÁRIO, E O CONJUNTO DE LINHAS COMENTADAS.    
def t_comment_multiline(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    pass
 
 
# FUNÇÃO QUE VERIFICA A QUEBRA DE LINHA.     
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# RESPONSÁVEL POR IGNORAR ESPAÇOS EM BRANCO.
t_ignore  = ' \t'

# FUNÇÃO PARA DEFINIR UM CARACTERE ILEGAIS, OU SEJA, UM CARACTERE NÃO RECONHECIDO POR NENHUMA REGRA DEFINIDA.  
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

    
# VERIFICA SE A ENTRADA REFERE-SE A UMA POSSIVEL VARIÁVEL NO CÓDIGO, RETORNANDO SEU TOKEN.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')
    return t
 
lex.lex()
from Impressao import Impressao
impressao = Impressao()

precedence = (
    ('right', 'REDUCE'),
  	('right', 'ELSE'),
    ('left', 'ou'),
    ('left', 'and'),
    ('right', 'negacao'),
    ('left', 'igual', 'diferente'),
    ('left', 'maior', 'maior_igual', 'menor', 'menor_igual'),
    ('left', 'mais', 'menos'),
    ('left', 'mult', 'barra_n', 'mod'),
    ('right', 'atribuicao'),
    ('right', 'UMULT', 'UMINUS', 'UMAIS', 'e_comercial'),
)

from const_int import const_int_expression
from stm import stm
from condition_if import condition_if
def p_scope_main(p):
    '''scope_main : INT MAIN l_parentese r_parentese l_chave statement RETURN expression ponto_virgula r_chave'''
    p[0] = initial(p[6])

def p_statement(p):
    '''statement : declaration_vector statement
                | declaration_pointer statement
                | declaration_const statement
                | assignment_value statement
                | condition
                | iteration_while statement
                | iteration_for statement
                | iteration_do_while statement
                | display statement
                | change_flow_break statement
                | change_flow_continue statement
                | read_scan statement
                | block statement
                | lambda
                '''

    if(len(p) == 3):
      p[0] = stm(p[1], p[2])
    elif(len(p) == 2):
      p[0] = p[1]

from _lambda import _lambda

def p_lambda(p):
  '''lambda : '''
  p[0] = _lambda('')

from _break import _break
from _continue import _continue

def p_change_flow_break(p): 
  '''change_flow_break : BREAK ponto_virgula
  '''
  p[0] = _break(p[1])

def p_change_flow_continue(p): 
  '''change_flow_continue : CONTINUE ponto_virgula
  '''
  p[0] = _continue(p[1])

from declaracaoVetor import declaracaoVetor
from declaracao_vetor_explicita_sem_tamanho import declaracao_vetor_explicita_sem_tamanho
from declaracao_vetor_explicito import declaracao_vetor_explicito
from declaracao_vetor_ponteiro import declaracao_vetor_ponteiro
from declaracao_vetor_ponteiro_explicito import declaracao_vetor_ponteiro_explicito

def p_declaration_vector(p):
  '''declaration_vector : type_variable ID l_cochete expression r_cochete declaration_matriz ponto_virgula 
  					  | type_variable ID l_cochete r_cochete declaration_matriz atribuicao l_chave declaration_vector_swap r_chave ponto_virgula 
  					  | type_variable ID l_cochete expression r_cochete declaration_matriz atribuicao l_chave declaration_vector_swap r_chave ponto_virgula 
              | type_variable declaration_pointer_swap ID l_cochete expression r_cochete declaration_matriz ponto_virgula 
  					  | type_variable declaration_pointer_swap ID l_cochete expression r_cochete declaration_matriz atribuicao l_chave declaration_vector_swap r_chave ponto_virgula 
  					  '''
  if(len(p) == 8):
    p[0] = declaracaoVetor(p[1], p[2], p[4], p[6])     
  elif(len(p) == 11):
    p[0] = declaracao_vetor_explicita_sem_tamanho(p[1], p[2], p[5], p[8]) 
  elif(len(p) == 9):
    p[0] = declaracao_vetor_ponteiro(p[1], p[2], p[3], p[5], p[7])
  elif(len(p) == 12):
    p[0] = declaracao_vetor_explicito(p[1], p[2],  p[4], p[6], p[9])    
  elif(len(p) == 13):
    p[0] = declaracao_vetor_ponteiro_explicito(p[1], p[2], p[3], p[5], p[7], p[10])

from declaracao_matriz_rec import declaracao_matriz_rec
from declaracao_matriz import declaracao_matriz

def p_declaration_matriz(p):
  '''declaration_matriz : l_cochete expression r_cochete declaration_matriz
                        | l_cochete r_cochete declaration_matriz
                        | lambda
  '''
  if(len(p) == 5):
    p[0] = declaracao_matriz_rec(p[2], p[4])
  elif(len(p) == 4):
    p[0] = declaracao_matriz(p[3])
  else:
    p[0] = p[1]

from valor_declaracao_vetor import valor_declaracao_vetor
from sub_valor_declaracao_vetor import sub_valor_declaracao_vetor
from vetor_valor_rec import vetor_valor_rec
from declaracao_ponteiro import declaracao_ponteiro
from declaracao_ponteiro_explicito import declaracao_ponteiro_explicito
def p_declaration_vector_swap(p):
    '''
    declaration_vector_swap : const_values virgula declaration_vector_swap
                            | l_chave declaration_vector_swap r_chave declaration_vector_swap
                            | expression 
                            | virgula declaration_vector_swap
                            | lambda
    '''
    if(len(p) == 4):
      p[0] = valor_declaracao_vetor(p[1], p[3])
    elif(len(p) == 5):
      p[0] = sub_valor_declaracao_vetor(p[2], p[4])
    elif(len(p) == 3):
      p[0] = vetor_valor_rec(p[2])      
    elif(len(p) == 2):
      p[0] = p[1]
      
def p_declaracao_pointer(p):
  '''declaration_pointer : type_variable declaration_pointer_swap ID ponto_virgula
                         | type_variable declaration_pointer_swap ID atribuicao expression ponto_virgula
                        '''
  if(len(p)==5):
    p[0] = declaracao_ponteiro(p[1], p[2], p[3])
  elif(len(p)==7):
    p[0] = declaracao_ponteiro_explicito(p[1], p[2], p[3], p[5])
    
from ponteiro_rec import ponteiro_rec
from asterisco_ponteiro import asterisco_ponteiro

def p_declaration_pointer_swap(p):
  '''
  declaration_pointer_swap : mult declaration_pointer_swap
                           | mult
  '''
  if(len(p) == 3):
    p[0] = ponteiro_rec(p[1], p[2])

  else:
    p[0] = asterisco_ponteiro(p[1])

from declaracao_const_explicita import declaracao_const_explicita
from declaracao_const import declaracao_const
from Assignment_value_vet import Assignment_value_vet

def p_declaration_const(p):
  '''declaration_const : type_variable ID atribuicao expression ponto_virgula 
                       | type_variable ID ponto_virgula '''
  if(len(p) == 6):
        p[0] = declaracao_const_explicita(p[1], p[2], p[4])
  else:
    p[0] = declaracao_const(p[1], p[2]) 

from condition_if import condition_if
from condition_if_else import condition_if_else
from block import block


def p_condition(p):
  '''condition : IF l_parentese expression r_parentese statement %prec REDUCE
               | IF l_parentese expression r_parentese statement ELSE statement
  '''
  if(len(p) == 6):
    p[0] = condition_if(p[3], p[5])
  else:
    p[0] = condition_if_else(p[3], p[5], p[7])
    
        
def p_block(p):
  '''block : l_chave statement r_chave'''
  p[0] = block(p[2])

from _while import _while
from do_while import do_while
from Assignment_pointer import Assignment_pointer
def p_iteration_while(p):
  '''iteration_while : WHILE l_parentese expression r_parentese l_chave statement r_chave'''
  p[0] = _while(p[3], p[6])

def p_iteration_do_while(p):
  '''iteration_do_while : DO l_chave statement r_chave WHILE l_parentese expression r_parentese ponto_virgula'''
  p[0] = do_while(p[3], p[7])

from _for import _for
def p_iteration_for(p):
  ''' iteration_for : FOR l_parentese arg ponto_virgula arg ponto_virgula arg r_parentese block
  '''
  p[0] = _for(p[3], p[5], p[7], p[9])

def p_arg(p):
      '''arg : expression 
             | lambda'''
      p[0] = p[1]
      
def p_assignment_value(p):
  '''assignment_value : ID atribuicao expression ponto_virgula
                      | ID l_cochete expression r_cochete declaration_matriz atribuicao expression ponto_virgula
                      | declaration_pointer_swap ID atribuicao expression ponto_virgula
                        '''
  if(len(p) == 5):
    p[0] = Assignment_value_const(p[1], p[3])
  elif(len(p) == 9):
    p[0] = Assignment_value_vet(p[1], p[3], p[5], p[7])
  elif(len(p) == 6):
    p[0] = Assignment_pointer(p[1], p[2], p[4])
    

def p_expression(p):
  '''expression : expression_mais
                | expression_menos
                | expression_mult
                | expression_barra_n
                | expression_mod
                | expression_and
                | expression_ou
                | expression_igual
                | expression_diferente
                | expression_menor
                | expression_maior
                | expression_menor_igual
                | expression_maior_igual
                | expression_unary_e_comercial 
                | expression_unary_menos
                | expression_unary_mais
                | expression_unary_mult
                | expression_negacao
                | expression_type_variable
                | expression_type_variable_atrib
                | expression_const_values
                | expression_id
                | expression_id_atrib
                | expression_id_cochete
                | expression_parentese_init
  '''
  p[0] = p[1]

from expression_mais import expression_mais
from expression_menos import expression_menos
from expression_mult import expression_mult
from expression_barra_n import expression_barra_n
from expression_mod import expression_mod
from expression_and import expression_and
from expression_ou import expression_ou
from expression_igual import expression_igual
from expression_diferente import expression_diferente
from expression_maior import expression_maior
from expression_menor import expression_menor
from expression_maior_igual import expression_maior_igual
from expression_menor_igual import expression_menor_igual
from expression_unary_e_comercial import expression_unary_e_comercial
from expression_unary_mais import expression_unary_mais
from expression_unary_menos import expression_unary_menos
from expression_unary_mult import expression_unary_mult


def p_expression_mais(p):
  ''' expression_mais : expression mais expression
  '''
  p[0] = expression_mais(p[1], p[3])

def p_expression_menos(p):
  ''' expression_menos : expression menos expression
  '''
  p[0] = expression_menos(p[1], p[3])

def p_expression_mult(p):
  ''' expression_mult : expression mult expression
  '''
  p[0] = expression_mult(p[1], p[3])

def p_expression_barra_n(p):
  ''' expression_barra_n : expression barra_n expression
  '''
  p[0] = expression_barra_n(p[1], p[3])

def p_expression_mod(p):
  ''' expression_mod : expression mod expression
  '''
  p[0] = expression_mod(p[1], p[3])

def p_expression_and(p):
  ''' expression_and : expression and expression
  '''
  p[0] = expression_and(p[1], p[3])

def p_expression_ou(p):
  ''' expression_ou : expression ou expression
  '''
  p[0] = expression_ou(p[1], p[3])

def p_expression_igual(p):
  ''' expression_igual : expression igual expression
  '''
  p[0] = expression_igual(p[1], p[3])

def p_expression_diferente(p):
  ''' expression_diferente : expression diferente expression
  '''
  p[0] = expression_diferente(p[1], p[3])

def p_expression_menor(p):
  ''' expression_menor : expression menor expression
  '''
  p[0] = expression_menor(p[1], p[3])

def p_expression_maior(p):
  ''' expression_maior : expression maior expression
  '''
  p[0] = expression_maior(p[1], p[3])

def p_expression_maior_igual(p):
  ''' expression_maior_igual : expression maior_igual expression
  '''
  p[0] = expression_maior_igual(p[1], p[3])

def p_expression_menor_igual(p):
  ''' expression_menor_igual : expression menor_igual expression 
  '''
  p[0] = expression_menor_igual(p[1], p[3])

def p_expression_e_comercial(p):
  ''' expression_unary_e_comercial : e_comercial expression
  '''
  p[0] = expression_unary_e_comercial(p[2])

def p_expression_menos_unary(p):
  ''' expression_unary_menos : menos expression %prec UMINUS
  '''
  p[0] = expression_unary_menos(p[2])


def p_expression_mais_unary(p):
  ''' expression_unary_mais : mais expression %prec UMAIS 
  '''
  p[0] = expression_unary_mais(p[2])


def p_expression_mult_unary(p):
  ''' expression_unary_mult : mult expression %prec UMULT
  '''
  p[0] = expression_unary_mult(p[2])

from expression_parentese import expression_parentese
from expression_negacao import expression_negacao
from expression_type_variable_atrib import expression_type_variable_atrib
from id_variable import id_variable
from expression_id_cochete import expression_id_cochete
from expression_id_atrib import expression_id_atrib
from expression_parentese import expression_parentese
from expression_cochete import expression_cochete
from expression_cochete_rec import expression_cochete_rec
from expression_parentese_init import expression_parentese_init


def p_expression_parentese_init(p):
  ''' expression_parentese_init : expression_parentese expression_parentese_rec
  '''
  p[0] = expression_parentese_init(p[1], p[2])


def p_expression_negacao(p):
  ''' expression_negacao : negacao expression
  '''
  p[0] = expression_negacao(p[2])


def p_expression_type_variable(p):
  ''' expression_type_variable : type_variable
  '''
  p[0] = p[1]


def p_expression_type_variable_atrib(p):
  ''' expression_type_variable_atrib : type_variable ID atribuicao expression
  '''
  p[0] = expression_type_variable_atrib(p[1], p[2], p[4])

def p_expression_const_values(p):
  ''' expression_const_values : const_values
  '''
  p[0] = p[1]

from id_variable import id_variable

def p_expression_id(p):
  ''' expression_id : ID
  '''
  p[0] = id_variable(p[1])


def p_expression_id_cochete(p):
  ''' expression_id_cochete : ID expression_cochete
  '''
  p[0] = expression_id_cochete(p[1], p[2])


def p_expression_id_atrib(p):
  ''' expression_id_atrib : ID atribuicao expression
  '''
  p[0] = expression_id_atrib(p[1], p[3])


def p_expression_parentese_rec(p):
  '''expression_parentese_rec  : const_values
                              | expression_id 
                              | expression_parentese
                              | lambda
       '''
  p[0] = p[1]

def p_expression_parentese(p):
  '''expression_parentese : l_parentese expression r_parentese
  '''
  p[0] = expression_parentese(p[2])


def p_expression_id(p):
  '''expression_id : ID'''
  p[0] = id_variable(p[1])

  
def p_expression_cochete(p):
  '''expression_cochete : l_cochete expression r_cochete
                        | l_cochete expression r_cochete expression_cochete
          '''
  if(len(p) == 5):
    p[0] = expression_cochete_rec(p[2], p[4])
  elif(len(p) == 4):
    p[0] = expression_cochete(p[2])

from print import declaracao_print
from print import display_option
from print import display_option_const
from print import display_option_pointer
def p_display(p):
  '''display : PRINTF l_parentese const_string display_option r_parentese ponto_virgula
  '''
  p[0] = declaracao_print(p[3] ,p[4])

def p_display_option(p):
  '''display_option : display_opt_id
                    | display_opt_const
                    | display_opt_pointer
                    | lambda
  '''
  p[0] = p[1]

def p_display_opt_id(p):
  '''display_opt_id : virgula ID display_option'''
  p[0] = display_option(p[2], p[3])

def p_display_opt_const(p):
  '''display_opt_const : virgula const_values display_option'''
  p[0] = display_option_const(p[2], p[3])

def p_display_opt_pointer(p):
  '''display_opt_pointer : virgula declaration_pointer_swap ID display_option'''
  p[0] = display_option_pointer(p[2], p[3], p[4])

from scan import _scan
from read_option import read_option

def p_read_scan(p):
  '''read_scan : SCANF l_parentese const_string read_option r_parentese ponto_virgula
  '''
  p[0] = _scan(p[3], p[4])

def p_read_option(p):
  '''read_option : virgula e_comercial ID read_option
                 | lambda
  '''
  if(len(p) == 5):
    p[0] = read_option(p[2], p[3], p[4])
  elif(len(p) == 2):
    p[0] = p[1]

def p_type_variable(p):
  '''type_variable : type_variable_int
                   | type_variable_float
                   | type_variable_char
                   | type_variable_boolean
                   | type_variable_void
  '''
  p[0] = p[1]

from type_variable_int import type_variable_int
from type_variable_float import type_variable_float
from type_variable_char import type_variable_char
from type_variable_boolean import type_variable_boolean
from type_variable_void import type_variable_void


def p_type_variable_int(p):
  '''type_variable_int : INT
  '''
  p[0] = type_variable_int(p[1])

def p_type_variable_float(p):
  '''type_variable_float : FLOAT
  '''
  p[0] = type_variable_float(p[1])

def p_type_variable_char(p):
  '''type_variable_char : CHAR
  '''
  p[0] = type_variable_char(p[1])


def p_type_variable_boolean(p):
  '''type_variable_boolean : BOOLEAN
  '''
  p[0] = type_variable_boolean(p[1])
         

def p_type_variable_void(p):
  '''type_variable_void : VOID
  '''
  p[0] = type_variable_void(p[1])

from const_int import const_int_expression
from const_float import const_float_expression
from const_char import const_char_expression
from const_true import const_true_expression
from const_false import const_false_expression
from const_string import const_string_expression

def p_const_values(p):
  '''const_values : value_const_int
                  | value_const_float
                  | value_const_char
                  | value_const_string
                  | value_const_true
                  | value_const_false
  '''
  p[0] = p[1]

def p_value_const_int(p):
  '''value_const_int : const_int
  '''
  p[0] = const_int_expression(p[1])

def p_value_const_float(p):
  '''value_const_float : const_float
  '''
  p[0] = const_float_expression(p[1])

def p_value_const_char(p):
  '''value_const_char : const_char
  '''
  p[0] = const_char_expression(p[1])

def p_value_const_string(p):
  '''value_const_string : const_string
  '''
  p[0] = const_string_expression(p[1])

def p_value_const_true(p):
  '''value_const_true : TRUE
  '''
  p[0] = const_true_expression(p[1])

def p_value_const_false(p):
  '''value_const_false : FALSE
  '''
  p[0] = const_false_expression(p[1])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc
import sys
yacc.yacc()
arqTexto = sys.argv[1]
arquivo = open(arqTexto, 'r')
s = arquivo.read()

yacc.parse(s).accept(impressao)
