import math

class Learner:
    def __init__(self, initialvalue): #initialization
        self.space = initialvalue.S
        self.trajectories = initialvalue.trajectories
        self.patient = initialvalue.patientTrajectories
        self.health = initialvalue.healthTrajectories
        self.unknown = initialvalue.unknownTrajectories
        self.hygiene = initialvalue.H
        self.timeSetter = initialvalue.timeSetter
        
        # beeing patient ratio
        self.beta = 0.8
        # social distance impact
        self.socialDis = 0.1
        
        self.learn()
        
    def learn(self):    # DETECTING THE HAZARD PLACES
        for pTraj in self.patient:  #Checking path of the patients
            t = 0
            day = 0
            for place in self.trajectories[pTraj]:
                if t == self.timeSetter:
                    day += 1
                    t = 0
                    
                else:
                    self.space[day][t][place] = self.updateProbability(pTraj, day, place, t)
                t += 1
            
        for hTraj in self.health:   #Checking path of the healty individuals
            t = 0
            day = 0
            for place in self.trajectories[hTraj]:
                if t == self.timeSetter:
                    day += 1
                    t = 0
                    
                else:
                    self.space[day][t][place] = self.updateProbability2(hTraj, day, place, t)
                    
                t += 1
        
        self.rounding()
        
    def updateProbability(self, pTraj, day, place, t):
        pusp = (1-self.hygiene[pTraj])*self.PBP(day)  #probability of unsaifty of the patient
        return 1-((1-self.space[day][t][place])*(1-pusp))
        
    def PBP(self, day): #probability of being patient in a day
        return (self.beta)**(day)
        
    def updateProbability2(self, hTraj, day, place, t):
        return (1+math.log(self.hygiene[hTraj])/8)*self.space[day][t][place]
        
    def rounding(self):
        for day in range(len(self.space)):
            for t in range(len(self.space[day])):
                for place in range(len(self.space[day][t])):
                    self.space[day][t][place] = round(self.space[day][t][place], 2)
        
