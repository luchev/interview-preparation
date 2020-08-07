/**
 * Complexity (n = input length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut parentheses : Vec<char> = Vec::new();
        for c in s.chars() {
            if c == '{' || c == '(' || c == '[' {
                parentheses.push(c);
            } else if c == ')' {
                if parentheses.len() > 0 {
                    let paren = parentheses.pop();
                    if paren != Some('(') {
                        return false;
                    }
                } else {
                    return false;
                }
            } else if c == '}' {
                if parentheses.len() > 0 {
                    let paren = parentheses.pop();
                    if paren != Some('{') {
                        return false;
                    }
                } else {
                    return false;
                }
            } else if c == ']' {
                if parentheses.len() > 0 {
                    let paren = parentheses.pop();
                    if paren != Some('[') {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }

        return parentheses.len() == 0;
    }
}
