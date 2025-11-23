from typing import List
import statistics


def find_best_booking_time(prices: List[float]) -> int:
    if not prices:
        return 0

    n = len(prices)

    min_price = min(prices)
    min_day = prices.index(min_price)

    window = min(7, n // 4)
    trends = calculate_trend_scores(prices, window)

    best_day = 0
    best_score = float("-inf")

    avg_price = statistics.mean(prices)
    std_price = statistics.stdev(prices) if n > 1 else 0

    for day in range(n):
        price_score = (avg_price - prices[day]) / (std_price + 1)
        trend_score = -trends[day] if day < len(trends) else 0
        time_penalty = (day / n) * 0.3
        future_risk = calculate_future_risk(prices, day)

        total_score = (
            price_score * 0.5
            + trend_score * 0.2
            + future_risk * 0.2
            - time_penalty
        )

        if total_score > best_score:
            best_score = total_score
            best_day = day

    threshold = avg_price - std_price * 1.5
    for day in range(min(10, n)):
        if prices[day] <= threshold:
            return day

    return best_day


def calculate_trend_scores(prices: List[float], window: int) -> List[float]:
    trends = []
    for i in range(len(prices)):
        if i < window:
            avg = statistics.mean(prices[: i + 1])
        else:
            avg = statistics.mean(prices[i - window : i])
        trends.append(prices[i] - avg)
    return trends


def calculate_future_risk(prices: List[float], day: int) -> float:
    if day >= len(prices) - 1:
        return 0

    future = prices[day + 1 :]
    current = prices[day]

    higher_days = [p for p in future if p > current]
    ratio = len(higher_days) / len(future)
    avg_increase = (
        statistics.mean([p - current for p in higher_days]) if higher_days else 0
    )

    return ratio * (1 + avg_increase / (current + 1))


def analyze_price_patterns(prices: List[float]) -> dict:
    if not prices:
        return {}

    min_price = min(prices)
    max_price = max(prices)

    analysis = {
        "min_price": min_price,
        "max_price": max_price,
        "avg_price": statistics.mean(prices),
        "std_dev": statistics.stdev(prices) if len(prices) > 1 else 0,
        "min_day": prices.index(min_price),
        "max_day": prices.index(max_price),
        "price_volatility": (max_price - min_price)
        / statistics.mean(prices),
    }

    half = len(prices) // 2
    first_half_avg = statistics.mean(prices[:half])
    second_half_avg = statistics.mean(prices[half:])

    if second_half_avg > first_half_avg * 1.05:
        analysis["trend"] = "increasing"
    elif second_half_avg < first_half_avg * 0.95:
        analysis["trend"] = "decreasing"
    else:
        analysis["trend"] = "stable"

    return analysis
