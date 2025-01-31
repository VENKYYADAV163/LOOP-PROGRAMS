# s=input('enter a string')
# s1='aeiouAEIOU'
# c=0
# for i in s
#     if i in s1:
#         c+=1
# print(c)

# a='venky'
# c=0
# for i in a:
#     if i not in 'aeiouAEIOU':
#         c+=1
# print(c)


# s=input('enter a string')
# count=0
# for i in s:
#     if i in '02468':
#         count+=1
# print(count)


# n=int(input("enter a number"))
# if n%2==0:
#     print('n is even')
# else:
#     print('n is odd')


        
# s=(input('enter a value:'))
00000# if s==s[::-1]:
#     print('s is palindrome')
# else:
#     print('s is not a palindrome')


# s=input('enter a value:')
# s1=input('enter a s1 value')
# if sorted(s)==sorted(s1):
#     print('s is anagram')
# else:
#     print('s is not a anagram')



# s=input('enter a string')
# c=0
# for i in s:
#     if  i.isalnum():
#         c+=1
# print(c)



# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)``





# n=44
# s=0
# while n>0:
#     rem=n%10
#     n//=10
#     s+=rem
# if s%2==0:
#     print(f'{s} even no')
# else:
#     print(f'{s} sumofdigit is odd')



# n=int(input("enter a number"))
# l=len(str(n))
# summ=0
# dummy=n
# while dummy>0:
#     rem=dummy%10
#     dummy//=10
#     summ+=rem**l
# if summ==n:
#     print('n is a armstrong no')
# else:
#     print("n is not armstrong no")





# n=int(input("enter a number"))
# l=len(str(n))
# summ=0
# dummy=n
# while dummy>0:
#     rem=dummy%10
#     dummy//=10
#     summ+=rem**l
#     l-=1
# if summ==n:
#     print('n is a disaruim no')
# else:
#     print("n is not disaruim no")



# n=int(input("enter a number"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#         print('n is prime')
# else:
#         print("n is not prime")





# n=int(input("enter a number"))
# fact=1
# for i in range (1,n+1):
#         fact*=i
# print(fact)
    


# s="venky"
# for ip in range(len(s)):
#     if ip%2==0:
#        print(s[ip])



# # Function to check if the number is a palindrome
# def is_palindrome(num):
#     # Convert the number to a string to easily reverse it
#     num_str = str(num)
    
#     # Check if the number is equal to its reverse
    # if num_str == num_str[::-1]:
    #     return True
    # else:
    #     return False

# # Input from the user
# number = int(input("Enter a number: "))

# # Check if the number is a palindrome and print the result
# if is_palindrome(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")


# # Function to check if the number is a palindrome using loops
# def is_palindrome(num):
#     original_num = num
#     reversed_num = 0

#     # Reverse the number using a loop
#     while num > 0:
#         digit = num % 10  # Extract the last digit
#         reversed_num = reversed_num * 10 + digit  # Build the reversed number
#         num = num // 10  # Remove the last digit from num

#     # Check if the original number is equal to the reversed number
#     if original_num == reversed_num:
#         return True
#     else:
#         return False

# # Input from the user
# number = int(input("Enter a number: "))

# # Check if the number is a palindrome and print the result
# if is_palindrome(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")




 
# for i in range(5):
#     for j in range(i):
#         print('*',end=' ')
#     print()



# n=5
# for i in range(n):
#     for j in range(n-i):
#         print('*',end=' ')
#     print()



# num=5
# count=0
# for i in range(num):
#     for j in range(i+1):
#         count=count+1
#         print(count,end=' ')
#     print()



# for i in range(1,6):
#  for j in range(1,i+1):
#     print(j, end=" ")
#  print('')

# n=int(input()) # input = 10
# count=0
# for i in range(n):
#     for j in range(i+1):
#         count=count+1
#         print(count,end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     num=i
#     for j in range(1,num+1):
#         print(j,end=' ')
#         num+=1
#     print()



# n=5
# for i in range(1,n+1):
#     dummy=1
#     for j in range(1,n+1):
#         print(chr(64+dummy),end=' ')
#         dummy+=1
#     print()




# n=5
# spaces=n
# num=1
# for i in range(1,n+1):
#     for j in range(1,spaces+1):
#         print(' ',end=' ')
#     for k in range(1,num+1):
#         print(k,end=' ')
#     print()
#     spaces-=1
#     num+=1


# n=5
# num=1
# space=n
# for i in range(1,n+1):
#     for j in range(1,space+1):
#         print(' ',end=' ')
#     for k in range(1,num+i):
#         print(num,end=' ')
#     print()
#     space-=1



# n=int(input())
# dummy=1
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print(chr(64+dummy),end=' ')
#     dummy+=1
#     print()




# d="venky"
# # print(d[0:2],d[-2:])



# def string_ex(string):
#     if len(string)<2:
#         return ''
#     return string[0:2] +string[-2:]
# print(string_ex('venky'))
    

# def add_ex(element):
#     sum_number=0
#     for i in element:
#          sum_number+=i
#     return sum_number
# print(add_ex([1,2,3]))



# a=int(input("enter a number"))
# b=int(input("enter a number"))
# print((a-b))

a=int(input("enter a number"))
if a%2==0:
    print("a is even")
else:
    print("a is odd")