/**
 * Complexity (n = input string length)
 * Time complexity: O(n)
 * Space complexity: O(ALPHABET SIZE)
 */
var isIsomorphic = function ( s, t ) {
    if ( s.length !== t.length ) {
        return false;
    }
    let sToT = {}; // todo better names for this hash map
    let tToS = {};

    for ( let i = 0; i < s.length; i++ ) {
        if ( sToT[s[i]] === undefined ) {
            sToT[s[i]] = t[i];
        } else {
            if ( sToT[s[i]] !== t[i] ) {
                return false;
            }
        }

        if ( tToS[t[i]] === undefined ) {
            tToS[t[i]] = s[i];
        } else {
            if ( tToS[t[i]] !== s[i] ) {
                return false;
            }
        }
    }

    return true;
};

// S = E G Y
// T = A D D
//         |
// {E -> A, G -> D, Y -> D}
// {A -> E, D -> G}
