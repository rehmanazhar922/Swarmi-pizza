# Commands

create = Like sudo docker service create
scale = Like sudo docker service scale
node  = Like sudo docker node
_print_  =  echo -e
version '1' = version that must be specifyed at the top of Pizzafile


# Vars

"network=", "repl=", "label=", "cpu=", "mem=", "name="



Pizzafile

```
version '1'
create name=testing network=vpc1 mem=300MB repl=4 nginx
_print_ Created nginx image on vpc1 4 replicas and this service name is testing
scale testing=10
_print_ testing service scaled to 10 replicas
node ls
_print_ Show all nodes
node ps
_print_ Shows running containers on all nodes
```

