/**
 * Complexity
 * Time complexity per operation: O(1)
 * Space overhead: O(1)
 */

/*   Below is the interface for Iterator, which is already defined for you.
 *
 *   type Iterator struct {
 *
 *   }
 *
 *   func (this *Iterator) hasNext() bool {
 *		// Returns true if the iteration has more elements.
 *   }
 *
 *   func (this *Iterator) next() int {
 *		// Returns the next element in the iteration.
 *   }
 */

type PeekingIterator struct {
	iter        *Iterator
	buffer      int
	isBufferNil bool
}

func Constructor(iter *Iterator) *PeekingIterator {
	return &PeekingIterator{
		iter,
		0,
		true,
	}
}

func (this *PeekingIterator) hasNext() bool {
	return this.iter.hasNext() || !this.isBufferNil
}

func (this *PeekingIterator) next() int {
	if this.isBufferNil {
		return this.iter.next()
	} else {
		this.isBufferNil = true
		return this.buffer
	}
}

func (this *PeekingIterator) peek() int {
	if this.isBufferNil {
		this.buffer = this.iter.next()
		this.isBufferNil = false
	}
	return this.buffer
}
