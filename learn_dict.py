import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.decomposition import DictionaryLearning

from scipy.misc import toimage
from scipy.misc import imread

from PIL import Image


def img2mtx(filename):
    #Returns an array corresponding the image
    imgm = imread(filename)
    imgm = imgm / 255
    return imgm

def mtx2patches(imgm):
    print('Extracting reference patches...')
    patch_size = (7, 7)
    data = extract_patches_2d(imgm[:7**3, :7**3, 1], patch_size)
    data = data.reshape(data.shape[0], -1)
    data -= np.mean(data, axis=0)
    data /= np.std(data, axis=0)
    return data

def learn_dictionary(data):
    print('Learning the dictionary...')
    #Learn dictionary
    dico = MiniBatchDictionaryLearning(n_components=50, alpha=1, n_iter=500)
    V = dico.fit(data).components_
    return V

def plot_dictionary(V, outputfilename):
    plt.figure(figsize=(4.2, 4))
    patch_size = (7, 7)

    for i, comp in enumerate(V[:100]):
        plt.subplot(10, 10, i + 1)
        plt.imshow(comp.reshape(patch_size), cmap=plt.cm.gray_r,
               interpolation='nearest')
        plt.xticks(())
        plt.yticks(())
    plt.suptitle('Dictionary learned from face patches\n',
             fontsize=16)
    plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)
    savefig(outputfilename)

    #plt.show()

def save_dict_img(filename, outputfilename):
    patch_size = (7,7)
    imgm = img2mtx(filename)
    imgm = imgm[:7**3, :7**3, :]
    data = mtx2patches(imgm)
    V = learn_dictionary(data)
    plot_dictionary(V, outputfilename)


if __name__ == "__main__": 

    #Take image 'kiiski.jpg' as an input, compute 
    #dictionary and export dictionary plot to file named 'dict.png'
    save_dict_img('kiiski.jpg', 'dict')
    
