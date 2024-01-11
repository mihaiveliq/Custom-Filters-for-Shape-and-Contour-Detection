from resolutions import *
from image import *

def h_filtering():

    # prepare filters
    g_f = Gaussian_Filter(7, 3)
    h_f = Box_Filter(7)

    # resolution 10

    # prepare image
    image_10_h = Image(resolutions_map[10])

    # filter and save image
    image_10_h.filter_h_image(h_f)
    image_10_h.filter_h_image_2(h_f)

    image_10_h.filter_image(g_f)

    image_10_h.save_image("Scara_10_H_Filter.jpg")

    # resolution 20

    # prepare image
    image_20_h = Image(resolutions_map[20])

    # filter and save image
    image_20_h.filter_h_image(h_f)
    image_20_h.filter_h_image_2(h_f)

    image_20_h.filter_image(g_f)

    image_20_h.save_image("Scara_20_H_Filter.jpg")

    # resolution 40

    # prepare image
    image_40_h = Image(resolutions_map[40])

    # filter and save image
    image_40_h.filter_h_image(h_f)
    image_40_h.filter_h_image_2(h_f)

    image_40_h.filter_image(g_f)

    image_40_h.save_image("Scara_40_H_Filter.jpg")

    # resolution 80

    # prepare image
    image_80_h = Image(resolutions_map[80])

    # filter and save image
    image_80_h.filter_h_image(h_f)
    image_80_h.filter_h_image_2(h_f)

    image_80_h.filter_image(g_f)

    image_80_h.save_image("Scara_80_H_Filter.jpg")

    # resolution 100

    # prepare image
    image_100_h = Image(resolutions_map[100])

    # filter and save image
    image_100_h.filter_h_image(h_f)
    image_100_h.filter_h_image_2(h_f)

    image_100_h.filter_image(g_f)

    image_100_h.save_image("Scara_100_H_Filter.jpg")

def blue_pool_filtering():

    # prepare filters
    g_f = Gaussian_Filter(7, 3)
    b_p_f = Blue_Pool_Filter()

    # resolution 10

    # prepare image
    image_10_b_p = Image(resolutions_map[10])

    # filter and save image
    image_10_b_p.filter_blue_image(b_p_f)
    image_10_b_p.filter_image(g_f)

    image_10_b_p.save_image("Scara_10_Blue_Pool_Filter.jpg")

    # resolution 20

    # prepare image
    image_20_b_p = Image(resolutions_map[20])

    # filter and save image
    image_20_b_p.filter_blue_image(b_p_f)
    image_20_b_p.filter_image(g_f)

    image_20_b_p.save_image("Scara_20_Blue_Pool_Filter.jpg")

    # resolution 40

    # prepare image
    image_40_b_p = Image(resolutions_map[40])

    # filter and save image
    image_40_b_p.filter_blue_image(b_p_f)
    image_40_b_p.filter_image(g_f)

    image_40_b_p.save_image("Scara_40_Blue_Pool_Filter.jpg")

    # resolution 80

    # prepare image
    image_80_b_p = Image(resolutions_map[80])

    # filter and save image
    image_80_b_p.filter_blue_image(b_p_f)
    image_80_b_p.filter_image(g_f)

    image_80_b_p.save_image("Scara_80_Blue_Pool_Filter.jpg")

    # resolution 100

    # prepare image
    image_100_b_p = Image(resolutions_map[100])

    # filter and save image
    image_100_b_p.filter_blue_image(b_p_f)
    image_100_b_p.filter_image(g_f)

    image_100_b_p.save_image("Scara_100_Blue_Pool_Filter.jpg")

def red_roof_filtering():

    # prepare filters
    g_f = Gaussian_Filter(7, 3)
    r_r_f = Red_Roof_Filter()

    # resolution 10

    # prepare image
    image_10_r_r = Image(resolutions_map[10])

    # filter and save image
    image_10_r_r.filter_red_image(r_r_f)
    image_10_r_r.filter_image(g_f)

    image_10_r_r.save_image("Scara_10_Red_Roof_Filter.jpg")

    # resolution 20

    # prepare image
    image_20_r_r = Image(resolutions_map[20])

    # filter and save image
    image_20_r_r.filter_red_image(r_r_f)
    image_20_r_r.filter_image(g_f)

    image_20_r_r.save_image("Scara_20_Red_Roof_Filter.jpg")

    # resolution 40

    # prepare image
    image_40_r_r = Image(resolutions_map[40])

    # filter and save image
    image_40_r_r.filter_red_image(r_r_f)
    image_40_r_r.filter_image(g_f)

    image_40_r_r.save_image("Scara_40_Red_Roof_Filter.jpg")

    # resolution 80

    # prepare image
    image_80_r_r = Image(resolutions_map[80])

    # filter and save image
    image_80_r_r.filter_red_image(r_r_f)
    image_80_r_r.filter_image(g_f)

    image_80_r_r.save_image("Scara_80_Red_Roof_Filter.jpg")

    # resolution 100

    # prepare image
    image_100_r_r = Image(resolutions_map[100])

    # filter and save image
    image_100_r_r.filter_red_image(r_r_f)
    image_100_r_r.filter_image(g_f)

    image_100_r_r.save_image("Scara_100_Red_Roof_Filter.jpg")


def ex4():
    red_roof_filtering()
    blue_pool_filtering()
    h_filtering()
    

if __name__ == "__main__":

    ex4()