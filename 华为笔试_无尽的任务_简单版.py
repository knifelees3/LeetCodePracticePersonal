# %%
import numpy as np
def func():
    # mison_num=int(input().strip())
    # mison_v_str=input().strip().split()
    # mison_time_str=input().strip().split()
    # mison_dead_str=input().strip().split()

    # mison_v=[]
    # mison_time=[]
    # mison_dead=[]
    # for l in range(mison_num):
    #     mison_v.append(mison_v_str[l])
    #     mison_time.append(mison_time_str[l])
    #     mison_dead.append(mison_dead_str[l])

    mison_num=4
    mison_v=[0,60,100,120]
    mison_time=[0,10,20,30]
    misson_dead=[0,50,50,50]
    dead=50
    val_array=np.zeros(dead+1,dtype=np.int32)
    for l in range(1,mison_num):
        for m in range(dead,0,-1):
            if mison_time[l]<=m:
                val_array[m]=max(val_array[m],val_array[m-mison_time[l]]+mison_v[l])

    value_opt=val_array[-1]
    print(value_opt)
    return value_opt


if __name__ == "__main__":
    func()
# %%