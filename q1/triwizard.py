import numpy as np

# ---- Task (a) -------
# Do as directed in function:
# 'my_list': a list of 25 integers
def avada_kedavra(my_list):
	# Create an array 'a0' from this list 'my_list'
    a0=np.array(my_list)
	# print a0
    print("a0 at beginning:\n{}".format(a0))

	# reshape a0 to create a 5X5 matrix a1
    a1=a0.reshape(5,5)
	# print a1
    print("a1 at the beginning:\n{}".format(a1))
    
	# now, change the central element of a1 to 0
    a1[int(a1.shape[0]/2),int(a1.shape[1]/2)] =0
	# print a1
    print("a1 after change:\n{}".format(a1))

	# print a0
    print("a0 after changing a1:\n{}".format(a0))
    print("reshaping doesn't create a copy of array. It just returns another view. So, changing one changed the other")

	# make a copy of a1 and flatten it (call it a1cpy)
    a1cpy=a1.copy()
    a1cpy=a1cpy.flatten()
	# multiply each element of a1cpy by 0.7:
    a1cpy= np.array(list(map(lambda x : x*(0.7) , a1cpy)))
	# print a1cpy:
    print("a1cpy\n{}".format(a1cpy))

	# print a1:
    print("a1 after changing its copy:\n{}".format(a1))


# ---- Task (b) -------
# Do as directed in function:
# 'my_integer': an even integer
def incendio(my_integer):
	# create an array 'arng0' of shape (3,2) containing consecutive even numbers starting from 'my_integer', arranged along rows
    arng0=np.arange(my_integer,my_integer + 12,2).reshape(3,2)
	# print arng0
    print("arng0\n{}".format(arng0))

	# create another array 'arng1' of shape ((4,3)) containing consecutive numbers starting from 'my_integer' arranged along columns:
    arng1=np.transpose(np.arange(my_integer,my_integer + 12,1).reshape(3,4))
	# print arng1
    print("arng1\n{}".format(arng1))

	# multiply transpose of arng0 with transpose of arng1 to get mult0:
    mult0=np.dot(np.transpose(arng0),np.transpose(arng1))
	# print mult0:
    print("mult0\n{}".format(mult0))

	# take min of mult0 along its rows and store it in v0:
    v0=np.min(mult0,axis=1)
	# print v0's shape:
    print("shape of v0: \n{}".format(v0.shape))
    
	# reshape v0 to make it a column vector:
    v0=v0.reshape(-1,1)
	# subtract v0 from each column of mult0 and store it in base0:
    base0=np.subtract(mult0,v0)
	# print base0
    print("base0\n{}".format(base0))

	# square all the elements present in base0
    base0=np.square(base0)
	# store the sum of all elements of base0 in ans
    ans=base0.sum()
	# print ans
    print("ans : {}".format(ans))


# ---- Task (c) -------
# 'n': integer
# 'm': integer that divides n
# return type: int numpy Ndarray; dim: nxn
def alohomora(n, m):
    k=np.zeros(n*n,dtype=int).reshape(n,n)
    for j in range(int(n/m)):
        index= j*2*m
        for i in range(n):
            if((int(i/m))%2==0):
                k[index:m+index,i:i+1]=1
    for j in range(int(n/m)):
        index= j*2*m + m
        for i in range(n):
            if((int(i/m))%2==1):
                k[index:m+index,i:i+1]=1
    return k


# ---- Task (d) -------
# 'arr': float Ndarray; dim: Nx3, 
# 'theta': float; 0≤theta<360 (in degrees)
# 'axis': str; axis ∈ {'X','Y','Z'}
# return type: float Ndarray; dim: Nx3
def expelliarmus(arr, theta, axis):
    theta=np.radians(30)
    if (axis=='Y'):
        Rt= np.array([np.cos(theta),0,np.sin(theta),0,1,0,-np.sin(theta),0,np.cos(theta)]).reshape(3,3)
    if (axis=='X'):
        Rt= np.array([1,0,0,0,np.cos(theta),-np.sin(theta),0,np.sin(theta),np.cos(theta)]).reshape(3,3)
    if(axis=='Z'):
        Rt= np.array([np.cos(theta),-np.sin(theta),0,np.sin(theta),np.cos(theta),0,0,0,1]).reshape(3,3)
    rs=np.array(list(map(lambda x:np.dot(Rt,x), arr)))
    return rs.round(decimals=2,out=None)
	


# ---- Task (e) -------
# 'arr': float Ndarray; dim: MxN
# return type: float Ndarray; dim: MxN
def crucio(arr):
    mean=np.mean(arr,axis=0)
    xyz=np.subtract(arr,mean)
    dev=np.std(arr,axis=0)
    xyz=np.divide(xyz,dev).round(decimals=2,out=None)
    return xyz


# ---- Task (f) -------
# 'arr': int 1-D array; dim: (n,)
# k: integer
# return type: int 1-D array; dim: (n+k-1,)
def leviosa(arr, k):
#     https://stackoverflow.com/questions/12709853/python-running-cumulative-sum-with-a-given-window
    nn=np.cumsum(arr)
    z=np.arange(k-1)
    nn[k:]=nn[k:]-nn[:-k]
    zk = np.array(list(map(lambda x:((arr[-k+x+1:]).sum()),z )))
    nn=np.append(nn,zk)
    return nn
    


# ---- Task (g) -------
# 'mat': int n-D array; dim: (m,n)
# k: integer
# return type: n-D integer array; dim: (m,k)
def accio(mat, k):
    #https://www.geeksforgeeks.org/numpy-argsort-in-python/#:~:text=argsort()%20in%20Python,-Last%20Updated%3A%2028&text=28%2D12%2D2018-,numpy.,that%20would%20sort%20the%20array.
    return np.argsort(arr,axis=1)[:,arr.shape[1]-k:]
