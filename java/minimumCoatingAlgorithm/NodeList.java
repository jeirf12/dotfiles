public class NodeList<T>{
	private T date;
	private int cost;
	private NodeList<T> next;

	public NodeList(T date) {
		this.date = date;
		this.cost = 0;
		this.next = null;
	}

	public NodeList(T date, int cost) {
		this.date = date;
		this.cost = cost;
		this.next = null;
	}

	public void setDate(T date) {
		this.date = date;
	}

	public T getDate() {
		return this.date;
	}

	public void setCost(int cost) {
		this.cost = cost;
	}

	public int getCost() {
		return this.cost;
	}

	public void setNext(NodeList<T> next) {
		this.next = next;
	}

	public NodeList<T> getNext() {
		return this.next;
	}
}
