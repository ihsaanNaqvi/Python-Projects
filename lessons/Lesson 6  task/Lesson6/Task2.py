import os
import zipfile
import string
import numpy as np

class NamesDataset:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.data = []
        self.countries = []
        self.letters = list(string.ascii_lowercase)  # Dictionary of English letters
        self.letter_to_index = {letter: i for i, letter in enumerate(self.letters)}

        # Extract files and process data
        self._load_data()

    def _load_data(self):
        with zipfile.ZipFile(self.zip_path, 'r') as archive:
            archive.extractall("temp_data")  # Extract contents

            for file_name in archive.namelist():
                country = file_name.replace(".txt", "")
                self.countries.append(country)

                with open(os.path.join("temp_data", file_name), "r", encoding="utf-8") as f:
                    names = f.read().strip().split("\n")
                    for name in names:
                        self.data.append((name.lower(), country))

        # Assign index to each country
        self.country_to_index = {country: i for i, country in enumerate(self.countries)}

    def _one_hot_encode(self, name):
        """Convert a name into a sequence of one-hot vectors."""
        one_hot_vectors = []
        for letter in name:
            vector = np.zeros(len(self.letters))
            if letter in self.letter_to_index:
                vector[self.letter_to_index[letter]] = 1
            one_hot_vectors.append(vector)
        return np.array(one_hot_vectors)

    def __getitem__(self, idx):
        """Return input (one-hot encoded name) and output (one-hot country vector)."""
        name, country = self.data[idx]
        input_vector = self._one_hot_encode(name)

        output_vector = np.zeros(len(self.countries))
        output_vector[self.country_to_index[country]] = 1

        return input_vector, output_vector

    def __len__(self):
        """Return the total number of words."""
        return len(self.data)

# Example usage
zip_path = r"D:\MS Big Data and Data Science\Second Semester\Python programming By Sir Mikhail Ovsiannikov\Python-Projects\lessons\Lesson 6  task\names.zip"
dataset = NamesDataset(zip_path)

# Fetch an example
input_vector, output_vector = dataset[0]
print("Input (one-hot encoded name):", input_vector)
print("Output (one-hot encoded country):", output_vector)
print("Total words:", len(dataset))
