# Imagem base
FROM python:3.9

# Diretório dentro da imagem que vamos trabalhar
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code

# 
CMD ["python", "main.py"]
