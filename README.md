# 👁️ Dark LK 

<p align="center">
<img width="300" height="250" alt="image" src="https://github.com/user-attachments/assets/0d563adc-1e55-44c7-84ca-d7c5500fcb92" />
</p>

---

### ⚠️ AVISO LEGAL

O criador deste projeto não tem nenhuma responsabilidade se este for usado para o
mal ou para crimes cibernéticos. Este projeto foi desenvolvido estritamente para fins 
educativos e de aprendizado em automação e segurança.

# 📝 Descrição

Este projeto é um coletor de dados de sistema. Ele executa um script em 
PowerShell para extrair informações técnicas da máquina e utiliza um script em Python para enviar esses dados automaticamente para o seu Webhook do Discord.

## 📊 O que ele coleta?

```

Nome do  proprietário registrado.

Versão e Produto do Windows.

Nome do Computador (Hostname).

Adaptadores de rede presentes.

Nome do usuário ativo no sistema.

Número de série do sistema operacional.

Endereços IPv4 (IP Local).
```

---

## 👁️ Como usar

Configuração do Webhook:
Abra o arquivo main.py e insira a URL do seu Webhook do Discord na variável DISCORD_WEBHOOK_URL.

```
Arquivos:
Mantenha os arquivos malwere.py e pcinfo.ps1 na mesma pasta.

Execução:
No terminal, instale a biblioteca necessária e execute o script:

pip install requests
python malwere.py.py

```

### ⚙️ Funcionamento

O código funciona em três etapas:

Executa o arquivo .ps1 ignorando restrições de execução do Windows.

Gera um relatório temporário em .txt.

Envia o relatório como anexo ao Discord e apaga o arquivo local em seguida para não deixar rastros.
