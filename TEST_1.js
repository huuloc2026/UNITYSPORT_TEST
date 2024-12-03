/*
1. Thuật toán kiểm tra chuỗi đối xứng.

Cho một chuỗi s, viết một thuật toán để kiểm tra xem chuỗi đó có phải là chuỗi đối xứng hay không. Một chuỗi đối xứng là chuỗi có thứ tự ký tự giống nhau 
khi đọc từ trái sang phải và từ phải sang trái. Ví dụ: "radar" và "level" là các chuỗi đối xứng.

Đầu Vào
    Một chuỗi s chứa các ký tự chữ cái, chữ số và ký tự đặc biệt (0 ≤ độ dài của s ≤ 10^5).
Đầu Ra
    Trả về true nếu chuỗi s là chuỗi đối xứng, ngược lại trả về false.

Ví Dụ
    Ví Dụ 1:
        Input: "level"
        Output: true
        Giải Thích: "level" đọc từ trái sang phải và từ phải sang trái đều giống nhau.
    Ví Dụ 2:
        Input: "hello"
        Output: false
        Giải Thích: "hello" không giống nhau khi đọc từ hai chiều.
*/

function isPalindrome(s){
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        if (s[left] !== s[right]) {
            return false; 
        }
        left++;
        right--;
    }
    return true

}
console.log(isPalindrome('radar')); 
console.log(isPalindrome('level')); 
console.log(isPalindrome('hello')); 