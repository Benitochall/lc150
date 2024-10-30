
def threeSum(nums):
    n = sorted(nums)
    solution_list = []
    # we don't want to use the same l twice and do not want to use the same a twice

    for i in range(len(n)):
            # skip duplicate starting numbers 
            if i != 0 and n[i] == n[i-1]:
                continue
            l= i+1
            r=len(n) -1
            while l < r:
                s = n[i] + n[l] + n[r]
                if s > 0:
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    solution_list.append([n[i], n[l], n[r]])
                    l+=1
                    r-=1
                    # skp duplicate middle numbers
                    # [-2,-2,1,1,2,2]
                    while n[l] == n[l-1] and l <r:
                        l+=1


    return solution_list
    
print(threeSum([-2,-2,0,0,2,2]))