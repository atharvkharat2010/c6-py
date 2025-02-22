my_dict={}
my_dict={1:'apple',2:'banana'}
my_dict={'name':'atharv' ,1:[2,3,4]}
my_dict={'name':'rohit' ,'age':15}
print(my_dict['name'])
print(my_dict['age'])
my_dict['age']=16
print(my_dict)
my_dict['address']='mumbai'
print(my_dict)
my_dict['address']='downtown'
print(my_dict)
my_dict.pop('address')
print(my_dict)
print("address:",my_dict.get('address'))
print("name:",my_dict.get('name'))
my_dict.clear()
print(my_dict)