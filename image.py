#coded BY abdeslam_karjout
from PIL import Image
import os
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i= Image.open(f)
        fn, fext= os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))        
print("done ^_^")
