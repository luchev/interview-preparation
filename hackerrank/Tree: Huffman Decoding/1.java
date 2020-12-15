/**
 * Complexity (n = input string length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/*  
class Node
    public  int frequency; // the frequency of this tree
    public  char data;
    public  Node left, right;
    
*/ 
void decode(String s, Node root) {
    Node ptr = root;
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == '0') {
            ptr = ptr.left;
        } else if (s.charAt(i) == '1') {
            ptr = ptr.right;
        }
        if (ptr.data != '\0') {
            System.out.print(ptr.data);
            ptr = root;
        }
    }
}
