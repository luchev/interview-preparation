package daily11;

import java.util.ArrayList;
import java.util.HashMap;

class Trie {
    private TrieNode root;

    private ArrayList<String> words = new ArrayList<>();

    Trie() {
        root = new TrieNode();
    }

    /**
     * Add a new word to the trie
     * Complexity (n = word length)
     * Time complexity: O(n)
     *
     * @param word - string as a word to add to the trie
     */
    void addWord(String word) {
        TrieNode iterator = root;
        for (int i = 0; i < word.length(); i++) {
            iterator.addTransition(word.charAt(i));
            iterator = iterator.getTransitionWith(word.charAt(i));
        }
        iterator.setWordEnd(true);
    }

    /**
     * Recursively generate all suffixes to the given word from the current node
     * Add a new word to the trie
     * Complexity (n = number of nodes in trie)
     * Time complexity: O(n)
     * Worst case we will have O( (sizeof alphabet)^depth of trie)
     * which is a horrible complexity
     *
     * @param root - current node in the trie
     * @param current - word so far
     */
    private void generateWords(TrieNode root, StringBuilder current) {
        if (root.isWordEnd()) {
            words.add(current.toString());
        }

        HashMap<Character, TrieNode> transitions = root.getTransitions();
        if (root.getTransitions() != null) {
            for (Character character : transitions.keySet()) {
                StringBuilder nextPrefix = new StringBuilder(current);
                nextPrefix.append(character);
                generateWords(transitions.get(character), nextPrefix);
            }
        }

    }

    /**
     * Generate all the words with a given prefix recursively
     * Time complexity can be improved with precomputing all the words for each node
     * but this will worsen the space complexity to exponential
     * It's either exponential time or space complexity
     *
     * @param prefix - look for words starting with this
     * @return list of words in the current trie with the given prefix
     */
    ArrayList<String> getWordsWithPrefix(String prefix) {
        words.clear();

        TrieNode iterator = root;
        for (int i = 0; i < prefix.length(); i++) {
            iterator = iterator.getTransitionWith(prefix.charAt(i));
            if (iterator == null) {
                return new ArrayList<>();
            }
        }
        generateWords(iterator, new StringBuilder(prefix));

        return words;
    }
}
