# Compass UOL

## Sobre o Author
Bráian Pereira 29 anos.
Gosta de ler livros, principalmente de literatura fantastica e ouvir musica: Musica clásica e quse todos os subgeneros do Rock.
Cursando o Tecnologia em Análise em Desenvolvimento de Sistemas no IFRS Campus Restinga.
Atualmente trabalhando como desenvolvedor na empresa Talto onde exerce a função de criar e dar manunteção em sistemas erp e crm, principalmente em PHP, HTML e JS.

## D&A - AWS

Repositório criado para exercítar e manter as anotações da trilha de aprendizado **D&A - AWS**.

### Sprint 1

Projetos de dados pressupõem o uso de metodologias e ferramentas que são básicas ao dia-a-dia de trabalho. Aqui você terá contato com conceitos de gestão Ágil e framework SCRUM, bem como ferramentas de versionamento de código, a saber Git e seus principais serviços.

#### 1. Curso SCRUM

#### 2. Curso GNU/List

#### 3. Curso Git/GitHub
- Criação de repositórios locais e remotos
    ```git
    git init
    ```
- Clone de repositórios
    ```git
    git clone <link_do_repositório> <nome_para_a_pasta_local>
    ```
- Trocar apontamento no repositório local do repositório remoto
    ```git
    git remote rm origin
    git remote add <link_do_repositorio>
    ```
- Adicionar alterações
    ```git
    git add . 
    git add <nome_do_arquivo>
    ```
- Realizar o commit das alterações adiciondas
    ```git
    git commit -m "Mensagem sobre as alterações feitas"
    ```
- Fazer push dos commits para repositório remoto
    ```git
    git push
    ```
- Trazendo as alterações repositório remoto
    ```git
    git pull
    ```
- Manutenção de branchs (criação, checkout, merge)

   *Listar as branchs*
    ```git
    git branch
    ```
    *Criar branch*
    ```git
    git branch <nome_da_branch>
    ```
    *Entrar na branch*
    ```git
    git checkout <nome_da_branch>
    ```
    *Cirar e entrar na branch*
    ```git
    git branch -b <nome_da_branch>
    ```
    *Mesclar branchs*
    ```git
    git merge <nome_da_outra_branch>
    ```
    *Deletar branch*
    ```git
    git branch -d <nome_da_branch>
    ```
- Tags (versões)

- Realizar o stash e reword dos commits
- Boas práticas de mensagens no commit
- Explicação em cada parte do GitHub
- Gist
- Markdown
- GirHub Pages

#### 4. curso Segurança
_Ainda não realizado_

### Sprint 2

#### Curso 1 - SQL
 - Instalação de vm com windows
 - Instalação do MySQL (Server, Workbench, Shell, Documentação e Exemplos)
 - Introdução ao banco de dados
 - Aprendendo as operações: 
    1. CREATE DATABASE;
    2. USE \<DATABASE\>;
    3. CREATE TABLE \<TABLE\>;
    4. SELECT \<OPERACAO>;
    5. INSERT VALUES (<\REGISTROS>);
    6. TABELA VERDADE;
    7. Clausula WHERE;
    8. Agrupamento
 - Exercícios de fixação
 - Modelagem de dados
    1. Regra Formal
        I. Todo campo vetorizado se tornará outra tabela
        II. Todo campo multivalorizado se tornará outra tabela.
        III. Toda tabela necessita de pelo menos um campo que identifique o registro como sendo unico (PK) 
- Cardinalidade e obrigatoriedade

### Sprint 3

A linguagem Python é, sem dúvidas, uma das mais populares em projetos de dados. Nesta Sprint você irá conhecer as principais características da linguagem, sua sintaxe e características que a tornam tão aderente ao processamento de dados.

#### Curso 1 - Sessões 16 - 19
    - Introdução a OO
    - Classes e seus elementos
    - Objetos, abstração e Encapsulamento
    - Heranças, Heranças multiplas e o método super()
    - MRO, Polimorfismo e métodos mágicos
    - Manipulando arquivos CSV
    - Manipulando JSON
    - Manipulação de data e hora, deltas
    - Métodos de datas e hotas.

### Sprint 4
Sabemos que a Linguagem Python suporta expressar algoritmos em diferentes paradigmas, sendo um deles o Paradigma Funcional. Nesta Sprint você irá aprender alguns importantes conceitos de programação funcional, além de adentrar ao mundo dos containers com Docker e Kubertentes. Também daremos início à exploração do fascinante mundo da Aprendizagem de Máquina (Machine Learning).

#### Curso 1 - Programação funcional

#### Curso 2 - Programação funcional com Python 

#### Docker para desenvolvedores

#### Estatística Descritiva com Python


