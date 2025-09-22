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
