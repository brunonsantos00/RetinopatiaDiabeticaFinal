# Use uma imagem base oficial do TensorFlow
FROM tensorflow/tensorflow:latest-jupyter

# Copie o diretório do projeto para o diretório de trabalho no container
COPY . /tf

# Defina o diretório de trabalho
WORKDIR /tf/src

# Exponha a porta padrão do Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
