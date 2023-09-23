
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e: 
        print("error in divide function",e)
        raise e


try:
    a=int(input("enetr number"))
    b=int(input("enetr number"))
    #print(d["x"])
    c=divide(a,b)
    print(c)
    print("error occured")
    print("in outer try block")
except (ValueError,ZeroDivisionError) as e:
    print("error occured pls enter number")
    print(e)
except KeyError:
    print("key not found")
except Exception as e:
    print("error occured",e)
finally:
    print("in finally block")


try:
    #error
    try:
        #error2
    except:
except:
