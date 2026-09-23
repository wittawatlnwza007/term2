import numpy as np

random_martix = np.random.randint(1,11,size=(3,3))
print("Random 3x3 Matrix:\n",random_martix)

matrix_sum = np.sum(random_martix)
print(f"\nSum of all elements: {matrix_sum}")

matrix_mean = np.mean(random_martix)
print(f"\nMean of the mtrix : {matrix_mean:2.2f}")

transposed_matrix = np.transpose(random_martix)
print("\nTransposed Matrix:\n" , transposed_matrix)