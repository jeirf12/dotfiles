public class Graph<T> {
    
    private List<NodeGraph<T>> vertexList;

    public Graph() {
        this.vertexList = new List<>();
    }

    public void setVertexList(List<NodeGraph<T>> vertexList) {
        this.vertexList = vertexList;
    }

    public List<NodeGraph<T>> getVertexList() {
        return this.vertexList;
    }

    public NodeGraph<T> add(T vertex) {
        NodeGraph<T> nodeNew = null;
        if(!this.exist(vertex)) {
            nodeNew = new NodeGraph<T>(vertex);
            this.vertexList.add(nodeNew, 0);
        }
        return nodeNew;
    }

    public boolean addEdge(T initial, T end, int cost) {
        if(this.exist(initial) && this.exist(end)) {
            if(cost > 0) {
                if(!initial.equals(end)) {
                    if(!this.existEdge(initial, end)) {
                        NodeGraph<T> nodeInitialFinded = this.getVertex(initial);
                        NodeGraph<T> nodeEndFinded = this.getVertex(end);
                        nodeInitialFinded.add(nodeEndFinded, cost);
                        nodeEndFinded.add(nodeInitialFinded, cost);
                        return true;
                    } else {
                        System.out.println("The edge already exists");
                    }
                } else {
                    System.out.println("Vertice cannot form a cycle");
                }
            } else {
                System.out.println("Cost must be greater than zero");
            }
        } else {
            System.out.println("Some of the vertices do not exist");
        }
        return false;
    }

    public boolean existEdge(T initial, T end) {
        if(this.exist(initial) && this.exist(end)) {
            NodeGraph<T> nodeInitialFinded = this.getVertex(initial);
            NodeGraph<T> nodeEndFinded = this.getVertex(end);
            if(nodeInitialFinded != null && nodeEndFinded != null) return nodeInitialFinded.exist(nodeEndFinded);
        }
        return false;
    }

    public boolean exist(T vertex) {
        return this.getVertex(vertex) != null;
    }

    public NodeGraph<T> getVertex(T vertex) {
        NodeList<NodeGraph<T>> nodeFinded = this.getVertex(this.vertexList.getHead(), vertex);
        if(nodeFinded == null) return null;
        return nodeFinded.getData();
    }

    private NodeList<NodeGraph<T>> getVertex(NodeList<NodeGraph<T>> nodeCurrent, T element) {
        if(nodeCurrent != null) {
            if(!nodeCurrent.getData().getElement().equals(element)) return this.getVertex(nodeCurrent.getNext(), element);
        }
        return nodeCurrent;
    }

    public void printGraph() {
        this.printGraph(this.vertexList.getHead());
    }

    private void printGraph(NodeList<NodeGraph<T>> nodeCurrent) {
        if(nodeCurrent != null) {
            System.out.print(nodeCurrent.getData().getElement() + " ->");
            printEdge(nodeCurrent.getData().getListNode().getHead());
            System.out.println("");
            this.printGraph(nodeCurrent.getNext());
        }
    }

    private void printEdge(NodeList<NodeGraph<T>> nodeCurrent) {
        if(nodeCurrent != null) {
            System.out.print(" [" + nodeCurrent.getData().getElement() + ", " + nodeCurrent.getCost() + "]");
            this.printEdge(nodeCurrent.getNext());
        }
    }
}
