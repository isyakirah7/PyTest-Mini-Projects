#This is a demo of using debugging tools to resolve common defects 

def calculate_average_of_evens(numbers):
    total=0 #sum of even numbers
    count=0 #keeps track of how many even numbers found

    for num in numbers: #loop through each number in the input list
        if num%2==0:
            total=total+num
            count=count+1
    if count==0:
        return 0
    
    return total/count

def main():
    nums={2,4,6,8}
    avg=calculate_average_of_evens(nums)
    print(f"Average of even number:{avg}")

if __name__=="__main__":
    main()