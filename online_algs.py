import math
import random as rand

class OnlineStats:
    def __init__(self):
        self.counts = 0
        self.mean = 0
        self.m2 = 0
        self.sd = 0
        self.var = 0
        self.total = 0
    
    #update stat for each new sample
    def update(self, sample):
        self.total += sample
        self.counts += 1
        delta = sample - self.mean
        self.mean = self.mean + delta/self.counts
        self.m2 = self.m2 + delta*(sample - self.mean)  #this line is due to Knuth book
        if (self.counts >= 2):
            self.sd = math.sqrt(self.m2/(self.counts - 1))       #sample sd
            self.var = math.sqrt(self.m2/self.counts)       #population variance

def main(n):
    stats = OnlineStats()
    samples = []
    for inx in xrange(n):
        sample = rand.random()
        samples.append(sample)
        stats.update(sample)
    print stats.mean
    print stats.sd
    print samples

if __name__ == '__main__':
    n = 10
    main(n)
