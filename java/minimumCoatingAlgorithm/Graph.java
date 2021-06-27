import java.util.ArrayList;

/**
 * Graph
 */
public class Graph<T>{
    private List<NodeGraph<T>> listVertex;

    public Graph() {
        this.listVertex = new List<NodeGraph<T>>();
    }

    public void addVertex(T vertex){
        if (!isVertex(vertex)) {
            NodeGraph<T> recent = new NodeGraph<T>(vertex);
            this.listVertex.add(recent);
        }
    }

    public void addEdge(T initial, T end, int cost){
        if(cost > 0) {
            if(!initial.equals(end)) {
                if(this.isVertex(initial) && this.isVertex(end)) {
                    if(!this.isEdge(initial, end)) {
                        NodeGraph<T> nInitial = this.getVertex(initial);
                        NodeGraph<T> nEnd = this.getVertex(end);
                        nInitial.setListNode(nEnd, cost);
                        nEnd.setListNode(nInitial, cost);
                    }else{
                        System.out.println("La arista ya existe");
                    }
                } else{
                    System.out.println("Algunos de los vertices no existe");
                }
            }else{
                System.out.println("Los vertices no pueden ser iguales");
            }
        }else{
            System.out.println("El coste debe ser mayor a cero");
        }
    }

    public void printVertex(){
        this.printVertex(this.listVertex.getHead());
    }

    private void printVertex(NodeList<NodeGraph<T>> aux){
        if (!this.isEmpty(aux)) {
            System.out.print(aux.getDate().getElement()+" ->");
            aux.getDate().printNodeList();
            System.out.println("");
            this.printVertex(aux.getNext());
        }
    }

    private boolean isEdge(T initial, T end){
        if (this.isVertex(initial) && this.isVertex(end)) {
            NodeGraph<T> nInitial = this.getVertex(initial);
            NodeGraph<T> nEnd = this.getVertex(end);
            if (nInitial != null && nEnd != null) {
                return nInitial.isNode(nEnd);
            }
        }
        return false;
    }

    private NodeGraph<T> getVertex(T vertex){
        return this.getVertex(this.listVertex.getHead(), vertex);
    }

    private NodeGraph<T> getVertex(NodeList<NodeGraph<T>> aux, T vertex){
        if (!this.isEmpty(aux)) {
            if (aux.getDate().getElement().equals(vertex)) {
                return aux.getDate();
            }
            return this.getVertex(aux.getNext(), vertex);	
        }
        return null;
    }

    private boolean isVertex(T vertex) {
        return this.isVertex(this.listVertex.getHead(), vertex);
    }

    private boolean isVertex(NodeList<NodeGraph<T>> aux, T vertex) {
        if (!this.isEmpty(aux)) {
            if (aux.getDate().getElement().equals(vertex)) {
                return true;
            }
            return this.isVertex(aux.getNext(), vertex);
        }
        return false;
    }

    private boolean isEmpty(NodeList<NodeGraph<T>> aux){
        return aux == null;
    }

    public List<NodeGraph<T>> getListVertex(){
        return this.listVertex;
    }

    private int costEdge(NodeGraph<T> initial, NodeGraph<T> end){
        return costEdge(initial.getListNode().getHead(), end);
    }

    private int costEdge(NodeList<NodeGraph<T>> aux, NodeGraph<T> end){
        if (!this.isEmpty(aux)) {
            if (!aux.getDate().equals(end)) {
                return this.costEdge(aux.getNext(), end);
            }
            return aux.getCost();
        }
        return 0;
    }

    private ArrayList<Edge<T>> getEdges(){
        List<NodeGraph<T>> tempList = listVertex;
        NodeList<NodeGraph<T>> aux = tempList.getHead();
        ArrayList<Edge<T>> list = new ArrayList<Edge<T>>();
        while (!this.isEmpty(aux)) {
            NodeList<NodeGraph<T>> aux2 = tempList.getHead();
            while(!this.isEmpty(aux2)){
                int cost = this.costEdge(aux.getDate(), aux2.getDate());
                if (cost > 0) {
                    list.add(new Edge<>(aux.getDate(), aux2.getDate(), cost));
                    aux2.getDate().deleteNode(aux.getDate());
                }
                aux2 = aux2.getNext();
            }
            aux = aux.getNext();
        }
        return list;
    }

    private ArrayList<Edge<T>> quicksort(ArrayList<Edge<T>> list){
        if (list.size() > 0) {
            int positionPivote = Math.round(list.size()/2);
            ArrayList<Edge<T>> left = new ArrayList<Edge<T>>();
            ArrayList<Edge<T>> right = new ArrayList<Edge<T>>();
            Edge<T> pivote = list.get(positionPivote);
            for (Edge<T> edge : list) {
                if (!edge.equals(pivote)) {
                    if (edge.getCost() < pivote.getCost()) {
                        left.add(edge);
                    } else {
                        right.add(edge);
                    }
                }
            }
            list.clear();
            list.addAll(quicksort(left));
            list.add(pivote);
            list.addAll(quicksort(right));
        }
        return list;
    }

    private void addVertexDinamic(NodeList<NodeGraph<T>> aux, Graph<T> graph){
        if (!this.isEmpty(aux)) {
            graph.addVertex(aux.getDate().getElement());
            this.addVertexDinamic(aux.getNext(), graph);
        }
    }

    private boolean isCicle(NodeGraph<T> initial, NodeGraph<T> end) {
        NodeList<NodeGraph<T>> aux = listVertex.getHead().getNext();
        while (aux != null) {
            NodeGraph<T> date = aux.getDate();
            if (date.isNode(initial) && date.isNode(end)) {
                return true;
            }
            aux = aux.getNext();
        }
        return false;
    }

    private ArrayList<Edge<T>> getAdjacencies(NodeGraph<T> head){
        List<NodeGraph<T>> tempList = head.getListNode();
        NodeList<NodeGraph<T>> aux = tempList.getHead();
        ArrayList<Edge<T>> listRecent = new ArrayList<Edge<T>>();
        while (!this.isEmpty(aux)) {
            int cost = this.costEdge(head, aux.getDate());
            if (cost > 0) {
                listRecent.add(new Edge<T>(head, aux.getDate(), cost));
                aux.getDate().deleteNode(head);
            }
            aux = aux.getNext();
        }
        return listRecent;
    }
    private ArrayList<Hashtag<T>> calculateTagMinimum(NodeGraph<T> vInitial, Hashtag<T> aux){
        int distance = Integer.MAX_VALUE;
        ArrayList<Edge<T>> adjacencies = this.getAdjacencies(vInitial);
        Hashtag<T> acumulative = aux;
        ArrayList<Hashtag<T>> lisTemporary = new ArrayList<Hashtag<T>>();
        for (Edge<T> ed: adjacencies) {
            if (ed.getCost() < distance) {
                if (acumulative.getCumulativeDistance() > 0) {
                    lisTemporary.remove(acumulative);
                }
                acumulative = new Hashtag<T>(ed.getCost(), ed.getEnd().getElement(), 0);
                acumulative.setInitialPredecessor(ed.getInitial().getElement());
                lisTemporary.add(acumulative);
                distance = ed.getCost();
            }else if(ed.getCost() == distance){
                acumulative = new Hashtag<T>(ed.getCost(), ed.getEnd().getElement(), 0);
                acumulative.setInitialPredecessor(ed.getInitial().getElement());
                lisTemporary.add(acumulative);
            }
        }
        return lisTemporary;
    }

    /** Algoritmos de recubrimiento minimo */

    /* Kruskal */
    public void methodKruskal(){
        int sizeVertex = listVertex.getSize(), counter = 0, cost = 0;
        ArrayList<Edge<T>> list = this.quicksort(this.getEdges());
        Graph<T> graphKruskal = new Graph<T>();
        this.addVertexDinamic(listVertex.getHead(), graphKruskal);
        System.out.print("T = ");
        for (Edge<T> edge : list) {
            NodeGraph<T> initial = edge.getInitial();
            NodeGraph<T> end = edge.getEnd();	
            if (!this.isCicle(initial, end) && counter < (sizeVertex - 1)) {
                graphKruskal.addEdge(initial.getElement(), end.getElement(), edge.getCost());
                System.out.print("[" + initial.getElement() + "-" + end.getElement() + "," + edge.getCost() + "],");
                cost += edge.getCost();
                counter++;
            }
        }
        System.out.println(" Longitud de camino = " + cost);
    }

    /* Prim */
    public void methodPrim(T vertex) {
        Graph<T> graphPrim = new Graph<T>();
        this.addVertexDinamic(listVertex.getHead(), graphPrim);
        int cost = 0,costEntire = 0;
        System.out.print("T = ");
        NodeGraph<T> vInitial = this.getVertex(vertex);
        ArrayList<Edge<T>> visited = new ArrayList<Edge<T>>();
        ArrayList<Edge<T>> temp = new ArrayList<Edge<T>>();
        NodeGraph<T> nInitial = null;
        NodeGraph<T> nEnd = null;
        int sizeVertex = listVertex.getSize();
        for (int i = 0; i < sizeVertex; i++) {
            ArrayList<Edge<T>> adjacencies = this.quicksort(this.getAdjacencies(vInitial));
            int size = adjacencies.size();
            Edge<T> edgeTemp = null;
            if (size == 0 && i < sizeVertex - 1) {
                NodeList<NodeGraph<T>> aux2 = nInitial.getListNode().getHead();
                int counter = 0;
                while (aux2 != null) {
                    if (counter == nInitial.getListNode().getSize()-1) {
                        int costEnd = this.costEdge(nInitial, aux2.getDate());
                        Edge<T> edge = new Edge<T>(nInitial, aux2.getDate(), costEnd);    
                        adjacencies.add(edge);
                    }
                    counter++;
                    aux2 = aux2.getNext();
                }
                vInitial = nInitial;
                size = adjacencies.size();
            }
            nInitial = vInitial;
            if (size > 0) {
                nEnd = adjacencies.get(size-1).getEnd();
                cost = adjacencies.get(size-1).getCost();
                for (Edge<T> edge : adjacencies) {
                    if (edge.getCost() <= cost) {
                        nInitial = edge.getInitial();
                        nEnd = edge.getEnd();
                        cost = edge.getCost();
                    } 
                    else {
                        if (!visited.contains(edge)) {
                            visited.add(edge);
                        }
                    }
                }
                if (i > 0 && i < sizeVertex-2) {
                    for (Edge<T> edge : visited) {
                        if (edge.getCost() <= cost) {
                            edgeTemp = new Edge<T>(nInitial, nEnd, cost);
                            temp.add(edgeTemp);
                            nInitial = edge.getInitial();
                            nEnd = edge.getEnd();
                            cost = edge.getCost();
                            edgeTemp = edge;
                        }
                    }   
                    if (edgeTemp != null) {
                        visited.remove(edgeTemp);
                        temp.addAll(visited);
                        visited.clear();
                        visited.addAll(temp);   
                        temp.clear();
                    }
                }
                if (!this.isCicle(nInitial, nEnd)) {
                    graphPrim.addEdge(nInitial.getElement(), nEnd.getElement(), cost);
                    System.out.print("[" + nInitial.getElement() + "-" + nEnd.getElement() + "," + cost + "],");
                    costEntire += cost;
                    vInitial = nEnd;
                }
            }
        }
        System.out.println(" Longitud de camino = " + costEntire);
    }

    

    /* Dijkstra */
    public void methodDijkstra(T vertex){
        Hashtag<T> permanent = new Hashtag<T>(0, vertex, 0);
        NodeGraph<T> vInitial = this.getVertex(vertex);
        ArrayList<Hashtag<T>> lisTemporary = new ArrayList<Hashtag<T>>();
        int iteration = 0; 
        for (int i = 0; i < listVertex.getSize(); i++) {
            int distance = Integer.MAX_VALUE, index = -1, counter = 0;
            T edgeVertex = null, initialVertex = null; 
            lisTemporary.addAll(this.calculateTagMinimum(vInitial, permanent));
            for (Hashtag<T> hashtag : lisTemporary) {
                if (hashtag.getCumulativeDistance() < distance) {
                    distance = hashtag.getCumulativeDistance();
                    edgeVertex = hashtag.getPredecessorVertex();
                    initialVertex = hashtag.getInitialPredecessor();
                    index = counter;
                }else if (hashtag.getCumulativeDistance() == distance) {
                    NodeGraph<T> vertexInitial = this.getVertex(edgeVertex);
                    NodeGraph<T> vertexEquals = this.getVertex(hashtag.getPredecessorVertex());
                    int costInitial = this.costEdge(vInitial, vertexInitial);
                    int costEquals = this.costEdge(vInitial, vertexEquals);
                    if (costInitial > costEquals) {
                        distance = hashtag.getCumulativeDistance();
                        edgeVertex = hashtag.getPredecessorVertex();
                        initialVertex = hashtag.getInitialPredecessor();
                        index = counter;
                    }
                }
                counter++;
            }
            if (index > -1) {
                lisTemporary.remove(index);
                permanent.setCumulativeDistance(distance);
                permanent.setPredecessorVertex(initialVertex);
                permanent.setIterationNumber(iteration);
                permanent.setInitialPredecessor(edgeVertex);
                vInitial = this.getVertex(edgeVertex);
            }
            iteration++;
        }
        System.out.println("Longitud de camino: ("+permanent.getCumulativeDistance()+", "+permanent.getPredecessorVertex()+") "+permanent.getIterationNumber());
    }
}
