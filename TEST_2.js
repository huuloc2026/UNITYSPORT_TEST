/*
2. Bài toán Two Sum

Mô Tả
    Cho một mảng số nguyên nums và một số nguyên target, hãy tìm tất cả các cặp chỉ số của hai số trong mảng mà tổng của chúng bằng target. Giả định rằng có thể có nhiều cặp thỏa mãn điều kiện này, và bạn cần trả về tất cả các cặp chỉ số khác nhau.

Đầu Vào
    Một mảng số nguyên nums với độ dài n (1 ≤ n ≤ 10^4) chứa các số nguyên. Các số trong mảng có thể là số dương, số âm hoặc số không.
    Một số nguyên target (−10^9 ≤ target ≤ 10^9) là tổng mà bạn cần tìm.
Đầu Ra
    Trả về một mảng hai chiều chứa tất cả các cặp chỉ số (i, j) (0 ≤ i < j < n) sao cho nums[i] + nums[j] == target.
    Nếu không tìm thấy cặp nào, hãy trả về mảng rỗng.
Điều Kiện
    Không sử dụng cùng một phần tử hai lần để tạo thành tổng.
    Các chỉ số trong các cặp trả về phải là duy nhất và không trùng lặp.
    Thứ tự của các cặp trong kết quả không quan trọng.
Ví Dụ
    Ví Dụ 1:

        Input:
            nums = [2, 7, 11, 15]
            target = 9
        Output:
            [[0, 1]]

        Giải Thích: Bởi vì nums[0] + nums[1] == 2 + 7 == 9, trả về cặp chỉ số [0, 1].

    Ví Dụ 2:

        Input:
            nums = [3, 2, 4, 3]
            target = 6
        Output:
            [[1, 2], [0, 3]]
            
        Giải Thích: Cả hai cặp [2, 4] (tại chỉ số [1, 2]) và [3, 3] (tại chỉ số [0, 3]) đều có tổng bằng 6.

*/

function TwoSum(nums, target) {
    let map = new Map(); 
    let result = []; 

    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i]; 
        if (map.has(complement)) {
            result.push([map.get(complement), i]); 
        }
        map.set(nums[i], i);
    }

    return result;
}

console.log(TwoSum([2,7,11,15],9))
console.log(TwoSum([3, 2, 4, 3], 6))