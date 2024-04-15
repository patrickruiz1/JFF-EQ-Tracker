import sqlite3

database = sqlite3.connect("JFFEQTracker.db")
db = database.cursor()

# Create Fixtures Tables
db.execute("""
           CREATE TABLE IF NOT EXISTS Fixtures (
           FixtureID VARCHAR(10) PRIMARY KEY, 
           Model TEXT, 
           PartNumber INTEGER, 
           Rev TEXT
           )
           """)

# Create LoadCells Table 
db.execute("""
           CREATE TABLE IF NOT EXISTS LoadCells (
           LoadCellID VARCHAR(10) PRIMARY KEY, 
           Model TEXT, 
           CalFreq INTEGER,
           IsActive TEXT
           )
           """)

# Create Calibrations Table
db.execute("""
           CREATE TABLE IF NOT EXISTS Calibrations (
           CalID INTEGER PRIMARY KEY, 
           LoadCellID VARCHAR(10), 
           CalDate DATE, 
           CalDue DATE, 
           CalCert VARCHAR,
           FOREIGN KEY (LoadCellID) REFERENCES LoadCells(LoadCellID)
           )
           """)

# Create JawForceFixtures Table
db.execute("""
           CREATE TABLE IF NOT EXISTS JawForceFixtures( 
           JFFID INTEGER PRIMARY KEY,
           FixtureID VARCHAR(10), 
           LoadCellID VARCHAR(10), 
           EQDIR INTEGER, 
           EQDate DATE, 
           FOREIGN KEY (FixtureID) REFERENCES Fixtures(FixtureID), 
           FOREIGN KEY (LoadCellID) REFERENCES LoadCells(LoadCellID)
           )
           """)

database.commit()
db.close()