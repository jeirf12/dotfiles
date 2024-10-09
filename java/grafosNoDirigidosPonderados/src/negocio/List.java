public class List<T> {
    
    private NodeList<T> head;

    private int size;

    public void setHead(NodeList<T> head) {
        this.head = head;
    }

    public NodeList<T> getHead() {
        return this.head;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public int getSize() {
        return this.size;
    }

    public void addAll(List<T> nodes) {
        NodeList<T> nodeCurrent = nodes.getHead();
        while (nodeCurrent != null) {
            this.add(nodeCurrent.getData(), size);
            nodeCurrent = nodeCurrent.getNext();
        }
    }

    public void add(T data, int cost) {
        NodeList<T> nodeNew = new NodeList<T>(data, cost);
        if(!this.isEmpty()) this.findLast(this.head).setNext(nodeNew);
        else this.head = nodeNew;
        ++this.size;
    }

    public NodeList<T> findLast(NodeList<T> nodeCurrent) {
        if(nodeCurrent.getNext() != null) return this.findLast(nodeCurrent.getNext());
        return nodeCurrent;
    }

    public T find(int position) {
        NodeList<T> nodeFinded = this.getNode(this.head, 0, position);
        if(nodeFinded == null) return null;
        return nodeFinded.getData();
    }

    private NodeList<T> getNode(NodeList<T> nodeCurrent, int positionArray,  int position) {
        if(nodeCurrent != null) {
            if(position != positionArray) return this.getNode(nodeCurrent.getNext(), positionArray + 1, position);
        }
        return nodeCurrent;
    }

    public NodeList<T> find(T nodeSearch) {
        if(this.isEmpty()) return null;
        if(this.head.getData().equals(nodeSearch)) return this.head;
        return this.getNode(this.head, nodeSearch).getNext();
    }

    public void delete(T nodeDelete) {
        if(this.isEmpty()) return;
        if(this.head.getData().equals(nodeDelete)) this.head = this.head.getNext();
        else {
            NodeList<T> nodeCurrent = this.getNode(this.head, nodeDelete);
            nodeCurrent.setNext(nodeCurrent.getNext().getNext());
        } 
        --this.size;
    } 

    private NodeList<T> getNode(NodeList<T> nodeCurrent, T nodeSearch) {
        if(nodeCurrent.getNext() != null) {
            if(!nodeCurrent.getNext().getData().equals(nodeSearch)) return this.getNode(nodeCurrent.getNext(), nodeSearch);
        }
        return nodeCurrent;
    }

    public boolean isEmpty() {
        return this.head == null;
    }

    public void clear() {
        this.size = 0;
        this.head = null;
    }
}
