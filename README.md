# Automação de Emissão de Notas Fiscais com Python e Selenium

Projeto demonstrativo de automação com **Python + Selenium** para preencher um formulário web local de emissão simulada de nota fiscal, a partir de uma planilha Excel, gerando um arquivo XML pelo próprio formulário HTML.

> Este projeto é educacional. Ele não emite NF-e real, não transmite dados para a SEFAZ, não assina XML digitalmente e não realiza validação fiscal oficial.

## Tecnologias

- Python
- Selenium
- Pandas
- OpenPyXL
- WebDriver Manager

## Objetivo

Demonstrar um fluxo de automação organizado em módulos:

- Leitura e validação básica da planilha
- Abertura e configuração do navegador
- Login em sistema demonstrativo local
- Preenchimento automático de formulário web
- Geração de arquivo XML pelo formulário HTML
- Separação de responsabilidades em módulos Python


## Estrutura do projeto

```text
emissao-nf-selenium/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── data/
│   ├── input/
│   │   └── NotasEmitir.xlsx
│   └── output/
│
├── web/
│   ├── login.html
│   └── index.html
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── navegador.py
│   ├── login.py
│   ├── planilha.py
│   └── emissor.py
```

## Responsabilidade dos módulos

| Módulo | Responsabilidade |
|---|---|
| `config.py` | Centraliza caminhos, parâmetros, variáveis de ambiente e configurações gerais. |
| `navegador.py` | Cria e configura o Chrome WebDriver, incluindo pasta de download. |
| `login.py` | Executa o login no sistema demonstrativo. |
| `planilha.py` | Lê a planilha de entrada e valida a existência das colunas obrigatórias.|
| `emissor.py` | Preenche o formulário web com os dados da planilha e aciona a geração do XML. |
| `main.py` | Orquestra o processo completo. |


