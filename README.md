Script para reindexa��o de �ndices do ElasticSearch.
Dado o ip do host, um index e um type de documentos de um banco de dados elasticsearch o script reindexa todos os documentos
em um novo index e type informados. Caso o index de destino n�o exista, ele ser� criado.

## Ajuda:
Para exibir o meu de ajuda, execute python reindex_elasticsearch.py -h

## Argumentos de linha de comando(Obrigat�rios):
index_from � o index de origem.

index_to � o index de destino.

host_from � o ip do host de origem, onde est� instalado o elasticsearch.

type_from � o type dos documentos de origem.

type_to � o type dos documentos de destino.

## Argumentos de linha de comando(Opcional):
host_to � o ip do host de destino. Quando n�o for passado, ser� considerado o mesmo que o par�metro host_from.

bulk_size Tamanho do bulk que ser� enviado para o elasticsearch. O valor default � 10.

number_of_shards N�mero de shards para o novo �ndice, que ser� criado caso n�o exista. O valor default � 1.

number_of_replicas N�mero de shards para o novo �ndice, que ser� criado caso n�o exista. O valor default � 0.

## Exemplo de execu��o:
python reindex_elasticsearch.py index_source index_dest 127.0.0.1 type_source type_dest --bulk_size 5000

Reindexa todos os documentos do index index_source, type type_source do host 120.0.0.1 no index index_dest, type type_dest
e host 120.0.0.1. O tamanho do bulk de envio dos dados ser� 5000.

## Depend�ncias:
� preciso ter a biblioteca elasticsearch instalada no python. Caso n�o tenha, execute o comando abaixo para instalar:

pip install -r requirements.txt
