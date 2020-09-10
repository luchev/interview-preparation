/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */


/**
 * Complexity (n = nodes in tree 1, m = nodes in tree 2)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */

var getAllElements = function ( root1, root2 ) {
    let arr1 = [];
    inorder( root1, arr1 );
    let arr2 = [];
    inorder( root2, arr2 );

    return merge( arr1, arr2 );
};

function inorder( root, result ) {
    if ( root ) {
        inorder( root.left, result );
        result.push( root.val );
        inorder( root.right, result );
    }
}

function merge( arr1, arr2 ) {
    let result = [];
    arr1.push( Infinity );
    arr2.push( Infinity );
    let p1 = 0;
    let p2 = 0;
    while ( arr1[p1] !== Infinity || arr2[p2] !== Infinity ) {
        if ( arr1[p1] <= arr2[p2] ) {
            result.push( arr1[p1] );
            p1++;
        } else {
            result.push( arr2[p2] );
            p2++;
        }
    }

    arr1.pop();
    arr2.pop();

    return result;
}
