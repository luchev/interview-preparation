package daily5;

abstract class Daily5 {
    static <KEY, VALUE> Pair<KEY, VALUE> cons(KEY key, VALUE value) {
        return new Pair<KEY, VALUE>(key, value);
    }

    static <KEY, VALUE> KEY car(Pair<KEY, VALUE> pair) {
        return pair.getKey();
    }

    static <KEY, VALUE> VALUE cdr(Pair<KEY, VALUE> pair) {
        return pair.getValue();
    }
}
