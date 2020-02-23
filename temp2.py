from temp import *
video = {'uri': [9, '2020-1-28', '2020-2-15'], 'don': [10, '2020-2-28', '2020-5-28']}
obj=VideoStore(video)
class execute(VideoStore):

    while (True):
        print("MAIN MENU")
        print("===========")
        print("1. Add Video  :")
        print("2. Checkout Video  :")
        print("3. Return Video  :")
        print("4. Receive Rating  :")
        print("5. List Inventory  :")
        print("6. Exit  :")
        val = input("Enter your choice(1..6) : ")
        if (val == '1'):
            obj.addvideo()
        elif (val == '2'):
            obj.checkoutvideo()
        elif (val == '3'):
            obj.returnvideo()
        elif (val == '4'):
            obj.addrating()

        elif (val == '5'):
            obj.inventorylist()

        elif (val == '6'):
            exit()
        else:
            print("invalid input")
