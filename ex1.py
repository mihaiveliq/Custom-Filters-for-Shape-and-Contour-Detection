from resolutions import *
from image import *

if __name__ == "__main__":

    for i in resolutions_map.values():
        print("\nImage " + i + ":")
        print(Image(i).image.shape)
        