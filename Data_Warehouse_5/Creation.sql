
CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY,
    FullDate DATE NOT NULL,
    Day INT NOT NULL,
    Month INT NOT NULL,
    MonthName VARCHAR(20) NOT NULL,
    Quarter INT NOT NULL,
    Year INT NOT NULL
);

CREATE TABLE DimClient (
    ClientKey INT PRIMARY KEY,
    ClientID INT NOT NULL UNIQUE,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Patronymic VARCHAR(50),
    Phone VARCHAR(20) NOT NULL
);

CREATE TABLE DimProperty (
    PropertyKey INT PRIMARY KEY,
    PropertyID INT NOT NULL UNIQUE,
    Address VARCHAR(255) NOT NULL,
    Rooms INT NOT NULL,
    MonthlyRent NUMERIC(10,2) NOT NULL,
    Status VARCHAR(20) NOT NULL,
    CHECK (Rooms > 0),
    CHECK (MonthlyRent > 0),
    CHECK (Status IN ('Available', 'Occupied', 'Repair'))
);

CREATE TABLE FactRental (
    RentalFactKey INT PRIMARY KEY,
    SettlementID INT NOT NULL,
    ClientKey INT NOT NULL,
    PropertyKey INT NOT NULL,
    CheckInDateKey INT NOT NULL,
    CheckOutDateKey INT,
    RentalCost NUMERIC(10,2) NOT NULL,
    RentalDays INT NOT NULL,
    PaidAmount NUMERIC(12,2) NOT NULL,
    FOREIGN KEY (ClientKey)
        REFERENCES DimClient(ClientKey),
    FOREIGN KEY (PropertyKey)
        REFERENCES DimProperty(PropertyKey),
    FOREIGN KEY (CheckInDateKey)
        REFERENCES DimDate(DateKey),
    FOREIGN KEY (CheckOutDateKey)
        REFERENCES DimDate(DateKey),
    CHECK (RentalCost > 0),
    CHECK (RentalDays >= 0),
    CHECK (PaidAmount >= 0)
);