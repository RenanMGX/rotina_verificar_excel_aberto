# Verificar Excel Aberto

Este projeto contém uma rotina em Python que monitora e fecha automaticamente livros do Excel abertos que excedam um tempo configurado, utilizando a biblioteca [xlwings](https://docs.xlwings.org/en/stable/).

## Estrutura do Projeto

- **[main.py](main.py)**  
  Script principal que inicia a rotina chamando o método [`close_excel`](Entities/excel_verify.py).

- **Entities/**  
  Contém as classes responsáveis pela lógica do projeto:
  - **[excel_verify.py](Entities/excel_verify.py)**  
    Define a classe [`ExcelVerify`](Entities/excel_verify.py) que percorre as instâncias do Excel abertas e fecha livros que excedam o limite de tempo informado.
  - **[files_control.py](Entities/files_control.py)**  
    Define a classe [`FilesControl`](Entities/files_control.py) que gerencia um arquivo JSON para registrar os tempos de abertura dos livros e realizar limpezas com base em um tempo limite.

- **json/**  
  - **[register.json](json/register.json)**  
    Arquivo que armazena os registros dos livros abertos.

- **requirements.txt**  
  Lista as dependências utilizadas pelo projeto.

## Funcionamento

1. Ao executar o script em **[main.py](main.py)**, o método estático `close_excel` da classe [`ExcelVerify`](Entities/excel_verify.py) é chamado.
2. Dentro deste método:
   - Uma instância de [`FilesControl`](Entities/files_control.py) é criada para gerenciar os registros (arquivo JSON) que controlam o tempo de abertura dos livros.
   - O método `limpar` é chamado para limpar registros antigos.
   - Para cada aplicativo Excel (`xw.apps`), o código percorre os livros abertos:
     - Se o livro estiver aberto por mais que o tempo configurado (padrão de 2 horas), ele será fechado.
     - Se não houver mais instâncias do Excel, o aplicativo é finalizado.
     
## Configuração e Execução

1. Instale as dependências usando o comando:
    ```sh
    pip install -r requirements.txt
    ```
2. Inicie o programa executando:
    ```sh
    python main.py
    ```

## Notas

- As configurações do Visual Studio Code estão em [.vscode/settings.json](.vscode/settings.json), que define o modo de verificação de tipos para Python.
- O diretório `json` é criado automaticamente, se necessário, para armazenar o arquivo de registros.
- O arquivo de controle JSON é gerado pela classe [`FilesControl`](Entities/files_control.py) na primeira execução, caso não exista.

## Licença

Este projeto está licenciado sob os termos da licença MIT.