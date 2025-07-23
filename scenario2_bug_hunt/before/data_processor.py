import pandas as pd
import json
from datetime import datetime

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        
    def load_data(self):
        """Load data from CSV file"""
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Loaded {len(self.data)} records")
        except Exception as e:
            print(f"Error loading data: {e}")
            
    def clean_data(self):
        """Clean the loaded data"""
        # Bug 1: No check if data is loaded
        self.data.dropna(inplace=True)
        
        # Bug 2: Accessing wrong column name
        self.data['price'] = self.data['cost'].str.replace('$', '').astype(float)
        
        # Bug 3: Division by zero potential
        self.data['price_per_unit'] = self.data['price'] / self.data['quantity']
        
        return self.data
    
    def calculate_statistics(self):
        """Calculate summary statistics"""
        if self.data is None:
            return None
            
        stats = {
            'total_records': len(self.data),
            'average_price': self.data['price'].mean(),
            'total_revenue': self.data['price'].sum(),
            'date_processed': datetime.now()
        }
        
        return stats
    
    def save_results(self, output_file):
        """Save processed data to JSON"""
        if self.data is None:
            raise ValueError("No data to save")
            
        # Bug 4: datetime not JSON serializable
        stats = self.calculate_statistics()
        
        result = {
            'data': self.data.to_dict('records'),
            'statistics': stats
        }
        
        with open(output_file, 'w') as f:
            json.dump(result, f)
            
    def process_all(self, output_file):
        """Main processing pipeline"""
        self.load_data()
        cleaned = self.clean_data()
        stats = self.calculate_statistics()
        self.save_results(output_file)
        
        print("Data processing completed successfully")
        return stats

# Usage example
if __name__ == "__main__":
    processor = DataProcessor("sales_data.csv")
    results = processor.process_all("output.json") 