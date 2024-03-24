# Visão geral sobre API's Rest

API’s REST (Representational State Transfer) são interfaces de programação que permitem a comunicação entre diferentes sistemas de forma padronizada e eficiente. Suas vantagens envolvem simplicidade, flexibilidade e escalabilidade, tornando-as ideais para diversos cenários, desde integrações entre aplicações web até o desenvolvimento de serviços em nuvem.

## Fundamentos:

### API (Application Programming Interface): 
Interface que permite que duas ou mais aplicações se comuniquem e troquem dados.
### REST (Representational State Transfer): 
Arquitetura para API’s que define um conjunto de princípios para a transferência de estado entre sistemas.
### Recursos: 
Entidades nomeadas que representam dados ou funcionalidades em um sistema.
### Métodos HTTP: 
Verbos utilizados para realizar ações em recursos, como GET (obter), POST (criar), PUT (atualizar) e DELETE (excluir).
### Payload: 
Dados que são enviados ou recebidos em uma requisição API.
### Formato de dados: 
Estrutura utilizada para representar os dados na payload, como JSON ou XML.
### JSON (JavaScript Object Notation): 
É um formato de dados leve e fácil de ler e escrever para humanos, e fácil de analisar e gerar para máquinas. É bastante usadoem API’s

## Características REST

### Arquitetura cliente-servidor: 
As API’s REST seguem o modelo cliente-servidor, no qual o cliente faz solicitações e o servidor fornece respostas.
### Padronização: 
O uso de verbos HTTP e URI’s padronizados facilita a compreensão e o uso da API por diferentes desenvolvedores.
### Leveza: 
As API’s REST são geralmente mais leves e eficientes do que outras API’s pois não exigem o uso de protocolos complexos.
### Flexibilidade: 
As API’s REST podem ser utilizadas para integrar diferentes tipos de sistemas, independentemente da linguagem de programação ou plataforma utilizada.
### Escalabilidade: 
As API’s REST podem ser facilmente escaladas para atender a um grande número de requisições.
### Cacheable: 
As API’s REST podem ser configuradas para permitir o cache de dados, o que pode melhorar o desempenho da aplicação, pois reduz a necessidade de solicitações repetidas ao servidor.

## Exemplo prático:

Um exemplo prático de uso de uma API REST seria acessar informações sobre filmes em uma plataforma de streaming. Um cliente pode fazer uma solicitação GET para `http://api.streaming.com/movies` para obter uma lista de filmes. Cada filme pode ser acessado individualmente por meio de uma URL específica, como `http://api.streaming.com/movies/123`, onde `123` é o ID do filme. A resposta pode incluir detalhes do filme em formato JSON, como título, descrição, e uma lista de links para acessar informações relacionadas, como atores, diretores, e avaliações.

## Conclusão:

As APIs REST são uma ferramenta poderosa e versátil para a comunicação entre sistemas. Sua simplicidade, flexibilidade e escalabilidade as tornam ideais para diversos cenários, desde pequenos projetos até grandes empresas.
