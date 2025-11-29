DROP DATABASE tiriantrainsdb;
CREATE DATABASE tiriantrainsdb;

USE tiriantrainsdb;

CREATE TABLE train (
    trainID INT NOT NULL PRIMARY KEY,
    model VARCHAR(20) NOT NULL,
    seriesType ENUM('S-Series', 'A-Series') NOT NULL DEFAULT 'S-Series',
    maxSpeed INT NOT NULL,
    numSeats INT NOT NULL,
    numToilets INT NOT NULL,
    recliningSeats BOOLEAN NOT NULL DEFAULT 1,
    foldingTables BOOLEAN NOT NULL DEFAULT 1,
    disabilityAccess BOOLEAN NOT NULL DEFAULT 1,
    luggageStorage BOOLEAN NOT NULL DEFAULT 0,
    vendingMachine BOOLEAN NOT NULL DEFAULT 0,
    foodService BOOLEAN NOT NULL DEFAULT 0,
    CHECK (model REGEXP '^[sSaA]-[0-9]+$')
);

CREATE TABLE maintenance (
    maintenanceID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    trainID INT NOT NULL,
    maintenanceDate DATE NOT NULL,
    crewInCharge VARCHAR(50),
    tasks VARCHAR(255),
    train_condition ENUM('Excellent', 'Very Good', 'Satisfactory', 'Poor') NOT NULL,
    FOREIGN KEY (trainID) REFERENCES train(trainID)
);

CREATE TABLE station (
    stationID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stationName VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE route (
    routeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    originStationID INT NOT NULL,
    destinationStationID INT NOT NULL,
    baseCost INT NOT NULL,
    isLocalRoute BOOLEAN NOT NULL DEFAULT 1,
    estimatedDuration INT NOT NULL,
    FOREIGN KEY (originStationID) REFERENCES station(stationID),
    FOREIGN KEY (destinationStationID) REFERENCES station(stationID),
    CHECK (originStationID != destinationStationID),
    CHECK (isLocalRoute = 0 OR (isLocalRoute = 1 AND estimatedDuration = 5)),
    UNIQUE (originStationID, destinationStationID)
);

CREATE TABLE routePriceHistory (
    priceHistoryID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    routeID INT NOT NULL,
    price INT NOT NULL,
    effectiveFrom DATE NOT NULL,
    effectiveTo DATE DEFAULT NULL,
    FOREIGN KEY (routeID) REFERENCES route(routeID)
);

CREATE TABLE scheduledTrip (
    tripScheduleID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    routeID INT NOT NULL,
    trainID INT NOT NULL,
    tripDate DATE NOT NULL,
    departureTime TIME NOT NULL,
    arrivalTime TIME NOT NULL,
    FOREIGN KEY (routeID) REFERENCES route(routeID),
    FOREIGN KEY (trainID) REFERENCES train(trainID)
);

CREATE TABLE customer (
    customerID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    givenName VARCHAR(50) NOT NULL,
    middleInitial VARCHAR(1),
    birthDate DATE NOT NULL,
    gender VARCHAR(10),
    email VARCHAR(100) UNIQUE 
);

CREATE TABLE ticket (
    ticketID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    customerID INT NOT NULL,
    ticketDate DATE NOT NULL,
    FOREIGN KEY (customerID) REFERENCES customer(customerID)
);

CREATE TABLE ticketTrip (
    ticketID INT NOT NULL,
    tripScheduleID INT NOT NULL,
    tripCost INT NOT NULL,
    PRIMARY KEY (ticketID, tripScheduleID),
    FOREIGN KEY (ticketID) REFERENCES ticket(ticketID),
    FOREIGN KEY (tripScheduleID) REFERENCES scheduledTrip(tripScheduleID)
);