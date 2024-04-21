import tensorflow as tf
from tensorflow.keras import layers, models
import chess
import numpy as np

'''
    Our functions
'''

# found in stuff_used_to_clean_data folder
from stuff_used_to_clean_data.fen_to_matrix import convert_csv_to_numeric


'''
    Parses our CSV returns an 8x8 matrix with piece values as below

    piece_values = 
        {
            'p': 1, 'P': -1, 'n': 2, 'N': -2, 'b': 3, 'B': -3, 'r': 4, 'R': -4,
            'q': 5, 'Q': -5, 'k': 6, 'K': -6
        }
    
    with best line of moves attached as shown below
'''
def parse_csv_data(csv_file):

    positions, moves, FEN, legalmoves = convert_csv_to_numeric(csv_file)

    return positions, moves, FEN, legalmoves

'''

'''
def build_move_cnn(input_shape, output_size):
    # Define the CNN model
    model = models.Sequential([
        layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape, padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(output_size, activation='softmax')  
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Print the model summary
    model.summary()

    return model


# Training
def train_move_cnn(x_train, y_train, num_epochs, batch_size):
    model.fit(x_train, y_train, epochs=num_epochs, batch_size=batch_size)


# Evaluation and Inference
def evaluate_move_cnn(model, x_test, y_test):
    loss, accuracy = model.evaluate(x_test, y_test)
    print("Validation Loss:", loss)
    print("Validation Accuracy:", accuracy)


def select_move(model, board):
    # Convert board to model input format
    input_board = preprocess_board(board)
    
    # Use the model to predict the move
    predicted_move = model.predict(input_board)
    
    return predicted_move



if __name__ == "__main__":
    # Step 1: Parse CSV data
    x_train, y_train, FEN, all_legal_moves = parse_csv_data("training_set/black/output_file_1_nocp.csv")
    x_train = np.array(x_train, dtype=np.float32)
    y_train = np.array(y_train, dtype=np.float32)
    '''

    '''


    # for i in range(len(x_train)):
    #     print("Index:", i)
    #     print("x_train:", x_train[i])
    #     print("y_train:", y_train[i])
    #     print("FEN:", FEN[i])
    #     print("Legal Moves:", all_legal_moves[i])
    #     print()


    # Step 2: Build the CNN model
    # input_shape = (8, 8, 1)  # Adjust input shape based on your data
    # output_size = len(all_legal_moves)  # Number of possible moves
    # model = build_move_cnn(input_shape, output_size)
    
    # # Define hyperparameters
    # num_epochs = 10  # Number of epochs for training
    # batch_size = 32  # Batch size for training
    
    # # Step 3: Train the CNN model
    # train_move_cnn(x_train, y_train, num_epochs, batch_size)
    
    # # Step 4: Evaluate the CNN model
    # x_test, y_test, _, _ = parse_csv_data("test_set/black/test_file_nocp.csv")  # Load test data
    # evaluate_move_cnn(model, x_test, y_test)
    
    # # Step 5: Select a move
    # board = chess.Board()  # Initialize a chess board
    # selected_move = select_move(model, board)
    
    # print("Selected Move:", selected_move)

