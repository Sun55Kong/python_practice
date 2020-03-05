#!/usr/bin/env python
# -*- coding:utf-8 -*-

product_list = [
    ('iphone',5000),
    ('Mac Pro',4000),
    ('Bike',1000),
    ('Watch',200),
    ('Coffee',100),
    ('python',10000),
]

salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    shopping_list = []
    while True:
        for index,item in enumerate(product_list):
            print(index,item)

        choice = input("you choice")
        if choice.isdigit():
            choice = int(choice)
            if choice < len(product_list) and choice >=0 :
                if salary >= product_list[choice][1]:
                    shopping_list.append(product_list[choice])
                    salary -= product_list[choice][1]
                    print("Add %s into shopping_list ,current salary is \033[31;1m%s\033[0m" % (product_list[choice],salary))
                else:
                    print("salary is less than product")
            else:
                print("输入的商品序号不存在")
        elif choice == "q":
            print(shopping_list)
            print("你的工资还剩%s" % salary)
            exit()
        else:
            print("输入的信号格式不对呀，臭婊子")

