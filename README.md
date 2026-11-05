# CMMS Andina

Sistema de Gestión de Mantenimiento e Insumos Industriales para **Manufacturas Andina S.A.**

Proyecto semestral de Ingeniería de Requisitos (RQY1101) - Duoc UC.
Autor: Esteban Chacana (Product Owner / Scrum Master / Desarrollador)

## Tecnologías

- Python + Flask (backend y pantallas)
- SQLite (base de datos)
- HTML + CSS (interfaces, funcionan en celular)

## Historias de Usuario del Sprint 1

| ID | Historia | Estado |
|----|----------|--------|
| HU-001 | Registro de activos | En desarrollo |
| HU-002 | Identificación por QR | Pendiente |
| HU-003a | Reporte de anomalía con foto | En desarrollo |
| HU-003b | Gestión de Órdenes de Trabajo | Pendiente |

## Estructura

```
database/   -> diseño de la base de datos (schema.sql y diagrama)
src/        -> código de la aplicación
docs/       -> documentación
```

## Cómo ejecutar

```
pip install -r src/requirements.txt
python src/app.py
```

Abrir en el navegador: http://localhost:5000
