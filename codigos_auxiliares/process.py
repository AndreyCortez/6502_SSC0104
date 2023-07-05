from PIL import Image
import numpy as np

im = Image.open('codigos_auxiliares/icmclogo.gif')
#im.show()
im = im.resize([32,32])

I = np.asarray(im)

x = 512

f = open("codigos_auxiliares/output.txt", "a")

for i in range(32):
    for j in range(32):
        if I[i][j] < 10:
            f.write(f"LDA #{0}\n")
        else:
            f.write(f"LDA #{255}\n")
        f.write(f"STA {x}\n")
        x += 1


f.close()

print(I)