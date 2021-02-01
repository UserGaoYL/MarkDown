'''
选择排序：

1、在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2、从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列末尾
3、以此类推，直到所有元素均排序完毕

主要优点与数据移动有关。如果某个元素位于正确的位置，则它不会移动。
每次交换一对元素，它们当中至少有一个元素将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换
在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种

时间复杂度

最优时间复杂度：O(n2)
最坏时间复杂度：O(n2)
稳定性：不稳定（考虑升序每次选择最大的情况）
'''

def selection_sort(source_list:list):
    n = len(source_list)
    # 进行n-1次选择
    for i in range(n - 1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选出最小数据
        for j in range(i+1, n):
            if source_list[j] < source_list[min_index]:
                min_index = j
        # 选择出的元素不在正确位置，则交换位置
        if min_index != i:
            source_list[min_index], source_list[i] = source_list[i], source_list[min_index]


l = [54,26,93,17,77,44,31,20]
selection_sort(l)
print(l)
