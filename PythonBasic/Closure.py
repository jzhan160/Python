# get the average of a stream

# ave() is an inner function of make_ave and can get access to the local var of the outer function such as nums[]
# but nums[] is invisible to scope out of the outer function so it is safe.
# The outer function will return the inner function.
def make_ave():
    nums = []

    def ave(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return ave

average = make_ave()
print(average(1))
print(average(2))
print(average(3))