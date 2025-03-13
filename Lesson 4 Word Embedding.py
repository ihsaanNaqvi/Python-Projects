 # word embedding 

#list of dictionary 
# 1- Apple  1,0,0,0,0
# 2- Orange 0,1,0,0,0
# 3 - juice 
# 4- like 
# 5- I  0,0,0,0,1
# 1-transform into vector -- word embedding 
# I like orange juice.
#one shot vector 

# I like orange juice 
#  orange = I , like , juice 

# 0,1 ,0,0,0
# 0,0,1,1,1


# x  0,1 ,0,0,0
# y  0,0,1,1,1


# 0,0,0,0,1 I
# 0,0,0,1,0 like
# 0,1,0,0,0 orange
# 0,0,1,0,0 juice 


# king - man+ women  reuslt in space vector  result queen 
#Feed forward newtork 

# y = f(w x + b)
# x,y,b are vectors 
# W is a matrix 

# Word2 vec was published by google in 2013
# z= f(W1 x + b1)
# y  = f(W2 + z + b2)

# we will get W1 , w2 , b1 and b2
 # w1
# my dictionary contains 100 000 words
# len(x) = 100000
# len(y) = 100000
# len (z)  = 300 or 500 
# x = 0,1,0,0,0
# y = 0,0,1,1,1
# W1 is a matrix with dimention len()
# W1 contain  len(x)  column and len(z) rows 

# contexs 

# W1  

# home work any of model construct  positive and negtive wrods 
# you must  build list of positve and  negative to get a result containing the words " sun"
# or "car"
#  the intitial lists contain  contain the desired words themselves.