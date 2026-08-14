# 1. Write a program to find the greatest of four numbers entered by the user.
# nums = [34,54,2,66,88,99]
# res = max(nums)
# print(res)

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# marks = []
# for i in range(1,4):
#     mark = int(input(f"Enter the marks of {i} sunjects : "))
#     marks.append(mark)

# # checking total of 40% and at least 33% in each subject to pass
# total = sum(marks) 
# percentage = (total/300) * 100
# print(f"Percentage : {percentage:.2f}%")
# if percentage <= 40 or any(x <35 for x in marks):
#     print("You are fail")
# else: 
#     print("You are pass")



# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# spam = ["Make a lot of money","buy now","subscribe this","click this"]
# user = input("Enter the message : ")
# if any(phrase in user for phrase in spam):
#     print("Spam detected")
# else:
#     print("comment is correct")




# 4. Write a program to find whether a given username contains less than 10 characters or not.
# username = input(f"Enter the username : ")
# print(len(username))
# if len(username) < 10:
#     print("Username is correct")
# else:
#     print("Username is exceeded more than 10 latters") 

# 5. Write a program which finds out whether a given name is present in a list or not.
# list = ["amit"," ","vivek"]
# name = "prabhat"
# if name in list:
#     print("Yes present ")
# else:
#     print("Not found")

# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

# marks_student = {}
# marks = []
# subjects = ["English","Maths","Physics","Biology"]
# for i in subjects:
#     subject_marks = int(input(f"Enter the marks for each subject {i} : "))
#     marks_student[i] = subject_marks
#     marks.append(subject_marks)

# total_marks = sum(marks)
# percentage = total_marks/400 * 100
# if 90 <= percentage <= 100:
#     grade = "Ex"
# elif 80 <= percentage <= 90:
#     grade = "A"
# elif 70 <= percentage < 80:
#     grade = "B"
# elif 60 <= percentage < 70:
#     grade = "C"
# elif 50 <= percentage < 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Percentage: {percentage:.2f}%, Grade: {grade}")




# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter your post text: ")

# 2. Check for the word "harry" in lowercase
if "harry" in post.lower():
    print("Yes! This post is talking about Harry.")
else:
    print("No, this post does not mention Harry.")
