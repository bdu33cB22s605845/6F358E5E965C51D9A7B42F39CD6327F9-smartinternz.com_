#implement a class called player that represent a cricket match player.The player class should have a method called play()which prints "the player is playing cricket  Derive two classes, Batsman and Bowler,from the player class.Override the play()method in each derived class to print "The Batsman is batting"and "The bowler is bowling" respectively.Write a program to crash objects of both the Batsman and bowler classes and call the play()method for each object.

class Player:
    def play(self):
        print ("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print ("The Batsman is batting.")

class Bowler(Player):
     def play(self):
         print("The bowler is Bowling.")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()