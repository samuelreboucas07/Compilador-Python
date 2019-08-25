import sys
sys.path.insert(0, "./classes/")

from teste import teste
from Main import initial

declaracoes = {}
declaracoes_explicitas = {}
tipo_variavel = [];
dentro_laco = {"into": ""}

#Classes de Impressão
class Impressao(object):
	error = False
#Funções de terminais(numeros e variáveis).
	def visita_main(self, initial2):
		initial2.expressao_esquerda.accept(self)
		
	def visita_type_int(self, variable):
		# print(variable.type_decl, end="")
		pass
	def visita_type_float(self, variable):
		# print(variable.type_decl, end="")
		pass
	def visita_type_char(self, variable):
		# print(variable.type_decl, end="")
		pass
	def visita_type_boolean(self, variable):
		# print(variable.type_decl, end="")
		pass
	def visita_type_void(self, variable):
		# print(variable.type_decl, end="")
		pass
	def visita_const_int(self, variable):
		# print(variable.const1, end="")
		pass
	def visita_const_float(self, variable):
		# print(variable.const1, end="")
		pass
	def visita_const_char(self, variable):
		# print(variable.const1, end="")
		pass
	def visita_const_string(self, variable):
		# print(variable.const1, end="")
		pass
	def visita_const_true(self, variable):
		# print(variable.const1, end="")
		pass

	def visita_const_false(self, variable):
		# print(variable.const1, end="")
		pass

	def visita_expression_operacao(self, op_expression):
		# print("(", end="")
		op_expression.expressao_esquerda.accept(self)
		# print(op_expression.type, end="")
		op_expression.expressao_direita.accept(self)
		# print(")", end="")

	def visita_expression_unary(self, op_expression):
		# print(op_expression.type, end="")
		op_expression.expressao_direita.accept(self)


	def visita_expression_parentese(self, op_operation):
		op_operation.expressao_centro.accept(self)

	def visita_expression_negacao(self, op_operation):
		# print(op_operation.type, end="")
		op_operation.expressao_centro.accept(self)

	def visita_expression_type_variable_atrib(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		# op_operation.expressao_centro.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_id_variable(self, op_operation):
		# print(op_operation._id)
		pass
	def visita_expression_id_cochete(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_expression_id_atrib(self, op_operation):
		# print("("+op_operation._id, end="")
		# print(" = ", end="")
		op_operation.expressao_direita.accept(self)
		# print(")", end="")

	def visita_expression_parentese(self, op_operation):
		op_operation.expressao_centro.accept(self)

	def visita_expression_cochete_rec(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_id(self, op_operation):
		# print(op_operation._id, end="")
		pass
	def visita_expression_parentese_init(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_lambda(self, op_operation):
		# print(op_operation.type)
		pass

	def visita_declaracao_const_explicita(self, op_operation):
		if(op_operation._id in declaracoes):
			print("\nError: Variárvel já existente")
		else:
			tipo_const = ""
			# print(type(op_operation.expressao_direita.avalia()))
			if(type(op_operation.expressao_direita.avalia()) == float):
				tipo_const = "float"
			if(type(op_operation.expressao_direita.avalia()) == int):
				tipo_const = "int"
			if(type(op_operation.expressao_direita.avalia()) == str):
				tipo_const = "char"
			if(op_operation.expressao_direita.avalia() == "true" or op_operation.expressao_direita.avalia() == "false"):
				tipo_const = "boolean"
			if((vars(op_operation.tipo_variavel)['type_decl']) == tipo_const):
				op_operation.expressao_esquerda.accept(self)
				# print(" "+op_operation._id+" ", end="")
				# print(op_operation.type, end="")
				op_operation.expressao_direita.accept(self)
				declaracoes[op_operation._id] = op_operation.tipo_variavel.avalia()
			else:
				print("Error -> Variável '"+op_operation._id+"' é do tipo "+op_operation.tipo_variavel.avalia()+", Entretanto foi passada um valor de outro tipo.")
	
	def visita_declaracao_const(self, op_operation):
		if(op_operation._id in declaracoes):
			print("\nError: Variárvel já existente")
		else:
			op_operation.expressao_esquerda.accept(self)
			# print(" "+op_operation._id, end="")
			declaracoes[op_operation._id] = op_operation.tipo_variavel.avalia()

	def visita_vetor(self, op_operation):

		if(type(op_operation.expressao_direita.avalia())==int):
			op_operation.expressao_esquerda.accept(self)
			# tesq = tipo
			# print(" "+op_operation._id, end = "")
			# print("[", end = "")
			op_operation.expressao_direita.accept(self)
			# print("]", end = "")
			op_operation.expressao_direita_rec.accept(self)
			declaracoes[op_operation._id] = op_operation.tipo_vetor.avalia()

		else:
			print("Error -> Argumento inválido.")

	def visita_vetor_explicito_sem_tamanho(self, op_operation):
		if(op_operation._id in declaracoes):
			print("\nError-> Variárvel já existente.")
			if(op_operation._id in declaracoes):
				print("\nError: Variárvel já existente")
			else:
				# if(tipo_const == op_operation.tipo.avalia()):
				op_operation.expressao_esquerda.accept(self)
				# print(" "+op_operation._id, end="")
				# print("[]", end="")
				op_operation.expressao_direita_rec.accept(self)
				# print(" = {", end="")
				op_operation.expressao_direita_valor.accept(self)
				# print("}", end="")
				declaracoes[op_operation._id] = op_operation.tipo_vetor.avalia()
		else:
			print("Error -> Argumento inválido.")

	def visita_vetor_explicito(self, op_operation):
		if(op_operation._id in declaracoes):
			print("\nError-> Variárvel já existente.")
		else:
			if(type(op_operation.expressao_esquerda_expressao.avalia())==int):

				op_operation.expressao_esquerda.accept(self)
				# print(" "+op_operation._id, end="")
				# print("[", end="")
				op_operation.expressao_esquerda_expressao.accept(self)
				# print("]", end="")
				op_operation.expressao_direita_rec.accept(self)
				# print(" = {", end="")
				op_operation.expressao_direita_valor.accept(self)
				# print("}", end="")
				declaracoes[op_operation._id] = op_operation.tipo_vetor.avalia()
				
			else:
				print("Error -> Argumento inválido.")

	def visita_vetor_ponteiro(self, op_operation):
		if(op_operation._id in declaracoes):
			print("\nError: Variárvel já existente")
		else:	
			op_operation.expressao_esquerda.accept(self)
			# print(" ", end="")
			op_operation.expressao_esquerda_pointer.accept(self)
			# print(""+op_operation._id, end="")
			# print("[", end="")
			op_operation.expressao_direita_expressao.accept(self)
			# print("]", end="")
			op_operation.expressao_direita_rec.accept(self)


	def visita_vetor_ponteiro_explicito(self, op_operation):
		if(op_operation._id in declaracoes):
			print("Error: Variárvel já existente")
		else:	
			op_operation.expressao_esquerda.accept(self)
			# print(" ", end="")
			op_operation.expressao_esquerda_pointer.accept(self)
			# print(op_operation._id, end="")
			# print("[", end="")
			op_operation.expressao_direita_expressao.accept(self)
			# print("]", end="")
			op_operation.expressao_direita_rec.accept(self)
			# print(" = {", end="")
			op_operation.expressao_direita_valor.accept(self)
			# print("}", end="")

	def visita_matriz(self, op_operation):
		# print("[]", end="")
		op_operation.expressao_direita.accept(self)


	def visita_valor_declaracao_vetor(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		# print(",", end='')
		op_operation.expressao_direita.accept(self)

	def visita_valor_declaracao_vetor_rec(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_valor_vetor_rec(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_declaracao_ponteiro(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_centro.accept(self)
		# print(" "+op_operation._id, end="")

	def visita_ponteiro_rec(self, op_operation):
		# print(""+op_operation.asterisco, end="")
		op_operation.expressao_direita.accept(self)

	def visita_asterisco_ponteiro(self, op_operation):
		# print(""+op_operation.asterisco+"", end="")
		pass
	def visita_print(self, op_operation):
		# print("printf("+op_operation.string, end="")
		op_operation.expressao_esquerda.accept(self)
		# print(")", end="")

	def visita_print_option(self, op_operation):
		if(op_operation._id in declaracoes):
			# print(", "+op_operation._id, end="")
			op_operation.expressao_direita.accept(self)
		else: 
			print("Error -> Variáveis não declaradas dentro do printf")

	def visita_print_option_const(self, op_operation):
		# print(", ", end="")
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_print_option_pointer(self, op_operation):
		# print(",", end="")
		op_operation.expressao_esquerda.accept(self)
		# print(op_operation._id, end="")
		op_operation.expressao_direita.accept(self)

	def visita_break(self, op_operation):
		if(dentro_laco['into'] != True):
			# print(op_operation.const)
			print("Error -> Break não pode ser executado fora do laço.")

	def visita_continue(self, op_operation):
		if(dentro_laco['into'] != True):
			print("Error -> Continue não pode ser executado fora do laço.")
			# print(op_operation.const)
		# else:


	def visita_scan(self, op_operation):
		# print("scanf", end="")
		# print(op_operation.const_string, end="")
		op_operation.expressao_direita.accept(self)

	def visita_read_option(self, op_operation):
		# print(", &"+op_operation._id, end="")
		if(op_operation._id in declaracoes):
			op_operation.expressao_direita.accept(self)
		else:
			print("Error -> Variável não declarada no scanf.")

	def visita_if(self, op_operation):
		# print("if(", end="")
		op_operation.expressao_esquerda.accept(self)
		# print(") {", end = "")
		op_operation.expressao_direita.accept(self)
		# print("}", end="")

	def visita_stm(self, op_operation):
		op_operation.expressao_esquerda.accept(self)
		op_operation.expressao_direita.accept(self)

	def visita_block(self, op_operation):
		op_operation.expressao_esquerda.accept(self)


	def visita_for(self, op_operation):
		# print("for(", end="")
		dentro_laco['into'] = True
		op_operation.expressao_esquerda1.accept(self)
		op_operation.expressao_esquerda2.accept(self)
		op_operation.expressao_esquerda3.accept(self)
		# print("){", end="")
		op_operation.expressao_direita.accept(self)
		# print("}", end="")
		dentro_laco['into'] = False

	def visita_assignment_value_const(self, op_operation):
		tipo_const =""
		if(op_operation._id in declaracoes):  

			if(type(op_operation.expressao_esquerda.avalia()) == float):
				tipo_const = "float"
			if(type(op_operation.expressao_esquerda.avalia()) == int):
				tipo_const = "int"
			if(type(op_operation.expressao_esquerda.avalia()) == str):
				tipo_const = "char"
			
			if(declaracoes[op_operation._id] == tipo_const):
			# print(type(op_operation.expressao_esquerda.avalia()))
			# print(op_operation._id+" = ", end="")
				op_operation.expressao_esquerda.accept(self)
			# print(op_operation.expressao.avalia())
			else:
				print("Error-> variável não compatível")

		else:
			print("ERROR -> Variável não declarada.")

	def visita_while(self, op_operation):
		# print(dentro_laco['into'])
		# print("while(", end="")
		dentro_laco['into'] = True
		op_operation.expressao_esquerda.accept(self)
		# print(") {", end="")
		op_operation.expressao_direita.accept(self)
		# print("}", end="")
		dentro_laco['into'] = False

	def visita_do_while(self, op_operation):
		# print("do { ", end="")
		dentro_laco['into'] = True
		op_operation.expressao_esquerda.accept(self)
		# print("}while(", end="")
		op_operation.expressao_direita.accept(self)
		# print(")", end="")
		dentro_laco['into'] = False

	def visita_if_else(self, op_operation):
		# print("if(", end="")
		op_operation.expressao_esquerda.accept(self)
		# print(") {", end = "")
		op_operation.expressao_direita1.accept(self)
		# print("}", end="")
		# print("else{", end="")
		op_operation.expressao_direita2.accept(self)
		# print("}", end="")

	def visita_matriz_rec(self, op_operation):
		if(type(op_operation.expressao.avalia()) != int):
			print("Error -> atributo não inteiro")
			return(True)
		else:
			# print("[", end="")
			op_operation.expressao_esquerda.accept(self)
			# print("]", end="")
			op_operation.expressao_direita.accept(self)

	def visita_assignment_value_vet(self, op_operation):
		if(type(op_operation.expressao1.avalia()) != int):
			print("Error -> Argumento do vetor é diferente de int.")
		else:
			# print(op_operation._id, end="")
			# print("[", end="")
			op_operation.expressao_esquerda1.accept(self)
			# print("]", end="")
			op_operation.expressao_esquerda2.accept(self)
			# print(" = ", end="")
			op_operation.expressao_direita.accept(self)


	def visita_assignment_value_pointer(self, op_operation):
		tipo_const = (vars(op_operation.expressao)['type'])
		tipo_variavel_dec = declaracoes[op_operation._id]
		# print(tipo_variavel_dec)
		if(tipo_const == tipo_variavel_dec):
			op_operation.expressao_esquerda.accept(self)
			# print(op_operation._id, end="")
			# print(" = ", end="")
			op_operation.expressao_direita.accept(self)
		else:
			print("Error -> Ponteiro '"+op_operation._id+"' é do tipo "+tipo_variavel_dec+", Entretanto foi passado um valor do tipo "+tipo_const+".")

	def visita_declaracao_ponteiro_explicito(self, op_operation):
		if(op_operation._id in declaracoes):
			print("\nError -> Variárvel já existente")
		else:
			tipo_const = ((op_operation.expressao.avalia()))
			if(tipo_const in declaracoes):
				# print(declaracoes[tipo_const])
				if(declaracoes[tipo_const] == op_operation.tipo.avalia()):
					op_operation.expressao_esquerda.accept(self)
					op_operation.expressao_direita_rec.accept(self)
					# print(" "+op_operation._id+"=", end="")
					op_operation.expressao_direita_exp.accept(self)
				else:
					print("Error -> Ponteiro '"+op_operation._id+"' é do tipo "+op_operation.tipo.avalia()+", Entretanto foi passada um valor do tipo "+declaracoes[tipo_const]+".")
			else:
				print("Error-> Variável atribuida não declarada");

	def visita_id_cochete(self, op_operation):
		op_operation.expressao_direita.accept(self)

	def visita_expression_cochete(self, op_operation):
		op_operation.expressao_centro.accept(self)
