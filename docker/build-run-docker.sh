
label="chain-dev"
version="v1.0"
#name=$label
name="witness"
if [ $# -gt 2 ]; then
    version=$1
    name=$2
fi
tag=${label}":"${version}

echo '>>> docker build '${tag}
docker build -t  ${tag}  .

echo ">>> docker run "${tag} " --> " ${name}
docker run --name  ${name} -e HOST_OPTS=`hostname`  -dit  -p 8051:8051 -p 8049:8049 -p 8041:8041 -p 8048:8048  -p 4306:3306 -p 28017:27017 -p 7379:6379 -v /Users/a123/data/docker/data:/data ${tag}

