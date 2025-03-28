echo "[1] Create docker network (bookstore-network)"
docker network inspect bookstore-network >/dev/null 2>&1 || docker network create -d bridge bookstore-network

echo "[2] Create FastAPI Catalog"
docker stop fastapi-catalog
docker rm fastapi-catalog
docker build -t api-gateway services/catalog/
#docker run -d --name  fastapi-catalog --net=bookstore-network  fastapi-catalog
docker run -d --name fastapi-catalog --net=bookstore-network -p 8888:80 fastapi-catalog


echo "[3] Create FastAPI Stores"
docker stop fastapi-store
docker rm fastapi-store
docker build -t fastapi-store services/stores/
#docker run -d --name  fastapi-store --net=bookstore-network  fastapi-store
docker run -d --name fastapi-store --net=bookstore-network -p 8889:80 fastapi-store


echo "[4] Create API Gateway"
docker stop api-gateway
docker rm api-gateway
docker build -t api-gateway gateway/
docker run -d --name api-gateway --net=bookstore-network  -p 443:443 api-gateway


echo "Containers running..."
docker ps

#echo "*****Testing API Gateway*****"
#curl -ik --header "apikey:abc123" --request GET  https://bookstore.io/api/bookstore/catalog/books

