#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from hiwonder.Controller import Controller
from hiwonder.ros_robot_controller_sdk import Board
import hiwonder.ActionGroupControl as AGC

print("Iniciando o programa para levantar o braço direito...")

try:
    # Inicializa a placa de controle e o controlador
    board = Board()
    ctl = Controller(board)

    # Retorna o robô à posição neutra de "stand"
    print("Retornando à posição de stand...")
    AGC.runActionGroup('stand')
    time.sleep(2)

    # Move o servo do braço direito para cima
    # O ID do servo do braço direito é geralmente 5
    # O valor 700 ou 800 define a posição. Ajuste para o seu robô!
    print("Levantando o braço direito...")
    ctl.set_pwm_servo_pulse(5, 700, 500)
    time.sleep(2)  # Mantém o braço na posição por 2 segundos

    # Retorna o braço para a posição inicial
    print("Voltando para a posição inicial...")
    ctl.set_pwm_servo_pulse(5, 1500, 500)
    time.sleep(1)

    print("Programa concluído.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Garante que o robô retorne à posição de "stand" em caso de erro
    AGC.runActionGroup('stand')