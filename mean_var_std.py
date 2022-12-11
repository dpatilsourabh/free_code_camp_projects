import numpy as np

def calculate(list):
    if len(list) < 9:
        return 'List must contain nine numbers'
    list = np.array(list).reshape(3,3)
    # calculating mean for numpy array
    mean_ax1 = list.mean(axis=0)
    mean_ax2 = list.mean(axis=1)
    mean_flat = list.flatten().mean()
    #calculate variance for numpy array
    var_ax1 = list.var(axis=0)
    var_ax2 = list.var(axis=1)
    var_flat = list.flatten().var()
    #calculate standard deviation for numpy array
    std_ax1 = list.std(axis=0)
    std_ax2 = list.std(axis=1)
    std_flat = list.flatten().std()
    #find max in numpy array
    max_ax1 = list.max(axis=0)
    max_ax2 = list.max(axis=1)
    max_flat = list.flatten().max()
    #find min in numpy array
    min_ax1 = list.min(axis=0)
    min_ax2 = list.min(axis=1)
    min_flat = list.flatten().min()
    #calculate sum for numpy array
    sum_ax1 = list.sum(axis=0)
    sum_ax2 = list.sum(axis=1)
    sum_flat = list.sum()
    
    calculations = {
        'mean' : [mean_ax1, mean_ax2, mean_flat],
        'variance' : [var_ax1, var_ax2, var_flat],
        'standard deviation' : [std_ax1, std_ax2, std_flat],
        'max' : [max_ax1, max_ax2, max_flat],
        'min' : [min_ax1, min_ax2, min_flat],
        'sum' : [sum_ax1, sum_ax2, sum_flat]
    }
    
    return calculations
