/**
 * Complexity (n = legth of version1, m = length of version2)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */
var compareVersion = function ( version1, version2 ) {
    let v1 = version1.split( '.' ).map( x => parseInt( x ) );
    let v2 = version2.split( '.' ).map( x => parseInt( x ) );
    for ( let i = 0; i < Math.max( v1.length, v2.length ); i++ ) {
        let v1Num = v1[i] !== undefined ? v1[i] : 0;
        let v2Num = v2[i] !== undefined ? v2[i] : 0;

        if ( v1Num < v2Num ) {
            return -1;
        } else if ( v1Num > v2Num ) {
            return 1;
        }
    }
    return 0;
};
