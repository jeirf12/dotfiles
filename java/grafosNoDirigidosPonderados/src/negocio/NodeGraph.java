public class NodeGraph<T> {

    private T element;
    
    private List<NodeGraph<T>> listNode;

    public NodeGraph(T element) {
        this.element = element;
        this.listNode = new List<>();
    }

    public void setElement(T element) {
        this.element = element;
    }

    public T getElement() {
        return this.element;
    }

    public void add(NodeGraph<T> nodeNew, int cost) {
        this.listNode.add(nodeNew, cost);
    }

    public List<NodeGraph<T>> getListNode() {
        return this.listNode;
    }

    public void delete(NodeGraph<T> node) {
        this.listNode.delete(node);
    }

    public boolean exist(NodeGraph<T> node) {
        return this.listNode.find(node) != null;
    }
}
