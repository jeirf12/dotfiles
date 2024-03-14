public class Edge<T> {
	private NodeGraph<T> initial;
	private NodeGraph<T> end;
	private int cost;

	public Edge(NodeGraph<T> initial, NodeGraph<T> end, int cost) {
		this.initial = initial;
		this.end = end;
		this.cost = cost;
	}

	public void setInitial(NodeGraph<T> initial) {
		this.initial = initial;
	}

	public NodeGraph<T> getInitial() {
		return this.initial;
	}

	public void setEnd(NodeGraph<T> end) {
		this.end = end;
	}
	
	public NodeGraph<T> getEnd() {
		return this.end;
	}

	public void setCost(int cost) {
		this.cost = cost;
	}

	public int getCost() {
		return this.cost;
	}
}
