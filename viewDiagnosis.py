import tensorflow as tf
import numpy as np
from PIL import Image

# Caminho para os arquivos
model_path = 'C:\\Users\\Bruno\\Desktop\\h5View\\diabetic_retinopathy_model.h5'
image_path = 'C:\\Users\\Bruno\\Desktop\\h5View\\3dd629fd6d09.png'  # Ajuste conforme necessário

# Carregar o modelo completo
model = tf.keras.models.load_model(model_path)

# Carregar a imagem
img = Image.open(image_path)
img = img.resize((256 , 256))  # Ajuste o tamanho para corresponder à entrada esperada
img = np.array(img)
img = img / 256.0  # Normalizar os valores dos pixels para o intervalo [0, 1]
img = np.expand_dims(img, axis=0)  # Adicionar uma dimensão para o batch

# Verificar a forma da imagem processada
print(f"Shape da imagem processada: {img.shape}")

# Fazer a previsão
predictions = model.predict(img)
predicted_class = np.argmax(predictions, axis=1)[0]

# Definir as etiquetas
labels = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]

# Exibir a previsão
print(f'Prediction: {predicted_class} - {labels[predicted_class]}')
