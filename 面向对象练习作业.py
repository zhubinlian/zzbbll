#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Student:
    
    def __init__(self, name, xuehao, phone):
        self.name = name
        self.xuehao = xuehao
        self.phone = phone
    def say_hello(self):
        print("你好，我是{n}".format(n=self.name))
    def print__phone(self):
        print("我的电话是{n}".format(n=self.phone))
    def say_hello(self):
        print("我的名字是{n}".format(n=self.name))


# In[2]:


#实例化
zhangsan = Student("zhangsan","01","123456")


# In[3]:


#属性
zhangsan.xuehao


# In[4]:


zhangsan.phone


# In[5]:


zhangsan.name


# In[ ]:




