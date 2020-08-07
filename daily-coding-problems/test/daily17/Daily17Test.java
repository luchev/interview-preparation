package daily17;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Daily17Test {

    @Test
    void findLongestAbsoluteFileName() {
        Daily17 solver = new Daily17();

        String testOne = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
        assertEquals(20, solver.findLongestAbsoluteFileName(testOne));

        String testTwo = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
        assertEquals(32, solver.findLongestAbsoluteFileName(testTwo));

        assertEquals(0, solver.findLongestAbsoluteFileName(""));
    }
}