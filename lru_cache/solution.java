class LRUCache {

    class Node {
        int key;
        int val;
        Node next = null;
        Node prev = null;
    }

    private void add(Node node) {
        node.prev = head;
        node.next = head.next;

        head.next.prev = node;
        head.next = node;
    }

    private void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;

        prev.next = next;
        next.prev = prev;
    }

    private void moveToHead(Node node) {
        remove(node);
        add(node);
    }

    private Node popTail() {
        Node to_remove = tail.prev;
        remove(to_remove);
        return to_remove;
    }

    private Map<Integer, Node> cache = new HashMap<>();
    private int size;
    private int cap;
    private Node head, tail;

    public LRUCache(int capacity) {
        size = 0;
        cap = capacity;

        head = new Node();
        tail = new Node();

        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node node = cache.get(key);

        if (node == null)
            return -1;

        moveToHead(node);

        return node.val;
    }

    public void put(int key, int value) {
        Node node = cache.get(key);

        if (node == null){
            node = new Node();
            node.key = key;
            node.val = value;

            cache.put(key, node);
            add(node);

            size++;

            if (size > cap) {
                Node tail = popTail();
                cache.remove(tail.key);
                size--;
            }
        }
        else {
            node.val = value;
            moveToHead(node);
        }
    }
}
