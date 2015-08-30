def max2diff(X):
    #define a function to find the pair with max difference
    def maxdiff(x):
        currentdiff=0
        temp=[0,0]
        result=temp[:]
        while temp[1]<len(x)-1:
            temp[1]=temp[1]+1
            next_diff=x[temp[1]]-x[temp[0]]
            if next_diff>currentdiff:
                result=temp[:]
                currentdiff=next_diff
            if next_diff<0:
                temp[0]=temp[1]
        return result

    #select the sub-array with max sum:
    max_ind=maxdiff(X)
    X_max=X[max_ind[0]:max_ind[1]+1]
    X_max_val=X[max_ind[1]]-X[max_ind[0]]

    X_left=X[:max_ind[0]]
    X_right=X[max_ind[1]+1:]
    l_left=len(X_left)
    l_max=len(X_max)
    #find the max for left and right part
    if X_left:
        X_l_max=maxdiff(X_left)
        diff_l=X_left[X_l_max[1]]-X_left[X_l_max[0]]
    else:
        diff_l=0
    if X_right:
        X_r_max=maxdiff(X_right)
        diff_r=X_right[X_r_max[1]]-X_right[X_r_max[0]]
    else:
        diff_r=0
    #find the sub-array with minimal sum in X_sum
    X_neg=map(lambda x:-x,X_max)
    min_ind=maxdiff(X_neg)
    max_min=-(X_neg[min_ind[1]]-X_neg[min_ind[0]])

    #there are several situations:
    #1. the two arrays with maximal diff are both subarrays of X_max, their sum is X_max_val-max_min
    #2. the two arrays are X_max and one of X_l_max and X_r_max
    diff_1=X_max_val-max_min
    diff_2=X_max_val+max([diff_l,diff_r])

    result=[]
    temp_result={}
    if diff_1>=diff_2:
        if max_min==0:#only X_max
            if max_ind[0]==max_ind[1]:
                max_ind=[]
            for i in max_ind:
                temp_result[i+1]=X[i]
            result.append(temp_result)
        else: #two pairs in X_max
            print 'b'
            index=[[max_ind[0],l_left+min_ind[0]],[l_left+min_ind[1],max_ind[1]]]
            for i in index:
                temp_result={}
                for j in i:
                    temp_result[j+1]=X[j]
                result.append(temp_result)
    else:#in this case max(diff_l,diff_r) can't be 0
        if diff_l>=diff_r:
            index=[X_l_max,max_ind]
            for i in index:
                temp_result={}
                for j in i:
                    temp_result[j+1]=X[j]
                result.append(temp_result)
        else:
            index=[max_ind,map(lambda i:i+l_left+l_max,X_r_max)]
            for i in index:
                temp_result={}
                for j in i:
                    temp_result[j+1]=X[j]
                result.append(temp_result)
    return result

print max2diff([5,4,3])
