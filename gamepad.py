import pygame
import time
from hiwonder import Board, PWM_Servo

# Inicializar a placa do TonyPi
Board.init()

# Inicializar pygame
pygame.init()
pygame.joystick.init()

# Verificar se há controles conectados
if pygame.joystick.get_count() == 0:
    print("Nenhum controle encontrado! Conecte um controle.")
    exit()

# Inicializar o primeiro controle
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Controle conectado: {joystick.get_name()}")

# Configuração dos servos (ajuste conforme sua calibração)
SERVO_CONFIG = {
    'head_yaw': 24,       # Cabeça horizontal
    'head_pitch': 23,     # Cabeça vertical
    'shoulder_r': 21,     # Ombro direito
    'elbow_r': 22,        # Cotovelo direito
    'shoulder_l': 17,     # Ombro esquerdo
    'elbow_l': 18,        # Cotovelo esquerdo
    'hip_r': 19,          # Quadril direito
    'knee_r': 20,         # Joelho direito
    'hip_l': 15,          # Quadril esquerdo
    'knee_l': 16          # Joelho esquerdo
}

# Posições neutras (ajuste conforme sua calibração)
NEUTRAL_POSITIONS = {
    SERVO_CONFIG['head_yaw']: 90,
    SERVO_CONFIG['head_pitch']: 90,
    SERVO_CONFIG['shoulder_r']: 90,
    SERVO_CONFIG['elbow_r']: 90,
    SERVO_CONFIG['shoulder_l']: 90,
    SERVO_CONFIG['elbow_l']: 90,
    SERVO_CONFIG['hip_r']: 90,
    SERVO_CONFIG['knee_r']: 90,
    SERVO_CONFIG['hip_l']: 90,
    SERVO_CONFIG['knee_l']: 90
}

def set_neutral_position():
    """Coloca o TonyPi na posição neutra"""
    for servo_id, angle in NEUTRAL_POSITIONS.items():
        PWM_Servo.setPosition(servo_id, angle)
    time.sleep(1)

def walk_forward():
    """Andar para frente"""
    print("Andando para frente")
    # Implementar sequência de caminhada aqui
    pass

def walk_backward():
    """Andar para trás"""
    print("Andando para trás")
    # Implementar sequência de caminhada aqui
    pass

def turn_left():
    """Virar à esquerda"""
    print("Virando à esquerda")
    # Implementar sequência de virada
    pass

def turn_right():
    """Virar à direita"""
    print("Virando à direita")
    # Implementar sequência de virada
    pass

def main():
    """Função principal de controle"""
    print("Controle Xbox ativo!")
    print("Pressione START para sair")
    
    # Colocar TonyPi na posição neutra inicial
    set_neutral_position()
    
    try:
        running = True
        while running:
            for event in pygame.event.get():
                # Botões para andar
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # Botão A
                        walk_forward()
                    elif event.button == 1:  # Botão B
                        walk_backward()
                    elif event.button == 2:  # Botão X
                        turn_left()
                    elif event.button == 3:  # Botão Y
                        turn_right()
                    elif event.button == 7:  # Botão START
                        running = False
                
                # Analógicos para movimentos precisos
                elif event.type == pygame.JOYAXISMOTION:
                    # Analógico esquerdo (movimento)
                    if event.axis == 0:  # Eixo X
                        if event.value > 0.5:
                            turn_right()
                        elif event.value < -0.5:
                            turn_left()
                    
                    if event.axis == 1:  # Eixo Y
                        if event.value < -0.5:
                            walk_forward()
                        elif event.value > 0.5:
                            walk_backward()
                    
                    # Analógico direito (cabeça)
                    if event.axis == 3:  # Eixo X direito
                        head_angle = NEUTRAL_POSITIONS[SERVO_CONFIG['head_yaw']] + int(event.value * 30)
                        PWM_Servo.setPosition(SERVO_CONFIG['head_yaw'], head_angle)
                    
                    if event.axis == 4:  # Eixo Y direito
                        head_angle = NEUTRAL_POSITIONS[SERVO_CONFIG['head_pitch']] + int(event.value * 30)
                        PWM_Servo.setPosition(SERVO_CONFIG['head_pitch'], head_angle)
                
                # Gatilhos para braços
                elif event.type == pygame.JOYHATMOTION:
                    # D-pad para controles adicionais
                    pass
            
            time.sleep(0.01)  # Pequeno delay para não sobrecarregar
            
    except KeyboardInterrupt:
        print("Controle interrompido")
    finally:
        # Voltar à posição neutra e limpar
        set_neutral_position()
        time.sleep(1)
        PWM_Servo.allPWMOff()
        Board.close()
        pygame.quit()

if __name__ == "__main__":
    main()