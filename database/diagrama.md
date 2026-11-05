# Diagrama de la base de datos

```mermaid
erDiagram
    ACTIVOS ||--o{ REPORTES_FALLA : "tiene"
    REPORTES_FALLA ||--o| ORDENES_TRABAJO : "genera"

    ACTIVOS {
        int id PK
        text codigo UK
        text nombre
        text tipo
        text marca
        text modelo
        text ubicacion
        text criticidad
        text fecha_registro
    }
    REPORTES_FALLA {
        int id PK
        int activo_id FK
        text reportado_por
        text descripcion
        text criticidad
        text foto
        text estado
        text fecha
    }
    ORDENES_TRABAJO {
        int id PK
        int reporte_id FK
        text tecnico
        text estado
        text fecha_creacion
        text fecha_cierre
    }
    USUARIOS {
        int id PK
        text nombre
        text rol
    }
```

## Relaciones

- Un **activo** puede tener muchos **reportes de falla** (HU-003a).
- Un **reporte** puede generar una **orden de trabajo** (HU-003b).
- La tabla **usuarios** define los roles (se usará para el control de acceso en el Sprint 2).
