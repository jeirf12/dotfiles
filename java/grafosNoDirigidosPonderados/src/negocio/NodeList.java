public class NodeList<T> {

    private T data;

    private int cost;

    private NodeList<T> next;

    public NodeList(T data, int cost) {
        this.data = data;
        this.cost = cost;
        this.next = null;
    }

    public void setData(T data) {
        this.data = data;
    }

    public T getData() {
        return this.data;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }

    public int getCost() {
        return this.cost;
    }

    public void setNext(NodeList<T> next) {
        this.next = next;
    }

    public NodeList<T> getNext() {
        return this.next;
    }
}
