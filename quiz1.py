#1_________________________________
def hypotenuse(x, y, z): #the hypotenuse is the longest side
  max = x
  if y > max:
    max = y
  if z > max:
    max = z
  return max
hypotenuse(4, 5, 3)

#2_________________________________
def calendarName(n):
  if n < 0 or n > 11: #Validating the month number
    return "Invalid"
  months = {0 : "January", 
            1 : "February",
            2 : "March",
            3 : "April",
            4 : "May",
            5 : "June",
            6 : "July",
            7 : "August",
            8 : "September",
            9 : "October",
            10: "November",
            11: "December"}
  return months[n]
calendarName(10)

#3_________________________________
def turn_clockwise(p):
  points = ["N", "E", "S", "W"]
  for i in range(0, len(points)):
    if points[i] == p:
      if i == len(points)-1:  #if last element
        return points[0]
      return points[i + 1]
  return "Invalid"
turn_clockwise("W")

#4_________________________________
def hours_in(s): #seconds to hour
  print("Hours: " + str(round(s/3600)))
  minutes_in(s%3600)
def minutes_in(s): #seconds to minute
  print("Minutes: " + str(round(s/60)))
  seconds_in(s%60)
def seconds_in(s): #rest of seconds
  print("Seconds: " + str(s))
seconds = 293845
hours_in(seconds)

#5_________________________________
def f2c(t):
  return round((t - 32)/1.8)
f2c(32)  #OUTPUT 0
f2c(45) 

#6_________________________________
def count(subS, s):
  c = 0
  for i in range(0, len(s)):
    if s[i:i+len(subS):1] == subS:  #getting the subString with the same len as subS
      c += 1
  return c
count("is", "Mississippi") #2
count("an", "banana")      #2
count("nanan", "banana")   #0
count("aaa", "aaaaaa")     #4

#7_________________________________
def remove(subS, s):
  for i in range(0, len(s)):
    if s[i:i+len(subS):1] == subS: #if substring in string
      return s[0:i:1] + s[i+len(subS)::1] #concatenate before and after the substring
  return s
remove("an", "banana")        #'bana'
remove("iss", "Mississippi")  #'Missippi'
remove("eggs", "bicycle")     #'bicycle'

#8_________________________________
def isPalindrome(s):
  s = s.lower() #non-case sensitive
  return s == s[::-1] #cloning the string reversed and comparing
isPalindrome("Magic")    #false
isPalindrome("Madam")    #true
isPalindrome("racecaR")  #true
