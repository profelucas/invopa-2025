class pilaestatica {
    private Object[] pila;
    private int tam;
    private int tope;


    //constructor 
    public pilaestatica(int tam){
        this.tam =tam;
        this.tope=-1;
        this.pila = new Object[tam];
    }

    public boolean espilallena(){
        return this.tope==(this.tam-1);
    }

    public boolean espilavacia(){
        return this.tope==-1;
    }

    public Object cima(){
        return this.pila[tope];
    }
    public void ingresar(Object x){
        if(!espilallena()){
            this.tope++;
            this.pila[tope] = x;
        }
        
    }
    public void eliminar(){
        //comprobar si esta vacio
        if(!this.espilavacia()){
            this.pila[tope]=null;
            this.tope--;
        }else{
            System.out.println("la pila esta vacia");
        }
    }

    public void mostrar(){
        pilaestatica pilaaux = new pilaestatica(this.tam);
        while(!espilavacia()) {
            System.out.println(cima());
            pilaaux.ingresar(cima());
            eliminar();
        }
        while(!pilaaux.espilavacia()){
            this.ingresar(pilaaux.cima());
            pilaaux.eliminar();
        }
    }
//dado un objeto devolver la posicion
    public void buscar(Object x){
        //desafio
    }
}
