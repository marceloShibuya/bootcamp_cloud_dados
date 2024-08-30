## 1. Projeto utilizando a Cloud da AWS e seus serviços

1. **S3 (Simple Storage Service):** Armazenamento escalável de objetos, ideal para dados brutos, backups e arquivos de grande volume.
2. **EC2 (Elastic Compute Cloud):** Serviço que permite criar e gerenciar instâncias de máquinas virtuais na nuvem, altamente configuráveis.
3. **RDS (Relational Database Service):** Serviço gerenciado de banco de dados relacional, que suporta mecanismos como MySQL, PostgreSQL, e SQL Server.

## 2. Bucket Policy: Exemplo de Permissão de Leitura para Usuário Anônimo

- **Bucket Policy:**
   - Adicione uma política ao bucket para permitir que usuários anônimos leiam os arquivos. Um exemplo de política de leitura pública para um bucket S3 pode ser adicionado através do editor de políticas no console da AWS.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::nome-do-bucket/*"
        }
    ]
}
```
