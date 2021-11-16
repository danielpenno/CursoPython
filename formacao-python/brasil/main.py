from cpf_cnpj import Documento
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "15316264754"

documento = Documento.cria_documento(exemplo_cpf)
print(documento)
