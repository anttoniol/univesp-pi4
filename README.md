# Instruções

1. Baixar o repositório
2. No diretório raiz, criar um arquivo properties.json com o mesmo conteúdo de default_properties.json
3. Inserir a chave da API no campo 'key' do arquivo properties.json (para criar uma chave, seguir as instruções em https://openweathermap.org/api/one-call-3)
4. Alterar os outros campos do arquivo properties.json, caso necessário
5. Instalar o interpretador do Python: https://www.python.org/downloads/
6. Instalar as bibliotecas contidas no arquivo requirements.txt, utilizando o seguinte comando: `pip install -r requirements.txt`
5. Para executar a aplicação, executar no diretório raiz:
    1. `python3 service.py` (Linux)
    2. `python service.py` (Windows)