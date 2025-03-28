# 列表推导式
# [表达式 for 变量 in 列表]
# [out_exp_res for out_exp in input_list]
# 或者
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)





# 字典推导式
# { key_expr: value_expr for value in collection }
# 或
# { key_expr: value_expr for value in collection if condition }

listdemo = ['Google','Runoob', 'Taobao']
dictDemo =  { item: len(item) for item in listdemo}
dic = {x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}
# dictDemo2={}
# for e in listdemo:
#     dictDemo2[e]=len(e);
# print(dictDemo2)







# 集合推导式
# { expression for variable in iterable }
setnew = {i**2 for i in (1,2,3)}

# 元组推导式
a = (x for x in range(1,10))