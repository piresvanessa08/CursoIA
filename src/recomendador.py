def recomendar_con_ia(datos, categoria_filtro=None, solo_gratis=False):
    recomendaciones = []
    
    for sitio in datos:
        score = 0.0
        
        if categoria_filtro:
            if categoria_filtro.lower() in sitio["categoria"].lower():
                score += 50.0
        else:
            score += 20.0
            
        if solo_gratis and sitio["precio"] == 0.0:
            score += 30.0
        elif not solo_gratis:
            score += 15.0
            
        score += (sitio["calificacion"] * 5)
        
        sitio_copia = sitio.copy()
        sitio_copia["compatibilidad"] = round(score, 1)
        recomendaciones.append(sitio_copia)
        
    recomendaciones_ordenadas = sorted(recomendaciones, key=lambda x: x["compatibilidad"], reverse=True)
    return recomendaciones_ordenadas

    if filtrado.empty:
        return df[df["precio_promedio"] <= presupuesto].head(3).copy()

    recomendados = filtrado[filtrado["precio_promedio"] <= presupuesto].copy()
    if recomendados.empty:
        recomendados = filtrado.head(3).copy()

    return recomendados.sort_values("precio_promedio").reset_index(drop=True)
