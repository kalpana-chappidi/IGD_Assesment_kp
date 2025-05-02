SELECT 
  txn_id,
  terminal_id,
  amount,
  DATE(txn_time) AS txn_date,
  category
FROM {{ ref('stg_transactions') }}
WHERE amount > 0
