public class List<T>{
	private NodeList<T> head;
	private int size;
	
	public void add(T date){
		NodeList<T> recent = new NodeList<T>(date);
		if(!this.isEmpty()){
			this.add(this.head, recent);
		}else{
			head = recent;
		}
		this.size++;
	}
	
	public void add(T date, int cost) {
		NodeList<T> recent = new NodeList<T>(date, cost);
		if(!this.isEmpty()){
			this.add(this.head, recent);
		}else{
			head = recent;
		}
		this.size++;
	}

	private void add(NodeList<T> aux, NodeList<T> recent){
		if (aux.getNext() != null) {
			this.add(aux.getNext(), recent);
		}else{
			aux.setNext(recent);
		}
	}

	public void delete(T date) {
		if (this.head.getDate().equals(date)) {
			this.head = this.head.getNext();
		} else {
			this.delete(this.head, date);
		}
		this.size--;
	}

	private void delete(NodeList<T> aux, T date){
		if(aux.getNext() != null){
			if (aux.getNext().getDate().equals(date)) {
				aux.setNext(aux.getNext().getNext());
			} else {
				this.delete(aux.getNext(), date);
			}
		}
	}

	public boolean isOnList(T date){
		return this.isOnList(this.head, date);
	}

	private boolean isOnList(NodeList<T> aux, T date){
		if(aux != null){
			if (!aux.equals(date)) {
				return this.isOnList(aux.getNext(), date);
			}
			return true;
		}
		return false;
	}

	public void setHead(NodeList<T> head) {
		this.head = head;
	}

	public NodeList<T> getHead(){
		return this.head;
	}
	
	public void setSize(int size){
		this.size = size;
	}

	public int getSize() {
		return this.size;
	}

	public boolean isEmpty() {
		return head == null;
	}
}
