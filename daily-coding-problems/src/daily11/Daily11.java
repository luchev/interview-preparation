package daily11;

import java.util.ArrayList;

class Daily11 {
    void solve() {
        Trie trie = new Trie();
        trie.addWord("dog");
        trie.addWord("deer");
        trie.addWord("deal");

        ArrayList<String> output = trie.getWordsWithPrefix("de");
        for (String word : output) {
            System.out.println(word);
        }
    }
}
