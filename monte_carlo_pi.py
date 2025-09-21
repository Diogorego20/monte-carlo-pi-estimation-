# -*- coding: utf-8 -*-
"""
Estima o Valor da Constante π (Pi) Utilizando o Método de Monte Carlo

Este script implementa o Método de Monte Carlo para estimar o valor da constante π.
O método consiste em gerar pontos aleatórios dentro de um quadrado e verificar
quantos deles caem dentro de um círculo inscrito. A proporção entre os pontos
dentro do círculo e o total de pontos permite estimar π.

Autor: Diogo da Silva Rego
Matrícula: 20240045381
Disciplina: Estatística Computacional
Professor: Pedro Rafael Diniz Marinho
Data: 19/09/2025

Dependências:
    - matplotlib: pip install matplotlib
    - numpy: pip install numpy
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np


def estimar_pi_com_visualizacao(numero_de_pontos, mostrar_grafico=True):
    """
    Estima o valor de π usando o Método de Monte Carlo com visualização gráfica.
    
    Args:
        numero_de_pontos (int): Número total de pontos a serem gerados
        mostrar_grafico (bool): Se True, exibe o gráfico da simulação
        
    Returns:
        tuple: (valor_estimado_pi, pontos_dentro, pontos_fora)
    """
    pontos_dentro_circulo = 0
    pontos_x_dentro = []
    pontos_y_dentro = []
    pontos_x_fora = []
    pontos_y_fora = []
    
    print(f"Gerando {numero_de_pontos:,} pontos aleatórios...")
    
    for i in range(numero_de_pontos):
        # Progresso da simulação
        if (i + 1) % (numero_de_pontos // 10) == 0:
            progresso = ((i + 1) / numero_de_pontos) * 100
            print(f"Progresso: {progresso:.0f}%")
        
        # Gera coordenadas aleatórias no quadrado [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Calcula a distância ao quadrado da origem
        distancia_ao_quadrado = x**2 + y**2
        
        # Verifica se o ponto está dentro do círculo unitário
        if distancia_ao_quadrado <= 1:
            pontos_dentro_circulo += 1
            pontos_x_dentro.append(x)
            pontos_y_dentro.append(y)
        else:
            pontos_x_fora.append(x)
            pontos_y_fora.append(y)
    
    # Calcula a estimativa de π
    pi_estimado = 4 * pontos_dentro_circulo / numero_de_pontos
    
    if mostrar_grafico:
        criar_visualizacao(pontos_x_dentro, pontos_y_dentro, 
                          pontos_x_fora, pontos_y_fora, 
                          pi_estimado, numero_de_pontos)
    
    return pi_estimado, pontos_dentro_circulo, numero_de_pontos - pontos_dentro_circulo


def criar_visualizacao(x_dentro, y_dentro, x_fora, y_fora, pi_estimado, total_pontos):
    """
    Cria a visualização gráfica da simulação de Monte Carlo.
    
    Args:
        x_dentro, y_dentro: Coordenadas dos pontos dentro do círculo
        x_fora, y_fora: Coordenadas dos pontos fora do círculo
        pi_estimado: Valor estimado de π
        total_pontos: Número total de pontos gerados
    """
    # Configuração da figura
    plt.figure(figsize=(10, 8))
    
    # Plota os pontos dentro do círculo (azuis)
    plt.scatter(x_dentro, y_dentro, c='blue', s=1, alpha=0.6, label=f'Dentro do círculo: {len(x_dentro):,}')
    
    # Plota os pontos fora do círculo (vermelhos)
    plt.scatter(x_fora, y_fora, c='red', s=1, alpha=0.6, label=f'Fora do círculo: {len(x_fora):,}')
    
    # Desenha o círculo unitário (verde)
    theta = np.linspace(0, 2*np.pi, 100)
    x_circulo = np.cos(theta)
    y_circulo = np.sin(theta)
    plt.plot(x_circulo, y_circulo, 'green', linewidth=2, label='Círculo unitário')
    
    # Desenha o quadrado de simulação (preto)
    quadrado_x = [-1, 1, 1, -1, -1]
    quadrado_y = [-1, -1, 1, 1, -1]
    plt.plot(quadrado_x, quadrado_y, 'black', linewidth=2, label='Área de simulação')
    
    # Configurações do gráfico
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))
    
    # Título com informações da estimativa
    diferenca = abs(math.pi - pi_estimado)
    precisao = (1 - diferenca/math.pi) * 100
    
    plt.title(f'Estima o Valor da Constante π (Pi) Utilizando o Método de Monte Carlo\n'
              f'Pontos: {total_pontos:,} | π estimado: {pi_estimado:.6f} | '
              f'π real: {math.pi:.6f} | Precisão: {precisao:.2f}%\n'
              f'Autor: Diogo da Silva Rego (20240045381)', 
              fontsize=12, pad=20)
    
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    
    # Salva o gráfico
    plt.tight_layout()
    plt.savefig('monte_carlo_pi_visualization.png', dpi=300, bbox_inches='tight')
    print("\nGráfico salvo como 'monte_carlo_pi_visualization.png'")
    
    # Exibe o gráfico
    plt.show()


def executar_simulacao_completa():
    """
    Executa a simulação completa com diferentes números de pontos.
    """
    print("=" * 60)
    print("ESTIMA O VALOR DA CONSTANTE π (PI) UTILIZANDO O MÉTODO DE MONTE CARLO")
    print("=" * 60)
    print(f"Autor: Diogo da Silva Rego")
    print(f"Matrícula: 20240045381")
    print(f"Disciplina: Estatística Computacional")
    print(f"Professor: Pedro Rafael Diniz Marinho")
    print("=" * 60)
    
    # Diferentes números de pontos para comparação
    numeros_pontos = [1000, 10000, 100000, 1000000]
    
    print("\nComparação de precisão com diferentes números de pontos:")
    print("-" * 60)
    
    for n_pontos in numeros_pontos:
        pi_est, dentro, fora = estimar_pi_com_visualizacao(n_pontos, mostrar_grafico=False)
        diferenca = abs(math.pi - pi_est)
        precisao = (1 - diferenca/math.pi) * 100
        
        print(f"Pontos: {n_pontos:>8,} | π estimado: {pi_est:.6f} | "
              f"Diferença: {diferenca:.6f} | Precisão: {precisao:.2f}%")
    
    # Simulação principal com visualização
    print(f"\n{'='*60}")
    print("SIMULAÇÃO PRINCIPAL COM VISUALIZAÇÃO GRÁFICA")
    print(f"{'='*60}")
    
    pontos_principais = 100000  # Número otimizado para visualização
    pi_final, dentro_final, fora_final = estimar_pi_com_visualizacao(
        pontos_principais, mostrar_grafico=True
    )
    
    # Resultados finais
    print(f"\n{'='*60}")
    print("RESULTADOS FINAIS")
    print(f"{'='*60}")
    print(f"Número total de pontos gerados: {pontos_principais:,}")
    print(f"Pontos dentro do círculo: {dentro_final:,}")
    print(f"Pontos fora do círculo: {fora_final:,}")
    print(f"Proporção dentro do círculo: {dentro_final/pontos_principais:.6f}")
    print(f"Valor estimado de π: {pi_final:.6f}")
    print(f"Valor real de π: {math.pi:.6f}")
    print(f"Diferença absoluta: {abs(math.pi - pi_final):.6f}")
    print(f"Precisão da estimativa: {(1 - abs(math.pi - pi_final)/math.pi) * 100:.2f}%")
    
    print(f"\n{'='*60}")
    print("EXPLICAÇÃO DO MÉTODO")
    print(f"{'='*60}")
    print("O Método de Monte Carlo para estimar π baseia-se na relação:")
    print("• Área do círculo = π × r²")
    print("• Área do quadrado = (2r)²")
    print("• Razão = (π × r²) / (2r)² = π/4")
    print("• Portanto: π = 4 × (pontos_dentro_círculo / total_pontos)")


if __name__ == "__main__":
    # Executa a simulação completa
    executar_simulacao_completa()
