import cv2
'''
Propose to Afla and Savannah on the possibility of making
this program a webpage. 
'''

# Load the image in Greyscale
image = cv2.imread('Images/image.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("error")
    exit()

# Canny formula to get dx and dy of image for gradients
edges = cv2.Canny(image, 100, 20)

# Save to file
cv2.imwrite('Images/edges.png', edges)


'''
Ok, now big question is how change white section perimiter into plottable points?

Or, do I even want to put it into plottable points? --> I think next part that will help me is if I just use arbitrary points to do it.
The thing with too many points is that the time complexity could go up exponentially, so thats pretty bad.

'''



