public class Hashtag<T>{
    private T predecessorVertex;
    private T initialPredecessor;
    private int cumulativeDistance;
    private int iterationNumber;
    
    public Hashtag(int cumulativeDistance, T predecessorVertex, int iterationNumber) {
        this.predecessorVertex = predecessorVertex;
        this.cumulativeDistance += cumulativeDistance;
        this.iterationNumber = iterationNumber;
    }

    public void setPredecessorVertex(T predecessorVertex) {
        this.predecessorVertex = predecessorVertex;
    }

    public T getPredecessorVertex(){
        return this.predecessorVertex;
    }
    
    public void setInitialPredecessor(T initialPredecessor) {
        this.initialPredecessor = initialPredecessor;
    }

    public T getInitialPredecessor(){
        return this.initialPredecessor;
    }
    public void setCumulativeDistance(int cumulativeDistance){
        this.cumulativeDistance += cumulativeDistance;
    }
    
    public int getCumulativeDistance(){
        return this.cumulativeDistance;
    }

    public void setIterationNumber(int iterationNumber){
        this.iterationNumber = iterationNumber;
    }

    public int getIterationNumber(){
        return this.iterationNumber;
    }
}
