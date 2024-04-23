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
           Sensor_SN INTEGER,
           Sensor_ItemNo VARCHAR,
           Sensor_Model VARCHAR, 
           Instrument_SN INTEGER, 
           Instrument_ItemNo VARCHAR,
           Instrument_Model VARCHAR
           )
           """)

# Create Calibrations Table
db.execute("""
           CREATE TABLE IF NOT EXISTS Calibrations (
           CalCertID INTEGER PRIMARY KEY, 
           LoadCellID VARCHAR(10), 
           CalDate DATE, 
           CalDue DATE, 
           FOREIGN KEY (LoadCellID) REFERENCES LoadCells(LoadCellID)
           )
           """)

# Create Equivalency Table
db.execute("""
           CREATE TABLE IF NOT EXISTS Equivalency( 
           EQDIR VARCHAR PRIMARY KEY,
           FixtureID VARCHAR(10), 
           LoadCellID VARCHAR(10), 
           EQDate DATE, 
           EQDIR_Ref VARCHAR,
           FOREIGN KEY (EQDIR_Ref) REFERENCES Equivalency(EQDIR)
           )
           """)

database.commit()
db.close()