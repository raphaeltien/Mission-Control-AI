# Variáveis
nome_missao = "Projeto Krypton"
nome_equipe = "Equipe Astra"
dados_missao = [
    [20, 95, 90, 99, 95],
    [26, 82, 78, 97, 90],
    [30, 67, 64, 93, 75],
    [35, 44, 42, 75, 55],
    [40, 30, 23, 66, 30],
    [35, 57, 36, 70, 45],
]
areas_monitoradas = [
    "Temperatura Interna",
    "Comunicacao com a base",
    "Sistema de Energia",
    "Suporte de Oxigenio",
    "Estabilidade Operacional",
]

# Funções

def analisar_temperatura(temperatura):
    if temperatura < 18:
        classificacao = "ATENCAO!!!"
        pontuacao = 1
        mensagem = "Temperatura baixa"
    elif temperatura >= 18 and temperatura <= 30:
        classificacao = "NORMAL"
        pontuacao = 0
        mensagem = "Temperatura normal"
    elif temperatura > 30 and temperatura < 35:
        classificacao = "ATENCAO!!!"
        pontuacao = 1
        mensagem = " Temperatura um pouco acima"
    else:
        classificacao = "Critico!!!"
        pontuacao = 2
        mensagem = "Temperatura muito alta"

    return classificacao, pontuacao, mensagem

def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        classificacao = "CRITICO!!!"
        pontuacao = 2
        mensagem = "Comunicacao com a base critica"
    elif comunicacao >= 30 and comunicacao < 60:
        classificacao = "ATENCAO!!!"
        pontuacao = 1
        mensagem = "Comunicacao com a base instavel"
    else:
        classificacao = "NORMAL"
        pontuacao = 0
        mensagem = "Comunicacao com a base estavel"

    return classificacao, pontuacao, mensagem

def analisar_bateria(bateria):
    if bateria < 20:
        classificacao = "CRITICO!!!"
        pontuacao = 2
        mensagem = "Sistema de energia muito baixo"
    elif bateria > 20 and bateria < 49:
        classificacao = "ATENCAO!!!"
        pontuacao = 1
        mensagem = "Sistema de energia baixo"
    else:
        classificacao = "NORMAL"
        pontuacao = 0
        mensagem = "Sistema de energia normal"
    return classificacao, pontuacao, mensagem

def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        classificacao = "CRITICO!!!"
        pontuacao = 2
        mensagem = "Suporte de oxigenio muito baixo"
    elif oxigenio > 80 and oxigenio < 89:
        classificacao = "ATENCAO!!!"
        pontuacao = 1
        mensagem = " Suporte de oxigenio baixo"
    else:
        classificacao = "NORMAL"
        pontuacao = 0
        mensagem = "Suporte de oxigenio normal"
    return classificacao, pontuacao, mensagem

def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        classificacao = "CRITICO!!!"
        pontuacao = 2
        mensagem = "Estabilidade operacional muito baixa"
    elif estabilidade > 40 and estabilidade < 69:
        classificacao = "ATENCAO!!!"
        pontuacao = 1
        mensagem = " Estabilidade operacional baixa"
    else:
        classificacao = "NORMAL"
        pontuacao = 0
        mensagem = "Estabilidade normal"
    return classificacao, pontuacao, mensagem

def classificar_ciclo(pontuacao_total):
    if pontuacao_total <= 2:
        classificacao = "MISSAO ESTAVEL"
    elif pontuacao_total > 2 and pontuacao_total <= 5:
        classificacao = "MISSAO EM ATENCAO!!!"
    else:
        classificacao = "MISSAO CRITICA!!!"
    return classificacao

def analisar_tendencia(risco_primeiro, risco_ultimo):
    if risco_ultimo > risco_primeiro:
        tendencia = "A MISSAO APRESENTOU TENDENCIA DE PIORA!!!"
    elif risco_ultimo < risco_primeiro:
        tendencia = "A MISSAO APRESENTOU TENDENCIA DE MELHORA!!!"
    else:
        tendencia = "A MISSAO APRESENTOU TENDENCIA ESTAVEL!!!"
    return tendencia

def identificar_area_mais_afetada(pontuacao_areas):
    maior_pontuacao = 0
    area_mais_afetada = ""

    for i in range(len(areas_monitoradas)):
        if pontuacao_areas[i] > maior_pontuacao:
            maior_pontuacao = pontuacao_areas[i]
            area_mais_afetada = areas_monitoradas[i]
    return area_mais_afetada, maior_pontuacao

def analisar_missao():
    pontuacao_areas = [0, 0, 0, 0, 0]
    riscos_ciclos = []

    for i in range(len(dados_missao)):
        ciclo = dados_missao[i]

        temperatura  = ciclo[0]
        comunicacao  = ciclo[1]
        bateria      = ciclo[2]
        oxigenio     = ciclo[3]
        estabilidade = ciclo[4]

        c_temp, p_temp, m_temp = analisar_temperatura(temperatura)
        c_com, p_com, m_com = analisar_comunicacao(comunicacao)
        c_bat, p_bat, m_bat = analisar_bateria(bateria)
        c_oxi, p_oxi, m_oxi = analisar_oxigenio(oxigenio)
        c_est, p_est, m_est = analisar_estabilidade(estabilidade)
        pontuacao_total = p_temp + p_com + p_bat +p_oxi +p_est
        print(f"\nCICLO {i + 1}")
        print("-" * 60)
        print(f"Temperatura: {temperatura}°C | {c_temp} | {m_temp}")
        print(f"Comunicacao: {comunicacao}% | {c_com} | {m_com}")
        print(f"Bateria: {bateria}% | {c_bat} | {m_bat}")
        print(f"Oxigenio: {oxigenio}% | {c_oxi} | {m_oxi}")
        print(f"Estabilidade: {estabilidade}% | {c_est} | {m_est}")
        pontuacao_areas[0] += p_temp
        pontuacao_areas[1] += p_com
        pontuacao_areas[2] += p_bat
        pontuacao_areas[3] += p_oxi
        pontuacao_areas[4] += p_est
        riscos_ciclos.append(pontuacao_total)

    return riscos_ciclos, pontuacao_areas


def gerar_relatorio_final():
    riscos_ciclos, pontuacao_areas = analisar_missao()
    maior_risco = max(riscos_ciclos)
    ciclo_critico = riscos_ciclos.index(maior_risco) + 1
    tendencia = analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1])
    area, pontos = identificar_area_mais_afetada(pontuacao_areas)
    print("=" * 60)
    print("MISSION CONTROL AI — RELATORIO FINAL")
    print("=" * 60)
    print(f"Missao: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Ciclos analisados: {len(dados_missao)}")
    print(f"Ciclo mais critico: Ciclo {ciclo_critico}")
    print(f"Maior pontuacao de risco: {maior_risco}")
    print(f"Tendencia da missao: {tendencia}")
    print(f"Area mais afetada: {area}")
    print(f"pontuacao da area mais afetada: {pontos}")
    print("=" * 60)
    print("FIM DO RELATORIO")
    print("=" * 60)

gerar_relatorio_final()