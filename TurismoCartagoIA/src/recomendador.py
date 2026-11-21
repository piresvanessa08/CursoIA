def recomendar_con_ia(datos, categoria_filtro=None, solo_gratis=False):
    recomendaciones = []

    for sitio in datos:
        if solo_gratis and sitio["precio"] != 0.0:
            continue

        score = 0.0

        if categoria_filtro:
            if isinstance(categoria_filtro, (list, tuple, set)):
                coincide_categoria = any(
                    categoria.lower() in sitio["categoria"].lower()
                    for categoria in categoria_filtro
                )
            else:
                coincide_categoria = categoria_filtro.lower() in sitio["categoria"].lower()

            if not coincide_categoria:
                continue

            score += 50.0
        else:
            score += 20.0

        if solo_gratis and sitio["precio"] == 0.0:
            score += 30.0
        elif not solo_gratis:
            score += 15.0

        if sitio["calificacion"] is not None:
            score += sitio["calificacion"] * 5
        else:
            score -= 10

        sitio_copia = sitio.copy()
        datos_estimados = bool(sitio.get("datos_estimados", False))
        sitio_copia["compatibilidad"] = round(score, 1)
        sitio_copia["datos_estimados"] = datos_estimados
        sitio_copia["datos_verificados"] = (
            not datos_estimados
            and bool(sitio.get("fuente"))
            and sitio["calificacion"] is not None
            and sitio["precio"] is not None
        )
        recomendaciones.append(sitio_copia)

    recomendaciones_ordenadas = sorted(recomendaciones, key=lambda x: x["compatibilidad"], reverse=True)
    return recomendaciones_ordenadas
