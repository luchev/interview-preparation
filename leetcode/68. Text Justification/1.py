# Complexity (n = number of words, k = average word length)
# Time complexity: O(n * k)
# Space complexity: O(n * k)

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = splitLines(words, maxWidth)
        for index, line in enumerate(lines[:-1]):
            if len(line) == 1:
                lines[index] = padRight(line, maxWidth)
            else:
                lines[index] = padInside(line, maxWidth)

        lines[-1] = padRight(lines[-1], maxWidth)
        return lines


def padInside(words: List[str], width: int) -> str:
    total_spaces = width - sum(len(word) for word in words)
    space_between_words = total_spaces // (len(words) - 1)
    k_places_with_more_spaces = total_spaces % (len(words) - 1)

    line = [words[0]]
    for word in words[1:]:
        spaces_to_insert = space_between_words
        if k_places_with_more_spaces > 0:
            spaces_to_insert += 1
            k_places_with_more_spaces -= 1
        line.append(' ' * spaces_to_insert)
        line.append(word)

    return ''.join(line)


def padRight(words: List[str], width: int) -> str:
    line = ' '.join(words)
    return line + (width - len(line)) * ' '


def splitLines(words: List[str], maxWidth: int) -> List[List[str]]:
    lines = [[]]
    current_line_len = 0
    for word in words:
        if current_line_len + len(word) <= maxWidth:
            lines[-1].append(word)
            current_line_len += len(word) + 1
        else:
            lines.append([word])
            current_line_len = len(word) + 1

    return lines
