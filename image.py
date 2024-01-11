from filter import *

import cv2
from copy import copy
from numpy import sqrt, ceil

class Image:

    def __init__(self, image_path: str, color="colored"):

        image = cv2.imread(image_path)

        if color == "gray":
            self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            self.image = image

        self.kernel = None

        self.image_path = image_path
        self.color = color
        self.matrix = ndarray(shape=self.image.shape)

    # filter colored images
    def filter_image(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, k):
                self.apply_kernel_top_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_kernel_top(i, j, k, w)


            for j in range(im_cols - k, im_cols):
                self.apply_kernel_top_right(i, j, k, w)

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.apply_kernel_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_kernel_center(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.apply_kernel_right(i, j, k, w)

        for i in range(im_lines - k, im_lines):
            for j in range(0, k):
                self.apply_kernel_bottom_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_kernel_bottom(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.apply_kernel_bottom_right(i, j, k, w)

    # apply kernels on colored images
    def apply_kernel_top(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)

            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)
    
    def apply_kernel_top_left(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index < 0:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)
    
    def apply_kernel_top_right(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        im_cols = copy(self.image.shape[1])

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index >= im_cols:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)
    
    def apply_kernel_left(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if (col_index < 0):
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)

    def apply_kernel_right(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        im_cols = copy(self.image.shape[1])

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if (col_index >= im_cols):
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)

    def apply_kernel_bottom(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)
    
    def apply_kernel_bottom_left(self, i: float, j: float, k: float, w: float):

        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index < 0:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)
    
    def apply_kernel_bottom_right(self, i: float, j: float, k: float, w: float):
        
        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index >= im_cols:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)
                
    def apply_kernel_center(self, i: float, j: float, k: float, w: float):

        sum_r = 0
        sum_g = 0
        sum_b = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum_r += current_pixel[0] * kernel_elem
                sum_g += current_pixel[1] * kernel_elem
                sum_b += current_pixel[2] * kernel_elem

        pixel_addr[0] = min(254, sum_r)
        pixel_addr[1] = min(254, sum_g)
        pixel_addr[2] = min(254, sum_b)

    # filter grey images
    def filter_grey_image(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, k):
                self.apply_grey_kernel_top_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_grey_kernel_top(i, j, k, w)


            for j in range(im_cols - k, im_cols):
                self.apply_grey_kernel_top_right(i, j, k, w)

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.apply_grey_kernel_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_grey_kernel_center(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.apply_grey_kernel_right(i, j, k, w)

        for i in range(im_lines - k, im_lines):
            for j in range(0, k):
                self.apply_grey_kernel_bottom_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_grey_kernel_bottom(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.apply_grey_kernel_bottom_right(i, j, k, w)

    # apply grey kernel
    def apply_grey_kernel_top(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)

            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
    
    def apply_grey_kernel_top_left(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)
            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index < 0:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
    
    def apply_grey_kernel_top_right(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_cols = copy(self.image.shape[1])

        for u in range(w):

            line_index = int(u + i_k)
            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index >= im_cols:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
    
    def apply_grey_kernel_left(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if (col_index < 0):
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum

    def apply_grey_kernel_right(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_cols = copy(self.image.shape[1])

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if (col_index >= im_cols):
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum

    def apply_grey_kernel_bottom(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
    
    def apply_grey_kernel_bottom_left(self, i: float, j: float, k: float, w: float):

        sum = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index < 0:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
    
    def apply_grey_kernel_bottom_right(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index >= im_cols:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
                
    def apply_grey_kernel_center(self, i: float, j: float, k: float, w: float):

        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.image[i][j] = sum
    
    # filter grey pre-gradient magnitude images
    def filter_pre_grad_mag_grey_image(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, k):
                self.apply_grey_pre_grad_mag_kernel_top_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_grey_pre_grad_mag_kernel_top(i, j, k, w)


            for j in range(im_cols - k, im_cols):
                self.apply_grey_pre_grad_mag_kernel_top_right(i, j, k, w)

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.apply_grey_pre_grad_mag_kernel_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_grey_pre_grad_mag_kernel_center(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.apply_grey_pre_grad_mag_kernel_right(i, j, k, w)

        for i in range(im_lines - k, im_lines):
            for j in range(0, k):
                self.apply_grey_pre_grad_mag_kernel_bottom_left(i, j, k, w)

            for j in range(k, im_cols - k):
                self.apply_grey_pre_grad_mag_kernel_bottom(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.apply_grey_pre_grad_mag_kernel_bottom_right(i, j, k, w)

    # apply pre-gradient magnitude grey kernel
    def apply_grey_pre_grad_mag_kernel_top(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)

            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)
    
    def apply_grey_pre_grad_mag_kernel_top_left(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)
            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index < 0:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)
    
    def apply_grey_pre_grad_mag_kernel_top_right(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_cols = copy(self.image.shape[1])

        for u in range(w):

            line_index = int(u + i_k)
            if line_index < 0:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index >= im_cols:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)
    
    def apply_grey_pre_grad_mag_kernel_left(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if (col_index < 0):
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)

    def apply_grey_pre_grad_mag_kernel_right(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_cols = copy(self.image.shape[1])

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if (col_index >= im_cols):
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)

    def apply_grey_pre_grad_mag_kernel_bottom(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)
    
    def apply_grey_pre_grad_mag_kernel_bottom_left(self, i: float, j: float, k: float, w: float):

        sum = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                    continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index < 0:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)
    
    def apply_grey_pre_grad_mag_kernel_bottom_right(self, i: float, j: float, k: float, w: float):
        
        sum = 0

        i_k = i - k
        j_k = j - k

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for u in range(w):

            line_index = int(u + i_k)

            if line_index >= im_lines:
                continue

            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)

                if col_index >= im_cols:
                    continue

                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)
                
    def apply_grey_pre_grad_mag_kernel_center(self, i: float, j: float, k: float, w: float):

        sum = 0

        i_k = i - k
        j_k = j - k

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                sum += current_pixel * kernel_elem

        self.matrix[i][j] = pow(sum, 2)

    def filter_my_gradient_magnitude(self, filter_x: Gx_Sobel_Filter, filter_y: Gy_Sobel_Filter, blur_filter=None):
        image_x = Image(self.image_path, self.color)
        image_y = Image(self.image_path, self.color)

        if blur_filter:
            image_x.filter_grey_image(blur_filter)
            image_y.filter_grey_image(blur_filter)

        image_x.filter_pre_grad_mag_grey_image(filter_x)
        image_y.filter_pre_grad_mag_grey_image(filter_y)

        self.image[:] = ceil(sqrt(image_x.matrix + image_y.matrix))

    # filter colored images to detect the red roof
    def filter_red_image(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.image[i][j][:] = 0

            for j in range(k, im_cols - k):
                self.apply_red_kernel_center(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.image[i][j][:] = 0

        for i in range(im_lines - k, im_lines):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0

    # apply kernels on colored images to detect the red roof                
    def apply_red_kernel_center(self, i: float, j: float, k: float, w: float):

        threshold = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                threshold += max(0, current_pixel[0] * kernel_elem[0] + current_pixel[1] * kernel_elem[1] + current_pixel[2] * kernel_elem[2])
        
        if (pixel_addr[0] or pixel_addr[1]) > threshold or pixel_addr[2] < threshold:
                pixel_addr[0] = pixel_addr[1] = pixel_addr[2] = 0

    # filter colored images to detect the blue pool
    def filter_blue_image(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.image[i][j][:] = 0

            for j in range(k, im_cols - k):
                self.apply_blue_kernel_center(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.image[i][j][:] = 0

        for i in range(im_lines - k, im_lines):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0
    
    # apply kernels on colored images to detect the blue pool
    def apply_blue_kernel_center(self, i: float, j: float, k: float, w: float):

        threshold = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                threshold += max(0, current_pixel[0] * kernel_elem[0] + current_pixel[1] * kernel_elem[1] + current_pixel[2] * kernel_elem[2])
        
        tmp = int(pixel_addr[2]) + int(pixel_addr[1])
        
        if (pixel_addr[2] or pixel_addr[1]) > threshold or pixel_addr[0] < threshold or tmp < pixel_addr[0]:
            pixel_addr[0] = pixel_addr[1] = pixel_addr[2] = 0

    # filter colored images to detect the h
    def filter_h_image(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.image[i][j][:] = 0

            for j in range(k, im_cols - k):
                self.apply_h_kernel_center(i, j, k, w)

            for j in range(im_cols - k, im_cols):
                self.image[i][j][:] = 0

        for i in range(im_lines - k, im_lines):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0
    
    def filter_h_image_2(self, filter: Filter):

        self.kernel = filter.kernel
        w = copy(self.kernel.shape[0])

        k = int((w - 1) / 2)

        im_lines = copy(self.image.shape[0])
        im_cols = copy(self.image.shape[1])

        for i in range(0, k):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0

        for i in range(k, im_lines - k):
            for j in range(0, k):
                self.image[i][j][:] = 0

            for j in range(k, im_cols - k):

                self.apply_aux_h_kernel_center(i, j)

            for j in range(im_cols - k, im_cols):
                self.image[i][j][:] = 0

        for i in range(im_lines - k, im_lines):
            for j in range(0, im_cols):
                self.image[i][j][:] = 0
    
    # apply kernels on colored images to detect the h
    def apply_h_kernel_center(self, i: float, j: float, k: float, w: float):

        threshold = 0

        i_k = i - k
        j_k = j - k

        pixel_addr = self.image[i][j]

        for u in range(w):

            line_index = int(u + i_k)
            pixel_line = copy(self.image[line_index])

            kernel_line = copy(self.kernel[u])

            for v in range(w):

                col_index = int(v + j_k)
                current_pixel = pixel_line[col_index]

                kernel_elem = kernel_line[v]

                threshold += (int(current_pixel[0]) + int(current_pixel[1]) + int(current_pixel[2])) * kernel_elem / 3

        threshold /= 255

        if (threshold > 0.8 or threshold < 0.45 or pixel_addr[0] > pixel_addr[2] or pixel_addr[1] > pixel_addr[2]) or pixel_addr[2] / 255 < threshold:
        
            pixel_addr[0] = pixel_addr[1] = pixel_addr[2] = 0
            
    def apply_aux_h_kernel_center(self, i: float, j: float):

        pixel_addr = self.image[i][j]

        tmp = int(pixel_addr[0]) + int(pixel_addr[1]) + int(pixel_addr[2])
        tmp /= 3
        tmp /= 255

        if tmp > 0.75 or tmp < 0.6 or ((pixel_addr[0] < pixel_addr[1]) and (pixel_addr[1] - pixel_addr[0] > 10)) or (pixel_addr[2] < pixel_addr[1]):
            pixel_addr[0] = pixel_addr[1] = pixel_addr[2] = 0


    def show_image(self, name: str):

        cv2.namedWindow(name, cv2.WINDOW_GUI_NORMAL)
        cv2.imshow(name, self.image)
        cv2.waitKey(0)

    def save_image(self, name: str):
        
        cv2.imwrite(name, self.image)
        