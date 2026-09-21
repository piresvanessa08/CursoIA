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

        if not solo_gratis:
            score += 15.0

        score += sitio["calificacion"] * 5

        sitio_copia = sitio.copy()
        sitio_copia["compatibilidad"] = round(score, 1)
        recomendaciones.append(sitio_copia)

    return sorted(
        recomendaciones,
        key=lambda sitio: sitio["compatibilidad"],
        reverse=True
    )
