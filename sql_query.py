

sql_qet_all_categories = f"SELECT COUNT(category_guid) AS cnt\
                    FROM categories"


sql_get_categories_guid = f"SELECT guid FROM product_category"

sql_get_categories_name = f"SELECT url, category_guid FROM categories"
sql_get_new_user_phone = f"SELECT phone FROM customers WHERE phone='0665315679'"
sql_delete_new_user = "DELETE FROM customers WHERE name = %s"