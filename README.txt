Bom dia Srs,
Gostaria de Dizer que utilizei de forma rapida uma analise do projeto para otimizar o tempo de desenvolvimento
sem levar muito em consideracao a performance.

arquivos nao foram enviados devido a espaco 

'C:/GIT/Nasa/access_log_Jul95.txt'

'C:/GIT/Nasa/access_log_Aug95.txt'




1)Qual o objetivo do comando cache em Spark?

O uso do comando cache ajuda a melhorar a execuc�o dentro do ambiente Spark, 
faz com que execu��es mais lenta possam ser armazenadas e reutilizadas varias
vezes durante o processamento deste codigo.

2)O mesmo c�digo implementado em Spark � normalmente mais r�pido que a implementa��o equivalente em
MapReduce. Por qu�?

MapReduce normalmente escreve em disco e o Spark pode ter processo realizado em memoria atraves de cache compartilhado
reduzindo acesso a disco.

3)Qual � a fun��o do SparkContext?

O SparkContext funciona como um cliente do ambiente de execu��o Spark. 
Atrav�s dele, passam-se as configura��es que v�o ser utilizadas na aloca��o de recursos, 
como mem�ria e processadores, pelos executors. 
Tamb�m usa-se o SparkContext para criar RDDs, colocar jobs em execu��o, 
criar vari�veis de broadcast e acumuladores.

4)Explique com suas palavras o que � Resilient Distributed Datasets (RDD).

Conjunto de dados resilientes e distribu�dos, conceito central do framework Spark. 

RDD sao como uma tabela do banco de dados que pode guardar qualquer tipo de dado.

Eles s�o chamados Resilient por serem tolerantes � falha e erros 
RDDs nao mudam, s�o objetos para leitura apenas, e s� podem ser mudados atrav�s de transforma��es 
que resultam na cria��o de novos RDDs 


5)GroupByKey � menos eficiente que reduceByKey em grandes dataset. Por qu�?

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
Na seguencia a linha � "dividida" por espacos,em uma sequ�ncia de tokens
depois mapeada com uma unica palavra por vez, formando a chave
e entao agregados por essa chave, e finalmente um count e salvo em um arquivo texto

