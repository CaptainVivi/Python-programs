def find_numbers_and_sum():
    count = 0
    total_sum = 0
    
    for number in range(101, 200):
        if number % 7 == 0:
            count += 1
            total_sum += number
    
    return count, total_sum

def main():
    count, total_sum = find_numbers_and_sum()
    print(f"The number of integers greater than 100 and less than 200 that are divisible by 7 is: {count}")
    print(f"The sum of these integers is: {total_sum}")

if __name__ == "__main__":
    main()
