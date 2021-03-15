/**
 * Complexity (n = length of url, q = number of queries)
 * Time complexity: O(1) amortized
 * Space complexity: O(n * q)
 */

type Codec struct {
	url2code map[string]string
	code2url map[string]string
}

func Constructor() Codec {
	return Codec{make(map[string]string), make(map[string]string)}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	if code, ok := this.url2code[longUrl]; ok {
		return "http://tinyurl.com/" + code
	}

	ok := true
	code := ""
	for ok {
		code = randomString(7)
		_, ok = this.url2code[code]
	}

	this.url2code[longUrl] = code
	this.code2url[code] = longUrl
	return "http://tinyurl.com/" + code
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	split := strings.Split(shortUrl, "/")
	return this.code2url[string(split[len(split)-1])]
}

const runes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

func randomString(length int) string {
	output := make([]byte, length)
	for i := 0; i < length; i += 1 {
		output[i] = runes[rand.Intn(len(runes))]
	}
	return string(output)
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
