class Gopi:
    g=[[100,"IndiGo",3500,"Trichy","Bangalore"],
       [200,"Deccan Airlines",5000,"Chennai","Delhi"],
       [300,"Air India",4500,"Hydrabad","Tricy"],
       [400,"Air Asia",2500,"Coimbatore","Mumbai"],
       [500,"Vistara",8000,"Pune","Pondichery"]]
    s={}
    pid=1

def passenger():
    global passname,passpwd,epid,f,tottic,i,pid
    while True:
          b=int(input("\t1.Signup:\n\t2.Signin:\n\t3.Exit:\n\nPress The Number:"))
          if b==1:
              passname=input("\tEnter your name \U0001F464:")
              passage=int(input("\t Enter your age:"))
              if (passage>=18):
                  passpwd=int(input("\tEnter your password \U0001F512:"))
                  Gopi.s[Gopi.pid]=[Gopi.pid,passname,passpwd,0,"nil",0,0,"nil","nil","yet to book"]
                  print("Your Id is \U0001F194:",Gopi.pid)
                  print("\t\t\t ****Your id is created successfully \U0001F44D****")
                  Gopi.pid+=1
              else:
                  print("Oops \U0001F641! ",passname," you are not eligible for applying")
                  print("Thanks for showing Intrest \U0001F64F")
                  break
          elif b==2:
              try:
                  print("\t\t\t ****Hi",passname,"****")
                  print("\t\t\t ****Welcome Back \U0001F600***")
                  epid=int(input("Enter your Id \U0001F194:"))
              except:
                print("Your Passenger Id Incorrect,please try again")
                try:
                    epid=int(input("Enter Your Id \U0001F194:"))
                except:
                    print("You have tryed for many time!!!...")
                    break
              if epid<1 or epid>=Gopi.pid:
                        print("your Id is Incorrect",passname,"please check it")
                        break
              else:
                  epwd=int(input("Enter your password \U0001F512:"))
                  if epwd==Gopi.s[epid][2]:
                      while True:
                           c=int(input("\t1.Check Availabiligt & Fare\n \t2.Book tickets \U0001F39F\U0000FE0F\n \t3.View\n \t4.Exit\n\n Enter the number:"))
                           print("\t\t\t***************✈✈✈***************\n")
                           if c==1:
                               print("\t\t\t\t****✈✈The avilable flights are✈✈****\n")
                               for i in Gopi.g:
                                   print(*i,sep=",")
                               print("\n\t\t\t***************✈✈✈***************\n")
                           elif c==2:
                               try:
                                   f=int(input("Enter the flight id ✈:"))
                               except:
                                   print("Oops \U0001F641! flight id is missing")
                                   break
                               for i in range(len(Gopi.g)):
                                   if f==Gopi.g[i][0]:
                                       tottic=int(input("enter the total number of tickets \U0001F39F\U0000FE0F \n"))
                                       Gopi.s[epid][3]=f
                                       Gopi.s[epid][4]=Gopi.g[i][1]
                                       Gopi.s[epid][5]=tottic
                                       Gopi.s[epid][6]=tottic*int(Gopi.g[i][2])
                                       Gopi.s[epid][7]=Gopi.g[i][3]
                                       Gopi.s[epid][8]=Gopi.g[i][4]
                                       Gopi.s[epid][9]="Hi "+passname+" your ticket is in pending list"
                                       print("Total price is",Gopi.s[epid][6])
                                       print("your Request are summitted successfully\n")
                                       break
                               else:
                                    print("Check the flight Id✈")
                           elif c==3:
                                #print("Passenger id\tpassenger name\tpassenger pass\tflight id\tflight name\tno.of tickets\ttotal fare\t takeoff\tlanding\tstatus\n")
                                #for i in Gopi.g:
                                   # print(Gopi.g[i],sep="\t")
                                   
                                print("Your id:,\tYour name :\tYour pwd:\tflight id:\tfllight name:\tno.of tickets \U0001F39F\U0000FE0F:\ttotal fare:\t Depature from:\tArrival to:\tstatus:\n")
                                print("\t\t\t***************✈✈***************\n\n")
                                for i in Gopi.s:
                                    print(*Gopi.s[i],sep="\t")
                                print("\t\t\t***************✈✈***************\n\n")
                           #else:
                               #break
                           elif c==4:
                               break
                  else:
                      print("Invalid password \U0001F512!")
          elif b==3:
              break


print("\t\t\t ****✈Welcome to FlyHigh Flight Reservation Booking Platform ✈****")
while True:
    a=int(input('1.passenger:\n2.Cashier:\n3.Exit:\n\nPress The Number:'))
    if a==1:
        passenger()
    elif a==2:
        while True:
            cashier=int(input("\t1.login password \U0001F512\n \t2.View\n \t3.Approve\n \t4.Cancel\n  \t5.Report\n \t6.Exit\n \tEnter the number:"))
            cmcpwd=1000
            if cashier==1:
                cname=input("Enter your name \U0001F464:")
                cpwd=int(input("Enter password \U0001F512 :"))
                if cmcpwd==cpwd:
                    print("\t\t\t ****hello cashier",cname,"\U0001F464****")
                else:
                    print("password \U0001F512 is wrong please check it")
            elif cashier==2:
                 #print("\t\t\t***************✈✈***************\n\n")
                 print("passanger id \U0001F464:\tpassanger name \U0001F464:\tpassanger pass:\tflight id ✈:\tfllight name ✈:\tno.of tickets \U0001F39F\U0000FE0F:\ttotal fare:\t Depature from:\tArrival to:\tstatus:\n")
                 print("\t\t\t\t***************✈✈***************\n\n")
                 for i in Gopi.s:
                    print(*Gopi.s[i],sep="\t")
                    print("\t\t\t\t***************✈✈***************\n\n")
            elif cashier == 3:
                d = int(input("\t1.Approve using Id\n \t2.Approve All\n \t3.Exit\n\nEnter the Number:"))
                if d == 1:
                    try:
                        epid = int(input("Enter Passenger Id \U0001F194 :"))
                        if epid < 1 or epid >= Gopi.pid:
                            print("Invalid Id")
                            break
                        else:
                            for i in Gopi.s:
                                if epid == i and Gopi.s[i][9].endswith("pending list"):
                                    Gopi.s[i][9] = "approved"
                                    print("Ticket approved for:", Gopi.s[epid][1], epid)
                                    break
                            else:
                                print("\t\t\t****No pending ticket available for:", Gopi.s[epid][1], epid,"****\n")
                    except:
                        print("Check the passenger Id")
                        break
                elif d == 2:
                    for i in Gopi.s:
                        if Gopi.s[i][9].endswith("pending list"):
                            Gopi.s[i][9] = "approved"
                    print("\t\t\t****All pending tickets \U0001F39F\U0000FE0F are approved****\n")
                elif d==3:
                    break
            elif cashier==4:
                for i in Gopi.s: 
                    if Gopi.s[i][9].endswith("pending list"):
                        Gopi.s[i][9]="cancel"
                        print("\t\t\t****all the pending tickets \U0001F39F\U0000FE0F are cancelled****\n")
                        break
                else:
                    print("No pending ticket are avaible\n")
                    break
            elif cashier==5:
                m=open("pass.txt","a")
                m.write(str(Gopi.s))
                print("\n")
                m.close()
                print("\t\t\t*****Report generated successfully! \U0001F44D****\n")
                break
            #else:
                #print("Some thing went wrong ,please check it")
                
            elif cashier==6:
                break
                
                    
                    
    elif a==3:
        p=input("Are you sure do you want to Exit? Yes/No:").lower()
        if p=="yes":
            print("\t\t\t ****✈✈Thanks For Visiting FlyHigh Flight Reservation Booking Platform✈✈****")
            print("\t\t\t\t ***************\U0001F64F***************")
            break
            
 
