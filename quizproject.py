#pyton code for icons
#question icon="\u2753" , correct icon="\u2705" , wrong icon="\u274C" , score icon="\U0001F3C6"
#start icon="\U0001F3C1" , person="\U0001F464"



def choose():
    score=0
    print("\t----------------------------------------------------------------------------")
    print("\t\t\t****your choise is choose mode****")
    print("\t----------------------------------------------------------------------------\n")
    print("1.How do you declare a variable in JavaScript")
    question=input("\na.Var \nb.Let \nc.Const \nd.All the above \nEnter your choice:").lower()
    if question.lower()=="d":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    print("2.A syntax Erroe is?")
    question=input("a.An erroe you will never find \nb.An error you find at the end when the program gives out a wrong value due to logic error. \nc.An error caused by languagae rules being broken. \nd.An error due to user error. \nEnter your choise:")
    if question.lower()=="c":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    print("3.Which data structure uses LIFO?")
    question=input("a.Array \nb.Int \nc.Stack \nd.Queues \nEnter your choise:")
    if question.lower()=="c":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    print("4.Which of the following HTML elements is used to create a hyperlink?")
    question=input("a.<div? \nb.<p> \nc.<a> \nd.<img> \nEnter your choise:")
    if question.lower()=="c":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    print("5.what does css stands for?")
    question=input("a.creative style sheets \nb.cascading style sheet \nc.computer style sheet \nd.colorful style sheet \nEnter your choise:")
    if question.lower()=="b":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    print("7.What is the output of the following python code?")
    print("(3**2)")
    question=input("a.5 \nb.6 \nc.8 \nd.9 \nEnter your choise:")
    if question.lower()=="c":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    print("8.Which of the follwing is not vaild variable name in python?")
    question=input("a.my_var \nb._myvar \nc.my-var \nd.myvar1 \nEnter your choise:")
    if question.lower()=="c":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    
    
    print(f"congratulations {name} your score is:"+ str(score)) 
    
        


def fillups():
    score=0
    print("\t----------------------------------------------------------------------------")
    print("\t\t\t****your choise is fill in the blanks mode****")
    print("\t----------------------------------------------------------------------------\n")
    question1=input("1.how do you write a command line in python:").lower()
    if question1=="#":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")

    question1=input("2.What is the fullform of LIFO in DSA:").lower()
    if question1.lower()=="lastinfirstout":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("3.Who introduced c?").lower()
    if question1.lower()=="dennis ritchie":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("4.In which year c was introduced?").lower()
    if question1.lower()=="1972":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("5.What command do you use to output data to the screen in c?").lower()
    if question1.lower()=="Cout<<":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("6.Entering comments is a useless task, it will not help in any way.say true or false?").lower()
    if question1.lower()=="false":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("7.Whaat is FIFO?").lower()
    if question1.lower()=="firstinfirstout":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("8.A memory location that holds a single letter or number is called?").lower()
    if question1.lower()=="char":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("9.A do-while and a while loop are the same. State true or flase?").lower()
    if question1.lower()=="false":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    question1=input("10.one loop inside the body of another loop is called?").lower()
    if question1.lower()=="Nested":
        print("correct \u2705")
        score+=1
    else:
        print("wrong \u274C")
    
    print(f"congratulations {name} your score is:"+ str(score)) 
        
        



print("\t\t\t****welcome to Genius Minds****")
player=input("do you want to play\u2753 yes/no:").lower()
if player != "yes":
    quit()
else:
    name=input("enter your name \U0001F464 :")

score=0

print("\t----------------------------------------------------------------------------")
print(f"\t\t\t****Welcome{name} \U0001F464****")
print("\t\t\t****ok lets play,All the best \U0001F44D***")
print("\t----------------------------------------------------------------------------\n")
p=input("choose your option of playing mode\u2753 fillups/choose \nEnter your choice:")
if p=="fillups":
     fillups()
else:
     choose()
