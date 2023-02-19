from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# make_blobs tiene 4 parametros, n_samples es la cantidad de muestras, centers es la cantidad de clusters
# cluster_std es la desviacion estandar de cada cluster (que tan esparcidos estan los puntos en su cluster)
# y random_state es una medida para la aleatoriedad de la posicion de los clusters

# Generate a dataset with 300 samples, 3 centers, and a standard deviation of 1
X, y = make_blobs(n_samples=100, centers=4, cluster_std=2.6, random_state=42)

# make_blobs devuelve una tupla (x,y) donde x es un array de arrays con las coordenadas de cada punto, 
# y es un array con el grupo al que cada coordenada de x pertenece, es decir len(x) == len(y) 


# x son las coordenadas
print(X)

print('\n\n\n')
# y son las 
print(y)
print('\n\n\n')

# Visualize the generated dataset
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()