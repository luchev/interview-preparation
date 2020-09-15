/**
 * Complexity (n = window size, q = number of queries)
 * Time complexity: O(q)
 * Space complexity: O(n) if we think of this.numbers as a queue
 */

// Constructor
var MovingAverage = function ( size ) {
    this.size = size;
    this.currentSum = 0;
    this.numbers = [];
};

// MovingAverage.next(X)
MovingAverage.prototype.next = function ( val ) {
    this.numbers.push( val );
    this.currentSum += val;

    if ( this.numbers.length > this.size ) {
        this.currentSum -= this.numbers.shift();
    }

    return this.currentSum / this.numbers.length;
};
