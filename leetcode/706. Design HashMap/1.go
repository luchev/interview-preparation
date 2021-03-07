/**
 * Complexity (n = number of queries)
 * Time complexity: O(1) Amortized per operation
 * Space complexity: O(n)
 */

type Pair struct {
	Key int
	Val int
}

type MyHashMap struct {
	data       [][]Pair
	capacity   int
	filled     int
	loadfactor float64
}

/** Initialize your data structure here. */
func Constructor() MyHashMap {
	return MyHashMap{
		data:       make([][]Pair, 8),
		capacity:   7,
		filled:     0,
		loadfactor: 0.6,
	}
}

func (this *MyHashMap) grow() {
	newCapacity := this.capacity << 1
	newData := make([][]Pair, newCapacity)
	for _, cell := range this.data {
		for _, pair := range cell {
			newData, _ = insert(newData, pair.Key, pair.Val)
		}
	}
	this.data = newData
	this.capacity = newCapacity
}

func insert(slice [][]Pair, key int, value int) ([][]Pair, bool) {
	position := key % cap(slice)
	if slice[position] == nil {
		slice[position] = make([]Pair, 0)
	}
	for index, pair := range slice[position] {
		if pair.Key == key {
			slice[position][index].Val = value
			return slice, false
		}
	}

	slice[position] = append(slice[position], Pair{key, value})
	return slice, true
}

/** value will always be non-negative. */
func (this *MyHashMap) Put(key int, value int) {
	if float64(this.filled)/float64(this.capacity) > this.loadfactor {
		this.grow()
	}
	newElement := false
	this.data, newElement = insert(this.data, key, value)
	if newElement {
		this.filled += 1
	}
}

/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
	position := key % cap(this.data)
	if this.data[position] == nil {
		return -1
	}

	for _, pair := range this.data[position] {
		if pair.Key == key {
			return pair.Val
		}
	}

	return -1
}

/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int) {
	position := key % cap(this.data)
	if this.data[position] == nil {
		return
	}

	for index, pair := range this.data[position] {
		if pair.Key == key {
			this.data[position] = append(this.data[position][:index], this.data[position][index+1:]...)
			return
		}
	}
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
