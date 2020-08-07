package daily11;

import java.util.HashMap;

class TrieNode {
    private HashMap<Character, TrieNode> transitions = null;
    private boolean wordEnd = false;

    void setWordEnd(boolean wordEnd) {
        this.wordEnd = wordEnd;
    }

    boolean isWordEnd() {
        return this.wordEnd;
    }

    void addTransition(Character character) {
        if (transitions == null) {
            transitions = new HashMap<>();
        }

        if (!transitions.containsKey(character)) {
            transitions.put(character, new TrieNode());
        }
    }

    TrieNode getTransitionWith(Character character) {
        return transitions.get(character);
    }

    HashMap<Character, TrieNode> getTransitions() {
        return transitions;
    }
}
