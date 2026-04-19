import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import matplotlib.pyplot as plt

# Simulate some sample data for the training
def generate_data():
    # Example: [CPU Usage, GPU Usage, RAM Usage] -> Power Consumption
    np.random.seed(42)
    num_samples = 1000
    X = np.random.rand(num_samples, 3)  # Features: CPU, GPU, RAM usage
    y = X[:, 0] * 0.05 + X[:, 1] * 0.07 + X[:, 2] * 0.02 + np.random.normal(0, 0.1, num_samples)  # Target: Power consumption
    return X, y

def train_model():
    # Generate training data
    X, y = generate_data()
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse}")
    
    # Save the trained model to a file
    joblib.dump(model, 'ai_scheduler_model.pkl')
    print("Model saved as 'ai_scheduler_model.pkl'")
    
    # Optionally, visualize the prediction vs actual power consumption
    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
    plt.xlabel("Actual Power Consumption")
    plt.ylabel("Predicted Power Consumption")
    plt.title("Prediction vs Actual Power Consumption")
    plt.show()

if __name__ == "__main__":
    train_model()
