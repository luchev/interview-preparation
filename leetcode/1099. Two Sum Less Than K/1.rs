///Complexity (n = input array size)
///Time complexity: O(n^2) but works very fast because of small input size and CPU cache
///Space complexity: O(1)
use std::cmp::max;

impl Solution {
    pub fn two_sum_less_than_k(a: Vec<i32>, k: i32) -> i32 {
        let mut s: i32 = -1;
        for i in 0..a.len() {
            for j in i+1..a.len() {
                if a[i] + a[j] < k {
                    s = max(s, a[i] + a[j]);
                }
            }
        }
        s
    }
}
