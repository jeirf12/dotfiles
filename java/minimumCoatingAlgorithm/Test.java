public class Test<T> {

    public static void main(String[] args) {
        /**
         * Grafo de prueba
         */
        Graph<String> grafoLetras = new Graph<String>();

        /**
        * Agrega los vertices
        */
        grafoLetras.addVertex("A");
        grafoLetras.addVertex("B");
        grafoLetras.addVertex("C");
        grafoLetras.addVertex("D");
        grafoLetras.addVertex("E");
        //Vertices para el metodo de prim
        // grafoLetras.addVertex("F");
        // grafoLetras.addVertex("G");

        /**
        * Agrega las aristas
        */
        //Adyacencia de prueba para el metodo Kruskal
        grafoLetras.addEdge("A", "B", 1);
        grafoLetras.addEdge("A", "C", 4);
        grafoLetras.addEdge("B", "C", 3);
        grafoLetras.addEdge("B", "D", 2);
        grafoLetras.addEdge("C", "D", 2);
        grafoLetras.addEdge("C", "E", 2);
        grafoLetras.addEdge("D", "E", 4);
        
        // adyacencias de prueba para el metodo de Prim
        // grafoLetras.addEdge("A", "B", 7);
        // grafoLetras.addEdge("A", "D", 5);
        // grafoLetras.addEdge("B", "C", 8);
        // grafoLetras.addEdge("B", "D", 9);
        // grafoLetras.addEdge("B", "E", 7);
        // grafoLetras.addEdge("C", "E", 5);
        // grafoLetras.addEdge("D", "E", 15);
        // grafoLetras.addEdge("D", "F", 6);
        // grafoLetras.addEdge("E", "F", 8);
        // grafoLetras.addEdge("E", "G", 9);
        // grafoLetras.addEdge("F", "G", 11);

        //Adyacencias de prueba para el metodo Djistra
        // grafoLetras.addEdge("A", "B", 4);
        // grafoLetras.addEdge("A", "C", 6);
        // grafoLetras.addEdge("B", "C", 1);
        // grafoLetras.addEdge("B", "D", 6);
        // grafoLetras.addEdge("C", "D", 2);
        // grafoLetras.addEdge("C", "E", 3);
        // grafoLetras.addEdge("D", "E", 1);

        /**
        * Imprime los vertices con sus adyacencias o aristas
        */
        grafoLetras.printVertex();

        /**
         * Metodos de recubrimiento mínimo descomente de a uno
         */
        grafoLetras.methodKruskal();
        // grafoLetras.methodPrim("A");
        // grafoLetras.methodDijkstra("A");
    }
}
