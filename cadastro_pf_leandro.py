import sqlite3, time

connect=sqlite3.connect('pessoafisica.db')
c=connect.cursor()

#def criar_db():
#    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, cpf varchar, endereco text, email text, empresa text, cargo text)')
#try:
#    criar_db()
#except:
#    print('Erro ao criar banco de dados.')
#else:
#    print('Banco de dados criado com sucesso.')

def inserirDados(n, cpf, end, e, emp, carg):
    c.execute('INSERT INTO cadastro VALUES(?, ?, ?, ?, ?, ?)', (n, cpf, end, e, emp, carg))
    connect.commit()

def pesquisaDados(pesquisarDados_db):
    sql_pesquisa='SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql_pesquisa, (pesquisarDados_db,)):
        print(row)
    connect.commit()

def relatarCadastros(relatarCadastros_db):
    sql_relatar='SELECT * FROM cadastro;'
    for row in c.execute(sql_relatar, (relatarCadastros_db)):
        print(row)
    connect.commit()

def deletarCadastro(deletarCadastro_db):
    sql_deletar='DELETE FROM cadastro WHERE nome = ?'
    for row in deletarCadastro(sql_deletar, (deletarCadastro_db,)):
        print(row)
    connect.commit()

funcao= int(input('1 - Cadastrar Pessoa Física\n2 - Consultar Cadastro PF\n3 - Relatório de Cadastros\n4 - Deletar Cadastro\nSelecione a opção desejada:'))
           
if funcao == 1:
    try:
        print('Cadastrar Pessoa Física - JCAVI Treinamentos')
        time.sleep(1)
        n=str(input('Digite o nome: '))
        cpf=str(input('Digite o CPF: '))
        end=str(input('Digite o endereço: '))
        e=str(input('Digite o email: '))
        emp=str(input('Digite o nome da empresa: '))
        carg=str(input('Digite o seu cargo: '))
        inserirDados(n, cpf, end, e, emp, carg)
    except:
        print('Erro ao realizar cadastro do cliente')
    else:
        print('{}, foi cadastrado com sucesso.'.format(n))
              
if funcao == 2:
    try:
        print('Consultar dados no Database...')
        pesquisardb=str(input('Digite o nome a ser localizado: '))
        pesquisaDados(pesquisardb)
        print('Pesquisa concluída.')
    except:
        print('Ocorreu um erro durante a pesquisa.')

if funcao == 3:
    try:
        print('Relatório de usuários:')
        print(relatarCadastros)
    except:
        print('Ocorreu um erro, não foi possível localizar os cadastros.')

if funcao == 4:
    try:
        deletarCadastro_db=str(input('Digite o nome a ser removido: '))
        deletarCadastro(deletarCadastro_db)
        print('{}, foi removido com sucesso.'.format(deletarCadastro_db))
    except:
        print('{} não foi localizado no cadastro.'.format(deletarCadastro_db))
