class CPilaConArreglo {
    int pila[];
    int tope;

    CPilaConArreglo(int tam) {
        pila = new int[tam];
        tope = -1;
    }

    void imprimir() {
        for (int i = 0; i <= tope; i++) {
            System.out.print(pila[i] + " ");
        }
        System.out.println();
        System.out.println("--------");
    }

    void push(int e) {
        tope++;
        pila[tope] = e;
    }

    int pop() {
        if (!isEmpty())
            return pila[tope--];
        else {
            System.out.println("Error, pila vacía [error 0]");
            return 0;
        } 
    }

    boolean isEmpty() {
        if (tope == -1)
            return true;
        else
            return false;
    }

    int peek() {
        if (!isEmpty())
            return pila[tope];
        else {
            System.out.println("Error, pila vacía [error 0]");
            return 0;
        }         
    }

    int size() {
        return tope + 1;
    }
}