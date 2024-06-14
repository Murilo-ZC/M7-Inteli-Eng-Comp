#287448677294 - AccountID
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 287448677294.dkr.ecr.us-east-1.amazonaws.com

aws ecr create-repository --repository-name hello-world --region us-east-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

# Construir
docker build --platform linux/amd64 -t docker-image:test .

# Pegar o "repositoryUri"
 "repositoryUri": "287448677294.dkr.ecr.us-east-1.amazonaws.com/hello-world"

# Taggear a imagem
docker tag docker-image:test 287448677294.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

# Enviar a imagem
docker push 287448677294.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest


--------------------------Para atualizar
# Construir
docker build --platform linux/amd64 -t docker-image:test .

# Taggear a imagem
docker tag docker-image:test 287448677294.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

# Enviar a imagem
docker push 287448677294.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest