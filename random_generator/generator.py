from importlib.metadata import distribution
import numpy as np
import os
os.chdir("./random_generator")

class Random_No:

    def output_to_file(self, filename, arr):
        with open(f"{filename}.csv", 'w') as f:
            for i in range(len(arr)):
                if (arr[i]>0):
                    f.write(f'{int(arr[i])}\n')
                else: 
                    f.write(f'{abs(int(arr[i]))}\n') 
        

    def gettriangular(self, left, mode, right, size):
        arr= np.random.triangular(left, mode, right, size)
        self.output_to_file("Triangular", arr)

    def getnormal(self, loc=0.0, scale=1.0, size=None):
        arr= np.random.normal(loc, scale, size)
        self.output_to_file("Normal", arr)

    def getlognormal(self, mean=0.0, sigma=1.0, size=None):
        arr= list(map(float,(np.random.lognormal(mean, sigma, size))))
        self.output_to_file("LogNormal", arr)

    def getuniform(self, low=0.0, high=1.0, size=None):
        arr = np.random.uniform(low, high, size)
        self.output_to_file("Uniform", arr)

    def getexponential(self, scale=1.0, size=None):
        arr= np.random.exponential(scale, size)
        self.output_to_file("Exponential", arr)
   

if __name__=="__main__":
    R = Random_No()
    R.gettriangular(1, 50, 100, 300)
    R.getexponential(100, 300)
    R.getlognormal(1, 10, 300)
    R.getnormal(1, 100, 300)
    R.getuniform(1,100,300)
    print("Files are created")
