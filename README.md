# Mission Control AI — Projeto Krypton

## Descrição
Sistema inteligente de monitoramento de missão espacial desenvolvido em Python.
O sistema analisa ciclos de monitoramento da missão, gera alertas automáticos,
calcula o nível de risco de cada ciclo e exibe um relatório final com a situação
da operação.

## Integrantes
Lana Namie Kano Ozeki - RM 569795
Luigi Borgheti Freire - RM 569958
Raphael Chen Rue Tien - RM 570261 
## Como rodar
1. Certifique-se de ter o Python instalado
2. Clone o repositório ou baixe o arquivo mission_control.py
3. Execute o comando no terminal:
python mission_control.py

## Estrutura do projeto
mission-control-ai/
├── README.md
└── mission_control.py

## Regras de alerta

### Temperatura
| Condição | Classificação |
|---|---|
| Menor que 18°C | ATENCAO |
| Entre 18°C e 30°C | NORMAL |
| Entre 30°C e 35°C | ATENCAO |
| Maior que 35°C | CRITICO |

### Comunicação
| Condição | Classificação |
|---|---|
| Menor que 30% | CRITICO |
| Entre 30% e 59% | ATENCAO |
| 60% ou mais | NORMAL |
