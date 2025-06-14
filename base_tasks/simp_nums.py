
def simp_nums(n : int) :
    nums = [i for i in range(n + 1)]

    i = 2
    while i <= n :

        if nums[i] != 0 :
            j = i + i

            while j <= n :
                nums[j] = 0
                j = j + i
    i += 1
    nums = [i for i in nums if i != 0]
    return(nums)

s = int(input('число '))
line = simp_nums(s)
print(line)

if __name__ == "__main__":
    print(line)

    


