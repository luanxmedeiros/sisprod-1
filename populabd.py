from appprod.models import *

#Inserindo dados no banco

# Criando cargos

cargo1=Cargo(cargo="Agrigultor",salario=1000)
cargo2=Cargo(cargo="Pescador",salario=900)
cargo3=Cargo(cargo="Cozinheiro",salario=1500)
cargo4=Cargo(cargo="Nutricionista",salario=2500)
cargo5=Cargo(cargo="Lavrador",salario=1200)
cargo6=Cargo(cargo="Agrônomo",salario=2200)

cargo1.save()
cargo2.save()
cargo3.save()
cargo4.save()
cargo5.save()
cargo6.save()

# Criando os Prestadores de Serviços
prestador1=Prestador(nome="Carlos",cpf="00212223245",data_nascimento="2000-05-05",email="carluxhenrique@gmail.com",telefone="3208-3725",cargo=cargo1)
prestador2=Prestador(nome="Luan",cpf="07894561235",data_nascimento="2001-01-15",email="luandalua@gmail.com",telefone="3206-0011",cargo=cargo2)
prestador3=Prestador(nome="Juliana",cpf="00456481512",data_nascimento="1999-02-20",email="jurubeba@gmail.com",telefone="3642-1540",cargo=cargo4)
prestador4=Prestador(nome="Matheus",cpf="05197568521",data_nascimento="2002-09-19",email="matheuzin@gmail.com",telefone="3605-0130",cargo=cargo3)
prestador5=Prestador(nome="Galego",cpf="00369258471",data_nascimento="1980-11-24",email="galego@gmail.com",telefone="3211-1200",cargo=cargo5)
prestador6=Prestador(nome="Matador",cpf="04789652321",data_nascimento="2001-10-02",email="matador@gmail.com",telefone="3222-7778",cargo=cargo6)

prestador1.save()
prestador2.save()
prestador3.save()
prestador4.save()
prestador5.save()
prestador6.save()

# Criação de Processo de produção
processo1=ProcessoProducao(data_inicio="2014-02-03",data_termino="2014-05-20",descricao="Processo de Plantação")
processo2=ProcessoProducao(data_inicio="2014-02-03",data_termino="2014-06-10",descricao="Processos Alimentícios")

processo1.save()
processo2.save()

processo1.prestador.add(prestador1,prestador2,prestador3,prestador4,prestador5)
processo2.prestador.add(prestador1,prestador2,prestador3,prestador4,prestador5,prestador6)

#Criação de unidade de medida
unidade1=UnidadeMedida(descricao="Kilograma",sigla="KG")
unidade2=UnidadeMedida(descricao="Litro",sigla="L")
unidade3=UnidadeMedida(descricao="Toneladas",sigla="T")

unidade1.save()
unidade2.save()
unidade3.save()

# Criação de materia prima
materia_prima1=MateriaPrima(descricao="Soja", quantidade_estoque=20, unidade_medida=unidade3, custo=500)
materia_prima2=MateriaPrima(descricao="Café", quantidade_estoque=20, unidade_medida=unidade3, custo=700)
materia_prima3=MateriaPrima(descricao="Milho", quantidade_estoque=20, unidade_medida=unidade3, custo=400)
materia_prima4=MateriaPrima(descricao="Carne Bovina", quantidade_estoque=20, unidade_medida=unidade1, custo=20)
materia_prima5=MateriaPrima(descricao="Leite de Vaca", quantidade_estoque=20, unidade_medida=unidade2, custo=10)

materia_prima1.save()
materia_prima2.save()
materia_prima3.save()
materia_prima4.save()
materia_prima5.save()

# Criando as etapas
etapa1=EtapaProducao(descricao="cultivo de soja", processo_producao=processo1)
etapa2=EtapaProducao(descricao="cultivo de café", processo_producao=processo1)
etapa3=EtapaProducao(descricao="criação de bovinos", processo_producao=processo2)
etapa4=EtapaProducao(descricao="Produção de laticínios", processo_producao=processo2)

etapa1.save()
etapa2.save()
etapa3.save()
etapa4.save()

# Vincular matérias primas as etapas de produção
matEtapa1 = MateriaEtapa(quantidade_materia_etapa=18, materia_prima=materia_prima1, etapa_producao=etapa1)
matEtapa2 = MateriaEtapa(quantidade_materia_etapa=15, materia_prima=materia_prima2, etapa_producao=etapa2)
matEtapa3 = MateriaEtapa(quantidade_materia_etapa=19, materia_prima=materia_prima3, etapa_producao=etapa3)
matEtapa4 = MateriaEtapa(quantidade_materia_etapa=17, materia_prima=materia_prima4, etapa_producao=etapa4)

matEtapa1.save()
matEtapa2.save()
matEtapa3.save()
matEtapa4.save()

