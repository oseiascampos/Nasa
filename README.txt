Bom dia Srs,
Gostaria de Dizer que utilizei de forma rapida uma analise do projeto para otimizar o tempo de desenvolvimento
sem levar muito em consideracao a performance.

arquivos nao foram enviados devido a espaco 

'C:/GIT/Nasa/access_log_Jul95.txt'

'C:/GIT/Nasa/access_log_Aug95.txt'




1)Qual o objetivo do comando cache em Spark?

O uso do comando cache ajuda a melhorar a execucão dentro do ambiente Spark, 
faz com que execuções mais lenta possam ser armazenadas e reutilizadas varias
vezes durante o processamento deste codigo.

2)O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em
MapReduce. Por quê?

MapReduce normalmente escreve em disco e o Spark pode ter processo realizado em memoria atraves de cache compartilhado
reduzindo acesso a disco.

3)Qual é a função do SparkContext?

O SparkContext funciona como um cliente do ambiente de execução Spark. 
Através dele, passam-se as configurações que vão ser utilizadas na alocação de recursos, 
como memória e processadores, pelos executors. 
Também usa-se o SparkContext para criar RDDs, colocar jobs em execução, 
criar variáveis de broadcast e acumuladores.

4)Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

Conjunto de dados resilientes e distribuídos, conceito central do framework Spark. 

RDD sao como uma tabela do banco de dados que pode guardar qualquer tipo de dado.

Eles são chamados Resilient por serem tolerantes à falha e erros 
RDDs nao mudam, são objetos para leitura apenas, e só podem ser mudados através de transformações 
que resultam na criação de novos RDDs 


5)GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

Porque o algoritimo de agrupamento(GroupByKey) utiliza disco em excesso para realizar o calculo
e depois filtrar causando resultado negativo em performance, ao contrario do (reduceByKey) que realiza um filtro
antes de calcular o resultado final.

6)
1. val textFile = sc . textFile ( "hdfs://..." )
2. val counts = textFile . flatMap ( line => line . split ( " " ))
3.           . map ( word => ( word , 1 ))
4.           . reduceByKey ( _ + _ )
5. counts . saveAsTextFile ( "hdfs://..." )

Leitura de um arquivo na linha 1 no formato hadoop (Hdfs).
Na seguencia a linha é "dividida" por espacos,em uma sequência de tokens
depois mapeada com uma unica palavra por vez, formando a chave
e entao agregados por essa chave, e finalmente um count e salvo em um arquivo texto

