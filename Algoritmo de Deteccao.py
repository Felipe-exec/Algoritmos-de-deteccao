import cv2
import numpy as np

# Carregar a rede YOLO
net = cv2.dnn.readNet("yolov4-tiny.cfg", "yolov4-tiny.weights")

# Carregar as classes
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f]

layer_names = net.getUnconnectedOutLayersNames()

# Carregar o vídeo
cap = cv2.VideoCapture("teste.mp4")

# Configuração de resolução
cap.set(3, 640)  # Largura
cap.set(4, 480)  # Altura

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Pré-processamento da imagem para a entrada da rede YOLO
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (320, 320), swapRB=True, crop=False)
    net.setInput(blob)

    # Executar a detecção
    detections = net.forward(layer_names)

    # Processar as detecções
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Ajuste o valor de confiança conforme necessário
                center_x = int(obj[0] * frame.shape[1])
                center_y = int(obj[1] * frame.shape[0])
                w = int(obj[2] * frame.shape[1])
                h = int(obj[3] * frame.shape[0])

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                label = f"{classes[class_id]}: {confidence:.2f}"
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Exibir o vídeo com as detecções
    cv2.imshow("YOLO Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
