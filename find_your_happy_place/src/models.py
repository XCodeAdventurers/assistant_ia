from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateur'
    id = Column(String, primary_key=True, unique=True)
    nom = Column(String)
    prenom = Column(String)
    telephone = Column(String)
    email = Column(String, unique=True)  # Ajout de la contrainte d'unicité pour l'email
    mot_de_passe = Column(String)
    statut = Column(String)
    biens = relationship("Bien", back_populates="utilisateur")

class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(String, primary_key=True, unique=True)
    date_debut = Column(Date)
    date_fin = Column(Date)
    transactions = relationship("Transaction", back_populates="reservation")

class Bien(Base):
    __tablename__ = 'bien'
    id = Column(String, primary_key=True, unique=True)
    type_bien = Column(String)
    adresse = Column(String)
    nb_chambre = Column(Integer)
    designation = Column(String)
    id_utilisateur = Column(String, ForeignKey('utilisateur.id'))
    utilisateur = relationship("Utilisateur", back_populates="biens")
    surface = Column(Integer)
    numero_chambre = Column(Integer)
    prix = Column(Integer)
    description = Column(String)
    images = Column(String)

class Caracteristique(Base):
    __tablename__ = 'caracteristique'
    id = Column(String, primary_key=True, unique=True)
    libelle = Column(String)

class Compte(Base):
    __tablename__ = 'compte'
    id = Column(String, primary_key=True, unique=True)
    numero_compte = Column(String, unique=True)  # Ajout de la contrainte d'unicité pour le numéro de compte
    montant_total = Column(Integer)

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(String, primary_key=True, unique=True)
    date_transaction = Column(Date)
    montant_transaction = Column(Integer)
    id_reservation = Column(String, ForeignKey('reservation.id'))
    reservation = relationship("Reservation", back_populates="transactions")

# Pour établir la connexion à la base de données
engine = create_engine('sqlite:///location_immobiliere.db')
Base.metadata.create_all(engine)

