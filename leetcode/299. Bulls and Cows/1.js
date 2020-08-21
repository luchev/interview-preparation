/**
 * Complexity (n = digits in the number)
 * Time complexity: O(n)
 * Space complexity: O(1)
 * Space is constant because our alphabet is of constant size [0-9]
 */
var getHint = function ( secret, guess ) {
    let bulls = 0;
    let missedGuess = '';
    let map = {};
    for ( let i = 0; i < secret.length; i++ ) {
        if ( secret[i] === guess[i] ) {
            bulls++;
        } else {
            map[secret[i]] = ( map[secret[i]] || 0 ) + 1;
            missedGuess += guess[i]; // lengths are always equal so we're good here
        }
    }

    let cows = 0;
    for ( let c of missedGuess ) {
        if ( map[c] && map[c] >= 1 ) {
            cows++;
            map[c] -= 1;
        }
    }
    return bulls + 'A' + cows + 'B';
};
