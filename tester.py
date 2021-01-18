import random

class Tester:
    def __init__(self, learn):  #Initialization
        self.space = learn.space
        self.trajectories = learn.trajectories
        self.patient = learn.patient
        self.healthy = learn.health
        self.newHealthy = []
        self.newPatient = []
        self.people = []
        self.unknown = learn.unknown
        self.hygiene = learn.hygiene
        self.timeSetter = learn.timeSetter
        self.socialDis = 0.1
        self.otherParameters = 0.1
        self.test()
        
    def test(self): #THE PREDICTOR SYSTEM FOR FINDING THE POSSIBILITY OF GETTING THE DISEASE FOR EACH PERSON
        self.people = self.unknown
        self.numberOfTest = len(self.people)
        
        for index in range(self.numberOfTest):
            person = random.choice(self.people)
            t = 0
            day = 0
            p = 1
            totalSP = 1
            
            for place in self.trajectories[person]:
                if t == self.timeSetter:
                    totalSP *= p    #probability of being healthy until today

                    totalP = 1-totalSP
                    day += 1
                    t = 0
                    p = 1
                    
                if day == 4:
                    break
                    
                else:
                    temp = self.PPPD(person, day, place, t) #probability of getting patient in a place in a day
                    p *= (1-temp)   #probability of being health in a day until now
                t += 1
                
            if totalP < 0.5:
                self.newHealthy.append(person)
            else:
                self.newPatient.append(person)
            
            print("person", person)
            print("hygiene:", self.hygiene[person])
            print("probability of patient:", totalP, "\n")
            
        if self.people == self.healthy:
            print("accuracy:", len(self.newHealthy)/len(self.healthy))
        elif self.people == self.patient:
            print("accuracy:", len(self.newPatient)/len(self.patient))
                
    def PPPD(self, traj, day, place, t): #probability of patient in a place in a day
        return (1-self.hygiene[traj])*self.space[day][t][place]*self.socialDis*self.otherParameters
