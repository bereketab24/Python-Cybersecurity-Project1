#This is a function that checks the strength of a Password given.
def check_password_strength(password):
    minimum_length = 8
    requirements_met = False

#Using "While loop" to ask the user to enter the password until he get it right.
    while not requirements_met:
        if len(password) < minimum_length:
            print( f"Your password has to be at least {minimum_length} characters.")
            requirements_met = False
        
        
        else:
            '''Using "any" function and list comprehension: "any" fun returns True value 
            if it finds even one true value in an itreable argument.
            And list comprehension is efficient way of using for loop.
            The following code checks if those four characters are found in the password.''' 
            upper_case = any(char.isupper() for char in password)
            lower_case = any(char.islower() for char in password)
            digits = any(char.isdigit() for char in password)
            special_characters = any( char in " ! @ # $ % ^ & * (  ) _ + - = [ ]}  {  ' | / ? . , " for char in password)

            '''The following code adds the truth values of the characters found in the password 
            and if the passowrd doesn't have all the characters, 
            it returns the missing types of character using list append method.'''  
            character_type_requirement = sum([upper_case, lower_case, digits, special_characters])
            if character_type_requirement < 4 :
                missing_character = []
                if not upper_case:
                    missing_character.append("Upper Case")
                if not lower_case:
                    missing_character.append("Lower Case")
                if not digits:
                    missing_character.append("Numerical Digits")
                if not special_characters:
                    missing_character.append("Special Characters")

                print( f"Your password misses the following characters: \n {", ".join(missing_character)}" )
            else:
                requirements_met = True
                print("Congrats! You have a strong password")
        if not requirements_met:
            password = input("Please Enter a stronger password: ")  

              
    

password = input("Enter your password: ")
check_password_strength(password)

