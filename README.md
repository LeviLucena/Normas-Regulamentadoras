# Sistema de Integração Inteligente de Normas com IA

## Descrição
Este projeto visa criar uma aplicação web que integra normas regulamentadoras e padrões internacionais com inteligência artificial para automatizar a análise de conformidade. O sistema permite a seleção de uma norma específica, descreve o contexto organizacional e utiliza a API da OpenAI para gerar uma análise de conformidade, identificando lacunas e sugerindo melhorias.

![image](https://github.com/user-attachments/assets/23197952-6893-41e7-bfee-f6280743f124)

## Tecnologias Utilizadas
Flask: Framework web para Python.
OpenAI API: Usada para análise inteligente e sugestões baseadas em IA.
HTML/CSS: Para a estruturação e estilização da interface de usuário.
Bootstrap: Framework CSS para criar um design responsivo e moderno.
JavaScript: Para interação com o usuário e integração com a API.

## Funcionalidades
Seleção de Norma: O usuário pode escolher uma norma da lista de normas, como ISO 9001, ISO 14001, ISO 45001, entre outras.
Descrição do Contexto Organizacional: O usuário pode fornecer informações sobre a organização, como setor, tamanho e desafios enfrentados.
Análise de Conformidade com IA: A partir das informações fornecidas, o sistema usa a API da OpenAI para gerar uma análise detalhada sobre o estado de conformidade da organização com os requisitos da norma selecionada. O sistema identifica lacunas de conformidade e sugere melhorias.
Interface Intuitiva: A interface é projetada para ser simples e interativa, com feedbacks claros para o usuário e possibilidade de visualizar as sugestões de forma organizada.

### Como Usar
Instalação Local com uso do VSCODE

1. Clone do Repositório
```
git clone <URL_DO_REPOSITORIO>
cd <diretorio_do_repositorio>
```

2. Crie um ambiente virtual (opcional)
```
python3 -m venv venv
source venv/bin/activate  # Para sistemas UNIX
venv\Scripts\activate  # Para Windows
```

3. Instale as dependências
```
pip install -r requirements.txt
```

4. Configure sua chave da API da OpenAI em app.py:
> Substitua a variável openai.api_key com sua chave da API.

5. Inicie o servidor Flask:
```
python app.py
```

6. Acesse a aplicação no navegador
```
http://127.0.0.1:5000
```
## Estrutura do Projeto
```
/project-root
│
├── app.py                 # Código principal da aplicação Flask
├── templates/
│   ├── index.html  # Template da interface do usuário
├── static/
│   ├── css/               # Arquivos CSS
│   └── js/                # Arquivos JavaScript
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
