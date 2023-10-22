import matplotlib.pyplot as plt
import random
import time

def make_random_image(savepath):
    """
    Function creates a list of 10 random numbers and plots it.

    This function is just intended as a helper to test if the create image idea works.    
    """
    data = [random.randint(1, 1000) for _ in range(10)]
    fig, ax = plt.subplots()
    ax.plot(data)
    ax.text(x=1, y=500, s=time.time())
    fig.savefig(savepath)

make_random_image(r"C:\Users\Benja\Code\Python\Webside - Fitness\app\static\images\test.png")