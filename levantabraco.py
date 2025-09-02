#!/usr/bin/env python3
# tonypi_levantar_braco_direito.py

import time
import hiwonder.ros_robot_controller_sdk as rrc

def inicializar_tonypi():
    """Inicializa a conexão com o TonyPi"""
    try:
        # Inicializar o controlador do robô
        robot_controller = rrc.RobotController()
        
        # Conectar ao robô
        robot_controller.connect()
        
        print("TonyPi conectado com sucesso!")
        return robot_controller
        
    except Exception as e:
        print(f"Erro ao conectar com TonyPi: {e}")
        return None

def levantar_braco_direito(robot_controller):
    """Levanta o braço direito do TonyPi"""
    
    # Configuração dos servos do braço direito (IDs podem variar - consulte a documentação)
    # Valores típicos para TonyPi:
    # - Ombro direito: Servo 21
    # - Cotovelo direito: Servo 22
    
    SERVO_OMBRO_DIREITO = 21
    SERVO_COTOVELO_DIREITO = 22
    
    try:
        print("Iniciando movimento do braço direito...")
        
        # Posição inicial (braço abaixado)
        posicao_inicial_ombro = 90   # Ângulo neutro
        posicao_inicial_cotovelo = 90 # Ângulo neutro
        
        # Posição final (braço levantado)
        posicao_levantada_ombro = 60    # Ombro para cima
        posicao_levantada_cotovelo = 30  # Cotovelo flexionado
        
        # Mover para posição inicial primeiro
        print("Posicionando braço na posição inicial...")
        robot_controller.set_servo_position(SERVO_OMBRO_DIREITO, posicao_inicial_ombro, 1000)  # 1000ms = 1 segundo
        robot_controller.set_servo_position(SERVO_COTOVELO_DIREITO, posicao_inicial_cotovelo, 1000)
        time.sleep(1.5)
        
        # Levantar o braço suavemente
        print("Levantando braço direito...")
        
        # Primeiro move o ombro
        robot_controller.set_servo_position(SERVO_OMBRO_DIREITO, posicao_levantada_ombro, 800)
        time.sleep(0.9)
        
        # Depois move o cotovelo
        robot_controller.set_servo_position(SERVO_COTOVELO_DIREITO, posicao_levantada_cotovelo, 600)
        time.sleep(1.0)
        
        print("Braço direito levantado!")
        
        # Manter a posição por 3 segundos
        time.sleep(3)
        
        # Voltar à posição inicial suavemente
        print("Voltando à posição inicial...")
        robot_controller.set_servo_position(SERVO_COTOVELO_DIREITO, posicao_inicial_cotovelo, 800)
        time.sleep(0.9)
        robot_controller.set_servo_position(SERVO_OMBRO_DIREITO, posicao_inicial_ombro, 1000)
        time.sleep(1.5)
        
        print("Movimento concluído!")
        
    except Exception as e:
        print(f"Erro durante o movimento: {e}")

def main():
    """Função principal"""
    print("=== PROGRAMA LEVANTAR BRAÇO DIREITO TONYPi ===")
    
    # Inicializar o TonyPi
    tonypi = inicializar_tonypi()
    
    if tonypi is None:
        print("Não foi possível conectar ao TonyPi. Verifique:")
        print("1. Se o TonyPi está ligado")
        print("2. Se a rede ROS está ativa")
        print("3. Se a SDK está instalada corretamente")
        return
    
    try:
        # Executar o movimento
        levantar_braco_direito(tonypi)
        
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        # Desconectar e limpar
        print("Desconectando do TonyPi...")
        tonypi.disconnect()
        print("Conexão encerrada.")

if __name__ == "__main__":
    main()