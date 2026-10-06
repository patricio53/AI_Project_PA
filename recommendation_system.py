import pandas as pd


# DataFrame ficticio con clientes, historial de compras y calificaciones.
datos = {
	"cliente": ["Ana", "Luis", "Marta", "Carlos", "Sofia", "Diego"],
	"historial_compras": [
		["Auriculares", "Teclado"],
		["Teclado", "Mouse"],
		["Auriculares", "Mouse"],
		["Teclado", "Auriculares"],
		["Mouse", "Teclado"],
		["Auriculares", "Mouse"],
	],
	"producto": ["Auriculares", "Teclado", "Mouse", "Teclado", "Mouse", "Auriculares"],
	"calificacion": [5, 4, 4, 5, 3, 4],
}

df = pd.DataFrame(datos)


def recomendar_producto(dataframe: pd.DataFrame):
	"""Devuelve el producto con la calificación promedio más alta."""
	if dataframe.empty:
		return None

	promedios = dataframe.groupby("producto")["calificacion"].mean()
	return promedios.idxmax()


if __name__ == "__main__":
	print(f"Producto recomendado: {recomendar_producto(df)}")

