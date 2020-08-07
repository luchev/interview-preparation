package daily11;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class Daily11Test {

    @Test
    void solve() {
        // dog, deer, deal
        Trie trie = new Trie();
        trie.addWord("dog");
        trie.addWord("deer");
        trie.addWord("deal");

        ArrayList<String> output = trie.getWordsWithPrefix("de");
        ArrayList<String> expectedOutput = new ArrayList<>(Arrays.asList("deal", "deer"));
        assertEquals(output, expectedOutput);
    }
}