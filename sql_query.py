

sql_qet_all_categories = f"SELECT COUNT(id) AS cnt\
                    FROM product_category"


sql_get_categories_guid = f"SELECT guid FROM product_category"

sql_get_categories_name = f"SELECT name, guid FROM product_category"