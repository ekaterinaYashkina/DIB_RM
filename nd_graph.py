import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import csv, math


h = []
def plot():
     h.sort()
     print(h)
     hmean = np.mean(h)
     hstd = np.std(h)
     pdf = stats.norm.pdf(h, hmean, hstd)
     plt.xlabel("Average difference between DIB-RM and Reddit rating")
     plt.ylabel("Distribution")
     plt.plot(h, pdf) # including h here is crucial
     plt.show()

def read(filename):
     karma  = 0
     dib = 0
     with open(filename, 'r') as input:
          c = 0
          reader = csv.reader(input)
          for row in reader:
               if c == 0:
                    if 'author_karma' in row:
                         karma = row.index('author_karma')
                    elif 'karma' in row:
                         karma = row.index('karma')
                    dib = row.index('dib_rm')
                    print(karma, dib)
               else:
                   h.append(math.fabs(float(row[karma])-float(row[dib])))
               c+=1

def main():
     read("test_data_comments.csv")
     plot()

if __name__ == "__main__":
    main()
