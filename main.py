import sys


# Als je terminal b
from PIL import Image





def contrast(infile,outfile,border):
    """Make an obvious contrast, where every pixel brighter than the bordervalue is made white, 
    and every darker pixel is made black."""
    im = Image.open(infile)
    pix = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if pix[x,y] > border:
                pix[x,y] = 255
            else:
                pix[x,y] = 0
    im.save(outfile)
    print('Picture {} complete!'.format(outfile))

if __name__ == "__main__":
    # greenify('groenefoto_004.jpg','groenefoto_005.jpg',640,725,190,20000000000)
    outfile = "img_out\\" + sys.argv[1].split("\\",1)[1]
    contrast(sys.argv[1],outfile,255-int(sys.argv[2]))

    """
    Stop je afbeeldingen in de \img_in\-folder, run vervolgens
        python main.py <bestandslocatie> <waarde>
    om je afbeelding te compilen.
    
    Voorbeeld:
    
        python main.py img_in\img_bp\2pos2fot2.jpg 180
    
    
    Je bestand wordt dan in \img_out\ voor je klaargemaakt.
    Zorg ervoor dat eventuele sub-folders in zowel \img_in\ als \img_out\ bestaan (door bijv. een tekstbestandje erin te droppen).
    Bekijk je bestand ook vooral live om hem precies bij te stellen.
    """
