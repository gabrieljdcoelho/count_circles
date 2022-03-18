import detect_circles as dc
import os


if __name__ == "__main__":

    data_folder = "data/"
    total_count = 0
    images = os.listdir(data_folder)
    
    for image in images:

        count_image = dc.detect_circles(image = image)
        total_count += count_image
    print(total_count)
