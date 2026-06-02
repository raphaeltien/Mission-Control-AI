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

### Bateria
| Condição | Classificação |
|---|---|
| Menor que 20% | CRITICO |
| Entre 20% e 49% | ATENCAO |
| 50% ou mais | NORMAL |

### Oxigênio
| Condição | Classificação |
|---|---|
| Menor que 80% | CRITICO |
| Entre 80% e 89% | ATENCAO |
| 90% ou mais | NORMAL |

### Estabilidade
| Condição | Classificação |
|---|---|
| Menor que 40% | CRITICO |
| Entre 40% e 69% | ATENCAO |
| 70% ou mais | NORMAL |

## Pontuação de risco
- NORMAL = 0 ponto
- ATENCAO = 1 ponto
- CRITICO = 2 pontos

## Classificação dos ciclos
- 0 a 2 pontos → MISSAO ESTAVEL
- 3 a 5 pontos → MISSAO EM ATENCAO
- 6 a 10
