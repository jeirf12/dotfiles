public class NodeGraph<T>{
    private List<NodeGraph<T>> listNode;
    private T element;

    public NodeGraph(T element) {
        this.element = element;
        this.listNode = new List<NodeGraph<T>>();
    }

    public void setListNode(NodeGraph<T> value, int cost){
        this.listNode.add(value, cost);
    }

    public List<NodeGraph<T>> getListNode(){
        return this.listNode;
    }

    public void setElement(T element) {
        this.element = element;
    }

    public T getElement(){
        return this.element;
    }

    public void deleteNode(NodeGraph<T> node){
        this.listNode.delete(node);
    }

    public boolean isNode(NodeGraph<T> node){
        return this.listNode.isOnList(node);
    }

    public void printNodeList(){
        this.printNodeList(this.listNode.getHead());
    }

    private void printNodeList(NodeList<NodeGraph<T>> aux){
        if (aux != null) {
            System.out.print("["+aux.getDate().getElement()+", "+aux.getCost()+"]");
            this.printNodeList(aux.getNext());
        }
    }
}
