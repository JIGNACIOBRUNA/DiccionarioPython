from conexion import conexion

def consult():
    connection = conexion()
    
    if connection is None:
        return None
    
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT
                p."EAN",
                p."SKU",
                m."Name" AS "Market",
                pr."normal_price"
            FROM
                "Product" p
            JOIN
                "Market" m ON p."MarketID" = m."MarketID"
            JOIN
                "Price" pr ON p."ProductId" = pr."productID"
            WHERE
                pr."active " = true
                AND pr."create_date" = (
                    SELECT
                        MAX("create_date")
                    FROM
                        "Price"
                    WHERE
                        "ProductId" = p."ProductId"
                        AND "active " = true
                        AND "normal_price" = (
                            SELECT
                                MIN("normal_price")
                            FROM
                                "Price"
                            WHERE
                                "ProductId" = p."ProductId"
                                AND "active " = true
                        )
                )
            """
            cursor.execute(query)

            results = cursor.fetchall()
        
        return results
    
    except Exception as ex:
        print(f"Error al realizar la consulta: {ex}")
        return None

        
resultados = consult()
print(resultados)



# SELECT
#     p."EAN",
#     p."SKU",
#     m."Name" AS "Market",
#     pr."normal_price"
# FROM
#     "Product" p
# JOIN
#     "Market" m ON p."MarketID" = m."MarketID"
# JOIN
#     "Price" pr ON p."ProductId" = pr."productID"
# WHERE
#     pr."active " = true
#     AND pr."create_date" = (
#         SELECT
#             MAX("create_date")
#         FROM
#             "Price"
#         WHERE
#             "ProductId" = p."ProductId"
#             AND "active " = true
#             AND "normal_price" = (
#                 SELECT
#                     MIN("normal_price")
#                 FROM
#                     "Price"
#                 WHERE
#                     "ProductId" = p."ProductId"
#                     AND "active " = true
#             )
#     );


#    EAN            SKU     Market     normal_price
#   "EAN001    "    1       Market1     10
#   "EAN002    "    2       Market2     20