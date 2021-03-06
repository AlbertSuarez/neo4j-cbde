SELECT  l_orderkey,
        sum(l_extendedprice*(1-l_discount)) as revenue,
        o_orderdate,
        o_shippriority
FROM customer, orders, lineitem
WHERE   c_mktsegment = '[SEGMENT]' AND
        c_custkey = o_custkey AND
        l_orderkey = o_orderkey AND
        o_orderdate < '[DATE1]' AND
        l_shipdate > '[DATE2]'
GROUP BY l_orderkey, o_orderdate, o_shippriority
ORDER BY revenue desc, o_orderdate;