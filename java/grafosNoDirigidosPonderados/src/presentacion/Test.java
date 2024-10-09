public class Test {

    public static void main(String[] args) {
        Graph<String> graphLetters = new Graph<>();
        graphLetters.add("A");
        graphLetters.add("B");
        graphLetters.add("C");
        graphLetters.add("D");
        graphLetters.add("E");

        graphLetters.addEdge("A", "B", 1);
        graphLetters.addEdge("A", "C", 4);
        graphLetters.addEdge("B", "C", 3);
        graphLetters.addEdge("B", "D", 2);
        graphLetters.addEdge("C", "D", 2);
        graphLetters.addEdge("C", "E", 2);
        graphLetters.addEdge("D", "E", 4);

        graphLetters.printGraph();
        RoadMinimal<String> roadMethod = new RoadMinimal<>();
        roadMethod.Kruskal(graphLetters);
    }
    
}
