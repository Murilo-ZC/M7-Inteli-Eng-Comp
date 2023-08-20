# Instruções Gerais para o Encontro:

Ao longo deste encontro, vamos utilizar um conjunto de containers para apresentar nosso banco de dados Postgres.
Primeiro, executar o arquivo docker-compose:

```yaml
version: '3.1'

services:

  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: senha
      POSTGRES_USER: postgres
      POSTGRES_DB: postgres
    ports:
      - 5432:5432
    container_name: banco-db

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
    depends_on:
      - db
    container_name: adminer
```

Para iniciar o conjunto de container (pela primeira vez), utilizar o comando:

```bash
docker-compose up
```

Isso vai lançar os containers do Postgres e do Adminer. Para acessar o Adminer, no navegador, ir para url: http://localhost:8080.

<p align="center">
  <img src="../../static/adminer.png" width="100%" height="auto" title="Tela de Login Inicial do Adminer">
</p>

O Adminer permite criar tabelas de forma gráfica, mas para este encontro, vamos utilizar o SQL para criar as tabelas. Para isso, copiar o arquivo *.sql disponível nos arquivos da sala.

Para popular a tabela criada, utilizar o arquivo *.sql também disponível nos arquivos da sala.

```sql
CREATE TABLE Person(
    person_id SERIAL PRIMARY KEY,
    sex VARCHAR(1) NOT NULL,
    name VARCHAR(100) NOT NULL,
    user_name VARCHAR(50) NOT NULL,
    job VARCHAR(100) NOT NULL,
    company VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    mail VARCHAR(100) NOT NULL,
    blood_group VARCHAR(3) NOT NULL,
    address VARCHAR(200) NOT NULL
)
```

Depois de criada a tabela, vamos executar o script que vai adicionar conteúdo nela.
    
```sql
INSERT INTO 
person (job,company,blood_group,user_name,"name",sex,address,mail,birthday)
VALUES ('Clinical research associate','Figueroa and Sons','AB+','lindsay78','Anne Abbott','F','84959 Janet Cape Apt. 413
South Joshuastad, GA 49021','jason41@hotmail.com','1994-01-18'),
('Dramatherapist','Daniel, Martin and Gray','AB+','teresa28','Jeffrey Chavez','M','PSC 4893, Box 2528
APO AP 00575','tracy15@yahoo.com','1940-03-21'),
('Barrister','Humphrey Inc','O-','perezrebecca','Adrienne Zimmerman','F','347 Amber Stream
Sanchezfort, AS 53855','clintonhopkins@yahoo.com','1965-04-12'),
('Paediatric nurse','Shields-Brown','B+','brianromero','Amy Silva','F','136 Shelly Port
New Brooke, RI 11246','ksandoval@hotmail.com','1950-09-08'),
('Games developer','Santiago LLC','A+','danagreen','Andrew Cook','M','011 Amy Village Suite 982
Andersonport, MN 05730','jason31@yahoo.com','2013-10-20'),
('Surveyor, minerals','Dickson-Brady','A+','carlsonmichael','Victor Baker','M','816 Jonathan Station Suite 088
West Ryan, TN 43780','elizabeth14@hotmail.com','1949-09-21'),
('Osteopath','Powell-Phillips','O-','jennifercruz','Randy Gibson','M','016 Gregory Square
Williamsbury, PW 16407','danderson@hotmail.com','1979-12-01'),
('Surveyor, land/geomatics','Stewart, Fischer and Ramos','O+','acastaneda','Tommy Evans','M','3467 Paul Skyway
Ramseymouth, PW 17229','meadowsbrittany@hotmail.com','1911-04-27'),
('Charity officer','Patterson, Camacho and White','B-','tsanders','Laura Odonnell','F','49190 Patel Shore
Caseymouth, AL 55558','xgarcia@hotmail.com','2020-06-01'),
('Psychiatric nurse','Hernandez, Thompson and Boyd','B-','thomas85','Dana Beck','F','7444 David Fields Suite 182
East Joanna, KY 95473','tina34@gmail.com','1956-09-29'),
('Editorial assistant','Smith-Ferguson','O+','moorericky','Angela Allen','F','0344 Jones Fort Suite 936
New Jeffreyberg, PW 35317','charlesmartin@yahoo.com','1988-08-12'),
('Teacher, adult education','Gonzales-Harrison','AB+','lmoon','Casey Stone','F','Unit 6717 Box 5655
DPO AP 14211','marksteele@yahoo.com','1997-10-22'),
('Oncologist','Johnson, Miller and King','AB+','michellehill','Tammy Romero','F','8404 Monroe Prairie Suite 278
Reedside, WV 71729','ugibson@gmail.com','2002-07-23'),
('Field trials officer','Reyes, Chase and Jenkins','O+','wendy16','Cynthia Cohen','F','Unit 1724 Box 0050
DPO AA 47485','ryan38@yahoo.com','1984-08-26'),
('Education administrator','Thompson PLC','O+','catherinegomez','Steven Parsons','M','210 Kramer Bypass Suite 214
Julieburgh, ID 17823','alyssa42@yahoo.com','2019-11-14');
```

Agora, verifique se os dados então na tabela executando o seguinte comando:
    
```sql
SELECT * FROM person LIMIT 50;
```

