# Music Demand Pipeline

A provider-agnostic data preprocessing pipeline for music demand forecasting research.

## Motivation

The original demand forecasting pipeline depended on Spotify data. This project decouples data ingestion from downstream machine learning by converting heterogeneous music popularity sources into a common canonical schema.

## Pipeline

Data Source

↓

Validation

↓

Canonical Schema

↓

Weekly Demand Vectors

↓

Spline Labels

↓

Forecasting Model

## Current Features

- Canonical demand schema
- Data validation
- Weekly demand vector generation
- Config-driven preprocessing

## Planned Features

- Soundcharts loader
- Multiple provider support
- Automated testing
- Logging
- CI/CD
- Benchmark suite
