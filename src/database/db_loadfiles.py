import sqlite3
import csv
import os

def load_calibrationdata():
    file_path = os.path.join(os.getcwd(), 'resources', 'data', 'CalibrationData.csv') 

    with open (file_path, 'r')  as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            db.execute('''INSERT OR IGNORE INTO Calibrations (CalCertID, LoadCellID, CalDate, CalDue) VALUES (?, ?, ?, ?)''', (int(line[0]), line[1], line[2], line[3]))

    file.close()

def load_equivalencydata():
    file_path = os.path.join(os.getcwd(), 'resources', 'data', 'EquivalencyData.csv')

    with open(file_path, 'r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            db.execute('''INSERT OR IGNORE INTO Equivalency (EQDIR, FixtureID, LoadCellID, EQDate, EQDIR_Ref) VALUES (?, ?, ?, ?, ?)''',(int(line[0]), line[1], line[2], line[3], line[4]))

def load_fixturedata():
    file_path = os.path.join(os.getcwd(), 'resources', 'data', 'FixtureData.csv')

    with open (file_path) as file:
        csv_file = csv.reader(file)
        next(csv_file)

        for line in csv_file:
            db.execute('''INSERT OR IGNORE INTO Fixtures (FixtureID, Model, PartNumber, Rev) VALUES (?, ?, ?, ?)''', (line[0], line[1], int(line[2]), line[3]))

def load_loadcelldata():
    file_path = os.path.join(os.getcwd(), 'resources', 'data', 'LoadCellData.csv')

    with open (file_path) as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            db.execute('''INSERT OR IGNORE INTO LoadCells (LoadCellID, Model, Sensor_SN, Sensor_ItemNo, Sensor_Model, Instrument_SN, Instrument_ItemNo, Instrument_Model) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',(line[0], line[1], int(line[2]), line[3], line[4], int(line[5]), line[6], line[7]))


database = sqlite3.connect("JFFEQTracker.db")
db = database.cursor()

# os.system('clear')
load_calibrationdata()
load_equivalencydata()
load_fixturedata()
load_loadcelldata()

database.commit()
db.close()