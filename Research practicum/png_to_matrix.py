import imageio
from PIL import Image
import numpy as np
import math as m

# Dit zet de foto om naar een grayscale matrix

im = imageio.imread("0.1.jpg" )

#print im.shape


# Hier probeer ik een plaatje van een normale verdeling te genereren om de normale verdeling fit functie te kunnen testen. 

def Norm(x,y,S_x,S_y,M_x,M_y):
    return 255 * m.exp( - ((x - M_x) ** 2)/(S_x) - ((y - M_y) ** 2)/(S_y))

normaldist = []
for i in range(256):
    normaldist.append([])
    for j in range(256):
        normaldist[i].append([])




for i in range(256):
    
    for j in range(256):
        
        normaldist[i][j] = Norm(j,i,20,20,20,20)
        
#print normaldist

#print max(normaldist)

#fromarray heeft een nparray nodig
normarray  = np.asarray(normaldist)

# Het gaat tot hier goed, maar fromarray leest het niet helemaal goed

foto = Image.fromarray(normarray,'L')
foto.show()

