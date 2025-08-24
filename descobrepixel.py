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

# --- Configuração do Texto ---
POSICAO_TEXTO = (22, 22)
TEXTO = "22,22"
FONTE = cv2.FONT_HERSHEY_SIMPLEX
ESCALA_FONTE = 0.5
COR_TEXTO = (255, 255, 255) # Branco no formato BGR
ESPESSURA_TEXTO = 1

print("Iniciando a câmera. Pressione 'q' na janela de vídeo para sair.")

try:
    while True:
        # Captura um array da câmera
        frame = picam2.capture_array()

        # Sobrepõe o texto na imagem
        cv2.putText(frame, TEXTO, POSICAO_TEXTO, FONTE, ESCALA_FONTE, COR_TEXTO, ESPESSURA_TEXTO)

        # Exibe o frame na janela
        cv2.imshow("Camera", frame)

        # Espera por uma tecla. Se 'q' for pressionada, sai do loop.
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:    # Ctrl c para interromper
    	picam2.stop()
    	cv2.destroyAllWindows()
    	print("Programa encerrado.")