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
