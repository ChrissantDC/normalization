# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# File_Name = input("")
# x = File_Name.split() #String split by spacebar.

with open('test', "r") as file_Read:
    file_Read_contents = file_Read.read()
    Final_Text = file_Read_contents
print(Final_Text)

x = Final_Text.split('\n') #String split by line.
print(x)

y = [] #this will store http:// and link name
z = [] #this will divide link name and /
a = [] #this will store the link names only

for i in x:
    _x = i.split('://')
    if _x[0] != 'http':
        if len(_x) > 1:
            y.append(_x[1])

print("this is y")
print(y)

for i in y:
    _y = i.split('/')
    z.append(_y)


print('this is z')
print(z)
print(z[0][1])

for i in z:
    a.append(i[0])

final_string = list(dict.fromkeys(a))
print(final_string)
# print('this is a')
# print(a)