from collections import defaultdict
from conexion import conexion

def group_products():
    connection = conexion()
    
    if connection is None:
        print("No se pudo establecer conexión.")
        return None
    
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT
                p."EAN",
                p."Name" AS "ProductName",
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
            # print("Resultados de la consulta")
            # for row in results:
            #     print(row)   
    
        productos_agrupados = defaultdict(list)
    
        for producto in results:
                ean = producto[0]
                nombre_producto = producto[1] 
                datos_query = {"Market": producto[2], "normal_price": producto[3]}
                # print(f"EAN: {ean}, Nombre Producto: {nombre_producto}, Datos Query: {datos_query}")
                
                if ean not in productos_agrupados:
                    productos_agrupados[ean] = {
                        "nombre_producto": nombre_producto,
                        "datos_query": [],
                        "markets_diferentes": set(),
                        "rango_precios": (float('inf'), float('-inf'))
                    }

                productos_agrupados[ean]["datos_query"].append(datos_query)
                productos_agrupados[ean]["markets_diferentes"].add(producto[2])
                productos_agrupados[ean]["rango_precios"] = (
                    min(productos_agrupados[ean]["rango_precios"][0], producto[3]),
                    max(productos_agrupados[ean]["rango_precios"][1], producto[3])
                )
        # print("Productos Agrupados:", dict(productos_agrupados))
        resultado_final = [{"Ean": ean, **productos_agrupados[ean]} for ean in productos_agrupados]
        
        for item in resultado_final:
            ean = item["Ean"]
            nombre_producto = item["nombre_producto"]
            datos_query = item["datos_query"]
            cantidad_markets = len(item["markets_diferentes"])
            rango_precios = item["rango_precios"]
            
            print(f"Ean: {ean}, Nombre Producto: {nombre_producto}, Datos Query: {datos_query}, Cantidad de Markets Diferentes: {cantidad_markets}, Rango de Precios: {rango_precios}")
        
        return resultado_final
        
    except Exception as ex:
            print(f"Error al realizar la consulta y agrupación: {ex}")
            return None
        
group_products()
        
    
   