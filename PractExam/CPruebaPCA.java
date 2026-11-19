public class CPruebaPCA {

    static boolean estaBalanceada(String expresion) {
        char[] arre = expresion.toCharArray();
        CPilaConArreglo pilaExp = new CPilaConArreglo(arre.length);

        for (int i = 0; i < arre.length; i++) {
            if (arre[i] == '(')
                pilaExp.push(1);
            else if (arre[i] == ')')
                    pilaExp.pop();
        }

        if (pilaExp.isEmpty())
            return true;
        else
            return false;

    }

    static String invertir(String cadena) {
        CPilaConArreglo pila = new CPilaConArreglo(cadena.length());
        
        for (int i = 0; i < cadena.length(); i++) {
            pila.push(cadena.charAt(i) - '0');
        }

        String resultado = "";
        while (!pila.isEmpty()) {
            resultado += pila.pop();
        }
        return resultado;
    }

    static String decimal_a_binario(int n) {
        CPilaConArreglo pila = new CPilaConArreglo(20);
        int aux = n;

        while (aux > 0) {
            pila.push(aux % 2);
            aux = aux / 2;
        }

        String resultado = "";
        while (!pila.isEmpty()) {
            resultado += pila.pop();
        }
        return resultado;
    }

    public static void main(String[] args) {
        

        System.out.println(invertir("987654"));       // Imprimirá "456789"
        System.out.println(decimal_a_binario(359));   // Imprimirá "101100111"

    }
}

