-- CMMS Andina - Diseño de base de datos (SQLite)
-- Sprint 1: HU-001, HU-002, HU-003a, HU-003b

CREATE TABLE IF NOT EXISTS usuarios (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre    TEXT NOT NULL,
    rol       TEXT NOT NULL CHECK (rol IN ('Operador','Tecnico','Jefe de Mantenimiento','Bodega'))
);

CREATE TABLE IF NOT EXISTS activos (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,   -- ID único (HU-001)
    codigo        TEXT NOT NULL UNIQUE,                -- código que va en el QR (HU-002)
    nombre        TEXT NOT NULL,
    tipo          TEXT NOT NULL,                       -- extrusora, inyectora, compresor, etc.
    marca         TEXT,
    modelo        TEXT,
    ubicacion     TEXT,
    criticidad    TEXT NOT NULL DEFAULT 'Media' CHECK (criticidad IN ('Alta','Media','Baja')),
    fecha_registro TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS reportes_falla (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    activo_id      INTEGER NOT NULL REFERENCES activos(id),
    reportado_por  TEXT NOT NULL,
    descripcion    TEXT NOT NULL,
    criticidad     TEXT NOT NULL DEFAULT 'Media' CHECK (criticidad IN ('Alta','Media','Baja')),
    foto           TEXT,                               -- nombre del archivo de la foto
    estado         TEXT NOT NULL DEFAULT 'Pendiente' CHECK (estado IN ('Pendiente','Con OT')),
    fecha          TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS ordenes_trabajo (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    reporte_id     INTEGER NOT NULL REFERENCES reportes_falla(id),
    tecnico        TEXT NOT NULL,                      -- técnico responsable
    estado         TEXT NOT NULL DEFAULT 'En Proceso' CHECK (estado IN ('En Proceso','Finalizada')),
    fecha_creacion TEXT NOT NULL DEFAULT (datetime('now')),
    fecha_cierre   TEXT
);
