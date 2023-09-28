import mysql.connector

conexao = mysql.connector.connect(
    host="",
    user="",
    password="password",
    database="AA"
)
cursor = conexao.cursor()

consulta = """
SELECT artist, SUM(sales) AS sales
FROM money_makers_bb mmb 
WHERE `year`  = 2020
GROUP BY artist
ORDER BY sales DESC
LIMIT 1
"""

cursor.execute(consulta)

resultado = cursor.fetchone()

if resultado:
    artista_maior_faturamento = resultado[0]
    faturamento_maior_faturamento = resultado[1]
    print(f"O artista com o maior faturamento em 2020 foi {artista_maior_faturamento} com um faturamento total de {faturamento_maior_faturamento}")
else:
    print("Nenhum resultado encontrado")

cursor.close()
conexao.close()
