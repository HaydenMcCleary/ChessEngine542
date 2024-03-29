# ChessEngine542


# **fen** 
the position FEN only contains pieces, active color, castling rights, and en passant square

# **evals** 
a list of evaluations, ordered by number of PVs.

## **knodes** 
number of kilo-nodes searched by the engine

## **depth** 
depth reached by the engine

## **pvs** 
list of principal variations

### **cp** 
centipawn evaluation. Omitted if mate is certain.

### **mate** 
mate evaluation. Omitted if mate is not certain.

### **line** 
principal variation, in UCI format.