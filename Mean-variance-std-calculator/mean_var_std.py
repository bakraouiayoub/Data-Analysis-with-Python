import numpy as np

def calculate(input_list):
    if len(input_list)!=9:
        raise ValueError("List must contain nine numbers.")
    input_arr=np.array(input_list).reshape((3,3))
    output_dict={'mean':[np.mean(input_arr,axis=0).tolist(),np.mean(input_arr,axis=1).tolist(),np.mean(input_arr).tolist()]}
    output_dict['variance']=[np.var(input_arr,axis=0).tolist(),np.var(input_arr,axis=1).tolist(),np.var(input_arr).tolist()]
    output_dict['standard deviation']=[np.std(input_arr,axis=0).tolist(),np.std(input_arr,axis=1).tolist(),np.std(input_arr).tolist()]
    output_dict['max']=[np.max(input_arr,axis=0).tolist(),np.max(input_arr,axis=1).tolist(),np.max(input_arr).tolist()]
    output_dict['min']=[np.min(input_arr,axis=0).tolist(),np.min(input_arr,axis=1).tolist(),np.min(input_arr).tolist()]
    output_dict['sum']=[np.sum(input_arr,axis=0).tolist(),np.sum(input_arr,axis=1).tolist(),np.sum(input_arr).tolist()]
    return output_dict
