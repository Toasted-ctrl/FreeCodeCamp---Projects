import numpy as np

def calculate(list):

    #determining number of items in list
    length = len(list)

    #if list contains less than 9 items, raise ValueError
    if length < 9:
        raise ValueError("List must contain nine numbers.")

    #if list does not contain less than 9 items, proceed with below
    else:

        #converting list to array
        array_from_list = np.array(list)

        #reshaping array into 3x3 matrix
        arranged_array = array_from_list.reshape((3,3))

        #calculating mean for axis = 1, axis = 0, and flattened array
        mean_axis_1 = np.mean(arranged_array, axis=0)
        mean_axis_2 = np.mean(arranged_array, axis=1)
        mean_flattened = np.mean(array_from_list)

        #calculating variance for axis = 1, axis = 0, and flattened array
        variance_axis_1 = np.var(arranged_array, axis=0)
        variance_axis_2 = np.var(arranged_array, axis=1)
        variance_flattened = np.var(array_from_list)

        #calculating standard deviation for axis = 1, axis = 0, and flattened array
        stdev_axis_1 = np.std(arranged_array, axis=0)
        stdev_axis_2 = np.std(arranged_array, axis=1)
        stdev_flattened = np.std(array_from_list)

        #calculating max for axis = 1, axis = 0, and flattened array
        max_axis_1 = np.max(arranged_array, axis=0)
        max_axis_2 = np.max(arranged_array, axis=1)
        max_flattened = np.max(array_from_list)

        #calculating min for axis = 1, axis = 0, and flattened array
        min_axis_1 = np.min(arranged_array, axis=0)
        min_axis_2 = np.min(arranged_array, axis=1)
        min_flattened = np.min(array_from_list)

        #calculating sum for axis = 1, axis = 0, and flattened array
        sum_axis_1 = np.sum(arranged_array, axis=0)
        sum_axis_2 = np.sum(arranged_array, axis=1)
        sum_flattened = np.sum(array_from_list)

        #creating dictinary for return, incuding converting numpy arrays to python lists
        calculations = {
            'mean': [np.ndarray.tolist(mean_axis_1), np.ndarray.tolist(mean_axis_2), mean_flattened],
            'variance': [np.ndarray.tolist(variance_axis_1), np.ndarray.tolist(variance_axis_2), variance_flattened],
            'standard deviation': [np.ndarray.tolist(stdev_axis_1), np.ndarray.tolist(stdev_axis_2), stdev_flattened],
            'max': [np.ndarray.tolist(max_axis_1), np.ndarray.tolist(max_axis_2), max_flattened],
            'min': [np.ndarray.tolist(min_axis_1), np.ndarray.tolist(min_axis_2), min_flattened],
            'sum': [np.ndarray.tolist(sum_axis_1), np.ndarray.tolist(sum_axis_2), sum_flattened]
        }

        return calculations