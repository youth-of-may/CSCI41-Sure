/*
Add code to init_schema or here to populate the database
*/

-- ============================================
-- 1. TRAIN DATA
-- ============================================
INSERT INTO train (trainID, model, seriesType, maxSpeed, numSeats, numToilets, recliningSeats, foldingTables, disabilityAccess, luggageStorage, vendingMachine, foodService) VALUES
(101, 'S-100', 'S-Series', 120, 80, 2, 1, 1, 1, 0, 0, 0),
(102, 'S-100', 'S-Series', 120, 80, 2, 1, 1, 1, 0, 0, 0),
(103, 'S-150', 'S-Series', 140, 100, 3, 1, 1, 1, 1, 0, 0),
(104, 'S-150', 'S-Series', 140, 100, 3, 1, 1, 1, 1, 0, 0),
(105, 'S-200', 'S-Series', 160, 120, 4, 1, 1, 1, 1, 1, 0),
(201, 'A-300', 'A-Series', 180, 150, 5, 1, 1, 1, 1, 1, 1),
(202, 'A-300', 'A-Series', 180, 150, 5, 1, 1, 1, 1, 1, 1),
(203, 'A-350', 'A-Series', 200, 180, 6, 1, 1, 1, 1, 1, 1),
(204, 'A-350', 'A-Series', 200, 180, 6, 1, 1, 1, 1, 1, 1),
(205, 'A-400', 'A-Series', 220, 200, 8, 1, 1, 1, 1, 1, 1);

-- ============================================
-- 2. MAINTENANCE DATA
-- ============================================
INSERT INTO maintenance (trainID, maintenanceDate, crewInCharge, tasks, train_condition) VALUES
(101, '2024-01-15', 'Crew Alpha', 'Routine inspection, brake check', 'Excellent'),
(101, '2024-04-20', 'Crew Beta', 'Engine service, cleaning', 'Very Good'),
(101, '2024-07-10', 'Crew Alpha', 'Wheel replacement, safety check', 'Excellent'),
(101, '2024-10-05', 'Crew Gamma', 'Full service, interior refurbishment', 'Excellent'),
(102, '2024-02-01', 'Crew Beta', 'Routine inspection', 'Very Good'),
(102, '2024-05-15', 'Crew Alpha', 'Brake system overhaul', 'Satisfactory'),
(102, '2024-08-20', 'Crew Gamma', 'Engine repair, AC maintenance', 'Very Good'),
(103, '2024-01-25', 'Crew Gamma', 'Annual inspection', 'Excellent'),
(103, '2024-06-10', 'Crew Beta', 'Routine maintenance', 'Excellent'),
(104, '2024-03-05', 'Crew Alpha', 'Safety inspection, toilet repair', 'Very Good'),
(104, '2024-09-12', 'Crew Beta', 'Full service', 'Excellent'),
(105, '2024-02-20', 'Crew Gamma', 'Vending machine installation check', 'Excellent'),
(201, '2024-01-10', 'Crew Alpha', 'Comprehensive inspection', 'Excellent'),
(201, '2024-04-15', 'Crew Beta', 'Food service equipment check', 'Excellent'),
(201, '2024-07-20', 'Crew Gamma', 'Engine overhaul', 'Very Good'),
(202, '2024-02-28', 'Crew Beta', 'Routine check', 'Excellent'),
(202, '2024-08-05', 'Crew Alpha', 'AC system repair', 'Very Good'),
(203, '2024-03-15', 'Crew Gamma', 'Full inspection', 'Excellent'),
(204, '2024-05-01', 'Crew Alpha', 'Safety certification', 'Excellent'),
(205, '2024-06-20', 'Crew Beta', 'Luxury train maintenance', 'Excellent');

-- ============================================
-- 3. STATION DATA
-- ============================================
INSERT INTO station (stationName) VALUES
('Beaver''s Dam'),
('Allies'' Enclave'),
('The Wardrobe'),
('The Lamp Post'),
('Mr. Tumms'),
('Aslan''s Camp'),
('Witch''s Camp'),
('The Stone Table'),
('Dancing Lawn'),
('Anvard'),
('Cherry Tree'),
('Father Christmas'),
('Cauldron Pool');

-- ============================================
-- 4. ROUTE DATA
-- ============================================
-- ============================================
-- 4. ROUTE DATA
-- ============================================
INSERT INTO route (originStationID, destinationStationID, baseCost, isLocalRoute, estimatedDuration) VALUES
-- LOCAL ROUTES (clockwise)
(1, 2, 2, 1, 5),
(2, 4, 2, 1, 5),
(4, 3, 2, 1, 5),
(3, 1, 2, 1, 5),

-- LOCAL ROUTES (counter-clockwise)
(2, 1, 2, 1, 5),
(4, 2, 2, 1, 5),
(3, 4, 2, 1, 5),
(1, 3, 2, 1, 5),

-- INTERTOWN ROUTES - From Allies' Enclave
(2, 5, 150, 0, 120),
(2, 13, 130, 0, 100),
(2, 12, 140, 0, 110),
(2, 7, 160, 0, 130),

-- INTERTOWN ROUTES - To Allies' Enclave
(5, 2, 150, 0, 120),
(13, 2, 130, 0, 100),
(12, 2, 140, 0, 110),
(7, 2, 160, 0, 130),

-- INTERTOWN ROUTES - Mr. Tumms connections
(5, 6, 180, 0, 150),
(6, 5, 180, 0, 150),

-- INTERTOWN ROUTES - Witch's Camp connections
(7, 6, 170, 0, 140),
(6, 7, 170, 0, 140),
(7, 8, 190, 0, 160),
(8, 7, 190, 0, 160),

-- INTERTOWN ROUTES - Cauldron Pool connections
(13, 12, 120, 0, 90),
(12, 13, 120, 0, 90),

-- INTERTOWN ROUTES - Father Christmas connections
(12, 11, 110, 0, 85),
(11, 12, 110, 0, 85),
(12, 9, 130, 0, 100),
(9, 12, 130, 0, 100),

-- INTERTOWN ROUTES - The Stone Table connections
(8, 9, 150, 0, 120),
(9, 8, 150, 0, 120),

-- INTERTOWN ROUTES - Dancing Lawn connections
(9, 10, 200, 0, 180),
(10, 9, 200, 0, 180),

-- INTERTOWN ROUTES - Cherry Tree connections
(11, 10, 130, 0, 100),
(10, 11, 130, 0, 100);

-- ============================================
-- 5. ROUTE PRICE HISTORY DATA
-- ============================================
INSERT INTO routePriceHistory (routeID, price, effectiveFrom, effectiveTo) VALUES
(1, 2, '2024-01-01', NULL),
(2, 2, '2024-01-01', NULL),
(3, 2, '2024-01-01', NULL),
(4, 2, '2024-01-01', NULL),
(5, 2, '2024-01-01', NULL),
(6, 2, '2024-01-01', NULL),
(7, 2, '2024-01-01', NULL),
(8, 2, '2024-01-01', NULL),
(9, 150, '2024-01-01', NULL),
(10, 130, '2024-01-01', NULL),
(11, 140, '2024-01-01', NULL),
(12, 160, '2024-01-01', NULL),
(13, 180, '2024-01-01', NULL),
(14, 120, '2024-01-01', NULL),
(15, 110, '2024-01-01', NULL),
(16, 170, '2024-01-01', NULL),
(17, 190, '2024-01-01', NULL),
(18, 150, '2024-01-01', NULL),
(19, 200, '2024-01-01', NULL),
(20, 130, '2024-01-01', NULL);

-- ============================================
-- 6. SCHEDULED TRIP DATA
-- ============================================
INSERT INTO scheduledTrip (routeID, trainID, tripDate, departureTime, arrivalTime) VALUES
(1, 101, '2024-12-01', '08:00:00', '08:05:00'),
(2, 102, '2024-12-01', '08:15:00', '08:20:00'),
(3, 103, '2024-12-01', '08:30:00', '08:35:00'),
(4, 104, '2024-12-01', '08:45:00', '08:50:00'),
(5, 101, '2024-12-01', '09:00:00', '09:05:00'),
(6, 102, '2024-12-01', '09:15:00', '09:20:00'),
(7, 103, '2024-12-01', '09:30:00', '09:35:00'),
(8, 104, '2024-12-01', '09:45:00', '09:50:00'),
(9, 201, '2024-12-01', '07:00:00', '09:00:00'),
(10, 202, '2024-12-01', '10:00:00', '11:40:00'),
(11, 203, '2024-12-02', '08:00:00', '09:50:00'),
(12, 204, '2024-12-02', '11:00:00', '13:10:00'),
(13, 205, '2024-12-02', '07:30:00', '10:00:00'),
(14, 201, '2024-12-02', '12:00:00', '13:30:00'),
(15, 202, '2024-12-02', '08:00:00', '09:25:00'),
(16, 203, '2024-12-02', '10:00:00', '12:20:00'),
(17, 204, '2024-12-03', '07:00:00', '09:40:00'),
(18, 205, '2024-12-03', '11:00:00', '13:00:00'),
(19, 201, '2024-12-03', '08:30:00', '11:30:00'),
(20, 202, '2024-12-03', '13:00:00', '14:40:00');

-- ============================================
-- 7. CUSTOMER DATA
-- ============================================
INSERT INTO customer (lastName, givenName, middleInitial, birthDate, gender, email) VALUES
('Pevensie', 'Peter', 'W', '1927-01-15', 'Male', 'peter.pevensie@narnia.com'),
('Pevensie', 'Susan', 'A', '1928-03-20', 'Female', 'susan.pevensie@narnia.com'),
('Pevensie', 'Edmund', 'H', '1930-09-10', 'Male', 'edmund.pevensie@narnia.com'),
('Pevensie', 'Lucy', 'M', '1932-05-05', 'Female', 'lucy.pevensie@narnia.com'),
('Scrubb', 'Eustace', 'C', '1933-07-18', 'Male', 'eustace.scrubb@narnia.com'),
('Pole', 'Jill', 'A', '1933-11-22', 'Female', 'jill.pole@narnia.com'),
('Kirke', 'Digory', 'A', '1888-02-14', 'Male', 'digory.kirke@narnia.com'),
('Plummer', 'Polly', 'E', '1889-06-30', 'Female', 'polly.plummer@narnia.com'),
('Ketterley', 'Andrew', NULL, '1850-12-01', 'Male', 'andrew.ketterley@narnia.com'),
('Beaversdam', 'Tom', 'R', '1995-04-10', 'Male', 'tom.beaversdam@narnia.com'),
('Archenland', 'Sarah', 'L', '1998-08-25', 'Female', 'sarah.archenland@narnia.com'),
('Caspian', 'Mary', 'J', '1975-03-15', 'Female', 'mary.caspian@narnia.com'),
('Trumpkin', 'David', 'K', '1980-11-08', 'Male', 'david.trumpkin@narnia.com'),
('Reepicheep', 'Charles', NULL, '1992-01-20', 'Male', 'charles.reepicheep@narnia.com'),
('Glenstorm', 'Anna', 'M', '1987-09-12', 'Female', 'anna.glenstorm@narnia.com'),
('Rilian', 'James', 'P', '2000-07-04', 'Male', 'james.rilian@narnia.com'),
('Drinian', 'Elizabeth', 'S', '1985-12-18', 'Female', 'elizabeth.drinian@narnia.com'),
('Ramandu', 'Michael', NULL, '1970-05-22', 'Male', 'michael.ramandu@narnia.com'),
('Prunaprismia', 'Jennifer', 'A', '1990-02-28', 'Female', 'jennifer.prunaprismia@narnia.com'),
('Cornelius', 'Robert', 'T', '1965-10-15', 'Male', 'robert.cornelius@narnia.com');

-- ============================================
-- 8. TICKET DATA
-- ============================================
INSERT INTO ticket (customerID, ticketDate) VALUES
(1, '2024-10-25'),
(2, '2024-10-25'),
(3, '2024-10-26'),
(4, '2024-10-26'),
(5, '2024-10-27'),
(6, '2024-10-27'),
(7, '2024-10-28'),
(8, '2024-10-29'),
(9, '2024-10-30'),
(10, '2024-10-30'),
(11, '2024-10-31'),
(12, '2024-10-31'),
(13, '2024-11-01'),
(14, '2024-11-01'),
(15, '2024-11-02'),
(1, '2024-11-03'),
(2, '2024-11-03'),
(16, '2024-11-04'),
(17, '2024-11-04'),
(18, '2024-11-05');

-- ============================================
-- 9. TICKET TRIP DATA
-- ============================================
INSERT INTO ticketTrip (ticketID, tripScheduleID, tripCost) VALUES
(1, 1, 2),
(1, 2, 2),
(1, 3, 2),
(2, 5, 2),
(2, 6, 2),
(2, 7, 2),
(3, 1, 2),
(3, 9, 150),
(4, 9, 150),
(4, 13, 180),
(5, 10, 130),
(5, 14, 120),
(5, 15, 110),
(6, 11, 140),
(6, 12, 160),
(6, 17, 190),
(7, 4, 2),
(7, 1, 2),
(8, 2, 2),
(8, 6, 2),
(9, 16, 170),
(9, 18, 150),
(10, 9, 150),
(10, 13, 180),
(10, 19, 200),
(11, 1, 2),
(11, 2, 2),
(11, 3, 2),
(12, 10, 130),
(12, 14, 120),
(12, 20, 130),
(13, 11, 140),
(13, 15, 110),
(14, 1, 2),
(14, 5, 2),
(14, 8, 2),
(15, 3, 2),
(15, 4, 2),
(15, 6, 2),
(16, 5, 2),
(16, 6, 2),
(16, 7, 2),
(17, 12, 160),
(17, 17, 190),
(17, 18, 150),
(18, 13, 180),
(18, 16, 170),
(18, 19, 200),
(19, 11, 140),
(19, 12, 160),
(19, 16, 170),
(20, 10, 130),
(20, 17, 190),
(20, 19, 200),
(20, 20, 130);