sudo docker service create --name testing --network vpc1 --limit-memory 300MB --replicas 4 nginx
echo -e '_print_ Created nginx image on vpc1 4 replicas and this service name is testing
'sudo docker service scale testing=10
echo -e '_print_ testing service scaled to 10 replicas
'sudo docker node ls
echo -e '_print_ Show all nodes
'sudo docker node ps
echo -e '_print_ Shows running containers on all nodes'
echo 'Operation finished'