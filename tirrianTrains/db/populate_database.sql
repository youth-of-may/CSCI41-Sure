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
('Cauldron Pool'),
('Glasswater Creek'),
('Lantern Waste'),
('Beruna'),
('Cair Paravel'),
('Dancing Lawn'),
('Stone Table'),
('Archenland Border'),
('Narrowhaven'),
('Beaversdam Junction'),
('Aslan''s How'),
('Ettinsmoor'),
('Chippingford');

-- ============================================
-- 4. ROUTE DATA
-- ============================================
INSERT INTO route (originStationID, destinationStationID, baseCost, isLocalRoute, estimatedDuration) VALUES
-- Local routes (short distances)
(1, 2, 50, 1, 30),    -- Beaver's Dam to Allies' Enclave
(2, 3, 45, 1, 25),    -- Allies' Enclave to Cauldron Pool
(3, 4, 40, 1, 20),    -- Cauldron Pool to Glasswater Creek
(4, 8, 55, 1, 35),    -- Glasswater Creek to Dancing Lawn
(8, 12, 50, 1, 30),   -- Dancing Lawn to Beaversdam Junction
(12, 15, 45, 1, 25),  -- Beaversdam Junction to Chippingford

-- Regional routes (medium distances)
(1, 5, 120, 0, 90),   -- Beaver's Dam to Lantern Waste
(5, 6, 150, 0, 120),  -- Lantern Waste to Beruna
(6, 7, 180, 0, 150),  -- Beruna to Cair Paravel
(4, 9, 130, 0, 100),  -- Glasswater Creek to Stone Table
(9, 13, 140, 0, 110), -- Stone Table to Aslan's How

-- Long-distance routes
(1, 7, 350, 0, 300),  -- Beaver's Dam to Cair Paravel (full route)
(5, 10, 200, 0, 180), -- Lantern Waste to Archenland Border
(7, 11, 250, 0, 240), -- Cair Paravel to Narrowhaven
(10, 14, 180, 0, 150),-- Archenland Border to Ettinsmoor
(1, 13, 280, 0, 240), -- Beaver's Dam to Aslan's How

-- Return routes
(2, 1, 50, 1, 30),    -- Allies' Enclave to Beaver's Dam
(3, 2, 45, 1, 25),    -- Cauldron Pool to Allies' Enclave
(7, 1, 350, 0, 300),  -- Cair Paravel to Beaver's Dam (return)
(6, 5, 150, 0, 120);  -- Beruna to Lantern Waste (return)

-- ============================================
-- 5. ROUTE PRICE HISTORY DATA
-- ============================================
INSERT INTO routePriceHistory (routeID, price, effectiveFrom, effectiveTo) VALUES
-- Price changes for route 1 (Beaver's Dam to Allies' Enclave)
(1, 45, '2024-01-01', '2024-06-30'),
(1, 50, '2024-07-01', NULL),

-- Price changes for route 12 (Beaver's Dam to Cair Paravel)
(12, 320, '2024-01-01', '2024-03-31'),
(12, 350, '2024-04-01', NULL),

-- Price changes for route 13 (Lantern Waste to Archenland Border)
(13, 180, '2024-01-01', '2024-05-31'),
(13, 200, '2024-06-01', NULL),

-- Current prices for other routes
(2, 45, '2024-01-01', NULL),
(3, 40, '2024-01-01', NULL),
(4, 55, '2024-01-01', NULL),
(5, 50, '2024-01-01', NULL),
(6, 45, '2024-01-01', NULL),
(7, 120, '2024-01-01', NULL),
(8, 150, '2024-01-01', NULL),
(9, 180, '2024-01-01', NULL),
(10, 130, '2024-01-01', NULL),
(11, 140, '2024-01-01', NULL),
(14, 250, '2024-01-01', NULL),
(15, 180, '2024-01-01', NULL),
(16, 280, '2024-01-01', NULL),
(17, 50, '2024-01-01', NULL),
(18, 45, '2024-01-01', NULL),
(19, 350, '2024-01-01', NULL),
(20, 150, '2024-01-01', NULL);

-- ============================================
-- 6. SCHEDULED TRIP DATA
-- ============================================
INSERT INTO scheduledTrip (routeID, trainID, tripDate, departureTime, arrivalTime) VALUES
-- November 2024 trips
(1, 101, '2024-11-01', '08:00:00', '08:30:00'),
(1, 102, '2024-11-01', '10:00:00', '10:30:00'),
(2, 103, '2024-11-01', '09:00:00', '09:25:00'),
(7, 201, '2024-11-01', '07:00:00', '08:30:00'),
(12, 203, '2024-11-01', '06:00:00', '11:00:00'),

(1, 101, '2024-11-02', '08:00:00', '08:30:00'),
(2, 103, '2024-11-02', '09:00:00', '09:25:00'),
(9, 202, '2024-11-02', '14:00:00', '16:30:00'),
(12, 204, '2024-11-02', '06:30:00', '11:30:00'),

(1, 102, '2024-11-03', '08:00:00', '08:30:00'),
(3, 104, '2024-11-03', '11:00:00', '11:20:00'),
(8, 201, '2024-11-03', '10:00:00', '12:00:00'),
(13, 205, '2024-11-03', '13:00:00', '16:00:00'),

-- Additional trips for variety
(4, 105, '2024-11-04', '15:00:00', '15:35:00'),
(10, 203, '2024-11-04', '08:00:00', '09:40:00'),
(14, 204, '2024-11-05', '07:30:00', '11:30:00'),
(16, 205, '2024-11-05', '09:00:00', '13:00:00'),

-- Return trips
(17, 101, '2024-11-06', '16:00:00', '16:30:00'),
(18, 103, '2024-11-06', '17:00:00', '17:25:00'),
(19, 202, '2024-11-06', '18:00:00', '23:00:00'),
(20, 201, '2024-11-06', '15:00:00', '17:00:00');

-- ============================================
-- 7. CUSTOMER DATA (UPDATED - Added email field)
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
(1, '2024-10-25'),  -- Ticket 1
(2, '2024-10-25'),  -- Ticket 2
(3, '2024-10-26'),  -- Ticket 3
(4, '2024-10-26'),  -- Ticket 4
(5, '2024-10-27'),  -- Ticket 5
(6, '2024-10-27'),  -- Ticket 6
(7, '2024-10-28'),  -- Ticket 7
(8, '2024-10-29'),  -- Ticket 8
(9, '2024-10-30'),  -- Ticket 9
(10, '2024-10-30'), -- Ticket 10
(11, '2024-10-31'), -- Ticket 11
(12, '2024-10-31'), -- Ticket 12
(13, '2024-11-01'), -- Ticket 13
(14, '2024-11-01'), -- Ticket 14
(15, '2024-11-02'), -- Ticket 15
(1, '2024-11-03'),  -- Ticket 16 (Peter's return trip)
(2, '2024-11-03'),  -- Ticket 17 (Susan's return trip)
(16, '2024-11-04'), -- Ticket 18
(17, '2024-11-04'), -- Ticket 19
(18, '2024-11-05'); -- Ticket 20

-- ============================================
-- 9. TICKET TRIP DATA (Junction Table)
-- ============================================
INSERT INTO ticketTrip (ticketID, tripScheduleID, tripCost) VALUES
-- Ticket 1 - Peter: Round trip journey
(1, 1, 50),    -- Beaver's Dam to Allies' Enclave
(1, 3, 45),    -- Allies' Enclave to Cauldron Pool
(1, 18, 50),   -- Return: Allies' Enclave to Beaver's Dam

-- Ticket 2 - Susan: Multi-city tour
(2, 3, 45),    -- Allies' Enclave to Cauldron Pool
(2, 11, 40),   -- Cauldron Pool to Glasswater Creek
(2, 19, 45),   -- Return: Cauldron Pool to Allies' Enclave

-- Ticket 3 - Edmund: Day trip
(3, 6, 50),    -- Beaver's Dam to Allies' Enclave
(3, 7, 45),    -- Allies' Enclave to Cauldron Pool

-- Ticket 4 - Lucy: Extended journey
(4, 4, 120),   -- Lantern Waste to Beruna
(4, 8, 150),   -- Beruna to Cair Paravel
(4, 21, 150),  -- Return: Beruna to Lantern Waste

-- Ticket 5 - Eustace: Complete route with stops
(5, 5, 350),   -- Full route to Cair Paravel
(5, 20, 350),  -- Return: Cair Paravel to Beaver's Dam

-- Ticket 6 - Jill: Long distance travel
(6, 9, 350),   -- Full route to Cair Paravel
(6, 16, 250),  -- Cair Paravel to Narrowhaven

-- Ticket 7 - Digory: Regional connections
(7, 12, 180),  -- Beruna to Cair Paravel
(7, 15, 130),  -- Glasswater Creek to Stone Table

-- Ticket 8 - Polly: Local commute
(8, 7, 45),    -- Allies' Enclave to Cauldron Pool
(8, 2, 50),    -- Allies' Enclave to Cauldron Pool (different day)

-- Ticket 9 - Andrew: Business trip
(9, 13, 200),  -- Lantern Waste to Archenland Border
(9, 16, 180),  -- Archenland Border to Ettinsmoor

-- Ticket 10 - Tom: Tourist package
(10, 5, 350),  -- Full route to Cair Paravel
(10, 12, 150), -- Beruna to Cair Paravel
(10, 16, 250), -- Cair Paravel to Narrowhaven

-- Ticket 11 - Sarah: Multi-leg commute
(11, 1, 50),   -- Beaver's Dam to Allies' Enclave
(11, 3, 45),   -- Allies' Enclave to Cauldron Pool
(11, 11, 40),  -- Cauldron Pool to Glasswater Creek

-- Ticket 12 - Mary: Complex itinerary
(12, 11, 40),  -- Cauldron Pool to Glasswater Creek
(12, 13, 200), -- Lantern Waste to Archenland Border
(12, 15, 130), -- Glasswater Creek to Stone Table

-- Ticket 13 - David: Weekend getaway
(13, 15, 40),  -- Cauldron Pool to Glasswater Creek
(13, 14, 55),  -- Glasswater Creek to Dancing Lawn

-- Ticket 14 - Charles: Daily commuter
(14, 2, 50),   -- Multiple trips same route
(14, 6, 50),   -- Beaver's Dam to Allies' Enclave
(14, 1, 50),   -- Beaver's Dam to Allies' Enclave

-- Ticket 15 - Anna: Connecting routes
(15, 14, 55),  -- Glasswater Creek to Dancing Lawn
(15, 5, 50),   -- Dancing Lawn to Beaversdam Junction
(15, 6, 45),   -- Beaversdam Junction to Chippingford

-- Ticket 16 - Peter: Return trip with detour
(16, 18, 50),  -- Return: Allies' Enclave to Beaver's Dam
(16, 1, 50),   -- Beaver's Dam to Allies' Enclave
(16, 3, 45),   -- Allies' Enclave to Cauldron Pool

-- Ticket 17 - Susan: Sightseeing tour
(17, 19, 45),  -- Return: Cauldron Pool to Allies' Enclave
(17, 4, 120),  -- Lantern Waste to Beruna
(17, 12, 150), -- Beruna to Cair Paravel

-- Ticket 18 - James: Long distance journey
(18, 16, 250), -- Cair Paravel to Narrowhaven
(18, 17, 280), -- Beaver's Dam to Aslan's How
(18, 13, 200), -- Lantern Waste to Archenland Border

-- Ticket 19 - Elizabeth: Business connections
(19, 17, 280), -- Beaver's Dam to Aslan's How
(19, 11, 140), -- Stone Table to Aslan's How
(19, 15, 130), -- Glasswater Creek to Stone Table

-- Ticket 20 - Michael: Complete tour package
(20, 20, 350), -- Full route return
(20, 5, 350),  -- Full route to Cair Paravel
(20, 16, 250), -- Cair Paravel to Narrowhaven
(20, 13, 200); -- Lantern Waste to Archenland Border