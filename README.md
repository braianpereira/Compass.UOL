# Compass UOL
## D&A - AWS

Repositório criado para exercítar e manter as anotações da trilha de aprendizado **D&A - AWS**.

### Sprint 1

Projetos de dados pressupõem o uso de metodologias e ferramentas que são básicas ao dia-a-dia de trabalho. Aqui você terá contato com conceitos de gestão Ágil e framework SCRUM, bem como ferramentas de versionamento de código, a saber Git e seus principais serviços.

#### 1. Curso SGRUM
 _Ainda não realizado_

#### 2. Curso GNU/List
_Ainda não realizado_

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