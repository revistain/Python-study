# # match, swtich of python
# def foo(num):
#     # num에 튜플 같은 자료형도 들어올 수 있음
#     match num:
#         case 0:
#             print("case 0")
#         case 1:
#             print("case 1")

# # 기본값은 오직 한번
# def f(a, L = []):
#     L.append(a)
#     return L
#     # L은 호출때마다 추가됨(static)

# # else if
# def f1(a, L=None):
#     if(L is None):
#         L = []
#     L.append(a)
#     return L

# # 매개인자 호출
# def create_marine(damage = 10, state='isAlive', action='ignore', type='normal'):
#     pass

# create_marine(30, state='isDead') # 1 positional Argument, 1 keyword Argument
# # create_marine(damage = 20, isDead) # Wrong Sequence

# def shuttle(*arguments, **keywords):
#     #*arguments는 가변인자를 받음
#     #**keywords는 딕셔너리를 받음
#     for arg in arguments:
#         print("currently "+ arg +" is in the shuttle");
#     for kw in keywords:
#         print(kw + ': ' + keywords[kw])
# shuttle('marine', 'dragon', 'ghost', health="100", armor="3", rank='lieutaent')

# # lambda
# def test_lambda():
#     pairs = [(1, "one"), (2, "two")]
#     pairs.sort(key = lambda a, b : a+b)

# # annotation
# def foo(ham : str, eggs: str = 'eggs') ->str:
#     return ham + ' and ' + eggs

# # 예외처리
# def foo():
#     while True:
#         try:
#             x = int(input("please input a number"))
#             break
#         except ValueError:
#             print("Value ERROR LOL!")
# foo()

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment: ", spam)
#     do_nonlocal()
#     print("After nonlocal assignment: ", spam)
#     do_global()
#     print("After global assignment: ", spam)

# scope_test()
# print("In global scope : ", spam)

# class Dog:
#         age = 1
#         list = [] # this is static
#     def __init__(self, age):
#         self.age = age
#         self.list = [] # this is correct
#     def add_list(self, arg):
#         self.list.append(arg)

# a = Dog(3)
# b = Dog(5)
# print(a.age)
# b.add_list("walk")
# print(a.list)