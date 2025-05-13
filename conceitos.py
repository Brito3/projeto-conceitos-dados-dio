# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "DBFS":
        return "Sistema de Arquivos do Databricks"
    elif conceito == "Lakehouse":
        return "Integra Data Lake e Data Warehouse"
    elif conceito == "Delta Lake":
        return "Camada de armazenamento de dados open-source"
    elif conceito == "Workspace":
        return "Ambiente colaborativo para dados e código"

# Função responsável por receber um recurso e retornar sua respectiva descrição.
def descrever_recurso(recurso):
    if recurso == "IA":
        return "Criação e implantação de IA generativa em escala"
    elif recurso == "Armazenamento":
        return "Armazenamento otimizado com arquitetura lakehouse"
    elif recurso == "ETL":
        return "Processamento de dados em lote e em tempo real"
    elif recurso == "Governança":
        return "Controle e segurança unificada de dados e IA"
    elif recurso == "Compartilhamento":
        return "Compartilhamento rápido de dados, modelos e notebooks"

# Tenta buscar a descrição do conceito ou recurso
descricao = descrever_conceito(entrada)
if descricao is None:
    descricao = descrever_recurso(entrada)

# Imprime a descrição, se encontrada
if descricao:
    print(descricao)
else:
    print("Conceito ou recurso não reconhecido.")
