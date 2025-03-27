import zipfile
import os
import numpy as np
import string

class NamesDataset:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.extract_path = "temp_data"  # Directory for extracted files
        self.alphabet = string.ascii_lowercase  # Dictionary of English letters
        self.letter_to_index = {letter: idx for idx, letter in enumerate(self.alphabet)}
        
        # Load data from the ZIP archive
        self._load_data()

    def _load_data(self):
        """Extracts files and loads names from the archive."""
        # Create extraction directory if it doesn't exist
        if not os.path.exists(self.extract_path):
            os.makedirs(self.extract_path)
        
        # Extract the ZIP archive
        with zipfile.ZipFile(self.zip_path, 'r') as archive:
            archive.extractall(self.extract_path)

        # List to store country names and data (name, country) pairs
        self.countries = []
        self.data = []

        # Folder containing names is inside the extracted directory
        names_folder = os.path.join(self.extract_path, 'names')
        if os.path.exists(names_folder):
            # Loop through the files in the 'names' folder
            for file_name in os.listdir(names_folder):
                if file_name.endswith(".txt"):
                    country = file_name.replace(".txt", "").strip()  # Extract country name from the file name
                    self.countries.append(country)  # Add to country list
                    file_path = os.path.join(names_folder, file_name)

                    # Read names from the country-specific file
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            name = line.strip().lower()
                            if name:
                                self.data.append((name, country))  # Store (name, country) tuple

        # Create a mapping from country names to indices
        self.country_to_index = {country: idx for idx, country in enumerate(self.countries)}

    def _one_hot_encode_name(self, name):
        """Convert a name into a sequence of one-hot vectors."""
        name_vectors = []
        for letter in name:
            # Create a one-hot vector for each letter in the name
            vector = np.zeros(len(self.alphabet))
            if letter in self.letter_to_index:
                vector[self.letter_to_index[letter]] = 1  # Set the corresponding index to 1
            name_vectors.append(vector)
        return np.array(name_vectors)

    def __getitem__(self, idx):
        """Returns a (input_vector, output_vector) pair."""
        if idx >= len(self.data):
            raise IndexError("Index out of range")
        
        name, country = self.data[idx]
        input_vector = self._one_hot_encode_name(name)  # Convert name to one-hot vectors
        
        # Create a one-hot encoded vector for the country
        output_vector = np.zeros(len(self.countries))
        output_vector[self.country_to_index[country]] = 1  # Set the corresponding country index to 1

        return input_vector, output_vector

    def __len__(self):
        """Returns the total number of words (names)."""
        return len(self.data)

# Example usage
zip_path = r"D:/MS Big Data and Data Science/Second Semester/Python programming By Sir Mikhail Ovsiannikov/Python-Projects/lessons/Lesson 6  task/names.zip"
dataset = NamesDataset(zip_path)

# Test the dataset
print("Total words:", len(dataset))

# Print an example
if len(dataset) > 0:
    input_vector, output_vector = dataset[0]
    print("Example input vector (name as one-hot):", input_vector)
    print("Example output vector (country as one-hot):", output_vector)
else:
    print("No names loaded from the dataset.")
