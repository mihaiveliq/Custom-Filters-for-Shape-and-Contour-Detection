from numpy import ndarray, array
from math import exp, pi

class Filter:

    def __init__(self, k: float):

        self.kernel = self.build_kernel(k)
    
    def build_kernel(self, k: float):

        raise NotImplementedError("Method not implemented")

class Gaussian_Filter(Filter):

    def __init__(self, k: float, sigma: float):

        self.sigma = sigma
        self.kernel = self.build_kernel(k)
    
    def build_kernel(self, k: float):

        sigma = self.sigma

        kernel = ndarray(shape=(k, k), dtype=float)

        middle_point_coord = int((k - 1) / 2)
        const_factor = 1 / (2 * pi * pow(sigma, 2))
        
        for x in range(middle_point_coord + 1):
            for y in range(middle_point_coord + 1):

                exponent = -1 * ((pow(x, 2) + pow(y, 2)) / (2 * pow(sigma, 2)))

                pixel_value = const_factor * exp(exponent)

                kernel[middle_point_coord - x][middle_point_coord - y] = \
                    kernel[k - 1 - middle_point_coord + x][middle_point_coord - y] = \
                        kernel[middle_point_coord - x][k - 1 - middle_point_coord + y] = \
                            kernel[k - 1 - middle_point_coord + x][k - 1 - middle_point_coord + y] = \
                                pixel_value
        
        return kernel

class Box_Filter(Filter):

    def __init__(self, k: float):

        self.kernel = self.build_kernel(k)
    
    def build_kernel(self, k: float):
        
        kernel = ndarray(shape=(k, k), dtype=float)

        middle_point_coord = (k - 1) / 2
        const_factor = 1 / (k * k)

        pixel_value = const_factor * 1
        
        for x in range(int(middle_point_coord + 1)):
            for y in range(int(middle_point_coord + 1)):

                kernel[x][y] = \
                    kernel[k - 1 - x][y] = \
                        kernel[x][k - 1 - y] = \
                            kernel[k - 1 - x][k - 1 - y] = \
                                pixel_value
        
        return kernel

class Edge_Detector_Filter(Filter):

    def __init__(self, k: float, sigma: float):

        self.sigma = sigma
        self.kernel = self.build_kernel(k)
    
    def build_kernel(self, k: float):

        sigma = self.sigma

        kernel = ndarray(shape=(k, k), dtype=float)

        middle_point_coord = int((k - 1) / 2)
        const_factor = 1 / (2 * pi * pow(sigma, 2))
        
        for x in range(middle_point_coord + 1):
            for y in range(middle_point_coord + 1):

                exponent = -1 * ((pow(x, 2) + pow(y, 2)) / (2 * pow(sigma, 2)))

                pixel_value = const_factor * exp(exponent)

                kernel[middle_point_coord - x][middle_point_coord - y] = \
                    kernel[k - 1 - middle_point_coord + x][middle_point_coord - y] = \
                        kernel[middle_point_coord - x][k - 1 - middle_point_coord + y] = \
                            kernel[k - 1 - middle_point_coord + x][k - 1 - middle_point_coord + y] = \
                                pixel_value
        
        return kernel

class Gx_Sobel_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([[-0.11, 0.0, 0.11],
            [-0.22, 0.0, 0.22],
            [-0.11, 0.0, 0.11]])
        
        return kernel

class Gy_Sobel_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([[0.11, 0.22, 0.11],
            [0.0, 0.0, 0.0],
            [-0.11, -0.22, -0.11]])
        
        return kernel

class Gx_Sobel_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([[-0.11, 0.0, 0.11],
            [-0.22, 0.0, 0.22],
            [-0.11, 0.0, 0.11]])
        
        return kernel

class Gy_Sobel_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([[0.11, 0.22, 0.11],
            [0.0, 0.0, 0.0],
            [-0.11, -0.22, -0.11]])
        
        return kernel

class Red_Roof_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([[[-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625]],
            [[-0.04, -0.02, -0.0625], [-0.04, -0.02, 0.077], [-0.04, -0.02, 0.077], [-0.04, -0.02, 0.077], [-0.04, -0.02, -0.0625]],
            [[-0.04, -0.02, -0.0625], [-0.04, -0.02, 0.153], [-0.04, -0.02, 0.23], [-0.04, -0.02, 0.153], [-0.04, -0.02, -0.0625]],
            [[-0.04, -0.02, -0.0625], [-0.04, -0.02, 0.077], [-0.04, -0.02, 0.077], [-0.04, -0.02, 0.077], [-0.04, -0.02, -0.0625]],
            [[-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625], [-0.04, -0.02, -0.0625]]])
        
        return kernel

class Blue_Pool_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]],
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]],
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [ 0.037, -0.01, -0.01], [ 0.037, -0.01, -0.01], [ 0.037, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]],
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [ 0.037, -0.01, -0.01], [ 0.037, -0.01, -0.01], [ 0.037, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]],
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [ 0.037, -0.01, -0.01], [ 0.037, -0.01, -0.01], [ 0.037, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]],
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]],
            [[-0.0625, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01], [-0.025, -0.01, -0.01]]])
        
        return kernel

class H_Filter(Filter):

    def __init__(self):

        self.kernel = self.build_kernel()
    
    def build_kernel(self):

        kernel = array([
            [[-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110]],
            [[-0.110, -0.110, -0.110], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [-0.110, -0.110, -0.110]],
            [[-0.110, -0.110, -0.110], [0.0484, 0.0484, 0.0777], [0.0158, 0.0250, 0.0250], [0.0158, 0.0250, 0.0250], [0.0158, 0.0250, 0.0250], [0.0484, 0.0484, 0.0777], [-0.110, -0.110, -0.110]],
            [[-0.110, -0.110, -0.110], [0.0484, 0.0484, 0.0777], [0.0158, 0.0250, 0.0250], [1.2000, 1.2000, 1.5000], [0.0158, 0.0250, 0.0250], [0.0484, 0.0484, 0.0777], [-0.110, -0.110, -0.110]],
            [[-0.110, -0.110, -0.110], [0.0484, 0.0484, 0.0777], [0.0158, 0.0250, 0.0250], [0.0158, 0.0250, 0.0250], [0.0158, 0.0250, 0.0250], [0.0484, 0.0484, 0.0777], [-0.110, -0.110, -0.110]],
            [[-0.110, -0.110, -0.110], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [0.0484, 0.0484, 0.0777], [-0.110, -0.110, -0.110]],
            [[-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110], [-0.110, -0.110, -0.110]]])
        
        return kernel