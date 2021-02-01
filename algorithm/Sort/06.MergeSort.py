'''
归并排序：

归并排序是采用分治法的一个典型应用。归并排序的思想就是先递归分解数组，再合并数组。

将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。


时间复杂度

最优时间复杂度：O(nlogn)
最坏时间复杂度：O(nlogn)
稳定性：稳定
'''

def merge_sort(source_list:list):
    if len(source_list) <= 1:
        return source_list
    # 二分分解
    num = int(len(source_list)/2) 
    left = merge_sort(source_list[:num])
    right = merge_sort(source_list[num:])
    # 合并
    return merge(left,right)

def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    #left与right的下标指针
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


alist = [54,26,93,17,77,31,44,55,20]
sorted_alist = merge_sort(alist)
print(sorted_alist)