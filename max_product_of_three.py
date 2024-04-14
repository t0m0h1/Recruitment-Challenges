from typing import List

def max_product_of_three(nums: List[int]) -> int:
    if len(nums) < 3:
        raise ValueError("Input list must have at least three elements")
    
    sorted_nums = sorted(nums)
    return max(sorted_nums[0] * sorted_nums[1] * sorted_nums[-1], sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3])

if __name__ == '__main__':
    # Test the function with sample inputs
    input_list = [-3, 1, 2, -2, 5, 6]
    input_list2 = [5, 6, 7, 8, 9, 10]
    
    print(max_product_of_three(input_list))  # Output: 60
    print(max_product_of_three(input_list2))  # Output: 720



    """
    Calculates the maximum product of three integers in a given list.

    Args:
        nums (List[int]): The input list of integers.

    Returns:
        int: The maximum product of three integers.

    Raises:
        ValueError: If the input list has less than three elements.
    """






