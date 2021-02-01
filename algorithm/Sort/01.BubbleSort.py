'''
冒泡排序算法：
1、比较相邻的元素。如果第一个比第二个大（升序），则交换两个位置
2、对每一对相邻的元素作相同的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数
3、针对所有的元素重复以上步骤，除了最后一个
4、持续每次对越来越少的元素重复上边的步骤，直到没有任何一对数字需要比较


时间复杂度

最优时间复杂度：O(n)（表示遍历一次发现没有任何元素可以交换，排序结束）
最坏事件复杂度：O(n²)
稳定性：稳定

'''


def bubble_sort(source_list:list):
    t = range(len(source_list) - 1, 0, -1)
    for j in t:
        # j每次需要遍历比较的次数是逐渐减小的
        for i in range(j):
            if source_list[i] > source_list[i + 1]:
                source_list[i], source_list[i+1] = source_list[i+1],source_list[i]


l = [54,26,93,17,77,44,31,20]
bubble_sort(l)
print(l)