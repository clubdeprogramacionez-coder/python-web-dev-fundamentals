# 📋 Modelos: La Estructura de Nuestros Datos

## ¿Qué es un Modelo?

Un **modelo** es como un **plano o esquema** que define cómo se ve un objeto en nuestro sistema.

### Analogía del Carnet de Identidad

Tu carnet tiene campos específicos:
- Nombre
- Apellido
- Fecha de nacimiento
- Número de ID
- Foto

Un **modelo** es exactamente eso: decir "cada usuario en nuestro sistema tiene estos campos".

### En Bases de Datos

Si la base de datos es un archivo, el modelo es la forma en que organizamos cada documento:

```
Usuario:
- id (número único)
- nombre (texto)
- email (texto único)
- password (contraseña encriptada)
- fecha_creacion (cuándo se registró)
```

**Producto**:
- id (número único)
- nombre (texto)
- descripcion (texto largo)
- precio (número con decimales)
- stock (cantidad disponible)

## 🏗️ ¿Por Qué Necesitamos Modelos?

### 1. **Validación**
El modelo dice: "un email debe ser válido". Si alguien intenta crear un usuario con email "esto_no_es_email", el modelo lo rechaza automáticamente.

### 2. **Consistencia**
Todos los usuarios tienen exactamente los mismos campos. No hay un usuario con "nombre" y otro con "nombreCompleto". Eso mantiene el orden.

### 3. **Seguridad**
Definimos qué puede ser `null` (vacío), qué es obligatorio, qué no se debe mostrar (como contraseñas).

### 4. **Documentación**
El modelo es como decir: "Mira, aquí te digo exactamente qué es un usuario en nuestro sistema".

## 📊 Tipos de Campos en un Modelo

### Campos Básicos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **String** | Texto | "Juan", "juan@email.com" |
| **Integer** | Número entero | 5, 100, -3 |
| **Float** | Número decimal | 19.99, 3.14 |
| **Boolean** | Verdadero/Falso | True, False |
| **DateTime** | Fecha y hora | 2024-10-01 14:30:00 |
| **Date** | Solo la fecha | 2024-10-01 |

### Características de los Campos

```
id: Integer, Única, No nula, Auto-incremento
Esto significa:
- Es un número
- No puede haber dos iguales (única)
- Obligatoria (no nula)
- Se incrementa automáticamente (1, 2, 3...)
```

## 🔗 Relaciones: Conectando Modelos

A veces, un modelo necesita saber sobre otro modelo. Por ejemplo:

- **Un usuario puede tener muchos pedidos**
- **Un pedido pertenece a exactamente un usuario**

### Tipos de Relaciones

#### 1. **Uno a Muchos** (1:N)
Un usuario tiene muchos pedidos, pero cada pedido pertenece a un usuario.

```
Usuario: Juan
  ├── Pedido 1
  ├── Pedido 2
  └── Pedido 3

Usuario: María
  ├── Pedido 4
  └── Pedido 5
```

#### 2. **Muchos a Muchos** (N:N)
Un estudiante puede inscribirse en muchos cursos, y cada curso tiene muchos estudiantes.

```
Estudiante: Juan → Curso: Python, Curso: JavaScript
Estudiante: María → Curso: Python, Curso: Bases de Datos
```

#### 3. **Uno a Uno** (1:1)
Un usuario tiene exactamente un perfil, y cada perfil pertenece a un usuario.

```
Usuario: Juan ↔ Perfil: Juan (foto, bio, etc)
```

## 💾 Modelos en la Práctica

### En Nuestra Aplicación

Tenemos dos modelos principales:

**`usuario.py`**:
- id
- nombre
- email
- contraseña
- fecha_creacion

**`producto.py`**:
- id
- nombre
- descripción
- precio
- stock
- categoria

### ¿Cómo se Relacionan?

Podrías expandir con:
- Un usuario puede crear muchos productos (tienda personal)
- Un producto puede tener muchas opiniones de usuarios

## 🔍 ORM: Traduciendo Python a SQL

Aquí viene algo importante: **no queremos escribir SQL directamente**. Queremos escribir código Python.

### Sin ORM (SQL puro)
```sql
SELECT * FROM usuarios WHERE email = 'juan@email.com'
```

### Con ORM (SQLAlchemy en Python)
```python
usuario = session.query(Usuario).filter(Usuario.email == 'juan@email.com').first()
```

¿Ves? El ORM es una **traducción automática**. Le decimos en Python qué queremos, y el ORM lo convierte a SQL.

**ORM = Traductor entre Python y SQL**

## 📚 Jerga Técnica Explicada

| Término | Significado |
|---------|-------------|
| **Schema** | El plano o estructura de la BD |
| **Tabla** | Colección de registros de un modelo |
| **Registro** | Una fila (un usuario específico) |
| **Campo** | Una columna (un atributo como email) |
| **Clave Primaria** | El campo único que identifica cada registro (normalmente `id`) |
| **Clave Foránea** | Referencia a un registro en otra tabla |
| **Índice** | Acelera búsquedas (como un índice en un libro) |
| **Constraint** | Regla que la BD debe cumplir (no nulos, únicos, etc) |
| **Migration** | Cambio en la estructura de la BD (agregar campo, eliminar tabla) |

## 🔐 Consideraciones de Seguridad

### Nunca Guardes Contraseñas en Texto Plano

Incorrecto:
```
usuario.password = "mi_contraseña_secreta"
```

Correcto:
```
usuario.password = hash("mi_contraseña_secreta")
```

**Hash** significa: convertir texto en una cadena que no se puede revertir (no se puede descifrar). Si alguien roba la BD, ve hashes, no contraseñas reales.

### Campos Sensibles

Algunos campos no deberían ser visibles:
- Contraseña
- Token de acceso
- Información bancaria

El modelo debe indicar: "este campo es secreto, no lo devuelvas en respuestas API".

## 🎯 Flujo: De Modelo a Base de Datos

```
1. Defines un modelo (usuario.py)
          ↓
2. El ORM crea una tabla en la BD con la estructura que describiste
          ↓
3. Cuando creas un nuevo usuario en Python, se guarda en esa tabla
          ↓
4. Cuando buscas un usuario, el ORM lo recupera de la tabla y lo devuelve como objeto Python
```

## ✨ Lo Importante

- **Los modelos son contratos**: Dicen exactamente cómo se ve cada objeto
- **Validación automática**: El modelo rechaza datos inválidos
- **Documentación viva**: Leyendo los modelos, entiendes qué datos tiene la aplicación
- **Seguridad integrada**: Puedes marcar campos como sensibles o no guardables

---

**Los modelos son el diccionario de tu aplicación. Definen qué es cada cosa y cómo se relacionan entre sí.** 📋
