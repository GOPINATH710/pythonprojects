class Gopi:
    g=[[100,"IndiGo",3500,"Trichy","Bangalore"],
       [200,"Deccan Airlines",5000,"Chennai","Delhi"],
       [300,"Air India",4500,"Hydrabad","Tricy"],
       [400,"Air Asia",2500,"Coimbatore","Mumbai"],
       [500,"Vistara",8000,"Pune","Pondichery"]]
    #s={}
    pid=1

def passenger():
    global passname,passpwd,epid,f,tottic,i,pid
    #s=[]
    while True:
          b=int(input("\t1.Signup:\n\t2.Signin:\n\t3.Exit:\n\nPress The Number:"))
          if b==1:
              passname=input("\tEnter your name \U0001F9D1:")
              passage=int(input("\t Enter your age:"))
              if (passage>=18):
                  passpwd=int(input("\tEnter your password \U0001F9D1:"))
                  Gopi.s=Gopi.pid,passname,passpwd,0,"nil",0,0,"nil","nil","yet to book"
                  #Gopi.s=Gopi.pid,passname,passpwd,f,Gopi.g[i][1],tottic,tottic*Gopi.g[i][2],Gopi.g[i][3],Gopi.g[i][4]
                  print("Your Id is:",Gopi.pid)
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
                  epid=int(input("Enter your Id:"))
              except:
                print("Your Passenger Id Incorrect,please try again")
                try:
                    epid=int(input("Enter Your Id:"))
                except:
                    print("You have tryed for many time!!!...")
                    break
              if epid<1 or epid>=Gopi.pid:
                        print("your Id is Incorrect",passname,"please check it")
                        break
              else:
                  epwd=int(input("Enter your password:"))
                  if epwd==passpwd:
                      while True:
                           c=int(input("\t1.Check Availabiligt & Fare\n \t2.Book tickets\n \t3.View\n \t4.Exit\n\n Enter the number:"))
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
                               for i in range(len(Gopi.g)):
                                   if f==Gopi.g[i][0]:
                                        #Gopi.s=Gopi.pid,passname,passpwd,0,"nil",0,0,"nil","nil","yet to book"
                                       #s.append(Gopi.pid,passname,passpwd,f,Gopi.g[i][1],tottic,tottic*Gopi.g[i][2],Gopi.g[i][3],Gopi.g[i][4])
                                       tottic=int(input("enter the total number of tickets\n"))
                                       print("\n\tflight id is ✈:",f)
                                       print("\n\tName of flight is:",Gopi.g[i][1])
                                       print("\n\tTotal ticket you have booked:",tottic)
                                       print("\n\tTotal price is:",tottic*Gopi.g[i][2])
                                       print("\n\tDepature from:",Gopi.g[i][3])
                                       print("\n\tArrival to:",Gopi.g[i][4])
                                       print("\n\tHi",passname,"you are in the waiting list\n")
                                       break
                               else:
                                    print("Check the flight Id")
                           elif c==3:
                                #print("Passenger id\tpassenger name\tpassenger pass\tflight id\tflight name\tno.of tickets\ttotal fare\t takeoff\tlanding\tstatus\n")
                                #for i in Gopi.g:
                                   # print(Gopi.g[i],sep="\t")
                                       iid=int(input("Enter your passanger Id:"))
                                       if (iid==epid):
                                               print("\n\tYour passsanger Id is:",epid)
                                               print("\n\tYour Name is:",passname)
                                               print("\n\tYour Password  is:",passpwd)
                                               print("\n\tYour flight Id is ✈:",f)
                                               print("\n\tName of flight is:",Gopi.g[i][1])
                                               print("\n\tTotal ticket you have booked:",tottic)
                                               print("\n\tTotal price is:",tottic*Gopi.g[i][2])
                                               print("\n\tFrom Location is:",Gopi.g[i][3])
                                               print("\n\tTo Location is:",Gopi.g[i][4])
                                               print("\n\tHi",passname,"your ticket is in pending list")
                                               print("\n\t**********************\n")
                                       else:
                                           print("check Your Id")
                                           #break
                           #else:
                              # break
                           elif c==4:
                                   break
          else:
              break                        
                                       
                               


print("\t\t\t ****✈Welcome to FlyHigh Flight Reservation Booking Platform ✈****")
while True:
    a=int(input('1.passenger:\n2.Cashier:\n3.Exit:\n\nPress The Number:'))
    if a==1:
        passenger()
    elif a==2:
        while True:
            cashier=int(input("\t1.login password\n \t2.View\n \t3.Approve\n \t4.Cancel\n  \t5.Report\n \t6.Exit\n \tEnter the number:"))
            cmcpwd=1000
            if cashier==1:
                cname=input("Enter your name \U0001F9D1:")
                cpwd=int(input("Enter password :"))
                if cmcpwd==cpwd:
                    print("\t\t\t ****hello cashier",cname,"****")
                else:
                    print("password is wrong please check it")
            elif cashier==2:
                iid=int(input("Enter your passanger Id:"))
                if iid==epid:
                        print("\n\tYour passsanger Id is:",epid)
                        print("\n\tYour Name is:",passname)
                        print("\n\tYour Password  is:",passpwd)
                        print("\n\tYour flight Id is ✈:",f)
                        print("\n\tName of flight is:",Gopi.g[i][1])
                        print("\n\tTotal ticket you have booked:",tottic)
                        print("\n\tTotal price is:",tottic*Gopi.g[i][2])
                        print("\n\tFrom Location is:",Gopi.g[i][3])
                        print("\n\tTo Location is:",Gopi.g[i][4])
                        print("\n\tHi",passname,"'s ticket is in pending list")
                        print("\n\t**********************\n")
                else:
                    print("passanger Id is wrong,please check it")
            elif cashier==3:
                d=int(input("\t1.Approve using Id\n  \t2.Approve All\n \t3.Exit\n\n Enter the Number:"))
                if d==1:
                    epid=int(input("Enter Passanger Id:"))
                    print("\n\tHi",passname,"'s ticket is Approved")
                    #try:
                       # epid=int(input("Enter Passanger Id:"))
                       # print("\n\tHi",passname,"'s ticket is Approved")
                    #except:
                       # print("No Pending ticket avilable")
                       # try:
                         #   epid=int(input("Enter Passanger Id:"))
                         #   print("\n\tHi",passname,"'s ticket is Approved")
                        #except:
                          #  print("you have tried many times")
                else:
                    break
                            
                    
                    
    elif a==3:
        p=input("Are you sure do you want to Exit Yes/No:")
        if p!="yes":
            print("\t\t\t ****✈✈Thanks For Visiting FlyHigh Flight Reservation Booking Platform✈✈****")
            print("\t\t\t\t ***************\U0001F64F***************")
            break
            
 
