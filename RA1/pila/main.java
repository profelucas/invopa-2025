public class main {

    public static void main(String[] args) {
        int tam = 5;
        pilaestatica p = new pilaestatica(tam);
        p.ingresar(5);
        p.ingresar(9);
        p.mostrar();
        System.out.println("eliminando la cima");
        p.eliminar();
        p.mostrar();
    }
}
