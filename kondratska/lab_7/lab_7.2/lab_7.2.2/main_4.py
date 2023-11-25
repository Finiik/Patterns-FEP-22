from pipeline import Pipeline
import pandas as pd


class GenreProcessor(Pipeline):
    def process_request_1(self, genres):
        return self.data[self.data['Genre'].isin(genres)]

    def process_request_2(self, genres):
        genres = self.data[self.data['Genre'].isin(genres)]
        return genres.describe()


class DeveloperProcessor(Pipeline):
    def process_request_1(self, developers):
        return self.data[self.data['Developer'].isin(developers)]

    def process_request_2(self, developers):
        developer_data = self.data[self.data['Developer'].isin(developers)]
        return developer_data.describe()


if __name__ == "__main__":
    # Instantiate GenreProcessor
    genre_pipeline = GenreProcessor("C:/Users/kondr/Desktop/uni_2_year/LABS/patterns/lab_7/lab_7.2/"
                                    "lab_7.2.2/dataset/playstation_4_games.csv")

    # Example 1: Get games for specific genres
    specific_genres = ['Action', 'Adventure']
    games_for_genres = genre_pipeline.process_request_1(specific_genres)
    print("Games for Specific Genres:")
    print(games_for_genres)

    # Example 2: Get simple statistics for specific genres
    genre_statistics = genre_pipeline.process_request_2(specific_genres)
    print("\nStatistics for Specific Genres:")
    print(genre_statistics)

    # Visualize the 'Genre' column
    genre_pipeline.visualize_features('Genre')

    # Instantiate DeveloperProcessor
    developer_pipeline = DeveloperProcessor("C:/Users/kondr/Desktop/uni_2_year/LABS/patterns/lab_7/lab_7.2/"
                                            "lab_7.2.2/dataset/playstation_4_games.csv")

    # Example 3: Get games for specific developers
    specific_developers = ['Gonzo Games', 'Toxic Games']
    available_developers = developer_pipeline.data['Developer'].unique()
    print("Available Developers:", available_developers)
    games_for_developers = developer_pipeline.process_request_1(specific_developers)
    print("\nGames for Specific Developers:")
    print(games_for_developers)

    # Example 4: Get simple statistics for specific developers
    developer_statistics = developer_pipeline.process_request_2(specific_developers)
    print("\nStatistics for Specific Developers:")
    print(developer_statistics)

    # Visualize the 'Developer' column
    developer_pipeline.visualize_features('Developer')
