def calculate(inputArr):
    import numpy as np
    if len(inputArr) < 9:
        return 'List must contain nine numbers'
    inputArr = np.array(inputArr).reshape(3,3)
    # calculating mean for numpy array
    mean_ax1 = inputArr.mean(axis=0)
    mean_ax2 = inputArr.mean(axis=1)
    mean_flat = inputArr.flatten().mean()
    #calculate variance for numpy array
    var_ax1 = inputArr.var(axis=0)
    var_ax2 = inputArr.var(axis=1)
    var_flat = inputArr.flatten().var()
    #calculate standard deviation for numpy array
    std_ax1 = inputArr.std(axis=0)
    std_ax2 = inputArr.std(axis=1)
    std_flat = inputArr.flatten().std()
    #find max in numpy array
    max_ax1 = inputArr.max(axis=0)
    max_ax2 = inputArr.max(axis=1)
    max_flat = inputArr.flatten().max()
    #find min in numpy array
    min_ax1 = inputArr.min(axis=0)
    min_ax2 = inputArr.min(axis=1)
    min_flat = inputArr.flatten().min()
    #calculate sum for numpy array
    sum_ax1 = inputArr.sum(axis=0)
    sum_ax2 = inputArr.sum(axis=1)
    sum_flat = inputArr.sum()
    
    output = {
        'mean' : [mean_ax1, mean_ax2, mean_flat],
        'variance' : [var_ax1, var_ax2, var_flat],
        'standard deviation' : [std_ax1, std_ax2, std_flat],
        'max' : [max_ax1, max_ax2, max_flat],
        'min' : [min_ax1, min_ax2, min_flat],
        'sum' : [sum_ax1, sum_ax2, sum_flat]
    }
    
    return output