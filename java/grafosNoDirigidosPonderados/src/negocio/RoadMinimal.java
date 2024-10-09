public class RoadMinimal<T> {
    
    public void Kruskal(Graph<T> graph) {
        int cost = 0, counter = 0;
        List<Edge<T>> listEdge = this.quickSort(this.getEdges(graph));
        Graph<T> graphNew = new Graph<>();
        this.addVertex(graph.getVertexList().getHead(), graphNew);
        System.out.print("T = ");
        NodeList<Edge<T>> nodeCurrent = listEdge.getHead();
        while(nodeCurrent != null) {
            if(!(graph.getVertexList().find(nodeCurrent.getData().getInitial()) == null || graph.getVertexList().find(nodeCurrent.getData().getEnd()) == null) && counter < graphNew.getVertexList().getSize() - 1) {
                graphNew.addEdge(nodeCurrent.getData().getInitial().getElement(), nodeCurrent.getData().getEnd().getElement(), nodeCurrent.getData().getCost());
                System.out.print("[" + nodeCurrent.getData().getInitial().getElement() + "-" + nodeCurrent.getData().getEnd().getElement() + "-" + nodeCurrent.getData().getCost() + "]");
                cost += nodeCurrent.getData().getCost();
                counter++;
            }
            nodeCurrent = nodeCurrent.getNext();
        }
        System.out.println(" Longitud de camino = " + cost);
    }

    public void addVertex(NodeList<NodeGraph<T>> vertexCurrent, Graph<T> graphNew) {
        if(vertexCurrent != null) {
            graphNew.add(vertexCurrent.getData().getElement());
            addVertex(vertexCurrent.getNext(), graphNew);
        }
    }

    public void printNode(NodeList<Edge<T>> nodeCurrent) {
        if(nodeCurrent != null) {
            System.out.println("NODO " + nodeCurrent.getData().toString());
            this.printNode(nodeCurrent.getNext());
        }
    }

    public List<Edge<T>> getEdges(Graph<T> graph) {
        List<Edge<T>> listEdge = new List<>();
        NodeList<NodeGraph<T>> vertex = graph.getVertexList().getHead();
        while(vertex != null) {
            NodeList<NodeGraph<T>> edges = graph.getVertexList().getHead();
            while(edges != null) {
                NodeList<NodeGraph<T>> nodeFinded = vertex.getData().getListNode().find(edges.getData());
                if(nodeFinded != null) {
                    listEdge.add(new Edge<T>(vertex.getData(), edges.getData(), nodeFinded.getCost()), 0);
                }
                edges = edges.getNext();
            }
            vertex = vertex.getNext();
        }
        return listEdge;
    }

    public List<Edge<T>> quickSort(List<Edge<T>> listEdge) {
        if(!listEdge.isEmpty()) {
            int positionPivote = Math.round(listEdge.getSize() / 2);
            List<Edge<T>> left = new List<>();
            List<Edge<T>> right = new List<>();
            Edge<T> pivote = listEdge.find(positionPivote);
            NodeList<Edge<T>> edge = listEdge.getHead();
            while (edge != null) {
                if(!edge.getData().equals(pivote)) {
                    if(edge.getData().getCost() < pivote.getCost()) left.add(edge.getData(), 0);
                    else right.add(edge.getData(), 0);
                }
                edge = edge.getNext();
            }
            listEdge.clear();
            listEdge.addAll(this.quickSort(left));
            listEdge.add(pivote, 0);
            listEdge.addAll(this.quickSort(right));
        }
        return listEdge;
    }
}
