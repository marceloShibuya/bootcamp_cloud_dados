# Bootcamp Cloud: Aula 08 - Integração entre EC2 e RDS para Processamento de Requisições de API e Armazenamento de Dados

**Objetivo**: Nesta aula, vamos aprender a configurar uma instância EC2 para rodar uma aplicação de API utilizando Docker e integrar essa aplicação com um banco de dados Amazon RDS. Vamos explorar as vantagens dessa arquitetura, as melhores práticas de segurança, e como configurar os recursos necessários na AWS.

### **1. Introdução à Integração EC2 e RDS**

A combinação de instâncias EC2 com o Amazon RDS é amplamente utilizada para construir aplicações robustas que precisam processar requisições de APIs e armazenar dados em um banco de dados relacional gerenciado. EC2 oferece flexibilidade e controle sobre a execução do código da aplicação, enquanto o RDS cuida da gestão do banco de dados, garantindo alta disponibilidade, backups automatizados e segurança.

### **2. Benefícios da Integração entre EC2 e RDS**

- **Escalabilidade e Flexibilidade**: A instância EC2 permite escalabilidade horizontal da aplicação, enquanto o RDS escala automaticamente o banco de dados de acordo com a demanda.
- **Gerenciamento Simplificado**: O RDS cuida de atualizações, backups, e manutenção do banco de dados, liberando tempo para focar no desenvolvimento da aplicação.
- **Segurança Avançada**: Com o uso de Security Groups, podemos restringir o acesso ao banco de dados, garantindo que apenas a instância EC2 tenha permissão para se conectar.
- **Alto Desempenho**: O uso combinado de EC2 e RDS permite que aplicações sejam otimizadas para lidar com grandes volumes de requisições e operações de banco de dados.
