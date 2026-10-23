import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

import numpy as np
import pandas as pd

from src.preparacion_datos import agregar_caracteristicas, visualizar_datos
from src.perceptron_proyecto import (
    binary_cross_entropy,
    entrenar_perceptron,
    preparar_datos,
    sigmoid,
)


PROJECT_DIR = Path(__file__).resolve().parents[1]


class PerceptronProyectoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datos = pd.read_csv(
            PROJECT_DIR / "data" / "sitios_turisticos_cartago.csv"
        )
        cls.datos["es_gratuito"] = cls.datos["precio"].eq(0).astype(int)

    def test_preparar_datos_define_umbral_y_estandariza_dos_entradas(self):
        X, y, medias, desviaciones, umbral = preparar_datos(self.datos)

        self.assertEqual(umbral, 3200)
        np.testing.assert_array_equal(y, [1, 1, 0, 0, 0, 1, 1])
        self.assertEqual(X.shape, (7, 2))
        np.testing.assert_allclose(X.mean(axis=0), [0, 0], atol=1e-12)
        np.testing.assert_allclose(X.std(axis=0), [1, 1], atol=1e-12)
        np.testing.assert_allclose(
            medias,
            self.datos[["calificacion", "es_gratuito"]].to_numpy().mean(axis=0),
        )
        self.assertEqual(len(desviaciones), 2)

    def test_sigmoid_y_perdida_logaritmica_son_finitas(self):
        probabilities = sigmoid(np.array([-1000.0, 0.0, 1000.0]))

        self.assertTrue(np.isfinite(probabilities).all())
        np.testing.assert_allclose(probabilities, [0.0, 0.5, 1.0], atol=1e-12)
        self.assertTrue(
            np.isfinite(binary_cross_entropy(np.array([0.0, 1.0]), probabilities[[0, 2]]))
        )

    def test_entrenamiento_baja_la_perdida_y_produce_parametros_finitos(self):
        X, y, _, _, _ = preparar_datos(self.datos)
        result = entrenar_perceptron(X, y)

        self.assertLess(result.loss_history[-1], result.loss_history[0])
        self.assertEqual(result.weights.shape, (2,))
        self.assertTrue(np.isfinite(result.weights).all())
        self.assertTrue(np.isfinite(result.bias))
        self.assertEqual(len(result.loss_history), 2001)

    def test_rechaza_entradas_distintas_de_dos_variables(self):
        with self.assertRaisesRegex(ValueError, "exactamente dos"):
            entrenar_perceptron(np.ones((3, 1)), np.array([0.0, 1.0, 0.0]))

    def test_visualizacion_genera_grafico_de_entradas_y_objetivo(self):
        datos = agregar_caracteristicas(self.datos)
        with TemporaryDirectory() as carpeta_temporal:
            visualizar_datos(datos, carpeta_temporal)
            grafico = Path(carpeta_temporal) / "seaborn_entradas_objetivo.png"
            self.assertTrue(grafico.is_file())
            self.assertGreater(grafico.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
