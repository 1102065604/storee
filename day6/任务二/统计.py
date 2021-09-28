def count(list = []):
    for i in list:
        if i not in list_dict:
            list_dict[i] = 1
        else:
            list_dict[i] += 1
List1 = [21, 21, 21, 56, 56, 56, 56, 56, 56, 56, 56, 56, 10, 10, 10]
list_dict = {}
count(List1)
print(list_dict)

'''
def count():
    List1 = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
    for i in List:
      if i not in  list_dict:
          list_dict[i] = 1
      else:
          list_dict[i] += 1
List1 = [21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
list_dict ={}
count()
print(list_dict)
'''