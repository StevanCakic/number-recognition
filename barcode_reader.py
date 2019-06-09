import sys
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(image):
    # Find barcodes and QR codes
    decoded_objects = pyzbar.decode(image)

    # Print results
    for obj in decoded_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decoded_objects

# Display barcode and QR code location
def display(im, decoded_objects):
    # Loop over all decoded objects
    for decoded_object in decoded_objects: 
        points = decoded_object.polygon
        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        # Number of points in the convex hull
        n = len(hull)
        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j+1) % n], (255, 0, 0), 3)
# Main
if __name__ == '__main__':
    # Read image
    IMG = cv2.imread(sys.argv[1])
    display(IMG, decode(IMG))
