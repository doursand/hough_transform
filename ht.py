import numpy as np
import imageio
import math
import matplotlib.pyplot as plt
import heapq

class ht():
    # define hough object
    def __init__(self, n_lines, img_path, n_threshold,b_negative=False):
        self.nlines = n_lines
        self.imgpath = img_path
        self.threshold = n_threshold
        self.negative=b_negative
        self.img=imageio.imread(self.imgpath)
        if self.img.ndim == 3:
            self.img = np.dot(self.img[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
        if self.negative == True:
            self.img=np.negative(self.img)
   
    def hough_line(self,angle_step=1, lines_are_white=True):
        """
        Hough transform for lines
        Input:
        img - 2D binary image with nonzeros representing edges
        angle_step - Spacing between angles to use every n-th angle
                     between -90 and 90 degrees. Default step is 1.
        lines_are_white - boolean indicating whether lines to be detected are white
        value_threshold - Pixel values above or below the value_threshold are edges
        Returns:
        accumulator - 2D array of the hough transform accumulator
        theta - array of angles used in computation, in radians.
        rhos - array of rho values. Max size is 2 times the diagonal
               distance of the input image.
        """
        img=self.img
        value_threshold=self.threshold
        
        # Rho and Theta ranges
        thetas = np.deg2rad(np.arange(-90.0, 90.0, angle_step))
        width, height = img.shape
        diag_len = int(round(math.sqrt(width * width + height * height)))
        rhos = np.linspace(-diag_len, diag_len, diag_len * 2)
    
        # Cache some resuable values
        cos_t = np.cos(thetas)
        sin_t = np.sin(thetas)
        num_thetas = len(thetas)
    
        # Hough accumulator array of theta vs rho
        accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint8)
        # (row, col) indexes to edges
        are_edges = img > value_threshold if lines_are_white else img < value_threshold
        y_idxs, x_idxs = np.nonzero(are_edges)
    
        # Vote in the hough accumulator
        for i in range(len(x_idxs)):
            x = x_idxs[i]
            y = y_idxs[i]
    
            for t_idx in range(num_thetas):
                # Calculate rho. diag_len is added for a positive index
                rho = diag_len + int(round(x * cos_t[t_idx] + y * sin_t[t_idx]))
                accumulator[rho, t_idx] += 1
    
        return accumulator, thetas, rhos


    def show_hough_line(self, accumulator, thetas, rhos, save_path=None):
    
        img=self.img
        
        fig, ax = plt.subplots(1, 2, figsize=(300, 100))
        img=np.invert(img)
        ax[0].imshow(img, cmap=plt.cm.gray)
        ax[0].set_title('Input image')
        ax[0].axis('image')
    
        ax[1].imshow(
            accumulator, cmap='jet',
            extent=[np.rad2deg(thetas[-1]), np.rad2deg(thetas[0]), rhos[-1], rhos[0]])
        ax[1].set_aspect('equal', adjustable='box')
        ax[1].set_title('Hough transform')
        ax[1].set_xlabel('Angles (degrees)')
        ax[1].set_ylabel('Distance (pixels)')
        ax[1].axis('image')
        
        # Easiest peak finding based on max votes
        # AD -- to be placed in a dedicated function or create a class
        #return top n max coordinates in accumulator matrix
        n=self.nlines
        indices = np.where(accumulator>=heapq.nlargest(n,accumulator.flatten())[-1])
        np_indices = np.array(indices)
        #get coordinates within accumulator matrix of top n rho and theta
        for j in range(0,n):
            ind_rho=np_indices[0][j] -int((len(rhos)/2))
            ind_theta=np_indices[1][j] -89
            #îtheta=accumulator[ind_rho,ind_theta]
            #rho=rhos[ind_rho]
            print("ind_rho={0:2f}, ind_theta={1:.0f}".format(ind_rho,ind_theta))
            #print("rho={0:.2f}, theta={1:.0f}".format(rho,theta ))
            m=-(np.cos(np.deg2rad(ind_theta))/np.sin(np.deg2rad(ind_theta)))
            b=ind_rho/np.sin(np.deg2rad(ind_theta))
            print("m={0:2f},b={1:2f}".format(m,b))
            x = np.arange(1, len(img[1]))
            y = b + m * x
            ax[0].plot(x, y, color="r")
   
if __name__ == '__main__':
    
    path = 'imgs\\LBIRD2.png'
    hough = ht(5,path,5,True)
    accumulator, thetas, rhos = hough.hough_line()
    hough.show_hough_line(accumulator,thetas,rhos,save_path='imgs\\output.png')
