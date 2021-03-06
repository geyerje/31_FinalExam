"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.  May 2018.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# TODO: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    piggy = Pig(10)
    pog = Pig(70000)
    pag = Pig(100)
    print(piggy.get_weight())
    piggy.eat(10)
    print(piggy.get_weight())
    piggy.eat_for_a_year()
    print(piggy.weight)
    print(piggy.heavier_pig(pog).weight)
    print(piggy.heavier_pig(pag).weight)
    print(piggy.new_pig(pog).weight)



    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------


class Pig(object):
    def __init__(self, weight):
        self.weight = weight

        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # Done: Implement and test this method.

    def get_weight(self):
        return self.weight
        """ Returns this Pig's weight. """
        # Done: Implement and test this method.

    def eat(self, pounds_of_slop):
        self.weight += pounds_of_slop
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # Done: Implement and test this method.

    def eat_for_a_year(self):
        for k in range(365):
            self.eat(k+1)
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # Done: Implement and test this method.

    def heavier_pig(self, other_pig):
        if self.weight > other_pig.weight:
            return self
        else:
            return other_pig
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # Done: Implement and test this method.

    def new_pig(self, other_pig):
        newpiggy = Pig(self.heavier_pig(other_pig).weight)
        return newpiggy
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # Done: Implement and test this method.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
