import streamlit as st
import spacy

# Load the saved model
nlp = spacy.load("spacy_car_model")


# Define the Streamlit app
def main():
    st.title('Car Acceptability Prediction')
    
    # Mapping for Buying Price, Maintenance Price, and Size of Luggage options
    buying_price_mapping = {
        'vhigh': '$50,000+',
        'high': '$30,000-$50,000',
        'med': '$20,000-$30,000',
        'low': 'less than $20,000'
    }

    maintenance_price_mapping = {
        'vhigh': '$2,000+',
        'high': '$1,000-$2,000',
        'med': '$500-$1,000',
        'low': 'less than $500'
    }
    
    size_of_luggage_mapping = {
        'small': 'less than 15 cubic feet',
        'med': '15-25 cubic feet',
        'big': '25+ cubic feet'
    }
    
    # Collect user input for car features
    st.header('Enter Car Features:')
    buying_price = st.selectbox('Buying Price', list(buying_price_mapping.values()))
    maintenance_price = st.selectbox('Maintenance Price', list(maintenance_price_mapping.values()))
    no_of_doors = st.selectbox('Number of Doors', ('2', '3', '4', '5more'))
    person_capacity = st.selectbox('Person Capacity', ('2', '4', 'more'))
    size_of_luggage = st.selectbox('Size of Luggage', list(size_of_luggage_mapping.values()))
    safety = st.selectbox('Safety', ('low', 'med', 'high'))
    
    # Perform prediction on button click
    if st.button('Predict'):
        # Map selected options back to descriptive categories for prediction
        reverse_buying_price_mapping = {v: k for k, v in buying_price_mapping.items()}
        buying_price_selected = reverse_buying_price_mapping[buying_price]
        
        reverse_maintenance_price_mapping = {v: k for k, v in maintenance_price_mapping.items()}
        maintenance_price_selected = reverse_maintenance_price_mapping[maintenance_price]
        
        reverse_size_of_luggage_mapping = {v: k for k, v in size_of_luggage_mapping.items()}
        size_of_luggage_selected = reverse_size_of_luggage_mapping[size_of_luggage]
        
        # Construct the text using user input
        sample_text = f"Buying_Price: {buying_price_selected}, Maintenance_Price: {maintenance_price_selected}, No_of_Doors: {no_of_doors}, Person_Capacity: {person_capacity}, Size_of_Luggage: {size_of_luggage_selected}, Safety: {safety}"
        
        # Process the text using the loaded model
        doc = nlp(sample_text)
        
        # Get the predicted category and its probabilities
        predicted_category = max(doc.cats, key=doc.cats.get)
        category_probabilities = doc.cats
        
        # Display the prediction result
        st.subheader('Prediction Result:')
        st.write(f'Predicted Category: {predicted_category}')
        st.write('Category Probabilities:', category_probabilities)

if __name__ == '__main__':
    main()