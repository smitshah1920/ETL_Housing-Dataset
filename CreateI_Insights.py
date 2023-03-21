from common.base import session

# Creating the view with the appropriate metrics
query = """
CREATE OR REPLACE VIEW insights AS
SELECT county,
       count (*) AS sales_count,
       sum (CAST(price AS int)) AS sales_total,
       max (CAST(price AS int)) AS sales_max,
       min (CAST(price AS int)) AS sales_min,
       avg (CAST(price AS int))::numeric(10,2) AS sales_avg
FROM ppr_clean_all
GROUP BY county
"""

# Executing and committing
session.execute(query)
session.commit()