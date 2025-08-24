import cv2
from picamera2 import Picamera2
import numpy as np
import time

picam2 = Picamera2()
dispW = 400
dispH = 400

picam2.preview_configuration.main.size = (dispW, dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# --- Configuração do Retângulo ---
TAMANHO_RETANGULO = 50
COR_RETANGULO = (0, 0, 255)  # Vermelho no formato BGR
ESPESSURA_RETANGULO = -1     # Preenche o retângulo. Use um valor positivo para a borda.
POSICAO_RETANGULO = (100, 150) # Coordenada do canto superior esquerdo do retângulo (x, y)

print("Pressione 'q' na janela de vídeo para sair.")
 

try:
    while True:
        # Captura um array da câmera
        frame = picam2.capture_array()

        # Calcula as coordenadas dos dois pontos (canto superior esquerdo e canto inferior direito)
        pt1 = POSICAO_RETANGULO
        pt2 = (pt1[0] + TAMANHO_RETANGULO, pt1[1] + TAMANHO_RETANGULO)
        
        # Desenha o retângulo na imagem
        cv2.rectangle(frame, pt1, pt2, COR_RETANGULO, ESPESSURA_RETANGULO)

        # Exibe o frame na janela
        cv2.imshow("Camera", frame)

        # Espera por uma tecla. Se 'q' for pressionada, sai do loop.
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:    # Ctrl c para interromper
    	picam2.stop()
    	cv2.destroyAllWindows()
    	print("Programa encerrado.")