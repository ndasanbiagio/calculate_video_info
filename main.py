import cv2

# Abre el archivo de video
video = cv2.VideoCapture("video.mp4")

# Obtiene la resolución del video
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Obtiene el número total de fotogramas en el video
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

# Obtiene la velocidad de fotogramas (frames per second - FPS) del video
fps = video.get(cv2.CAP_PROP_FPS)

# Imprime la información obtenida
print("Ancho:", width)
print("Alto:", height)
print("Número de fotogramas:", nr_frames)
print("FPS:", fps)

# Cierra el objeto VideoCapture
video.release()
