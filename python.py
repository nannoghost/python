# # This Is First Comment
# print ("Hello Ahmed")

# help("keywords")
# ############################################################
# msg = "I Love"
# lang = "Python"
# print(msg + " " + lang)

# full = msg + " " + lang
# print(full)

# ############################################################

# # format in version 3.6+ 

# MyName = "Ahmed Fawzy"
# MyAge= "23"

# print("My Name Is : {MyName}, And My Age Is : {MyAge}") # This Is Wrong
# print(f"My Name Is : {MyName}, And My Age Is : {MyAge}") # This Is Right

# ############################################################

# # append()

# myfriends = ["Ahmed", "Fawzy", "Sayed"]
# myoldfriends = ["Mohamed", "Youssef", "Hassan"]
# myfriends.append("Alaa")
# myfriends.append(100)
# myfriends.append(150.200)
# myfriends.append(True)
# myfriends.append(myoldfriends)

# print(myfriends)
# print(myfriends[2])
# print(myfriends[6])
# print(myfriends[7][1]) # To Print One Index

# # extend()

# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# a.extend(b)
# print(a)

# # remove()

# a = [1, 2, 3, 4]
# a.remove(1)
# print(a)

# # sort() => int Or str Not All 

# y = [1, 2, 100, 110, -1, 29]
# y.sort(reverse=False) # This Is By Default
# y.sort(reverse=True) # This Is By Order
# print(y)

# # reverse()

# z = [1, 2, 100, 110, -1, 29]
# z.reverse()
# print(z)

# # clear()
# c = [1, 2, 3, 4, 5, 6]
# c.clear()
# print(c)

# n = [1, 2, 3, 4, 5, 6]
# l = n.copy()
# print(n)
# print(l)

# n.append(11)

# print(n)
# print(l)

# # count()
# g = [1, 2, 3, 4, 5, 6]
# print(g.count(3))

# # index()

# print(myfriends.index("Fawzy"))

# # insert()
# r = [1, 2, 3, 5, 4, "A", "B"]
# r.insert(0, "C")
# print(r)

# # pop()
# h = [1, 2, 3, 4, 5, 6, 7]
# print(h.pop(-1))

# ############################################################

# # -------------------------------------------------------------
# # -- Tuple --
# # -----------
# # [1] Tuple Items Are Enclosed In Parentheses.
# # [2] You Can Remove The Parentheses If You Want.
# # [3] Tuple Are Inmutable => You Can't Add Or Delete.
# # [4] Tuple Are Ordered, To Use Index To Access Item.
# # [5] Tuple Items Is Not Unique.
# # [6] Tuple Can Have Different Data Types.
# # [7] Operators Used In Strings And Lists Available Int Tuples.
# # -------------------------------------------------------------

# MyAwesomeTupleOne = ("Ahmed", "Fawzy")
# MyAwesomeTupleTwo = "Mohamed", "Mahmoud"

# print(MyAwesomeTupleOne)
# print(MyAwesomeTupleTwo)

# # Tuple Destruct

# a = ("A", "B", "C")

# x, y, z = "A", "B", "C"
# x, y, z = a

# print(x, y, z)

# a = ("A", "B", 4, "C")
# x, y, _, z = a

# print(x, y, z)

# ############################################################

# # -------------------------------------------------------------
# # -- Set --
# # ---------
# # [1] Set Items Are Enclosed In Curly Braces.
# # [2] Set Items Are Not Ordered And Not Indexed.
# # [3] Set Indexing And Slicing Can't Be Done.
# # [4] Set Has Only Inmutable Data Types (Numbers, Strings, Tuples) List And Dict Are Not.
# # [5] Set Items Is Unique.
# # -------------------------------------------------------------

# # union()

# a = {"A", "B", "C"}
# c = {"q", "d", "w"}
# x = {"zero", "cool"}

# print(a | c)
# print(a.union(c, x))

# # add()

# d = {"A", "B", "C"}
# d.add("r")
# d.add("h")

# print(d)

# # update()

# j = {1, 2, 3, 4}
# k = {5, 6, 7, 8}
# j.update(["Html", "Css"])
# j.update(k)

# print(j)

# ############################################################

# # -------------------------------------------------------------
# # -- Dectionary --
# # -----------
# # [1] Dict Items Are Enclosed In Curly Braces.
# # [2] Dict Items Are Contatins Key : Value
# # [3] Dict Key Need To Be Inmutable => (Number, String, Tuple) List Not Allowed.
# # [4] Dict Value Can Have Any Data Types.
# # [5] Dict Key Need To Be Unique.
# # [6] Dict Is Not Ordered You Access Its Element With Key.
# # -------------------------------------------------------------

# user = {
#     "Name" : "Ahmed",
#     "Age" : 23,
#     "Country" : "Egypt"
# }

# print(user)

# # These Are The Same One.

# print(user["Country"])
# print(user.get("Country"))

# print(user.keys())
# print(user.values())

# # Tow-Dimensional Dictionary

# languages = {
#     "One" : {
#         "Name" : "Html",
#         "Progress" : "80%"
#     },
#     "Two" : {
#         "Name" : "Css",
#         "Progress" : "70%"
#     },
#     "Three" : {
#             "Name" : "Js",
#             "Progress" : "60%"
#     }  
# }

# print(languages)
# print(languages["One"])
# print(languages["One"]["Name"])

# AllDict = {
#     "One" : user,
#     "Two" : languages
# }
# print(AllDict)

# # To Add Items.

# AllDict ["Skills"] = "Fighting"
# AllDict.update({"Skills2" : "Writing"})

# print(AllDict)

# ############################################################

# # -------------------------------------------------------------------------------
# # -------------
# # -- Boolean --
# # -------------
# # [1] In Programming You Need To Known Your If Your Code Output Is True Or False.
# # [2] Boolean Values Are The Two Constant Objects False + True.
# # -------------------------------------------------------------------------------

# # -----------------------
# # -----------------------
# # -- Boolean Operators --
# # -----------------------
# # and
# # or
# # not
# # -----------------------

# age = 23
# country = "Egypt"
# rank = 10 

# print(age > 18 and country == "Egypt" and rank > 5) # True
# print(age > 18 and country == "Egypt" and rank > 10) # False

# print(age > 18 or country == "Egypt" or rank > 5) # True
# print(not age > 18) # False

# ############################################################

# # --------------------------
# # --------------------------
# # -- Assignment Operators --
# # --------------------------
# # =
# # +=
# # -=
# # *=
# # /=
# # **=
# # %=
# # //=
# # --------------------------

# # Var One = Self [Operator] Var Two
# # Var One [Operator]= Var Two

# x = 10
# y = 20

# x += y
# print(x)

# # ----------------------------
# # ----------------------------
# # --- Comparison Operators ---
# # ----------------------------
# # [ == ] Equal
# # [ != ] Not Equal
# # [ > ] Greater Than
# # [ < ] Less Than
# # [ >= ] Greater Than Or Equal
# # [ <= ] Less Than Or Equal
# # ----------------------------

# ############################################################

# # ----------------
# # -- User Input --
# # ----------------

# # What\'s Your => "\" To Skip ("'").
# fName = input('What\'s Your First Name?')
# mName = input('What\'s Your Middle Name?')
# lName = input('What\'s Your Last Name?')

# # ".strip" To Ignore Space Between Texts.
# # ".capitalize" To Make The First Letter Capital.
# # ".1s" To Make Only The First Letter Is Printed.

# fName = fName.strip().capitalize()
# mName = mName.strip().capitalize()
# lName = lName.strip().capitalize()

# print(f"Hello {fName} {mName:.1s} {lName} Good To See You.")

# ############################################################

# # ---------------------------
# # -- Practical Slice Email --
# # ---------------------------

# thename = input("What's Your Name ?").strip().capitalize()
# theemail = input("What's Your Email ?").strip()

# # [:theemail.index("@")] => To Start From 0 To End

# theusername = theemail[:theemail.index("@")].strip()

# # theemail.index("@") + 1 : => To Start After "@" To End

# thewebsite = theemail[theemail.index("@") + 1 :].strip()

# print(f"Hello {thename}, Your Email Is {theemail} \nYour Username Is {theusername}, And Your Website Is {thewebsite}")

# ############################################################

# # -------------------------------------
# # -- Practical Your Age Full Details --
# # -------------------------------------

# # Input Age 

# Age = int(input('What\'s Your Age ?').strip())

# # Get Age In All Time Units

# Months = Age * 12
# Weeks = Months * 4
# Days = Age * 365
# Hours = Days *24
# Minutes = Hours * 60
# Seconds = Minutes *60

# print("You Lived For:")
# print(f"{Months} Months.\n{Weeks:,} Weeks.\n{Days:,} Days.\n{Minutes:,} Minutes.\n{Seconds:,} Seconds.")

# ############################################################

# # --------------------
# # --  Control Flow  --
# # -- If, Elif, Else --
# # -- Make Decisions --
# # --------------------

# uname = str(input("What's Your Name ?").strip().capitalize())
# ucountry = str(input("What's Your Country ?").strip().capitalize())
# cname = "Python Course"
# cprice = int(100)

# if ucountry == "Egypt":

#     print(f"Hello {uname} Because You Are From {ucountry}")
#     print(f"The Course \"{cname}\" Price Is: ${cprice - 50}")

# elif ucountry == "KSA" or "ksa":

#     print(f"Hello {uname} Because You From {ucountry}")
#     print(f"The Course \"{cname}\" Price Is: ${cprice - 30}")

# else:

#     print(f"Hello {uname} Because You From {ucountry}")
#     print(f"The Course \"{cname}\" Price Is: ${cprice}")

# # ---------------
# # -- Nested If --
# # ---------------

# uname = str(input("What's Your Name ?").strip().capitalize())
# ucountry = str(input("What's Your Country ?").strip().capitalize())
# if ucountry == "Egypt" or ucountry == "KSA" : student = str(input("Are You Student ?").strip().capitalize())
# cname = "Python Course"
# cprice = int(100)

# if ucountry == "Egypt" or ucountry == "KSA" :
    
#     if student == "Yes" :
#         print(f"Hello {uname} Because You Are From {ucountry} And You're Student")
#         print(f"The Course \"{cname}\" Price Is: ${cprice - 70}")

#     else :
#         print(f"Hello {uname} Because You Are From {ucountry} And You're Not Student")
#         print(f"The Course \"{cname}\" Price Is: ${cprice - 50}")

# else:

#     print(f"Hello {uname} Because You From {ucountry}")
#     print(f"The Course \"{cname}\" Price Is: ${cprice}")

# # Short If 

# movierate = 18
# age = int(input("What's Your Age ?").strip())

# print("Movie Is Not Good For You." if age < movierate else "Movie Is Good For You Happy Watching.")

# ############################################################

# # -------------------------------------------------
# # -- Calcutate Age Advanced Version And Training --
# # -------------------------------------------------

# # Write A Very Beautiful Note
# print("#" * 80)
# print("You Can Write The First Letter Or Full Name Of The Time Unit".center(80, '#'))
# print("#" * 80)

# # Collect Age Data
# age = input("Please Write Your Age ").strip()

# # Collect Time Unit Data
# unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# # Get Time Units

# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365

# if unit == 'months' or unit == 'm':

#     print("You Choosed The Unit Months ")
#     print(f"You Lived For {months:,} Months.")

# elif unit == 'weeks' or unit == 'w':

#     print("You Choosed The Unit Weeks ")
#     print(f"You Lived For {weeks:,} Weeks.")

# elif unit == 'days' or unit == 'd':

#     print("You Choosed The Unit Days ")
#     print(f"You Lived For {days:,} Days.")

# ############################################################

# # --------------------------
# # -- Membership Operators --
# # --------------------------
# # -------
# # in 
# # not in 
# # -------

# # List

# friends = ["Ahmed", "Sayed", "Mahmoud"]
# print("Osama" in friends)

# # Using In And Not In With Condition 

# countriesone = ["Egypt", "KSA", "Kuwait", "Bahrain"]
# countriesonediscount = 80

# countriestwo = ["Italy", "USA"]
# countriestwodiscount = 50

# mycountry = input("Please Write Your Country: ").strip().capitalize()

# if mycountry in countriesone :
    
#     print(f"Hello You Have A Discount Equal To ${countriesonediscount}")

# elif mycountry in countriestwo :
    
#     print(f"Hello You Have A Discount Equal To ${countriestwodiscount}")

# else : 

#     print("You Have No Discount")

# ############################################################

# # ----------------------------------
# # -- Practical Membership Control --
# # ----------------------------------

# # List Contains Admins
# admins = ["Ahmed", "Mohamed", "Mahmoud", "Youssef"]

# # Login
# name = input("Please Type Your Name: ").strip().capitalize()

# # If Name Is In Admins
# if name in admins : 
#     print(f"Hello {name} You Are Admin")
#     option = input("Delete Or Update Your Name ? ").strip().capitalize()
    
#     # Update Option
#     if option == "Update" :
#         newname = input("Type Your New Name Please: ").strip().capitalize()
#         admins[admins.index(name)] = newname
#         print("Name Updated.")
#         print(admins)

#     # Delete Option
#     elif option == "Delete" :
#         print("Name Deleted.")
#         print(admins)

#     # Delete Option
#     else :
#         print("Wrong Option Choosed.")

# else :
#     status = input("You Are Not Admin, Add You Y, N ? ").strip().capitalize()
    
#     if status == "Yes" or status == "Y" : 
#         print("You Have Been Added.")
#         admins.append(name)
#         print(admins)

#     else : 
#         print("You Are Not Added.")

# ############################################################

# # -------------------
# # -- Loop => While --
# # -------------------
# # -----------------------
# # while condition_is_true
# #     Code Will Run
# # -----------------------

# a = 0

# while a <= 15 : 
#     print(a)
#     a += 1 # a = a + 1 

# print(" Loop Is Done. ".center(50, "#"))

# ############################################################

