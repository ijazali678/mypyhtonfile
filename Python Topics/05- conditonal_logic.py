## conditional logical or opperators are either true or flase or yes or no or 0 or 1

#equal to                   ==
#nor equal to               !=
#less then                  <
#greater then               >
#less then and equal to     <=
#greater than and equal to  >=

#is 4 equal to 4?
print(4==5)
print(4!=5)
print(4>3)
print(4<2)
print(3<=3)
print(5>=4)


#application of logical opperators
ijaz_age = 4
age_at_school= 5
print(ijaz_age==age_at_school)

#another way of writing this with input function
age_at_school= 5
ijaz_age = input("how old is ijaz? ") #input value is string you have to change at to numerical value
ijaz_age=int(ijaz_age)
print(type(ijaz_age))
print(ijaz_age>=age_at_school)

calories_in_1_gram = 4
find = input("how many gram are there in ")
find = int(find)


print(calories_in_1_gram * find)
