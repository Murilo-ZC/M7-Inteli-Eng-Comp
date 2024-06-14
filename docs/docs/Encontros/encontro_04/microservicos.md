---
sidebar_position: 3
title: Microsserviços
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Microsserviços

Microserviços são uma abordagem para o desenvolvimento de software que envolve a construção de um sistema de software como um conjunto de serviços independentes. Cada serviço é uma unidade de software independente que pode ser desenvolvida, implantada e escalada de forma independente. Os microserviços são frequentemente criticados por serem mais complexos do que monolitos, mas eles têm suas vantagens.

> Ok Murilo, então estamos falando de vários pequenos monolitos?

Não exatamente. Microserviços são diferentes de monolitos. Monolitos são uma abordagem tradicional para o desenvolvimento de software, onde todo o software é desenvolvido como uma única unidade. Microserviços, por outro lado, são uma abordagem moderna para o desenvolvimento de software, onde o software é desenvolvido como um conjunto de serviços independentes.

> Mas o que são serviços independentes?

Serviços independentes são serviços que podem ser desenvolvidos, implantados e escalados de forma independente. Eles são geralmente pequenos, focados em uma única tarefa e têm uma interface bem definida. Os serviços independentes são frequentemente criticados por serem mais complexos do que monolitos, mas eles têm suas vantagens.

<img src={useBaseUrl("/img/monolitos-servicos/microservicos.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

<p style={{ textAlign:"center", marginBottom:'24px' }}>(Referência: [link](https://media.licdn.com/dms/image/C4D12AQEt2ZNVJ5lk-g/article-cover_image-shrink_720_1280/0/1650374810008?e=2147483647&v=beta&t=nDvrz3mNuLumjk45Dij5m-IPUzR9HC6dAAjUGPLa30s))</p>

### Vantagens dos Microsserviços

A arquitetura de microsserviços é uma abordagem popular para o desenvolvimento de aplicações, especialmente em ambientes de grande escala e distribuídos. Aqui estão algumas das principais vantagens desta arquitetura:

1. **Modularidade**: Em microsserviços, cada serviço é um módulo que pode ser desenvolvido, implantado, operado e escalado de forma independente. Isso facilita a gestão de partes individuais do sistema sem afetar o todo.

2. **Escalabilidade**: Cada microsserviço pode ser escalado independentemente, permitindo alocar mais recursos apenas para os serviços que necessitam, o que é mais eficiente do ponto de vista de uso de recursos e custo.

3. **Flexibilidade tecnológica**: Diferentes microsserviços podem ser escritos em diferentes linguagens de programação, usar diferentes bancos de dados e diferentes tecnologias de armazenamento, permitindo que a equipe escolha as melhores ferramentas para cada serviço especificamente.

4. **Resiliência**: A falha em um microsserviço é isolada e geralmente não afeta outros serviços. Isso melhora a estabilidade geral do sistema, pois permite que apenas a parte afetada seja tratada, enquanto o restante do sistema continua operacional.

5. **Facilidade de manutenção**: Menos código em um serviço significa que é mais fácil de entender, testar e manter. Além disso, a autonomia dos serviços facilita a atualização e a correção de bugs em sistemas complexos.

6. **Ciclos de desenvolvimento mais rápidos**: Como os microsserviços são pequenos e independentes, podem ser desenvolvidos, testados e implantados mais rapidamente do que seria possível em uma arquitetura monolítica. Isso contribui para uma maior agilidade e velocidade na entrega de novas funcionalidades.

7. **Deploy contínuo e independente**: Os microsserviços permitem que diferentes equipes implantem seus serviços de forma independente em qualquer momento, sem interromper o funcionamento dos outros serviços. Isso facilita a integração e entrega contínuas (CI/CD).

### Desvantagens dos Microsserviços

Embora a arquitetura de microsserviços ofereça muitas vantagens, existem também desafios e desvantagens significativas que devem ser consideradas antes de adotar essa abordagem. Aqui estão algumas das principais desvantagens do uso de microsserviços:

1. **Complexidade de Gerenciamento**: A gestão de múltiplos serviços independentes pode ser mais complexa do que gerenciar um sistema monolítico. Isso inclui desafios com versionamento de serviços, gerenciamento de dependências entre serviços e manutenção de um gateway de API eficiente.

2. **Overhead de Comunicação**: Como os microsserviços frequentemente se comunicam através da rede, há um overhead de latência e carga associados com as chamadas de API. Isso pode resultar em um desempenho inferior se comparado com chamadas de função em um ambiente monolítico.

3. **Consistência de Dados**: Manter a consistência de dados em um ambiente distribuído pode ser desafiador. Transações que abrangem múltiplos serviços exigem padrões complexos, como a compensação de transações ou o uso de transações distribuídas, que podem ser difíceis de implementar e manter.

4. **Complexidade de Testes**: Testar uma aplicação baseada em microsserviços pode ser mais complicado do que testar um monolito. É necessário garantir que cada serviço funcione como esperado, tanto de forma isolada quanto em conjunto com outros serviços.

5. **Segurança**: Aumentar o número de serviços também aumenta a superfície de ataque potencial. Cada serviço é um ponto potencial de entrada para ataques, o que requer uma abordagem robusta de segurança, autenticação e autorização entre serviços.

6. **Dificuldade na Depuração e Monitoramento**: Acompanhar e diagnosticar problemas em um sistema distribuído pode ser complicado, pois é necessário correlacionar logs e dados de monitoramento de vários serviços e instâncias.

7. **Requisitos de Infraestrutura**: Operar uma arquitetura de microsserviços geralmente requer uma infraestrutura mais sofisticada e custosa, incluindo soluções para orquestração de contêineres, monitoramento distribuído, e balanceamento de carga.

8. **Custo de Desenvolvimento**: O desenvolvimento pode se tornar mais caro devido à necessidade de especialistas em várias tecnologias, ferramentas adicionais para gerenciamento de microsserviços, e o esforço extra necessário para garantir a integração e a entrega contínuas.

9. **Duplicação de Esforços**: Pode haver uma tendência à duplicação de esforços, como funções de autenticação ou chamadas de banco de dados, em vários serviços, o que pode aumentar a carga de trabalho e os custos de manutenção.

10. **Gestão de Equipes**: Coordenar múltiplas equipes trabalhando em diferentes serviços pode ser desafiador, especialmente em termos de comunicação e alinhamento com os objetivos gerais do projeto.

Cada organização deve avaliar cuidadosamente esses desafios ao considerar a transição para uma arquitetura de microsserviços, garantindo que os benefícios superem as desvantagens no contexto de seus requisitos e capacidades específicos.

---

### Sugestões de Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/_2bDOCTnbKc?si=cFOn1qAYRBKKkVBr" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }}></iframe>