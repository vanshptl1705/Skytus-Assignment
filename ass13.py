# Quiz Game:

que = ["(1) In which year did Rohit score his first ODI double century?",
       "(2) Against which team did Virat Kohli score his first ODI century?",
       "(3) Who was the first batsman to score a double century in ODI cricket?",
       "(4) Which Indian bowler took 10 wickets in a Test match at Lord's in 2021?",
       "(5) Who was the first Indian batsman to score a century in all three formats of international cricket?",
       "(6) Who holds the record for the highest individual score in ODI cricket?"]

opt = ["(a) 2012 (b) 2013 (c) 2014 (d) 2015",
       "(a) Sri Lanka (b) Australia (c) West Indies (d) Bangladesh",
       "(a) Virender Sehwag (b) Sachin Tendulkar (c) Rohit Sharma (d) Chris Gayle",
       "(a) Jasprit Bumrah (b) Mohammed Siraj (c) Ravichandran Ashwin (d) Mohammed Shami",
       "(a) Virat Kohli (b) Rohit Sharma (c) Suresh Raina (d) KL Rahul",
       "(a) Martin Guptill (b) Rohit Sharma (c) Virender Sehwag (d) Chris Gayle"]

ans = ["b",
       "a",
       "b",
       "d",
       "c",
       "b",]

cans = ["(b) 2013",
        "(a) Sri Lanka",
        "(b) Sachin Tendulkar",
        "(d) Mohammed Shami",
        "(c) Suresh Raina",
        "(b) Rohit Sharma",]

score = 0

for q in range(len(que)):
    print(que[q])
    print(opt[q], "\n")
    
    u_ans = input("Enter your answer:")
    
    if u_ans.lower() == (ans[q]):
        print("\n","> Your answer is Correct", "\n")
        score += 1
    else:
        print("\n","> Sorry you guess the wrong answer")
        print(" > Correct answer is", cans[q], "\n")
    
if score > 3:
       print("Congratulation you guess", score, "correct answer out of 6 in Quiz-Game.", "\n")
else:
       print("Sorry you guess only", score, "correct answer out of 6 in Quiz-Game.", "\n")

# Simple E-commerce cart system

product = {
       "Laptop":80000,
       "Ipad":20000,
       "Iphone":60000,
       "Headphone":2000,
       "Keyboard":1500,
}

cart = {}

while True:
       
       def main():
              print("\n""---------------------------")
              print("  E-COMMERCE CART SYSTEM")
              print("---------------------------""\n")
              print("1. View Products")
              print("2. Add to Cart")
              print("3. View Cart")
              print("4. Remove from Cart")
              print("5. Checkout""\n")

       main()
       act = int(input("Please enter your choice:"))

       def act1():
              print("---------------------------")
              print("    Available products")
              print("---------------------------")
              
              for items,price in product.items():
                     print(items, "Rs.",price)

       def act2():
              print("---------------------------")
              print("    Available products") 
              print("---------------------------")
              
              # For Product
              for items,price in product.items():  
                     print(items, "Rs.",price)
              
              i1 = input("\n""Enter needed product:").capitalize()
              
              # For Quantity
              
              if i1 in product:
                     i2 = int(input("Enter how many products you needed:"))
                     
                     if i1 in cart:
                            cart[i1] += i2
                     else:
                            cart[i1] = i2
                     
                     print(i2 , i1 , "Added to cart.")
              else:
                     print("Product not founded!!!")  
       
       def act3():
              print("---------------------------")
              print("         Your Cart")
              print("---------------------------")
              
              if len(cart) == 0:
                     print("Your cart is empty")    
                     
              else:
                     for items,quantity in cart.items():
                            price = product[items]
                            cost = quantity * price
                            print("\n",items, "x",quantity, "=",cost)
                            
       def act4():
              print("---------------------------")
              print("         Your Cart")
              print("---------------------------")
              
              if len(cart) == 0:
                     print("Your cart is empty")
              
              else:
                     for items,quantity in cart.items():
                            price = product[items]
                            cost = quantity * price
                            print("\n",items, "x",quantity, "=",cost,"\n")
                     
                     r1 = input("Enter product you want to remove:").capitalize()
                     r2 = int(input("\nEnter how many product you want to remove:\n"))
                     
                     if r1 in cart:
                            if r2 <= cart[r1]:
                                   cart[r1] = cart[r1] - r2
                                   
                                   price = product[r1]
                                   cost = cart[r1] *price
                                   
                                   print(r2,r1, "is removed from the cart")
                                   print(r1, "x", cart[r1], "=", cost)
                            
                            else:
                                   print("You don't have that much quantity in your cart")
                     
                     else:
                            print(r1, "product is not founded in cart")
       
       def act5():
              print("---------------------------")
              print("          Checkout")
              print("---------------------------")

              if len(cart) == 0:
                     print("Your cart is empty")
              
              else:
                     total_bill = 0
                     
                     for items,quantity in cart.items():
                            price = product[items]
                            cost = quantity * price
                            print("\n",items, "x",quantity, "=",cost,"\n")
                            total_bill = total_bill + cost
                             
                     print("---------------------------")
                     print("Total Rs:",total_bill)
       
       if act == 1:
              act1()
                                
       elif act == 2:
              act2()

       elif act == 3:
              act3()
       
       elif act == 4:
              act4()
       
       elif act == 5:
              act5()
              break

# To-do-list

task = []

while True:
       def main():
              print("\n""---------------------------")
              print("        To-Do List")
              print("---------------------------""\n")
              print("1. Add Task")
              print("2. View Task")
              print("3. Edit Task")
              print("4. Delete Task")
              print("5. Exit")

       main()
       user = int(input("Please enter your choice:"))

       def act1():
              print("\n--------Add Task--------\n")
       
       
              l1 = int(input("how many task you needed to add:\n"))
       
              for a in range(l1):
                     t1 = input("Please enter Task here:")
                     task.append(t1)

       def act2():
              print("\n--------View Task--------\n")
              
              for i in task:
                     print(i)
       
       def act3():
              print("\n--------Edit Task--------\n")
              
              e1 = input("Which task you want to change:")
              
              if e1 in task:
                     task.remove(e1)
                     print("Task:",e1,"\n")
                     e2 = input("Change task here:")  
                     task.append(e2)
                     print(e2,"Task Successfully changed!!!")  
              else:
                     print(e1, "Task Doesn't Exist")
       
       def act4():
              print("\n--------Delete Task--------\n")
              
              d1 = input("Which task you want to delete:")
              
              if d1 in task:
                     task.remove(d1)
                     print(d1, "Task deleted sucessfully!")
              else:
                     print(d1, "Task Doesn't Exist")
                     
       if user == 1:
              act1()
       
       if user == 2:
              act2()

       if user == 3:
              act3()
       
       if user == 4:
              act4()
       
       if user == 5:
              break