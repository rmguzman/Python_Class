# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Variable 
Residuo_4 = year % 4
Residuo_100 = year % 100
Residuo_400 = year % 400

if Residuo_4 == 0 :
  if Residuo_100 > 0 :
    print("Leap year.")
  elif Residuo_400 == 0:
    print("Leap year.")
  else:
   print("Not leap year.")
else:
  print("Not leap year.")

