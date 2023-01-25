# Commands

```
create = Like sudo docker service create

scale = Like sudo docker service scale

node  = Like sudo docker node

_print_  =  echo -e

version '1' = version that must be specifyed at the top of Pizzafile
```


# Vars

"network=", "repl=", "label=", "cpu=", "mem=", "name="

# How to use
```
1 . Create a Pizzafile use syntax given down
2. Run pizza.py
3. execute Pizzaout.sh on target server
```

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

Pizzaout.sh

```
sudo docker service create --name testing --network vpc1 --limit-memory 300MB --replicas 4 nginx
echo -e '_print_ Created nginx image on vpc1 4 replicas and this service name is testing
'sudo docker service scale testing=10
echo -e '_print_ testing service scaled to 10 replicas
'sudo docker node ls
echo -e '_print_ Show all nodes
'sudo docker node ps
echo -e '_print_ Shows running containers on all nodes'
echo 'Operation finished'
```

# want to extend this idea?
Contacts :

```
rehmanazhar922@gmail.com
cybersecurty922@gmail.com
+92 3258202936 | whatsapp
```
