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

# # ----------------------------
# # -- Loop => While Training --
# # ----------------------------
# # While Condition_Is_true
# # Code Will Run Until Condition Become false
# # ----------------------------

# myf = ["os", "ah", "ga", "al", "ra", "ta", "ma", "mo", "wa", "af"]

# print(len(myf)) # List Length

# a = 0

# while a < len(myf) : # a < 10

#     print(f"#{str(a + 1).zfill(2)} {myf[a]}")

#     a += 1 # a = a + 1

# else :
#     print("All Friends Are Printed.")

# print(myf[0])
# print(myf[1])
# print(myf[2])
# print(myf[3])
# print(myf[4])
# print(myf[5])
# print(myf[6])
# print(myf[7])
# print(myf[8])
# print(myf[9])

# ############################################################

# # ----------------------------
# # -- Loop => While Training --
# # -- Simple Bookmark Manage --
# # ----------------------------

# # Empty List To Fill Later
# myfavouritewebs = []

# # Maximum Allowed Websites
# maximum = 5

# while maximum > 0 : 
#     # Input The New Website
#     web = input("Website Name Without https:// ")

#     # Add The New Website To The List
#     myfavouritewebs.append(f"https://{web.strip().lower()}")

#     # Decrease One Number From Allowed Websites
#     maximum -= 1

#     # Print The Add Massage
#     print(f"Website Added, {maximum} Places Left.")

#     # Print The List
#     print(myfavouritewebs)

# else :
#     print("Bookmark Is Full, You Can't Add More.")

# # Check If List Is Not Emty
# if len(myfavouritewebs) > 0 :
#     # Sort The List
#     myfavouritewebs.sort()

#     index = 0

#     print("Printing The List Of Websites In Your Bookmark")

#     while index < len(myfavouritewebs)
        
#         print(myfavouritewebs[index])

#         index += 1

# ############################################################

# # ----------------------------
# # -- Loop => While Training --
# # -- Simple Password Guess --
# # ----------------------------

# tries = 5

# mainpassword = "ahmednanno2510"

# inputpassword = input("Write Your Password: ").strip().lower()

# while inputpassword != mainpassword : 
   
#     tries -= 1

#     print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

#     inputpassword = input("Write Your Password: ").strip().lower()
#     if tries == 0 : 
    
#         print("All Tries Is Finished.")

#         break

#         print("Will Not Printing")

# else :
#     print("Correct Password.")

# ############################################################

# # -----------------
# # -- Loop => For --
# # -----------------
# # For Item In Iterable_Object :
# #   Do Something With Item
# # -----------------------------
# # Item Is A Vairable You Create And Call Whenever You Want
# # Item Refer To The Current Position And Will Run And Visit All Items To The End
# # Iterable_Object => Sequence [ list, tuples, set, dict, string of charcters, etc ...]
# # ------------------------------------------------------------------------------------

# mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in mynumbers : 
    
    # print(number * 15)

#     if number % 2 == 0 : # Even

#         print(f"The Number {number} Is Even.")

#     else : 
        
#         print(f"The Number {number} Is Odd.")

# else : 
#     print("The Loop Is Finished.")

# myname = "Ahmed"

# for letter in myname : 
#     print(f" [ {letter.upper()} ] ")

# ############################################################

# # -----------------
# # -- Loop => For --
# # --  Trainings  --
# # -----------------

# # Range

# myrange = range(1, 101)

# for number in myrange : 
   
#     print(str(number).zfill(3))


# # Dictionary

# myskills = {
#     "Html" : "90%",
#     "Css" : "60%",
#     "Php" : "80%",
#     "Js" : "50%",
#     "Python" : "100%",
# }


# # The Same One

# print(myskills["Js"])
# print(myskills.get("Python"))


# for skill in myskills :
   
    # print(skill)


    # # The Same One

    # print(f"My Progress In Lang {skill} Is: {myskills.get(skill)}")
    # print(f"My Progress In Lang {skill} Is: {myskills[skill]}")

# ############################################################

# # -----------------
# # -- Loop => For --
# # -- Nested Loop --
# # -----------------

# peoples = {
#     "Osama" : {
#         "Html" : "70%",
#         "Css" : "80%",
#         "Js" : "60%",
#     },
#     "Ahmed" : {
#         "Html" : "90%",
#         "Css" : "40%",
#         "Js" : "70%",
#     },
#     "Sayed" : {
#         "Html" : "10%",
#         "Css" : "20%",
#         "Js" : "30%",
#     },
# }

# for name in peoples : 
#     print(f"Skills And Progress For {name} Is: ")

#     for skill in peoples[name] : 
#         print(f"{skill.upper()} => {peoples[name][skill]}")

# ############################################################

# # ---------------------------
# # -- Break, Continue, Pass --
# # ---------------------------

# mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Continue

# for number in mynumbers : 
#     if number == 7 : 

#         continue
    
#     print(number)

# print("#" * 50)


# # Break

# for number in mynumbers : 
    
#     if number == 7 : 
    
#         break
    
#     print(number)


# print("#" * 50)


# # Pass

# for number in mynumbers : 
#     if number == 7 : 

#         pass
    
#     print(number)


# print("#" * 50)


# ############################################################

# # ------------------------------
# # -- Advanced Dictionary Loop --
# # ------------------------------

# myskills = {
#     "Html" : "80%",
#     "Css" : "50%",
#     "Js" : "60%",
# }

# for skill_key, skill_progress in myskills.items() : 
#     print(f"{skill_key} => {skill_progress}")


# print("#" * 50)


# peoples = {
#     "Osama" : {
#         "Html" : "70%",
#         "Css" : "80%",
#         "Js" : "60%",
#     },
#     "Ahmed" : {
#         "Html" : "90%",
#         "Css" : "40%",
#         "Js" : "70%",
#     },
#     "Sayed" : {
#         "Html" : "10%",
#         "Css" : "20%",
#         "Js" : "30%",
#     },
# }

# for name, lang in peoples.items() : 

#     print(f"{name} Lang & Prog Is: ")
    
#     for lang2, progress in lang.items() :

#         print(f"- {lang2} => {progress}")

# ############################################################

# # -------------------------
# # -- Function And Return --
# # -------------------------
# # [1] A Function Is A Reusable Block Of Code A Task.
# # [2] A Function Run When You Call It.
# # [3] A Function Accept Element To Deal With Called [Parameters].
# # [4] A Function Can Do The Task Without Returning Data.
# # [5] A Function Can Return Data After Job Is Finished.
# # [6] A Function Create To Prevent DRY.
# # [7] A Function Accept Elements When You Call It Called [Arguments].
# # [8] There's A Built-In Functions And User Defined Functions.
# # [9] A Function Is For All Team And All Apps.
# # -------------------------------------------------------------

# def function_name() : 
    
#     print("Hello Python From Inside Function.")

#     return "Hello Python From Inside Function."

# function_name()


# print("#" * 50)


# # ---------------------------------------
# # -- Function Parameters And Arguments --
# # ---------------------------------------

# # def                     => Function Keyword [Define]
# # say_hello()             => Function Name
# # name                    => Parameter
# # print(f"Hello {name})   => Task
# # say_hello("Ahmed")      => Ahmed Is The Argument

# def say_hello(name) : 

#     print(f"Hello {name}")

# say_hello("Ahmed")


# print("#" * 50)


# def addition(n1, n2) :

#     if type(n1) != int or type(n2) != int : 
        
#         print("Only Integers Allowed")

#     else : 

#         print(n1 + n2)

# addition(100, 300)


# print("#" * 50)


# def full_name(f, m, l) :
    
#     print(f"Hello {f.strip().capitalize()} {m.upper():.1s} {l.capitalize()}")

# full_name("Ahmed", "Fawzy", "Fouad")

# ############################################################

