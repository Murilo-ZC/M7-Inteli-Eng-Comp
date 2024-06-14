---
sidebar_position: 2
title: Monolitos
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Monolitos

Monolitos são aplicações de software que são desenvolvidas como uma única unidade. Eles são geralmente grandes, complexos e difíceis de manter. Monolitos são frequentemente criticados por serem difíceis de escalar e manter, mas eles têm suas vantagens.

> Poxa Murilo, mas por que você está falando de monolitos? A gente não está falando de microserviços?

Sim, estamos falando de microserviços, mas é importante entender o que são monolitos para entender o que são microserviços. Monolitos são a abordagem tradicional para o desenvolvimento de software, e muitas empresas ainda usam monolitos para desenvolver seus sistemas.

Mesmo que monolitos tenham suas desvantagens, eles têm suas vantagens. Monolitos são mais fáceis de desenvolver e manter do que sistemas distribuídos, e eles são mais fáceis de escalar do que sistemas distribuídos. Monolitos são uma boa escolha para sistemas pequenos e médios.

<img src={useBaseUrl("/img/monolitos-servicos/monolitos.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

<p style={{ textAlign:"center", marginBottom:'24px' }}>(Referência: [link](https://media.licdn.com/dms/image/C4D12AQEt2ZNVJ5lk-g/article-cover_image-shrink_720_1280/0/1650374810008?e=2147483647&v=beta&t=nDvrz3mNuLumjk45Dij5m-IPUzR9HC6dAAjUGPLa30s))</p>

### Vantagens dos Monolitos

Aqui estão algumas vantagens dos monolitos:

1. **Simplicidade**: Monolitos são mais fáceis de desenvolver e manter do que sistemas distribuídos.

2. **Escalabilidade**: Monolitos são mais fáceis de escalar do que sistemas distribuídos (verticalmente).

3. **Facilidade de depuração**: Monolitos são mais fáceis de depurar do que sistemas distribuídos, enquanto os sistemas são menores.

4. **Facilidade de implementação**: Monolitos são mais fáceis de implementar do que sistemas distribuídos.

5. **Facilidade de teste**: Monolitos são mais fáceis de testar do que sistemas distribuídos.

6. **Facilidade de monitoramento**: Monolitos são mais fáceis de monitorar do que sistemas distribuídos.


### Desvantagens dos Monolitos


Os sistemas monolíticos, nos quais o software é construído como uma única unidade indissociável, têm suas vantagens, especialmente na simplicidade de desenvolvimento e deploy inicial. No entanto, à medida que a aplicação cresce, diversas desvantagens podem se tornar aparentes. Aqui estão algumas das principais desvantagens dos sistemas monolíticos:

1. ***Escalabilidade limitada***: Em um sistema monolítico, escalonar frequentemente significa replicar toda a aplicação, o que pode ser ineficiente se apenas partes específicas da aplicação precisarem de mais recursos. Isso resulta em uso desnecessário de recursos e pode ser custoso.

2. ***Dificuldade de manutenção***: À medida que o monolito cresce, ele pode se tornar complexo e difícil de entender. Isso torna o processo de manutenção, como correções de bugs e adição de novas funcionalidades, mais lento e mais propenso a erros.

3. ***Acoplamento forte***: Os componentes de um sistema monolítico são frequentemente fortemente acoplados e dependentes uns dos outros. Isso significa que mudanças em uma parte do sistema podem afetar outras partes de maneira imprevisível, aumentando o risco de falhas.

4. ***Implantação lenta***: Atualizar um sistema monolítico pode ser um processo lento e arriscado, já que qualquer alteração requer a reimplantação de todo o sistema. Isso pode levar a tempos de inatividade significativos e reduzir a agilidade do desenvolvimento.

5. ***Dificuldades na adoção de novas tecnologias***: Integrar novas tecnologias ou atualizar as antigas em um sistema monolítico pode ser complicado, uma vez que mudanças tecnológicas podem requerer alterações em toda a base do código.

6. ***Testabilidade***: Testar um sistema monolítico pode ser desafiador, especialmente à medida que ele cresce. Isso ocorre porque é difícil isolar componentes para testes unitários, o que pode levar a testes integrados mais complexos e demorados.

7. ***Risco de falha do sistema***: Em sistemas monolíticos, uma falha em um componente pode afetar toda a aplicação, resultando em falhas completas do sistema, o que pode ser catastrófico para a continuidade dos negócios.

8. ***Barreiras para novos desenvolvedores***: Para novos desenvolvedores, entender um sistema monolítico grande e complexo pode ser intimidador e demorado, o que pode retardar o processo de integração e contribuição efetiva ao projeto.

---

### Sugestão de Material

<iframe width="560" height="315" src="https://www.youtube.com/embed/CsrHHHPHKwE?si=HlYsHe6YISOb2rFv" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }}></iframe>