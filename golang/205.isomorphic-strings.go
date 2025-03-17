/*
 * @lc app=leetcode id=205 lang=golang
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	mmap := make(map[rune]rune)
	for i, c := range s {
		if val, exists := mmap[c]; exists {
			if val != rune(t[i]) {
				return false
			}
		} else {
			for _, v := range mmap {
				if v == rune(t[i]) {
					return false
				}
			}
			mmap[c] = rune(t[i])
		}
	}

	return true
}

// @lc code=end

