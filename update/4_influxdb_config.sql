INSERT OR IGNORE INTO config VALUES ('influx_db', 'NO', 'select', 'Use timeseries database InfluxDB for storing sensor values.', '["YES","NO"]' );
INSERT OR IGNORE INTO config VALUES ('influx_db_address', '127.0.0.1', 'text', 'Address for InfluxDB.', NULL );
INSERT OR IGNORE INTO config VALUES ('influx_db_port', 8086, 'number', 'Port for InfluxDB.', NULL );
INSERT OR IGNORE INTO config VALUES ('influx_db_username', 'username', 'text', 'Username for InfluxDB.', NULL );
INSERT OR IGNORE INTO config VALUES ('influx_db_password', 'password', 'text', 'Password for InfluxDB.', NULL );
INSERT OR IGNORE INTO config VALUES ('influx_db_database_name', 'database', 'text', 'Name of the InfluxDB to use.', NULL );
INSERT OR IGNORE INTO config VALUES ('influx_db_sampling_value', 10, 'number', 'A timeseries database has the advantage to aggregate data points and therefore to reduce the transmitted data. This value sets a time span in seconds to calculate the average', NULL );
INSERT OR IGNORE INTO config VALUES ('influx_db_start_relative', 1, 'number', 'If you have an ongoing brew or fermentation process only values related to this process will be shown in the graph. Additionally you can define in days how far the time series should reach in the past. The earliest time of both information defines when the data series starts.', NULL );
