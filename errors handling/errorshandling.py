def test():
    try:
        f = open("testfile", "r") #"r" mode will produce an OSError
        f.write("add line to test file")

    except OSError:
        print("There is an OSError")

    except:
        print("Damm there is an error")

    finally:
        print("I always run!")


def ask_for_int():    
    while True:
        
        try:
            result = int(input("please enter a number: "))
        
        except:
            print("woops! it's not a number")
            continue

        else:
            print("thank you")
            break

        finally:
            print("I allways run no matter what")

ask_for_int()