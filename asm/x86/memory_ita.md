# Funzionamento della memoria in un processo

## Struttura della memoria

La memoria è organizzata come un vettore i
cui indirizzi crescono dal basso verso l'alto.


|   Regione            | Address |
|----------------------|----------
|    STACK             | 0xFF...
|    ↓↓                | 
|    ↑↑                |
|      HEAP            |
|      data (readonly) | 
|      text (readonly) | 0x0...

## Come funziona lo stack
Lo stack è un pila LIFO.

La stack ha una `cima` e un `fondo`. Il fondo
è in alto, la cima è in basso, quindi lo stack
cresce verso indirizzi di memoria più bassi.

Lo stack si governa con due principali istruzioni `push` e `pop` che rispettivamente
inseriscono un elemento nella cima dello stack e lo rimuovono.

La `cima` dello stack è puntata dal registro `ESP` (Stack Pointer) della CPU.

L'`ESP` punta all'ultimo byte occupato dalla cima dello stack, cioé all'indirizzo più basso occupato nello stack stesso.

Nello stack vengono inseriti gli `activation
records`, cioé i blocchi contenenti le informazioni sulle chiamate alle funzioni.

Lo stack è l'ideale per questo compito, perché le funzioni si chiamano tra loro in modo innestato. Ogni chiamata a funzione è anticipata dalla preparazione del suo record di attivazione inserito nello stack.

Gli activation record costituiscono dei frame ed esiste un registro chiamato `EBP` (Base Pointer) che punta alla base di uno stack frame. I frame 

## Chiamiamo una funzione

La funzione si chiama con una `call`.
Infine si sovrascrive nell'`EBP` il valore attuale dell'`ESP`.

