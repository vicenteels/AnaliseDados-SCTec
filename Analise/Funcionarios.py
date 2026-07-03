import pandas as pd

funcionarios = {
    'Nome': ['Vicente', 'Isabela', 'Jorge', 'Ana'],
    'Endereco': ['Santa Catarina', 'Rio Grande do Sul', 'Rio de Janeiro', 'Mato Grosso'],
    'data_nascimento': ['11-11-2000', '09-09-2000', '21-12-1990', '03-03-2003'],
    'data_admissao': ['01-02-2020', '02-03-2020', '15-07-2023', '12-10-2025'],
    'salario': [5000, 4500, 3000, 2700],
    'cargo': ['Analista de Dados Pleno', 'DevOps Pleno', 'Engenheiro de Software Junior', 'Analista de Suporte Pleno']
}

df = pd.DataFrame(funcionarios)

print(df['data_admissao'])