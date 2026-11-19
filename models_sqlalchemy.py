from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database_sqlalchemy import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(67), nullable=False)
    creado_en = Column(TIMESTAMP, server_default=func.now())

   # Relaciones
    categorias = relationship("Categoria", back_populates="usuario")
    cuentas = relationship("Cuenta", back_populates="usuario")
    transacciones = relationship("Transaccion", back_populates="usuario")
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    tipo = Column(String(10), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"),nullable=False)

    #relaciones
    usuario = relationship("Usuario", back_populates="categorias")
    transacciones = relationship("Transaccion", back_populates="categoria")

class Cuenta(Base):
    __tablename__ = "cuentas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"),nullable=False)

    #relaciones
    usuario = relationship("Usuario", back_populates="cuentas")
    transacciones = relationship("Transaccion", back_populates="cuenta")

class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Numeric(12,2), nullable=False)
    descripcion = Column(String(255), nullable=False)
    fecha = Column(TIMESTAMP, server_default=func.now())
    categoria_id = Column(Integer, ForeignKey("categorias.id"),nullable=False)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"),nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"),nullable=False)

    #relaciones
    usuario = relationship("Usuario", back_populates="transacciones")
    categoria = relationship("Categoria", back_populates="transacciones")
    cuenta = relationship("Cuenta", back_populates="transacciones")