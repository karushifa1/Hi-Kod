import numpy as np # type: ignore
#2boyutlu
dizi1=np.array([[1,2,3],[4,5,6]],dtype='str')
np.array([[1,2,3],[4,5,6]],ndmin=4)
print(dizi1.ndim)
print(dizi1)
print(dizi1[0,1])#indexing
print(dizi1[0:2,2])#slicing
print(dizi1.size)
print(np.shape(dizi1))

#3boyutlu
dizi2=np.array([[[1,2,3],[4,5,6]],
          [[9,8,7],[6,5,4]]],dtype="int")

np.array([[[1,2,3],[4,5,6]],
          [[9,8,7],[6,5,4]]])
print(dizi2.ndim)
print(dizi2)
print(dizi2[0,1,1])#indexing
print(dizi2[0,1,:])#slicing
print(dizi2.size)
print(np.shape(dizi2))

#1boyutlu
dizi3=np.array([7,8,9,10])
np.array([7,8,9,10])
print(dizi3[3])
print(dizi3)

array1 = np.zeros((2, 2), dtype=int)
array2 = np.ones((2, 2), dtype=int)
print(array1)
print(array2)

satirbirlestirme = np.concatenate((array1, array2), axis=0)
print(satirbirlestirme)

sutunbirlestirme = np.concatenate((array1, array2), axis=1)
print(sutunbirlestirme)



