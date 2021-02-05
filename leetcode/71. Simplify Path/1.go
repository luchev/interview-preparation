/**
 * Complexity (n = length of path)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

func simplifyPath(path string) string {
	fields := strings.Split(path, "/")
	pathParts := make([]string, 0)
	for _, field := range fields {
		if field == "." {
			// pass
		} else if field == ".." {
			if len(pathParts) > 0 {
				pathParts = pathParts[:len(pathParts)-1]
			}
		} else if field != "" {
			pathParts = append(pathParts, field)
		}
	}

	if len(pathParts) == 0 {
		return "/"
	}
	return "/" + strings.Join(pathParts, "/")
}
