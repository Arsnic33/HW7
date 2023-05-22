import numpy as np

def main():
    arr = np.array([[1, 2], [3, 4]])
    eig_val, eig_vec = np.linalg.eig(arr)
    determinant = int(np.linalg.det(arr))
    
    print("고유값:")
    print(eig_val)
    print("\n고유벡터:")
    print(eig_vec)
    print("\n행렬식:")
    print(determinant)

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])
    output = np.cross(vec1, vec2)
    print("\n벡터곱:")
    print(output)

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([-15,-21,18])
    x = np.linalg.solve(A,b)
    print("\nx1, x2, x3:")
    print(x)
    
if __name__ == "__main__":
    main()
