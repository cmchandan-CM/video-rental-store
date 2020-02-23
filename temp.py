from datetime import *
class VideoStore:
    def __init__(self,videok):
        self.video=videok

    def addvideo(self):
        key = input("enter movie name : ")
        j=True
        while j:
            if key in self.video.keys():
                print("already video is of this name :")
                key = input("AGAIN Enter Video Name : ")
                j = True
            else:
                j=False
        self.video[key] = [0, '', '']
        print(f"Video {key} added successfully.")
        return 0
    def checkoutvideo(self):
        print("checkout")
        ck = input("enter check out movie   :  ")
        if ck in self.video.keys():
            listd = self.video[ck][2].split('-')
            if (self.video[ck][1] == '' or self.video[ck][2] == ''):
                rdate = input("enter return date format : yyyy-mm-dd   : ")
                self.video[ck][1] = str(date.today())
                self.video[ck][2] = rdate
                print(f"video {ck} checked out successfully.")
            elif (date(int(listd[0]), int(listd[1]), int(listd[2])) < date.today()):
                rdate = input("enter return date format : yyyy-mm-dd :  ")
                self.video[ck][1] = str(date.today())
                self.video[ck][2] = rdate
                print(f"video {ck} checked out successfully.")
            else:
                print(f"this video will not checkout beacause return date is : {self.video[ck][2]}")
        else:
            print("this video is not available")
        return 0

    def returnvideo(self):
        mvn = input("enter movie name : ")
        if mvn in self.video.keys():
            self.video[mvn][2] = str(date.today())
            print("movie successful returned")
        else:
            print("video not available")
        return 0

    def inventorylist(self):
        for i in self.video.keys():
            print(f"Video Name     =  {i.upper()}")
            print(f"Rating         =  {self.video[i][0]}")
            print(f"Checkout Date  =  {self.video[i][1]}")
            print(f"Return   Date  =  {self.video[i][2]}")
            print("---------------------------------------------------------")

        return 0
    def addrating(self):
        mvn = input("enter video name : ")
        if mvn in self.video.keys():
            rat = int(input("enter the rating : "))
            while rat > 10 or rat < 0:
                rat = int(input("enter the rating : between 1 to 10 : "))
            self.video[mvn][0] = int(rat)
            print(f"Video Name     =  {mvn.upper()} || Rating         =  {self.video[mvn][0]}")
            print(f"Rating {rat} has been mapped to the video '{mvn.upper()}'")
        return 0





