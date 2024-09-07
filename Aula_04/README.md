# **Bootcamp Cloud: Aula 04: IAM na AWS**

**Objetivo**: Nesta aula, vamos explorar o IAM (Identity and Access Management) da AWS. Vamos entender como proteger a conta AWS, o papel do usuário root, como criar e gerenciar usuários, grupos, políticas, e configurar o MFA.

### **1. Protegendo a Conta AWS**

- **Importância**: A conta AWS é o coração da sua infraestrutura na nuvem. Protegê-la é essencial para evitar acessos não autorizados e garantir a segurança dos seus recursos.

### **2. Usuário Root**

- **O que é o Usuário Root**: 
  - O usuário root é a conta inicial criada ao configurar a AWS. Ele tem acesso total a todos os recursos e configurações.
  - **Riscos**: O uso contínuo do usuário root é arriscado, pois ele tem permissões ilimitadas, o que pode levar a potenciais danos em caso de comprometimento.

- **Boas Práticas**:
  - Evitar o uso diário do usuário root.
  - Criar usuários IAM com permissões específicas para tarefas do dia a dia.
  - Habilitar o MFA (Multi-Factor Authentication) para a conta root.

### **3. IAM (Identity and Access Management)**

- **O que é IAM**:
  - IAM permite criar e gerenciar usuários, grupos, e permissões na AWS.
  - Facilita a implementação do princípio do menor privilégio, garantindo que cada usuário tenha apenas as permissões necessárias.

### **4. Configuração do MFA (Multi-Factor Authentication)**

- **O que é MFA**: 
  - MFA adiciona uma camada extra de segurança, exigindo que o usuário forneça uma segunda forma de autenticação além da senha, como um código gerado por um dispositivo móvel.

- **Passo a Passo para Configurar o MFA no Usuário Root**:
  
  1. **Acessar o Console de Gerenciamento da AWS**:
     - Faça login como o usuário root.
  
  2. **Navegar até a Página de Segurança da Conta**:
     - No canto superior direito, clique no nome da conta e selecione "Minha Conta".
     - Role para baixo até "Configurações de segurança" e clique em "Ativar MFA" na seção de autenticação multifator.

  3. **Escolher o Tipo de Dispositivo MFA**:
     - Selecione "Aplicativo autenticador" para usar um dispositivo móvel como segundo fator de autenticação.

  4. **Configurar o Aplicativo Autenticador**:
     - Abra o aplicativo autenticador no seu dispositivo móvel (ex: Google Authenticator).
     - Escaneie o código QR fornecido pela AWS ou insira a chave manualmente.
  
  5. **Verificar o Código MFA**:
     - Insira os códigos gerados pelo aplicativo para verificar a configuração.
  
  6. **Salvar a Configuração**:
     - Confirme e salve a configuração do MFA.

  7. **Testar a Configuração**:
     - Saia e faça login novamente para verificar se o MFA está funcionando corretamente.

---

### **5. Criando um Usuário Administrativo**

**Passo a Passo para Criar um Usuário Administrativo:**

1. **Acessar o Console IAM**:
   - **Faça login** no console da AWS com o usuário root.
   - Navegue até o serviço **IAM (Identity and Access Management)**.
   
2. **Adicionar Novo Usuário**:
   - Clique em **"Usuários"** e selecione **"Adicionar usuário"**.
   - Insira um nome para o novo usuário administrativo, como "admin-user".

3. **Selecionar o Tipo de Acesso**:
   - **Acesso programático**: Marque essa opção para gerar **chaves de acesso** (Access Key ID e Secret Access Key), necessárias para scripts ou automações que interagem com a AWS via API.
   - **Acesso à AWS Management Console**: Marque essa opção para permitir que o usuário faça login no console da AWS. Defina uma senha inicial (você pode permitir que o usuário a redefina no primeiro login ou definir uma senha permanente).

4. **Configurar Permissões**:
   - **Anexar Políticas Diretamente**: 
     - **AdministratorAccess**: Selecione esta política para conceder ao usuário todas as permissões administrativas, permitindo acesso completo a todos os recursos da AWS.
     - **PowerUserAccess** (Alternativa): Selecione esta política se desejar conceder permissões administrativas amplas, mas sem acesso ao gerenciamento de contas, como a criação de novos usuários IAM ou configuração de billing.

5. **Revisar e Criar o Usuário**:
   - Revise as configurações e clique em **"Criar usuário"**.
   - **Download do CSV**: Faça o download do arquivo CSV contendo as chaves de acesso e a senha do console para uso futuro. Estas informações são essenciais para acessar a AWS programaticamente e via console.

6. **Encerramento do Uso do Usuário Root**:
   - Após a criação do usuário administrativo, saia do console e faça login novamente utilizando as credenciais do novo usuário.
   - A partir deste ponto, o uso do usuário root deve ser restrito a tarefas críticas e configurações de segurança inicial.

---

### **6. Comparação: Root vs AdministratorAccess vs PowerUserAccess**

| **Característica**                  | **Usuário Root**                                      | **AdministratorAccess**                          | **PowerUserAccess**                            |
|-------------------------------------|------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| **Acesso Total**                    | Sim, acesso total e irrestrito a todos os recursos   | Sim, acesso completo a quase todos os recursos  | Não, acesso restrito a certos recursos        |
| **Gerenciamento de IAM**            | Sim                                                  | Sim                                              | Não, sem acesso ao IAM                        |
| **Configuração de Billing**         | Sim                                                  | Sim                                              | Não                                            |
| **Criação de Recursos**             | Sim                                                  | Sim                                              | Sim                                            |
| **Modificação de Políticas de Conta**| Sim                                                  | Sim                                              | Não                                            |
| **Gerenciamento de Faturamento e Conta** | Sim, incluindo alteração de informações de pagamento e fechamento da conta | Não                                              | Não                                            |
| **Cancelamento de Serviços e Fechamento da Conta** | Sim | Não | Não |
| **Alteração de Suporte AWS**        | Sim, pode alterar o plano de suporte (ex: suporte básico para empresarial) | Não | Não |
| **Exclusão de CloudFront Key Pairs**| Sim, pode criar, gerenciar ou excluir CloudFront key pairs | Não | Não |
| **Uso recomendado**                 | Configuração inicial e tarefas críticas de segurança | Uso diário para administração e operações gerais | Uso para administração sem acesso a IAM e Billing |

---

### **7. Questões Frequentes**

1. **O AdministratorAccess pode alterar o Usuário Root?**

   Não, um usuário com a política AdministratorAccess não pode alterar o usuário root. Somente o próprio usuário root pode alterar suas próprias configurações, como o nome de usuário, senha, chaves de acesso, ou desativar o MFA. Isso é uma medida de segurança importante para proteger a conta AWS, garantindo que apenas o usuário root tenha controle total sobre suas próprias credenciais e configurações.

2. **Eu contratei uma consultoria, qual acesso criar?**

   A escolha entre conceder `AdministratorAccess` ou `PowerUserAccess` à consultoria depende da natureza das tarefas que eles irão realizar e do nível de controle que você deseja manter sobre sua conta AWS.

   - **Quando conceder `AdministratorAccess`**:
     - **Cenário**: A consultoria precisa ter acesso completo para gerenciar todos os recursos da AWS, incluindo a criação e gerenciamento de usuários IAM, configuração de políticas, gerenciamento de billing, e outras tarefas administrativas completas.
     - **Risco**: Eles terão permissão para alterar quase todos os aspectos da sua conta, incluindo ações sensíveis que podem impactar a segurança ou o faturamento.

   - **Quando conceder `PowerUserAccess`**:
     - **Cenário**: A consultoria precisa realizar tarefas administrativas gerais, como criar e gerenciar recursos, mas você deseja limitar o acesso a configurações de conta e gerenciamento de usuários IAM.
     - **Risco**: Eles não poderão criar ou gerenciar usuários IAM, alterar configurações de faturamento, ou fazer mudanças no plano de suporte, o que oferece um nível adicional de segurança e controle sobre aspectos críticos da sua conta.

   - **Recomendação**:
     - **PowerUserAccess** pode ser mais apropriado se você quiser manter controle sobre as configurações mais sensíveis da sua conta, como gerenciamento de usuários IAM e informações de faturamento. 
     - **AdministratorAccess** deve ser concedido somente se a consultoria realmente precisar de controle total sobre todos os aspectos da sua infraestrutura AWS, e você confia plenamente que eles irão gerenciar esses recursos de forma segura e responsável. 

---

### **8. Criando um Grupo de "Engenheiro de Dados" no IAM**

**Passo a Passo para Criar um Grupo de "Engenheiro de Dados" no IAM**

1. **Acessar o Console IAM:**
   - Faça login no console da AWS com um usuário que tenha permissões suficientes para gerenciar o IAM.
   - Navegue até o serviço **IAM (Identity and Access Management)**.

2. **Criar um Novo Grupo:**
   - No painel do IAM, selecione **"Gr

upos"** no menu lateral.
   - Clique em **"Criar Novo Grupo"**.
   - Insira o nome do grupo como **"EngenheiroDeDados"**.

3. **Copiar Permissões de um Grupo Existente (Opcional):**
   - Se você já possui um grupo com permissões similares e deseja copiar suas permissões, selecione essa opção e escolha o grupo de referência.
   - Caso contrário, pule esta etapa e prossiga para anexar políticas diretamente.

4. **Anexar Políticas Diretamente:**
   - Na tela de anexar políticas, você verá uma lista de políticas gerenciadas pela AWS.
   - Para o grupo de "Engenheiro de Dados", selecione as seguintes políticas relevantes:

     - **AmazonS3FullAccess**: Dá ao grupo acesso completo ao Amazon S3, permitindo criar, ler, escrever e excluir buckets e objetos.
     - **AmazonEC2FullAccess**: Permite ao grupo gerenciar instâncias EC2, incluindo o provisionamento, configuração e encerramento de instâncias.
     - **AmazonVPCFullAccess**: Concede ao grupo a capacidade de gerenciar redes VPC, sub-redes, roteamento e segurança de redes.
     - **AmazonRDSFullAccess**: Concede permissão para gerenciar instâncias de bancos de dados no Amazon RDS.
     - **AmazonGlueConsoleFullAccess**: Permite ao grupo acessar e usar o serviço de ETL Amazon Glue para operações de dados.
     - **AmazonAthenaFullAccess**: Dá ao grupo a permissão para consultar dados armazenados no S3 usando o Amazon Athena.

   - Após selecionar as políticas desejadas, clique em **"Next Step"**.

5. **Revisar o Grupo:**
   - Revise as permissões que serão concedidas ao grupo.
   - Verifique se todas as políticas necessárias estão anexadas.

6. **Criar o Grupo:**
   - Clique em **"Create Group"** para finalizar a criação do grupo "EngenheiroDeDados".

7. **Adicionar Usuários ao Grupo:**
   - Após a criação do grupo, você pode adicionar usuários existentes ao grupo "EngenheiroDeDados" ou criar novos usuários e associá-los ao grupo.
   - Isso garantirá que todos os membros do grupo tenham as mesmas permissões para acessar e gerenciar os recursos associados ao projeto de dados.

---

### **9. Tags Sugeridas para o Grupo "Engenheiro de Dados"**

As tags ajudam a organizar e identificar recursos relacionados ao grupo, facilitando a gestão e a automação:

- **Project:** Nome do projeto específico (ex: "DataPipeline2024", "CustomerAnalytics").
- **Department:** Nome do departamento ou equipe (ex: "DataEngineering", "AnalyticsTeam").
- **Role:** Descrição da função (ex: "DataEngineer", "DataOps").
- **Environment:** Ambiente onde o grupo atuará (ex: "Production", "Staging", "Development").
- **Owner:** Nome do proprietário ou responsável pelo grupo (ex: "Luciano", "DataTeamLead").
- **CostCenter:** Código ou nome do centro de custos (ex: "CC1001", "MarketingData").
- **Compliance:** Requisitos de conformidade específicos (ex: "GDPR", "HIPAA").
- **BusinessUnit:** Unidade de negócio relevante (ex: "Sales", "ProductDevelopment").
- **Purpose:** Finalidade do grupo (ex: "DataProcessing", "ETLTasks").
- **SecurityLevel:** Nível de segurança exigido (ex: "High", "Confidential").
