# -*- coding: utf-8 -*-
"""
Sample Stationary Bandit Skeleton.
Author: Dr. Collin F. Lynch

This code probides a basic skeleton for the 
stationary bandit code.  It should be adapted
by the students for their work.
"""


import csv, random, sys


        
    
class BanditSet(object):
    """
    This object represents a set of arms for a stationary multi-armed 
    bandit problem it will store a fixed set of arms from a set and
    will then maintain them over multiple iterations.
    """
    
    def __init__(self, DataRows, ArmNames, ExpRate,
                 DistribParam, DecayRate, RewardWeight):
        """
        This initializes the set of choices by acting as a factory
        class to create one arm instance for each of the choices.
        The names and the rows will come from the file that 
        is read in. 
        """

        # Store the Data for later use.
        self.Data = DataRows
        
        # Initialize the parameters.
        self.ExplorationRate       = ExpRate
        self.DistributionParameter = DistribParam
        self.DecayRate             = DecayRate
        self.RewardWeight          = RewardWeight

        # Store items for each of the arms.
        self.Names         = ArmNames

        

        # Calculate the starting probability and add it.
        StartProb = 1 / float(len(ArmNames))
        self.Probabilities = [StartProb for I in range(len(ArmNames))]
        # Store a list for the weights.
        self.Weights       = [StartProb for I in range(len(ArmNames))]

        # And store the Cumulative Reward
        self.CumulativeReward = 0



    def handleRows(self):
        """
        Process each of the rows and update our running reward 
        and the basic probabilies for each one.
        """
        # We initialize the cumulative
        # Reward to be 0
        self.CumulativeReward = 0

        # Now iterate over the rows and make each
        # of the choices.
        for CurrRow in self.Data:
            print(CurrRow)
            reward_arm_index = self.pickArmIndex()

            rewardValue = self.getReward(reward_arm_index,CurrRow)            
            self.updateWeight(reward_arm_index,rewardValue)
            self.updateProbability(reward_arm_index) 
            self.normalizeProbabilities(reward_arm_index,rewardValue)
            self.CumulativeReward = float(self.CumulativeReward)+float(rewardValue)
            print('choice made: ',reward_arm_index)
            print('reward from choice: ',rewardValue)
            print('cumulative reward: ',self.CumulativeReward)
            

            # Now pick one from the list of probabilities.
            # Get the reward value from the row.
            # Update the reward weight.
            # And update the probabilities.


        # Return the cumulative reward.
        return(self.CumulativeReward)
    

    def pickArmIndex(self):
        """
        Pick an index based upon the probabilities
        using the cumulative score approach based
        upon a random value.
        """
        return random.choices(range(len(self.Probabilities)), weights=self.Probabilities, k=1)[0]
        


    def getReward(self, Index,row):
        choosenArm = self.Names[Index]

        """
        Use the Armnames to get the reward for the 
        chosen arm.
        """
        return row[choosenArm]
        
    
    def updateWeight(self, Index, Reward):
        """
        Update the weight for the chosen index using 
        the parameters.
        """
        weight = float(self.DecayRate)*float(self.Weights[Index])+float(self.RewardWeight)*float(Reward)
        totalWeight = 0
        self.Weights[Index]=weight
        for currentweight in self.Weights:
            totalWeight = totalWeight+ currentweight
        names = self.Names            
        for weightIndex in range(len(self.Weights)):
            weightIndex  
            self.Weights[weightIndex] =float(self.Weights[weightIndex])/float(totalWeight)
        


    def updateProbability(self, Index):
        """
        Update the probability for the index from its weight.
        """
        probability = float(self.Weights[Index]) * float(1-float((self.ExplorationRate)))+ float(self.ExplorationRate)*float(self.DistributionParameter)
        self.Probabilities[Index]= probability
        pass


    def normalizeProbabilities(self, Index, Reward):
        """
        Normalize the probability values.
        """
        totalProbability=0
        for probability in self.Probabilities:
            totalProbability = totalProbability+ probability
        for probabilityIndex in range(len(self.Probabilities)):
            self.Probabilities[probabilityIndex] =float(self.Probabilities[probabilityIndex])/float(totalProbability)
        
        
def main():
    fileName = sys.argv[1]
    DataRows =[]
    
    # gamma    
    ExpRate= .3
    # uniform distribution parameter epsilon
    DistribParam=.1
    # decay rate beta
    DecayRate=.6
    # n
    RewardWeight=.9
    with open(fileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ArmNames = reader.fieldnames
        for row in reader:
            DataRows.append(row)


    bandits = BanditSet(DataRows, ArmNames, ExpRate,
                 DistribParam, DecayRate, RewardWeight)
    bandits.handleRows();                 
main()    