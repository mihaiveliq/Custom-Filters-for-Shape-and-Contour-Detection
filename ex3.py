from resolutions import *
from image import *

def ex3():

    # prepare blurring filters
    b_f_3 = Box_Filter(3)
    b_f_5 = Box_Filter(5)

    # prepare sobel filters
    gx_s_f = Gx_Sobel_Filter()
    gy_s_f = Gy_Sobel_Filter()
    
    # resolution 10

    # prepare images to be filtered
    image_10 = Image(resolutions_map[10], "gray")
    image_10_3 = Image(resolutions_map[10], "gray")
    image_10_5 = Image(resolutions_map[10], "gray")
    
    # filter images and save the results
    image_10.filter_my_gradient_magnitude(gx_s_f, gy_s_f)
    image_10_3.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_3)
    image_10_5.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_5)

    image_10.save_image("Scara_10__My_Magnitude_Gradient.jpg")
    image_10_3.save_image("Scara_10_My_Magnitude_Gradient_Filter_Blured_3x3.jpg")
    image_10_5.save_image("Scara_10_My_Magnitude_Gradient_Filter_Blured_5x5.jpg")

    # resolution 20

    # prepare images to be filtered
    image_20 = Image(resolutions_map[20], "gray")
    image_20_3 = Image(resolutions_map[20], "gray")
    image_20_5 = Image(resolutions_map[20], "gray")

    # filter images and save the results
    image_20.filter_my_gradient_magnitude(gx_s_f, gy_s_f)
    image_20_3.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_3)
    image_20_5.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_5)

    image_20.save_image("Scara_20__My_Magnitude_Gradient.jpg")
    image_20_3.save_image("Scara_20_My_Magnitude_Gradient_Filter_Blured_3x3.jpg")
    image_20_5.save_image("Scara_20_My_Magnitude_Gradient_Filter_Blured_5x5.jpg")

    # resolution 40

    # prepare images to be filtered
    image_40 = Image(resolutions_map[40], "gray")
    image_40_3 = Image(resolutions_map[40], "gray")
    image_40_5 = Image(resolutions_map[40], "gray")


    # filter images and save the results
    image_40.filter_my_gradient_magnitude(gx_s_f, gy_s_f)
    image_40_3.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_3)
    image_40_5.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_5)

    image_40.save_image("Scara_40__My_Magnitude_Gradient.jpg")
    image_40_3.save_image("Scara_40_My_Magnitude_Gradient_Filter_Blured_3x3.jpg")
    image_40_5.save_image("Scara_40_My_Magnitude_Gradient_Filter_Blured_5x5.jpg")


    # resolution 80

    # prepare images to be filtered
    image_80 = Image(resolutions_map[80], "gray")
    image_80_3 = Image(resolutions_map[80], "gray")
    image_80_5 = Image(resolutions_map[80], "gray")


    # filter images and save the results
    image_80.filter_my_gradient_magnitude(gx_s_f, gy_s_f)
    image_80_3.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_3)
    image_80_5.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_5)

    image_80.save_image("Scara_80__My_Magnitude_Gradient.jpg")
    image_80_3.save_image("Scara_80_My_Magnitude_Gradient_Filter_Blured_3x3.jpg")
    image_80_5.save_image("Scara_80_My_Magnitude_Gradient_Filter_Blured_5x5.jpg")

    # resolution 100

    # prepare images to be filtered
    image_100 = Image(resolutions_map[100], "gray")
    image_100_3 = Image(resolutions_map[100], "gray")
    image_100_5 = Image(resolutions_map[100], "gray")

    # filter images and save the results
    image_100.filter_my_gradient_magnitude(gx_s_f, gy_s_f)
    image_100_3.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_3)
    image_100_5.filter_my_gradient_magnitude(gx_s_f, gy_s_f, b_f_5)

    image_100.save_image("Scara_100__My_Magnitude_Gradient.jpg")
    image_100_3.save_image("Scara_100__My_Magnitude_Gradient_Filter_Blured_3x3.jpg")
    image_100_5.save_image("Scara_100__My_Magnitude_Gradient_Filter_Blured_5x5.jpg")

if __name__ == "__main__":

    ex3()
