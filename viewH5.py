import h5py

# Caminho para o seu arquivo .h5
file_path = 'C:\\Users\\Bruno\\Desktop\\h5View\\diabetic_retinopathy_model.h5'

# Abrir o arquivo HDF5
with h5py.File(file_path, 'r') as f:
    # Função recursiva para imprimir as informações do arquivo
    def print_h5_structure(name, obj):
        print(name)
        if isinstance(obj, h5py.Group):
            print("Group")
        elif isinstance(obj, h5py.Dataset):
            print("Dataset: shape = {}, dtype = {}".format(obj.shape, obj.dtype))

    # Iterar sobre todos os grupos e datasets no arquivo
    f.visititems(print_h5_structure)
