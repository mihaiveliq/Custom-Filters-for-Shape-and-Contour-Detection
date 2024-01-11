from resolutions import *
from image import *

def ex2():
    # prepare gaussian filters
    g_f_3_3 = Gaussian_Filter(3, 3)
    g_f_5_3 = Gaussian_Filter(5, 3)
    g_f_7_3 = Gaussian_Filter(7, 3)

    g_f_3_5 = Gaussian_Filter(3, 5)
    g_f_5_5 = Gaussian_Filter(5, 5)
    g_f_7_5 = Gaussian_Filter(7, 5)

    # prepare box filters
    b_f_3 = Box_Filter(3)
    b_f_5 = Box_Filter(5)
    b_f_7 = Box_Filter(7)

    # resolution 10

    # prepare images to be filtered
    image_10_g_f_3_3 = Image(resolutions_map[10])
    image_10_g_f_5_3 = Image(resolutions_map[10])
    image_10_g_f_7_3 = Image(resolutions_map[10])

    image_10_g_f_3_5 = Image(resolutions_map[10])
    image_10_g_f_5_5 = Image(resolutions_map[10])
    image_10_g_f_7_5 = Image(resolutions_map[10])

    image_10_b_f_3 = Image(resolutions_map[10])
    image_10_b_f_5 = Image(resolutions_map[10])
    image_10_b_f_7 = Image(resolutions_map[10])


    # filter images and save the results
    image_10_g_f_3_3.filter_image(g_f_3_3)
    image_10_g_f_3_3.save_image("Scara_10_Gaussian_Filter_3x3_sig_3.jpg")

    image_10_g_f_5_3.filter_image(g_f_5_3)
    image_10_g_f_5_3.save_image("Scara_10_Gaussian_Filter_5x5_sig_3.jpg")

    image_10_g_f_7_3.filter_image(g_f_7_3)
    image_10_g_f_7_3.save_image("Scara_10_Gaussian_Filter_7x7_sig_3.jpg")

    image_10_g_f_3_5.filter_image(g_f_3_5)
    image_10_g_f_3_5.save_image("Scara_10_Gaussian_Filter_3x3_sig_5.jpg")

    image_10_g_f_5_5.filter_image(g_f_5_5)
    image_10_g_f_5_5.save_image("Scara_10_Gaussian_Filter_5x5_sig_5.jpg")

    image_10_g_f_7_5.filter_image(g_f_7_5)
    image_10_g_f_7_5.save_image("Scara_10_Gaussian_Filter_7x7_sig_5.jpg")

    image_10_b_f_3.filter_image(b_f_3)
    image_10_b_f_3.save_image("Scara_10_Box_Filter_3x3.jpg")

    image_10_b_f_5.filter_image(b_f_5)
    image_10_b_f_5.save_image("Scara_10_Box_Filter_5x5.jpg")

    image_10_b_f_7.filter_image(b_f_7)
    image_10_b_f_7.save_image("Scara_10_Box_Filter_7x7.jpg")

    # resolution 20

    # prepare images to be filtered
    image_20_g_f_3_3 = Image(resolutions_map[20])
    image_20_g_f_5_3 = Image(resolutions_map[20])
    image_20_g_f_7_3 = Image(resolutions_map[20])

    image_20_g_f_3_5 = Image(resolutions_map[20])
    image_20_g_f_5_5 = Image(resolutions_map[20])
    image_20_g_f_7_5 = Image(resolutions_map[20])

    image_20_b_f_3 = Image(resolutions_map[20])
    image_20_b_f_5 = Image(resolutions_map[20])
    image_20_b_f_7 = Image(resolutions_map[20])


    # filter images and save the results
    image_20_g_f_3_3.filter_image(g_f_3_3)
    image_20_g_f_3_3.save_image("Scara_20_Gaussian_Filter_3x3_sig_3.jpg")

    image_20_g_f_5_3.filter_image(g_f_5_3)
    image_20_g_f_5_3.save_image("Scara_20_Gaussian_Filter_5x5_sig_3.jpg")

    image_20_g_f_7_3.filter_image(g_f_7_3)
    image_20_g_f_7_3.save_image("Scara_20_Gaussian_Filter_7x7_sig_3.jpg")

    image_20_g_f_3_5.filter_image(g_f_3_5)
    image_20_g_f_3_5.save_image("Scara_20_Gaussian_Filter_3x3_sig_5.jpg")

    image_20_g_f_5_5.filter_image(g_f_5_5)
    image_20_g_f_5_5.save_image("Scara_20_Gaussian_Filter_5x5_sig_5.jpg")

    image_20_g_f_7_5.filter_image(g_f_7_5)
    image_20_g_f_7_5.save_image("Scara_20_Gaussian_Filter_7x7_sig_5.jpg")

    image_20_b_f_3.filter_image(b_f_3)
    image_20_b_f_3.save_image("Scara_20_Box_Filter_3x3.jpg")

    image_20_b_f_5.filter_image(b_f_5)
    image_20_b_f_5.save_image("Scara_20_Box_Filter_5x5.jpg")

    image_20_b_f_7.filter_image(b_f_7)
    image_20_b_f_7.save_image("Scara_20_Box_Filter_7x7.jpg")

    # resolution 40

    # prepare images to be filtered
    image_40_g_f_3_3 = Image(resolutions_map[40])
    image_40_g_f_5_3 = Image(resolutions_map[40])
    image_40_g_f_7_3 = Image(resolutions_map[40])

    image_40_g_f_3_5 = Image(resolutions_map[40])
    image_40_g_f_5_5 = Image(resolutions_map[40])
    image_40_g_f_7_5 = Image(resolutions_map[40])

    image_40_b_f_3 = Image(resolutions_map[40])
    image_40_b_f_5 = Image(resolutions_map[40])
    image_40_b_f_7 = Image(resolutions_map[40])

    # filter images and save the results
    image_40_g_f_3_3.filter_image(g_f_3_3)
    image_40_g_f_3_3.save_image("Scara_40_Gaussian_Filter_3x3_sig_3.jpg")

    image_40_g_f_5_3.filter_image(g_f_5_3)
    image_40_g_f_5_3.save_image("Scara_40_Gaussian_Filter_5x5_sig_3.jpg")

    image_40_g_f_7_3.filter_image(g_f_7_3)
    image_40_g_f_7_3.save_image("Scara_40_Gaussian_Filter_7x7_sig_3.jpg")

    image_40_g_f_3_5.filter_image(g_f_3_5)
    image_40_g_f_3_5.save_image("Scara_40_Gaussian_Filter_3x3_sig_5.jpg")

    image_40_g_f_5_5.filter_image(g_f_5_5)
    image_40_g_f_5_5.save_image("Scara_40_Gaussian_Filter_5x5_sig_5.jpg")

    image_40_g_f_7_5.filter_image(g_f_7_5)
    image_40_g_f_7_5.save_image("Scara_40_Gaussian_Filter_7x7_sig_5.jpg")

    image_40_b_f_3.filter_image(b_f_3)
    image_40_b_f_3.save_image("Scara_40_Box_Filter_3x3.jpg")

    image_40_b_f_5.filter_image(b_f_5)
    image_40_b_f_5.save_image("Scara_40_Box_Filter_5x5.jpg")

    image_40_b_f_7.filter_image(b_f_7)
    image_40_b_f_7.save_image("Scara_40_Box_Filter_7x7.jpg")

    # resolution 80

    # prepare images to be filtered
    image_80_g_f_5_3 = Image(resolutions_map[80])
    image_80_g_f_7_3 = Image(resolutions_map[80])
    image_80_g_f_3_3 = Image(resolutions_map[80])

    image_80_g_f_3_5 = Image(resolutions_map[80])
    image_80_g_f_5_5 = Image(resolutions_map[80])
    image_80_g_f_7_5 = Image(resolutions_map[80])

    image_80_b_f_3 = Image(resolutions_map[80])
    image_80_b_f_5 = Image(resolutions_map[80])
    image_80_b_f_7 = Image(resolutions_map[80])

    # filter images and save the results
    image_80_g_f_3_3.filter_image(g_f_3_3)
    image_80_g_f_3_3.save_image("Scara_80_Gaussian_Filter_3x3_sig_3.jpg")

    image_80_g_f_5_3.filter_image(g_f_5_3)
    image_80_g_f_5_3.save_image("Scara_80_Gaussian_Filter_5x5_sig_3.jpg")

    image_80_g_f_7_3.filter_image(g_f_7_3)
    image_80_g_f_7_3.save_image("Scara_80_Gaussian_Filter_7x7_sig_3.jpg")

    image_80_g_f_3_5.filter_image(g_f_3_5)
    image_80_g_f_3_5.save_image("Scara_80_Gaussian_Filter_3x3_sig_5.jpg")

    image_80_g_f_5_5.filter_image(g_f_5_5)
    image_80_g_f_5_5.save_image("Scara_80_Gaussian_Filter_5x5_sig_5.jpg")

    image_80_g_f_7_5.filter_image(g_f_7_5)
    image_80_g_f_7_5.save_image("Scara_80_Gaussian_Filter_7x7_sig_5.jpg")

    image_80_b_f_3.filter_image(b_f_3)
    image_80_b_f_3.save_image("Scara_80_Box_Filter_3x3.jpg")

    image_80_b_f_5.filter_image(b_f_5)
    image_80_b_f_5.save_image("Scara_80_Box_Filter_5x5.jpg")

    image_80_b_f_7.filter_image(b_f_7)
    image_80_b_f_7.save_image("Scara_80_Box_Filter_7x7.jpg")

    # resolution 100

    # prepare images to be filtered
    image_100_g_f_3_3 = Image(resolutions_map[100])
    image_100_g_f_5_3 = Image(resolutions_map[100])
    image_100_g_f_7_3 = Image(resolutions_map[100])

    image_100_g_f_3_5 = Image(resolutions_map[100])
    image_100_g_f_5_5 = Image(resolutions_map[100])
    image_100_g_f_7_5 = Image(resolutions_map[100])

    image_100_b_f_3 = Image(resolutions_map[100])
    image_100_b_f_5 = Image(resolutions_map[100])
    image_100_b_f_7 = Image(resolutions_map[100])


    # filter images and save the results
    image_100_g_f_3_3.filter_image(g_f_3_3)
    image_100_g_f_3_3.save_image("Scara_100_Gaussian_Filter_3x3_sig_3.jpg")

    image_100_g_f_5_3.filter_image(g_f_5_3)
    image_100_g_f_5_3.save_image("Scara_100_Gaussian_Filter_5x5_sig_3.jpg")

    image_100_g_f_7_3.filter_image(g_f_7_3)
    image_100_g_f_7_3.save_image("Scara_100_Gaussian_Filter_7x7_sig_3.jpg")

    image_100_g_f_3_5.filter_image(g_f_3_5)
    image_100_g_f_3_5.save_image("Scara_100_Gaussian_Filter_3x3_sig_5.jpg")

    image_100_g_f_5_5.filter_image(g_f_5_5)
    image_100_g_f_5_5.save_image("Scara_100_Gaussian_Filter_5x5_sig_5.jpg")

    image_100_g_f_7_5.filter_image(g_f_7_5)
    image_100_g_f_7_5.save_image("Scara_100_Gaussian_Filter_7x7_sig_5.jpg")

    image_100_b_f_3.filter_image(b_f_3)
    image_100_b_f_3.save_image("Scara_100_Box_Filter_3x3.jpg")

    image_100_b_f_5.filter_image(b_f_5)
    image_100_b_f_5.save_image("Scara_100_Box_Filter_5x5.jpg")

    image_100_b_f_7.filter_image(b_f_7)
    image_100_b_f_7.save_image("Scara_100_Box_Filter_7x7.jpg")

if __name__ == "__main__":

    ex2()
