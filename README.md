# ✈️ Flight Price Prediction Challenge

An intelligent flight booking recommendation system that analyzes price trends and recommends the optimal day to book your flight.

## 🎯 Problem Statement

Given flight prices for the next 30 days, determine the best day to book to get the optimal balance between:
- **Lowest price** - Getting the best deal
- **Booking certainty** - Not waiting too long and missing deals
- **Risk management** - Avoiding price spikes

## 🚀 Solution Approach

### Multi-Factor Analysis Strategy

The solution uses a sophisticated scoring system that considers:

1. **Price Analysis** (50% weight)
   - Compares each day's price against the mean and standard deviation
   - Identifies exceptional deals

2. **Trend Analysis** (20% weight)
   - Uses moving averages to detect price trends
   - Identifies if prices are increasing or decreasing

3. **Risk Assessment** (20% weight)
   - Calculates the probability of future price increases
   - Measures the magnitude of potential price spikes

4. **Time Penalty** (10% weight)
   - Slight preference for earlier booking to reduce uncertainty
   - Prevents over-optimization that leads to missing deals

### Key Features

- **Smart Early Booking**: If an exceptional deal appears early (> 1.5 std dev below average), recommends immediate booking
- **Trend Detection**: Uses moving averages to identify price patterns
- **Risk-Adjusted Scoring**: Balances potential savings against risk of price increases
- **Comprehensive Analysis**: Provides detailed price pattern analysis

## 📋 Requirements

```bash
Python 3.7+
```

No external dependencies required - uses only Python standard library!

## 💻 Usage

### Basic Usage

```python
from solution import find_best_booking_time

# Your price data for the next 30 days
prices = [1200, 1150, 1100, 1050, 1000, 1050, 1100, 1150]

# Get recommendation
best_day = find_best_booking_time(prices)
print(f"Book on day {best_day} at ${prices[best_day]}")
```

### Advanced Analysis

```python
from solution import find_best_booking_time, analyze_price_patterns

prices = [1200, 1180, 1190, 1170, 1150, 1160, 1140, 1120, 1100]

# Get recommendation
best_day = find_best_booking_time(prices)

# Get detailed analysis
analysis = analyze_price_patterns(prices)

print(f"Best booking day: {best_day}")
print(f"Price on that day: ${prices[best_day]}")
print(f"Average price: ${analysis['avg_price']:.2f}")
print(f"Price trend: {analysis['trend']}")
print(f"Volatility: {analysis['price_volatility']:.2%}")
```

### Run Examples

```bash
python solution.py
```

## 📊 Example Scenarios

### Example 1: Simple Decreasing Trend
```python
prices = [1000, 950, 900, 1100, 850]
# Recommends: Day 4 (Price: $850)
# Rationale: Lowest price with no significant future drop expected
```

### Example 2: U-Shaped Pattern
```python
prices = [1200, 1150, 1100, 1050, 1000, 1050, 1100, 1150, 1200]
# Recommends: Day 4 (Price: $1000)
# Rationale: Minimum price before the upward trend begins
```

### Example 3: Volatile Market
```python
prices = [1000, 1200, 950, 1300, 900, 1250, 950, 1100, 920]
# Recommends: Day 4 or 8 (depending on risk assessment)
# Rationale: Balances low price with acceptable risk
```

### Example 4: Early Deal
```python
prices = [800, 1100, 1150, 1200, 1180, 1190, 1200]
# Recommends: Day 0 (Price: $800)
# Rationale: Exceptional deal detected early - book immediately!
```

## 🧪 Testing

The solution includes built-in examples that demonstrate various scenarios:

```bash
python solution.py
```

This will run 4 different test cases and show:
- Recommended booking day
- Price on that day
- Detailed analysis (for complex scenarios)
- Reasoning behind the recommendation

## 🔍 Algorithm Details

### Scoring Formula

```
Total Score = (Price Score × 0.5) + (Trend Score × 0.2) + (Risk Score × 0.2) - (Time Penalty × 0.1)
```

Where:
- **Price Score**: `(avg_price - current_price) / std_deviation`
- **Trend Score**: Negative of moving average deviation (lower is better)
- **Risk Score**: Probability × magnitude of future price increases
- **Time Penalty**: `current_day / total_days × 0.3`

### Early Booking Trigger

If any price in the first 10 days is below `average - 1.5 × std_deviation`, recommend immediate booking.

## 📁 Repository Structure

```
flight-price-prediction/
├── solution.py          # Main solution with all functions
├── README.md           # This file
├── examples.py         # Additional test cases (optional)
└── requirements.txt    # Dependencies (empty - no external deps!)
```

## 🎓 Educational Value

This solution demonstrates:
- **Statistical Analysis**: Mean, standard deviation, moving averages
- **Risk Management**: Probabilistic decision making
- **Algorithm Design**: Multi-factor scoring systems
- **Python Best Practices**: Type hints, documentation, clean code

## 🤝 Contributing

Feel free to submit issues or pull requests to improve the algorithm!

Ideas for enhancement:
- Machine learning predictions based on historical data
- Seasonal pattern recognition
- Integration with real flight APIs
- Visualization of price trends and recommendations

## 📄 License

MIT License - feel free to use this in your projects!

## 👨‍💻 Author

Created as a solution to the Flight Price Prediction Challenge

---

**Happy Booking! ✈️💰**