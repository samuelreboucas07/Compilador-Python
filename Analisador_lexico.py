#coding: utf-8
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
            'false'     : 'FALSE' 
            }

#SIMBOLOS POSSÍVEIS DE ACORDO COM A DESCRIÇÃO DO TRABALHO MAIS AS PALAVRAS RESERVADAS
tokens = list(keywords.values()) + [
   'ID',
   'const_float',
   'asterisco',
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
   'e',
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
]

# EXPRESSÕES REGULARES PARA CADA TOKEN DEFINIDO ACIMA.

t_asterisco = r'\*'              # => *
t_mais  = r'\+'                  # => +
t_menos  = r'-'                  # => -
t_barra_n  = r'/'                # => /
t_l_parentese  = r'\('           # => (
t_r_parentese  = r'\)'           # => )
t_l_chave  = r'\{'               # => {
t_r_chave  = r'\}'               # => }
t_l_cochete  = r'\['             # => [
t_r_cochete  = r'\]'             # => ]
t_ou = r'\|\|'                   # => \\
t_e = r'&&'                      # => &&
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
t_diferente = r'!='              # => !=
t_negacao = r'!'                 # => !
t_virgula = r','                 # => ,
t_ponto = r'\.'                  # => .
t_e_comercial = r'&'             # => &

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
   r'\d+\.\d+'
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
 
lexer = lex.lex()

# FUNÇÃO CONTENDO CASO TESTE.
def teste():
  data = ''' 
         int main()
         {
            int number;
            // printf() dislpays the formatted output 
            printf("Enter an integer\n:\b");  
            
            // scanf() reads the formatted input and stores them
            scanf("%d", &number);  
            
            // printf() displays the formatted output
            printf("You entered: %d", number);
            return 0;
         }
         '''
  lexer.input(data)

  while True:
     tok = lexer.token()
     if not tok: 
          break     
     print(tok)


teste()

