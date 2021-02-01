'''
希尔排序：

希尔排序是插入排序的一种，也称为缩小增量排序，是直接插入排序算法的一种更高效的改进版
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

希尔排序的基本思想是：
将数组列在一个表中并对列分别进行插入排序，重复这过程，
不过每次用更长的列（步长更长了，列数更少了）来进行。
最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

时间复杂度

最优时间复杂度：根据步长序列的不同而不同
最坏时间复杂度：O(n2)
稳定想：不稳定
'''


def shell_sort(source_list:list):
    n = len(source_list)
    # 初始步长
    gap = int(n/2)

    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and source_list[j - gap] > source_list[j]:
                source_list[j - gap], source_list[j] = source_list[j], source_list[j - gap]
                j -= gap
        # 得到新的步长
        gap = int(gap/2) 


l = [54,26,93,17,77,44,31,20]
shell_sort(l)
print(l)