import tensorflow as tf


model_path = 'C:\\Users\\Bruno\\Desktop\\h5View\\diabetic_retinopathy_model.h5'
# Carregar o modelo completo
model = tf.keras.models.load_model(model_path)

# Resumir a arquitetura do modelo
model.summary()
