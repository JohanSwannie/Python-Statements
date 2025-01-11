

# * ######################################################################################
# *                                                                                      #
# *                    SOME OF THE FOLLOWING EXCEPTIONS MAY OCCUR                        #
# *                                                                                      #
# * 1) FileNotFoundError: Happens when you try to open or access a file that does        # 
# *    not exist.                                                                        #
# * 2) ValueError: Happens when you pass an argument of the correct type but with an     # 
# *    invalid value.                                                                    #
# * 3) ZeroDivisionError: This occurs when you try to divide a number by zero.           #
# * 4) NameError: This is raised when you try to use a variable or function that         # 
# *    hasn’t been defined.                                                              #
# * 5) TypeError: This one occurs when you pass an argument of the wrong data type.      #         
# * 6) ImportError: Raised when you try to import a module or package that doesn’t       # 
# *    exist or can’t be found.                                                          # 
# * 7) OverflowError: This error is raised when a calculation result is too large        # 
# *    to be represented.                                                                #         
# * 8) FloatingPointError: This one is raised when a floating point operation fails.     #         
# * 9) IndexError: Happens when you try to access an index that is out of the range      # 
# *    of a sequence.                                                                    #         
# * 10) KeyError: Occurs when you try to access a key that does not exist in a           # 
# *     dictionary.                                                                      #         
# * 11) EOFError: Raised when Python encounters the End Of File (EOF) while reading      # 
# *     input, usually from a read() call.                                               #                                                                                     #
# * 12) ArithmeticError: A superclass for arithmetic exceptions, such as                 # 
# *     ZeroDivisionError, OverflowError, and FloatingPointError.                        #
# *                                                                                      #
# * ######################################################################################

# * Always catch out the very first error in the try block by the except error block

# * TRY - EXCEPT - IF - FINALLY -- EXAMPLE 1

def tryThem1(num, bType):
    try:
        num / 0
        if oType == 'int':
            print('Hallo', oType)
    except ZeroDivisionError:
        print("Division by Zero is not allowed")
    except NameError:
        print("You try to use a variable or function that hasn't been defined")
    else:
        print('All okay')
    finally:
        print('All done')
        
num = 17
bType = "int"

tryThem1(num, bType)
    
# * TRY - EXCEPT - IF - FINALLY -- EXAMPLE 2

def tryThem2(dict):
    try:
        print(dict["salary"])
    except KeyError:
        print("You are using the wrong key for the particulary dictionary")
    else:
        print("There is no error here")
    finally:
        print("Try - Except block completed")

dict1 = {"name": "Luke", "surname": "Brown", "age": 44}

tryThem2(dict1)

# * TRY - EXCEPT - IF - FINALLY -- EXAMPLE 3

def tryThem3():
    try:
        newNumber = int('Here we go')
    except ValueError:
        print("You can NOT convert this particular string into an INTEGER")
    else:
        print("All went well")
    finally:
        print('End of Try Block reached')
        
tryThem3()