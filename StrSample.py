str,str10 = 'hello world','saojdaoiwjd'

print(len(str))
print(str.capitalize())
print(str.upper())
print(str.find('or'))
print(str.find('shit'))
print(str.startswith('he'))
print(str.endswith('ld'))
print(str.center(50,'*'))
print(str.rjust(50,'-'))

str1 = 'abcdefg1'
print(str1[1])
print(str1[0:2])
print(str1[0:2])
print(str1[::2])
print(str1[-1])
print(str1.isdigit()) #check whether num in str
print(str1.isalpha()) #check whether alpha in str
print(str1.isalnum()) #check whether num and alpha are all in str

str2 = '     asss'
print(str2.strip()) #cut off the space in the left and right


#list

list1 = [1,'hello']
list1.append('no')
list1.insert(2,2)
list1 += [100]
print(list1)
del list1[0]
print(list1)
list1.clear()

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
for fr in fruits:
    print(fr.title(), end=' ')  #use any words like fr or fur or whatever
print()

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print('list1:',list1)
print('list2:',list2)
print('list3:',list3)
print('list4:',list4)
list1.sort(reverse=True)
print(list1)

import sys

f = [x for x in range(1,10)]    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
print(f)
print(sys.getsizeof(f))
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x for x in range(1,10))
print(sys.getsizeof(f))
for val in f:
    print(val)

#除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数。
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
