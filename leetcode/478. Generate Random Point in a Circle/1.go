/**
 * Complexity ()
 * Time complexity: O(1) expected
 * Space complexity: O(1) amortized
 */

type Solution struct {
	radius   float64
	x_center float64
	y_center float64
}

func Constructor(radius float64, x_center float64, y_center float64) Solution {
	return Solution{radius, x_center, y_center}
}

func (this *Solution) RandPoint() []float64 {
	x := 1.0
	y := 1.0
	for math.Sqrt(x*x+y*y) >= 1 {
		x = rand.Float64()
		if rand.Intn(2) == 0 {
			x = -x
		}

		y = rand.Float64()
		if rand.Intn(2) == 0 {
			y = -y
		}
	}

	ans := make([]float64, 2)
	ans[0] = x*this.radius + this.x_center
	ans[1] = y*this.radius + this.y_center
	return ans
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(radius, x_center, y_center);
 * param_1 := obj.RandPoint();
 */
