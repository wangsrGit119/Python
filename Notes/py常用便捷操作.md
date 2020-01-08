###  常用的便捷操作
```
import time


# 重复元素判定
def all_unique_number_list(lst):
    return len(lst) == len(set(lst))


# 英文段落首字母大写
def ele_to_big(s):
    return s.title()


# 单词首字母小写或者大写
def word_big_small(ti, word):
    if ti == 1:
        return word[:1].lower() + word[1:]
    elif ti == 2:
        return word[:1].title() + word[1:]
    else:
        return word


#  回文序列判断
def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]


x = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 8]
y = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    start_time = time.time()
    #  all_unique_number_list 测试用例
    print(all_unique_number_list(x))  # False
    print(all_unique_number_list(y))  # True
    print(set(x))  # {1, 2, 3, 4, 5, 6, 7, 8}
    #  ele_to_big  测试用例
    s1 = "my name is ok "
    print(ele_to_big(s1))  # My Name Is Ok
    print(s1[1:].lower())
    print(s1[:1].title())
    #  word_big_small  测试用例
    word_test = "hello"
    print(word_big_small(2, word_test))
    # palindrome 测试用例
    print(palindrome("abba"))
    end_time = time.time()
    print("执行时间：", end_time-start_time)
```