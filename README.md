Script para reindexação de índices do ElasticSearch.
Dado o ip do host, um index e um type de documentos de um banco de dados elasticsearch o script reindexa todos os documentos
em um novo index e type informados. Caso o index de destino não exista, ele será criado.

## Ajuda:
Para exibir o meu de ajuda, execute python reindex_elasticsearch.py -h

## Argumentos de linha de comando(Obrigatórios):
index_from é o index de origem.

index_to é o index de destino.

host_from é o ip do host de origem, onde está instalado o elasticsearch.

type_from é o type dos documentos de origem.

type_to é o type dos documentos de destino.

## Argumentos de linha de comando(Opcional):
host_to é o ip do host de destino. Quando não for passado, será considerado o mesmo que o parâmetro host_from.

bulk_size Tamanho do bulk que será enviado para o elasticsearch. O valor default é 10.

number_of_shards Número de shards para o novo índice, que será criado caso não exista. O valor default é 1.

number_of_replicas Número de shards para o novo índice, que será criado caso não exista. O valor default é 0.

## Exemplo de execução:
python reindex_elasticsearch.py index_source index_dest 127.0.0.1 type_source type_dest --bulk_size 5000

Reindexa todos os documentos do index index_source, type type_source do host 120.0.0.1 no index index_dest, type type_dest
e host 120.0.0.1. O tamanho do bulk de envio dos dados será 5000.

## Dependências:
É preciso ter a biblioteca elasticsearch instalada no python. Caso não tenha, execute o comando abaixo para instalar:

pip install -r requirements.txt
