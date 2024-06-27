Este projeto realiza a raspagem de dados de vagas de emprego do LinkedIn para identificar as tecnologias mais
requisitadas no mercado de trabalho. Atualmente, apenas a descrição das vagas é raspada. Futuramente, serão
implementadas funcionalidades para capturar mais dados, como nome da empresa, tamanho da empresa, número de aplicações
na vaga, modalidade de trabalho, entre outros.

# Instalação e configuração

Você deve ter instalado previamente **Python 3.12** e **Pip 23.2**, nessas versões ou posteriores.

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

### 1.° Passo: Adicionando suporte ao Selenium 4

Este projeto utiliza Scrapy, Selenium e uma biblioteca chamada scrapy-selenium, que infelizmente não é mais mantida e
suporta apenas Selenium 3. Queremos rodar com Selenium 4, então precisamos fazer algumas modificações.

Para isso, execute o comando abaixo para encontrar a localização da instalação do
scrapy-selenium: ```pip show scrapy-selenium | grep Location```.

Acesse a pasta retornada e substitua o arquivo middlewares.py da biblioteca pelo arquivo middlewares.py presente na raiz
deste projeto. Isso adicionará suporte ao Selenium 4.

### 2.° Passo: Preencher os dados de acesso ao LinkedIn

```bash
cp config_template.py config.py
```

* Preenche EMAIL com seu e-mail do LinkedIn
* Preenche SENHA com sua senha do LinkedIn
* Preencha URL com o url das vagas do LinkedIn que você deseja raspar, elas devem começar
  com `https://www.linkedin.com/jobs/search/`

### 3.° Passo: Definindo o navegador

Este projeto utiliza Selenium, que precisa do driver do seu navegador para funcionar. Se optar por usar
outro navegador que não seja o Chrome, acesse o arquivo `linkedin/linkedin/settings.py` e mude o valor da variável
SELENIUM_DRIVER_NAME para o nome do driver do seu navegador.

🎉 Após isso, o script estará pronto para ser executado!

# Executando o script

## 1.° Passo: raspando os dados

No arquivo `linkedin/linkedin/spiders/jobs.py` existe um `sleep(60)`. Esse sleep é necessário porque o LinkedIn pode
solicitar a resolução de um captcha ou um código enviado ao e-mail. Após o Selenium fazer o login, ele ficará parado por
60 segundos para que isso seja resolvido. Isso normalmente ocorre apenas nos primeiros acessos. Após isso, esse sleep
pode ser removido.

```bash
cd linkedin
scrapy crawl jobs -o jobs_example.json
```

## 2.° Passo: analisando os dados

1. No arquivo main.py, há várias tecnologias listadas em `technologies`. Apenas as tecnologias listadas aqui aparecerão
   na análise. Caso a tecnologia que você deseja analisar não esteja listada, adicione-a e envie um PR.
2. Atualmente, a exibição é feita no terminal. Sinta-se à vontade para editar isso. Futuramente, os dados serão
   analisados utilizando Streamlit.
