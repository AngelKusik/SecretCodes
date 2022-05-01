'''
==========================================================================================

Title:    Secret Codes Application
Author:   Angelica Kusik
Date:     November 24, 2021 (Updated on December 8)
Description:
  A simple Python application that will encode or decode a message entered by the user 
  using cipher. If the message entered is in English the program will translate it to 
  Al Bhed or vice and versa.

===========================================================================================
'''
################ FUNCTIONS ###################

# The encode_the_message function will replace the English characters in the user's message for Al Bhed characters.
def encode_the_message(message_input):
    ######## Input ##########
    # The function will get the input through the message_input parameter that will get it's value from the user input
    #####Variables & Arrays declarations #########
    encrypted_message = ''
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    al_bhed = list('YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow')
    key = 1
    
    ###### Processing ######
    #The statement below create a loop that will run the processing code below the number of times determined
    # by the variable key, which in this case is equal to 1.
    for count in range(key):
        # The statement below creates a loop that will repeat until all characters in the message are checked.
        for letter_index in range(len(message_input)):
            match_found = False
            # This statement creates a second loop will repeat for every character in the alphabet.
            for alphabet_index in range(len(alphabet)):
                # This statement compares the letters in the message with the letters in the alphabet.
                # If they match the program will add the correspondent character from the Al Bhed alphabet to the encrypted_message variable.
                if message_input[letter_index] == alphabet[alphabet_index]:
                    encrypted_message += al_bhed[alphabet_index]
                    match_found = True
            #If the character in the message does not match any character in the alphabet the program will add the unmatched character from the message
            #to the encrypted_message. (It means its a space, number or punctuation)
            if not match_found:
                encrypted_message += message_input[letter_index]
        ######## Output #########
        #The return statement will assign the function the value of the variable encrypted_message containg the output.
        return encrypted_message

# The decode_the_message function will replace the Al Bhed characters in the user's message for English characters.
def decode_the_message(message_input):
    #####Variables & Arrays declarations #########
    encrypted_message = ''
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    al_bhed = list('YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow')
    key = 1
    
    ######Processing######
    #The statement below create a loop that will run the processing code below the number of times determined
    # by the variable key, which in this case is equal to 1.
    for count in range(key):
        # The statement below creates a loop that will repeat until all characters in the message are checked.
        for letter_index in range(len(message_input)):
            match_found = False
            # This statement creates a second loop will repeat for every character in the alphabet.
            for al_bhed_index in range(len(al_bhed)):
                # This statement compares the letters in the message with the letters in the alphabet.
                # If they match the program will add the correspondent character from the Al Bhed alphabet to the encrypted_message variable.
                if message_input[letter_index] == al_bhed[al_bhed_index]:
                    encrypted_message += alphabet[al_bhed_index]
                    match_found = True
            #If the character in the message does not match any character in the alphabet the program will add the unmatched character from the message
            #to the encrypted_message. (It means its a space, number or punctuation)
            if not match_found:
                encrypted_message += message_input[letter_index]
        ######## Output #########
        #The return statement will assign the function the value of the variable encrypted_message containg the output.
        return encrypted_message

############### DECLARATIONS #################
#Constants:
#The constants below represent each of the option numbers that the user can select from.
FIRST_OPTION = 1
SECOND_OPTION = 2
THIRD_OPTION = 3

#Variables:
#The flag continue_processing is used within the while loop to determine when the program must end.
continue_processing = True
input_message = '\n1) Encode text' + '\n2) Decote text' + '\n3) Exit program' + '\nPlese select an option (' + str(FIRST_OPTION) + '-' + str(THIRD_OPTION) + '): '

################# INPUT #####################
#The statement below creates a loop that will keep the program running as long as continue_processing remains = True
while continue_processing:
    #The try & except will be used to validate the option number input. An error message will be display if input can not be stored as an integer and the user will be asked to enter a new input.
    try:
        option_input = int(input(input_message))
        ################ PROCESSING ##################
        #Range validation. If the first input is not whithin the range 1-3 incluse an error message will be displayed and the user will be asked to enter a new input.
        if FIRST_OPTION <= option_input <= THIRD_OPTION:
            #If input is equal one the encode option was selected and the user will be prompt to enter the text to be encoded.
            if option_input == FIRST_OPTION:
                input_message = '\nPlease enter text to encode: '
                message_to_encode = input(input_message)
                #We store the second input (message to be encoded) in a variable and pass it to the encode_the_message function as a parameter.
                output_message = 'Encoded text: ' + encode_the_message(message_to_encode)
                ############# OUTPUT ###############
                #We print the message encoded
                print(output_message)
            elif option_input == SECOND_OPTION:
                #If input is equal otwo the decode option was selected and the user will be prompt to enter the text to be decoded.
                input_message = '\nPlease enter text to decode: '
                message_to_decode = input(input_message)
                #We store the second input (message to be decoded) in a variable and pass it to the decode_the_message function as a parameter.
                output_message = 'Decoded text: ' + decode_the_message(message_to_decode)
                ############# OUTPUT ###############
                #We print the message decoded
                print(output_message)
            #If option_input is equal 3 we end the program by setting the continue_processing to false.
            else:
                continue_processing = False
            #We set a new value to the input_message variable in case the user choose to restart the program.
            input_message = '\n1) Encode text' + '\n2) Decote text' + '\n3) Exit program' + '\nPlese select an option (' + str(FIRST_OPTION) + '-' + str(THIRD_OPTION) + '): '
        # If range validation fails we set a new value to the input message, asking the user to enter a valid answer.
        else:
            input_message = '\nPlease select a valid option between ' + str(FIRST_OPTION) + ' and ' + str(THIRD_OPTION) + ': '
    # If try & except validation fails we set a new value to the input message, asking the user to enter a valid answer.
    except:
        input_message = '\nPlease enter a numeric value between ' + str(FIRST_OPTION) + ' and ' + str(THIRD_OPTION) + ': '

    
    
    
    
    
    

    
    