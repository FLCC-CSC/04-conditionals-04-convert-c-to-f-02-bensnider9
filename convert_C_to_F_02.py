# FILE NAME - convert_C_to_F_02.py

# NAME: Ben Snider
# DATE: October 1, 2025
# BRIEF DESCRIPTION: Convert C to F 2 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print('===== Temperature Converter =====')
print('')
print('  1. Convert from Celsius to Fahrenheit')
print('  2. Convert from Fahrenheit to Celsius')
print('')
answer = int(input('Please choose from the above menu:'))
num = float(input('Enter a temperature to convert:'))
temp_f = num * 9/5 + 32
temp_c = (num - 32) * 5/9
if answer == (1):
    print('')
    print(f'{num} degrees Celsius is {temp_f:.1f} degrees Fahrenheit.')
else:
    print('')
    print(f'{num} degrees Fahrenheit is {temp_c:.1f} degrees Celsius')








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
I suppose it would be more like relearn how to format the equation for converting F to C.
I only say that because it took me a little bit to go back through the notebook to find where it was mentioned.





'''
