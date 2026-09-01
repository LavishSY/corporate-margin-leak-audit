-- Day 1: Target Database Architecture Matching Your Selected Kaggle Dataset
CREATE TABLE raw_ecommerce_sales (
    order_id VARCHAR(50),
    order_date DATE,
    customer_name VARCHAR(150),
    customer_segment VARCHAR(100),
    country VARCHAR(100),
    region VARCHAR(100),
    product_category VARCHAR(100