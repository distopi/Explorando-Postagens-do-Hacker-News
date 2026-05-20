import csv
import datetime as dt
import sys
from collections import defaultdict

FILE_PATH = 'hacker_news.csv'


def load_data(filepath: str) -> list[dict]:
    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"O arquivo '{filepath}' não foi encontrado.")
        sys.exit(1)


def separate_posts(data: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    ask_posts, show_posts, other_posts = [], [], []

    for row in data:
        title = row.get('title', '').lower()

        if title.startswith('ask hn'):
            ask_posts.append(row)
        elif title.startswith('show hn'):
            show_posts.append(row)
        else:
            other_posts.append(row)

    return ask_posts, show_posts, other_posts


def calculate_average_comments(posts: list[dict]) -> float:
    if not posts:
        return 0.0

    total_comments = sum(int(post.get('num_comments', 0)) for post in posts)
    return total_comments / len(posts)


def calculate_hourly_average(posts: list[dict]) -> list[tuple[float, str]]:

    comments_by_hour = defaultdict(int)
    counts_by_hour = defaultdict(int)
    date_format = "%m/%d/%Y %H:%M"

    for post in posts:
        created_at = post.get('created_at')
        num_comments = int(post.get('num_comments', 0))

        if not created_at:
            continue

        try:
            hour = dt.datetime.strptime(created_at, date_format).strftime("%H")
            comments_by_hour[hour] += num_comments
            counts_by_hour[hour] += 1
        except ValueError:
            continue
    avg_by_hour = [
        (comments / counts_by_hour[hour], hour)
        for hour, comments in comments_by_hour.items()
    ]

    return sorted(avg_by_hour, reverse=True)


def main():
    print("📊 Iniciando análise do Hacker News...\n")

    hn_data = load_data(FILE_PATH)
    ask_posts, show_posts, other_posts = separate_posts(hn_data)

    print("--- DISTRIBUIÇÃO DOS POSTS ---")
    print(f"Ask HN: {len(ask_posts)} posts")
    print(f"Show HN: {len(show_posts)} posts")
    print(f"Outros: {len(other_posts)} posts\n")

    avg_ask = calculate_average_comments(ask_posts)
    avg_show = calculate_average_comments(show_posts)

    print("--- MÉDIA DE COMENTÁRIOS ---")
    print(f"Ask HN: {avg_ask:.2f} comentários/post")
    print(f"Show HN: {avg_show:.2f} comentários/post\n")

    # 3. Análise Temporal (Melhores Horários)
    print("--- TOP 5 HORÁRIOS PARA POSTAR 'ASK HN' ---")
    hourly_averages = calculate_hourly_average(ask_posts)

    for avg, hr in hourly_averages[:5]:
        formatted_time = dt.datetime.strptime(hr, "%H").strftime("%H:%M")
        print(f"⏰ {formatted_time} -> {avg:.2f} comentários em média por post")


if __name__ == "__main__":
    main()