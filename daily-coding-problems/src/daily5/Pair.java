package daily5;

class Pair<KEY, VALUE> {
    private KEY key;
    private VALUE value;

    Pair(KEY key, VALUE value) {
        this.key = key;
        this.value = value;
    }

    KEY getKey() {
        return key;
    }

    void setKey(KEY key) {
        this.key = key;
    }

    VALUE getValue() {
        return value;
    }

    void setValue(VALUE value) {
        this.value = value;
    }
}
