import json
import pandas as pd

class Few_Shot_posts:
    def __init__(self, file_path='data/processed_posts.json'):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            df = pd.json_normalize(data)
            df['Length'] = df['line_count'].apply(self.line_count_categories)
            tags = df['tags'].apply(lambda x: x).sum()
            tags = list(set(tags))
            self.unique_tags = tags
            self.df = df
    
    def line_count_categories(self, line_count):
        if line_count < 5:
            return 'Short'
        elif 5 <= line_count < 11:
            return 'Medium'
        else:
            return 'Long'
        
    def get_tags(self):
        return self.unique_tags
    
    def get_filtered_posts(self, length, tag):
        df_filtered = self.df[(self.df['Length'] == length) & (self.df['tags'].apply(lambda tags: tag in tags))]
        return df_filtered.to_dict(orient='records')

if __name__ == "__main__":
    fs = Few_Shot_posts()
    posts = fs.get_filtered_posts("Medium", "Robotics")
    print(posts)
