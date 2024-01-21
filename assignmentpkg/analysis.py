from typing import Any, Optional
import matplotlib.pyplot as plt
import argparse
import yaml
import requests
import logging

class Analysis():
    def __init__(self, analysis_config: str):
        CONFIG_PATHS =['system_config.yml', 'user_config.yml', 'job_config.yml']
        parser = argparse.ArgumentParser(description='Analysis package')
        parser.add_argument('job_config', type=str)
        args = parser.parse_args()
        paths_to_load = CONFIG_PATHS + [args.job_config]
        # setting the logging level
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        self.config = {}
        for path in paths_to_load:
            with open(path, 'r') as file:
                logging.debug('reading from file')
                this_config = yaml.safe_load(file)
            # Check if this_config is not None before updating config
            if this_config:
                self.config.update(this_config)
        logging.info('config dictionary: %s',self.config)
        topic = "artificial intelligence"
        self.url = (
            self.config["url"]
            + 'articlesearch.json?q='
            + topic
            + '&api-key='
            + self.config["api_key"]
        )

    def load_data(self):
        all_articles = []
        page = 0
        logging.info('loading data')
        while True:
            # Add 'page' parameter to the URL for pagination
            url_with_page = f"{self.url}&page={page}"
            try:
                response = requests.get(url_with_page)
                json_resp = response.json()
                articles = json_resp.get("response", {}).get("docs", [])
            except requests.exceptions.HTTPError as httpError:
                logging.error('HTTP Exception raised',httpError.args[0])
            except requests.exceptions.RequestException as re:
                logging.error('request exception',re.response("request exception caused"))
            except requests.exceptions.Timeout as timeEx:
                raise SystemExit(timeEx)
                logging.error('Timeout exception',timeEx)
            except requests.exceptions.TooManyRedirects as redirectException:
                logging.error('Too many redirects',redirectException)
            # Break the loop if no more articles are returned
            if not articles:
                break

            # Extend the list of articles with the new results
            all_articles.extend(articles)
            page += 1

        return all_articles

    def compute_analysis(self):
        articles = self.load_data()

        # Calculate mean word count
        word_counts = [article.get("word_count", 0) for article in articles]
        mean_word_count = sum(word_counts) / len(word_counts) if len(word_counts) > 0 else 0

        print(f"Mean Word Count of Articles: {mean_word_count}")

    def extract_year_from_pub_date(self, pub_date):
        return pub_date.split("-")[0] if pub_date else None

    def plot_data(self, save_path: Optional[str] = None):
        articles = self.load_data()

        # Extract the publication year for each article
        years = [self.extract_year_from_pub_date(article.get("pub_date", "")) for article in articles]

        # Print list of titles and years
        # print("List of Titles and Years:")
        for article in articles:
            title = article.get("headline", {}).get("main")
            pub_year = self.extract_year_from_pub_date(article.get("pub_date", ""))
            print(f"Title: {title}, Year: {pub_year}")

        # Count the occurrences of each year
        year_counts = {year: years.count(year) for year in set(years)}

        # Prepare data for plotting
        sorted_years = sorted(year_counts.keys())
        article_counts = [year_counts[year] for year in sorted_years]
        topic = self.config['topic']
        # Create a bar plot
        plt.bar(sorted_years, article_counts)
        plt.xlabel("Year")
        plt.ylabel("Number of Articles")
        plt.title(f"Number of Articles with {topic} in Title per Year")
        plt.show()

# Test the class and plot the graph
logging.debug('About to instantiate Analysis class')
analysis = Analysis('test')
analysis.plot_data()