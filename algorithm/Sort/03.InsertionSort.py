'''
插入排序：

通过构造有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置插入
实现上，在从后向前扫描过程中，需要反复把已排序的元素逐步向后挪位，为新元素提供插入空间

时间复杂度

最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n2)
稳定性：稳定
'''

def insertion_sort(source_list:list):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(source_list)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if source_list[j] < source_list[j-1]:
                source_list[j], source_list[j-1] = source_list[j-1], source_list[j]


l = [54,26,93,17,77,44,31,20]
insertion_sort(l)
print(l)



