import pickle
import numpy as np


def main():
    print('Enter the ID of the dataset you want to transoform (currently 4 available)')
    dataset_id = input()
    # Open the pickled dataset
    print('Loading dataset...')
    with open('dataset/LLD_icon_pickle/LLD-icon_data_' + dataset_id + '.pkl', 'rb') as file:
        images = pickle.load(file, encoding='bytes')
    file.close()
    print('Finished')

    # Clip the values from range [0;255] to range [0;1]
    print('Clipping the values...')
    images = images / 255.0
    print('Finished')

    # Change the data type from float64 to float32
    print('Changing the data type...')
    images.astype('float32')
    print('Finished')

    # Serialize the transformed dataset as a numpy array with *.npy extension
    print('Serializing the new object...')
    np.save('dataset/LLD_icon_numpy/dataset' + dataset_id + '.npy', images)
    print('Finished')


if __name__ == '__main__':
    main()
