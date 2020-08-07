package daily17;

import java.security.InvalidParameterException;
import java.util.Stack;

class Daily17 {
    // Iterate the string with this index
    private int currentIndex = 0;
    // Object-wide variable to pass info between the readNextName function and findLongestAbsoluteFileName
    private int currentTokenTabs = 0;
    // Stack keeping the current path
    private Stack<String> parents = new Stack<>();

    private boolean isTab(char character) {
        return character == '\t';
    }

    private boolean isNewLine(char character) {
        return character == '\n';
    }

    /**
     * Return the next partial path of a file/dir from the filesystem string and also save its indentation
     * in currentTokenTabs
     *
     * Complexity (n = input string length)
     * Time complexity: Amortized O(1), Overall - O(n)
     *
     * @param filesystem - string to read the next partial path from
     * @param startIndex - index to start reading from
     * @return - return a file path and save its indentation in the currentTokenTabs variable
     */
    private String readNextName(String filesystem) {
        currentTokenTabs = 0;
        // Count the number of tabs in the next token and move the start index we get a substring from
        // to the corresponding place
        int startIndex = currentIndex;
        while (startIndex < filesystem.length() && isTab(filesystem.charAt(startIndex))) {
            startIndex++;
            currentTokenTabs++;
        }

        // Move the end index which we'll use to substring
        int endIndex = startIndex;
        while (endIndex < filesystem.length() && !isNewLine(filesystem.charAt(endIndex))) {
            endIndex++;
        }

        // +1 for the new line character we need to ignore
        currentIndex = endIndex + 1;

        return filesystem.substring(startIndex, endIndex);
    }

    /**
     * Find the longest absolute path in a serialized filesystem tree as string
     *
     * Complexity (n = length of input)
     * Time complexity: O(n)
     * Space complexity: O(n)
     * Actual space complexity O(depth of filesystem)
     *
     * @param filesystem - serialized filesystem
     * @return - longest path in the filesystem
     */
    int findLongestAbsoluteFileName(String filesystem) {
        int longestName = 0;
        currentIndex = 0;
        int currentLength = 0;
        parents.clear();

        while (currentIndex < filesystem.length()) {
            String fileName = readNextName(filesystem);
            if (currentTokenTabs < parents.size()) {
                // Pop all the old directories we've entered, until we reach the same level as the current
                // item being added. This inner loop may seem to make for a quadratic complexity, but
                // we can pop only as many items as we've added, and because we add items only once per iteration
                // of the outer loop, this loop is executed at most N times if the outer loop is executed N times
                while (parents.size() > currentTokenTabs) {
                    String previous = parents.pop();
                    currentLength -= 1 + previous.length();
                }
            } else if (currentTokenTabs == 0) {
                // Executed only once when adding the root
                parents.push(fileName);
                currentLength += fileName.length();
                continue;
            }

            // Check if the current depth in the file system is correct and if so - add the new file to the
            // current path, file can be directory or regular file
            if (currentTokenTabs != 0 && currentTokenTabs == parents.size()) {
                parents.push(fileName);
                currentLength += 1 + fileName.length();
            } else {
                throw new InvalidParameterException("File system is invalid");
            }

            // Check if the current path we have is longer than any previous one and if so make the current one
            // the longest one so far.
            if (currentLength > longestName) {
                longestName = currentLength;
            }
        }

        return longestName;
    }
}
