# solr_migrate_api_solution
Before run the code, you need to create the target collection. 

- For that download the collection's conf (Linux):

cd <solr_diirectory>/bin/
./solr zk downconfig -d <download_path> -n <conf_name> -z localhost:2181

- If you want to check for the conf you can use:

./solr zk ls /configs -z localhost:2181

- If you want to upload the conf:

sh <solr_diirectory>/zkcli.sh -zkhost <zookeeper_hostname>:<port> -cmd upconfig --confdir <conf_download_path> --confname <conf_name>

- To Create the Collection

curl-k --negotiate -u: "https://<solr_host>:<solr_port>/solr/admin/collections?action=CREATE&name=<collection_name>&router.name=compositeld&numShards=4&replicationFactor=2&maxShardsPerNode=3&collection.configName=<conf_name>"
