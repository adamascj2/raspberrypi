#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from hiwonder import Board, PWM_Servo

# Inicializa os servos do TonyPi
def init_servos():
    # Configura os servos para suas posições iniciais
    # (Você pode precisar ajustar os canais e posições conforme seu hardware)
    pass

# Função para dar um passo à frente
def step_forward():
    # Sequência de movimentos para um passo
    # Levanta a perna direita
    PWM_Servo.setPosition(15, 90)  # Ajuste o canal e ângulo conforme necessário
    PWM_Servo.setPosition(16, 120)
    time.sleep(0.5)
    
    # Move a perna direita para frente
    PWM_Servo.setPosition(15, 60)
    time.sleep(0.5)
    
    # Abaixa a perna direita
    PWM_Servo.setPosition(16, 90)
    time.sleep(0.5)
    
    # Levanta a perna esquerda
    PWM_Servo.setPosition(12, 90)  # Ajuste o canal e ângulo conforme necessário
    PWM_Servo.setPosition(13, 60)
    time.sleep(0.5)
    
    # Move a perna esquerda para frente
    PWM_Servo.setPosition(12, 120)
    time.sleep(0.5)
    
    # Abaixa a perna esquerda
    PWM_Servo.setPosition(13, 90)
    time.sleep(0.5)
    
    # Retorna à posição neutra
    PWM_Servo.setPosition(15, 90)
    PWM_Servo.setPosition(12, 90)
    time.sleep(0.5)

# Programa principal
def main():
    # Inicializa a placa
    Board.init()
    
    try:
        # Inicializa os servos
        init_servos()
        time.sleep(1)
        
        print("TonyPi vai dar 5 passos...")
        
        # Dá 5 passos para frente
        for i in range(5):
            print(f"Passo {i+1}")
            step_forward()
            time.sleep(0.5)
        
        print("TonyPi parou!")
        
    except KeyboardInterrupt:
        # Para o robô se o usuário pressionar Ctrl+C
        pass
    finally:
        # Limpa e desliga os servos
        PWM_Servo.allPWMOff()
        Board.close()

if __name__ == "__main__":
    main()