# Flight Price Recommendation System

This project provides a straightforward method for identifying the best day to book a flight based on a short-term list of prices. The goal is to find a balance between securing a low fare and avoiding the risk of future price increases.

## Problem Overview

Given flight prices for the upcoming days, the system recommends a booking day by considering price levels, short-term trends, the likelihood of price spikes, and the cost of waiting longer.

## Approach

The recommendation is based on a scoring system that evaluates each day using four components.

1. **Price Evaluation (50%)**
   Each day's price is compared with the average and standard deviation to highlight unusually low prices.

2. **Trend Evaluation (20%)**
   A moving-average comparison helps determine whether prices are rising, falling, or stable around each day.

3. **Risk Evaluation (20%)**
   The system checks how often and how significantly future prices exceed the current day's price.

4. **Time Penalty (10%)**
   A small penalty for later days encourages practical early booking and prevents unnecessary waiting.

### Early Booking Rule

If a price appears early that is significantly below the typical range (more than 1.5 standard deviations below the mean), the system recommends booking immediately.

## Features

* Detects unusually low prices
* Identifies basic trends from moving averages
* Evaluates the probability and severity of future price increases
* Uses only Python’s standard library

## Usage Summary

You can call the main function with a list of daily prices to receive the recommended booking day. Additional analysis functions provide details such as volatility, overall trend, and key statistics.

Example outcomes include decreasing trends, U-shaped curves, volatile price sequences, and early low-price opportunities. The system adapts its recommendation based on these patterns.

## Algorithm Summary

The total score for each day is calculated by combining price score, trend score, risk score, and a time penalty. Trend scores use moving averages, risk scores examine higher future prices, and the time penalty grows gradually over the range of days.

## Repository Structure

flight-price/

* solution.py
* README.md
* examples.py (optional)
* requirements.txt

## Contributing

Improvements are welcome. Possible areas for expansion include integrating learning-based models, handling seasonal effects, connecting to real pricing APIs, and adding visualisations.
