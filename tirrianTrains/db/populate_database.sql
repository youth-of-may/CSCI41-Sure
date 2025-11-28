/*
Add code to init_schema or here to populate the database
*/

INSERT INTO train (trainID, model, seriesType, maxSpeed, numSeats, numToilets, recliningSeats, foldingTables, disabilityAccess, luggageStorage, vendingMachine, foodService)
VALUES
(1, 'S-100', 'S-Series', 220, 180, 4, 1, 1, 1, 1, 0, 0),
(2, 'A-210', 'A-Series', 260, 220, 6, 1, 1, 1, 1, 1, 1),
(3, 'S-305', 'S-Series', 200, 150, 3, 1, 1, 1, 0, 1, 0),
(4, 'A-500', 'A-Series', 300, 300, 8, 1, 1, 1, 1, 1, 1),
(5, 'S-420', 'S-Series', 240, 200, 5, 1, 1, 1, 0, 0, 1);


INSERT INTO maintenance (trainID, maintenanceDate, crewInCharge, tasks, train_condition)
VALUES
(1, '2025-01-15', 'Crew Alpha', 'Brake inspection, oil replacement', 'Very Good'),
(2, '2025-02-10', 'Crew Beta', 'Engine tuning, wheel alignment', 'Excellent'),
(3, '2025-03-01', 'Crew Gamma', 'Interior cleaning, ventilation check', 'Satisfactory'),
(4, '2025-03-20', 'Crew Delta', 'Full system diagnostics', 'Excellent'),
(5, '2025-04-05', 'Crew Echo', 'Door system maintenance', 'Poor');

INSERT INTO station (stationName, isLocalStation)
VALUES
('Central Station', 0),
('North Point', 1),
('East Junction', 1),
('South Terminal', 0),
('West Link', 1);

INSERT INTO route (originStationID, destinationStationID, baseCost, isLocalRoute, estimatedDuration)
VALUES
(1, 2, 150, 1, 45),
(2, 3, 120, 1, 35),
(3, 4, 250, 0, 70),
(4, 5, 180, 0, 55),
(1, 5, 300, 0, 90);

INSERT INTO routePriceHistory (routeID, price, effectiveFrom, effectiveTo) VALUES
(1, 100, '2025-01-01', '2025-02-01'),
(1, 110, '2025-02-01', '2025-03-01'),
(1, 120, '2025-03-01', '2025-04-01'),
(1, 130, '2025-04-01', '2025-05-01'),
(1, 150, '2025-05-01', '2025-06-01'),
(2, 120, '2025-01-01', NULL),
(3, 250, '2025-01-01', NULL),
(4, 180, '2025-01-01', NULL),
(5, 300, '2025-01-01', NULL);

INSERT INTO scheduledTrip (routeID, trainID, tripDate, departureTime, arrivalTime, actualDuration)
VALUES
(1, 1, '2025-05-01', '08:00:00', '08:45:00', 45),
(2, 2, '2025-05-02', '09:15:00', '09:50:00', 35),
(3, 3, '2025-05-03', '10:00:00', '11:10:00', 70),
(4, 4, '2025-05-04', '07:30:00', '08:25:00', 55),
(5, 5, '2025-05-05', '06:40:00', '08:10:00', 90);

INSERT INTO customer (lastName, givenName, middleInitial, birthDate, gender)
VALUES
('Santos', 'Maria', 'L', '1995-03-12', 'Female'),
('Reyes', 'Juan', 'D', '1988-07-21', 'Male'),
('Gonzales', 'Anne', 'M', '2000-11-05', 'Female'),
('Cruz', 'Mark', NULL, '1992-01-30', 'Male'),
('Lopez', 'Julia', 'A', '1999-09-09', 'Female');

INSERT INTO ticket (customerID, ticketDate, totalCost)
VALUES
(1, '2025-05-01', 450),
(2, '2025-05-02', 300),
(3, '2025-05-03', 600),
(4, '2025-05-04', 250),
(5, '2025-05-05', 700);

INSERT INTO ticketTrip (ticketID, tripScheduleID, tripCost)
VALUES
(1, 1, 150),
(2, 2, 120),
(3, 3, 250),
(4, 4, 180),
(5, 5, 300);