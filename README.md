# Fluxo de dados no Nifi


## Requerimentos:
- É necessário realizar o download da biblioteca requests:
    - ```shell 
      $ pip install -r requirements.txt
      ```
- Também é preciso conter o docker instalado na maquina para rodar o Nifi:

    - ```shell
      $ docker-compose up -d
      ```
      
- OBS: É preciso dar permissão de escrita no diretório treinamento_nifi do seu host:
    - ```shell 
      $ sudo chmod 777 /opt/nifi/output
      ```
      
- OBS 2: Para que você consiga prosseguir, é necessário instalar o **Spark 2.3.2** 
      
## Fluxo no Nifi:

- É preciso importar o template do fluxo:

 - Clique no botão de upload template
   
   ![nifi](https://user-images.githubusercontent.com/17969551/96472949-71e77f80-1207-11eb-82dd-954052dedb4c.jpg)

 - Após selecionar o template xml (data_flow_json.xml), basta selecionar a opção de template que encontra-se na parte superior e arraste para o meio da tela
 
 
 - Depois de selecionar o template, o fluxo estará montado e será exibido desta forma:
 
   ![flux](https://user-images.githubusercontent.com/17969551/96458174-01386700-11f7-11eb-9a54-4d611c72745c.png)
   
   OBS: Para funcionar, é necessário dar um start nos processor, basta clicar com o botão direito e em seguida **start**<br><br>

# Enviar dados para o Nifi:

- ```shell 
  $ python generator_json.py
  ```

# Execute o spark:
 
- ```shell 
  $ python spark/run_spark.py
  ```
 
# Resultado:

- Os arquivos parquet serão armazenados em **/opt/nifi/trusted**:<br><br>

  ![exemplo](https://user-images.githubusercontent.com/17969551/96468886-faafec80-1202-11eb-9f9b-aaf6c4cac324.png)<br><br>

  ![nifi](https://user-images.githubusercontent.com/17969551/96492523-25596f80-121a-11eb-9274-f9b44494cc03.png)<br><br>

  ![data](https://user-images.githubusercontent.com/17969551/96476830-21265580-120c-11eb-8b82-c660b561b10d.png)
