# Algoritmos-de-deteccao
Entendendo um pouco sobre YOLO (algoritmo de detecção), KCF de CSRT (algoritmos de rastreamento)

Para rodar os códigos, primeiramente tenha Python : https://www.python.org
Depois, realize esse comando no terminal -> pip install opencv-python opencv-contrib-python
Observação: vai ser necessário o numpy também (pip install numpy)
Pronto, você pode rodar o KCF e CSRT! Baixe um video mp4 e chame-o de teste.mp4, coloque na mesma pasta do arquivo .py, abra um terminal que aponte para a pasta e faça um -> python AlgoritmosdeRastreamento.py
<br>
Para rodar o YOLO:
Vá no repositório da darknet (https://github.com/AlexeyAB/darknet) e baixe algumas coisas:
- coco.names (está em /data)
- yolov4-tiny.cfg e yolov4-tiny.weights (caso você tenha o CUDA e o CMake no seu computador, tente modelos mais pesados como o yolov4-p6.cfg e yolov4-p6.weights, não esqueça de modificar o código para funcionar!)
- pronto, faça um python AlgoritmodeDeteccao.py
