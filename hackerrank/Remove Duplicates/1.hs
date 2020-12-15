-- Complexity (n = input size)
-- Time complexity: O(n)
-- Space complexity: O(n)
f x[] = x
f out (x:xs) = if ( elem x out) then f out xs else f( out++ [x] ) xs

main = do
    input <- getLine
    putStrLn( f "" input )
