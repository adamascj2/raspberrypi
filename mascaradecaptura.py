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

print("Pressione 'q' para sair.")

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

        # Exibe o frame original em uma janela
        cv2.imshow("Camera", frame)

        # Exibe a máscara em uma segunda janela
        cv2.imshow("Mascara Vermelha", mask)

        if cv2.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    picam2.stop()
    cv2.destroyAllWindows()
    print("Programa encerrado.")