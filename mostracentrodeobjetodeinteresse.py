import cv2
from picamera2 import Picamera2
import numpy as np
import time

picam2 = Picamera2()
dispW = 640
dispH = 480

picam2.preview_configuration.main.size = (dispW, dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# --- Definições de Cor em HSV ---
# O vermelho tem duas faixas na roda de cores HSV
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

print("Iniciando o rastreamento do objeto vermelho. Pressione 'q' para sair.")
 
try:
    while True:
        # Captura um frame da câmera
        frame = picam2.capture_array()

        # Converte o frame para o espaço de cor HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Cria as duas máscaras para as faixas de vermelho
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        
        # Combina as duas máscaras em uma única
        mask = mask1 + mask2

        # Exibe a máscara para diagnóstico. Descomente esta linha para ver a máscara.
        cv2.imshow("Mascara Vermelha", mask)

        # --- Encontrando Contornos e o Centro do Objeto ---
        # Encontra os contornos na máscara.
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Encontra o maior contorno (assumindo que seja o objeto desejado)
            maior_contorno = max(contours, key=cv2.contourArea)
            
            # Se o contorno for grande o suficiente
            # O valor 100 é um limite mais baixo para detectar objetos menores
            if cv2.contourArea(maior_contorno) > 100: 
                # Calcula os momentos do contorno para encontrar o centro
                M = cv2.moments(maior_contorno)
                
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    
                    # Desenha um círculo no centro do objeto
                    cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)
                    
                    # Coloca as coordenadas do centro na tela
                    coordenadas_texto = f"({cX}, {cY})"
                    cv2.putText(frame, coordenadas_texto, (cX + 10, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Exibe o frame original com as marcações
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:    # Ctrl c para interromper
    picam2.stop()
    cv2.destroyAllWindows()
    print("Programa encerrado.")