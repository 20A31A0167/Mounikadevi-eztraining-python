q1="""who is the present president of india?
a.Droupadi murmu
b.Narendra modi
C.Jagdeep dhankhar
d.jagdish mukhi"""
q2="""how many states in india?
a.28
b.29
c.26
d.22"""
q3="""who is father of science?
a.albert einstein
b.galileo
c.herodotus
d.panini"""
q4="""who is the winner of bigboss 4?
a.abhijeeth
b.akhil
c.harika
d.arayana"""
q5="""what is the famous food in hyderabad?
a.biriyani
b.idly
c.puri
d.orange"""

questions={q1:"a",q2:"a",q3:"b",q4:"a",q5:"a"}
name = input("hi whats ur name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this questions(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow!you got one point")
        score=score+1
        print("your current score is",score)
    else:
        print("wrong answer,you lost 1 point")
        score=-1
        print("your current score:",score)
    flag2=input("do u want to quit?(yes/no)")
    if flag2=="yes":
        break
print("your total score:",score)
