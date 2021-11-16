from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"

documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)
