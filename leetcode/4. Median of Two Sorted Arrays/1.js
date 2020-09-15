/**
 * Complexity (n = nums1 size, m = nums2 size)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */
var findMedianSortedArrays = function ( nums1, nums2 ) {
    let merged = [];
    nums1.push( Infinity );
    nums2.push( Infinity );
    let left = 0;
    let right = 0;

    while ( nums1[left] !== Infinity || nums2[right] !== Infinity ) {
        if ( nums1[left] <= nums2[right] ) {
            merged.push( nums1[left] );
            left++;
        } else {
            merged.push( nums2[right] );
            right++;
        }
    }

    if ( merged.length % 2 == 0 ) {
        return ( merged[merged.length / 2 - 1] + merged[merged.length / 2] ) / 2;
    } else {
        return merged[Math.floor( merged.length / 2 )];
    }
};
