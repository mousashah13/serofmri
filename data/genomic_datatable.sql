USE gene_neuronal_data;

CREATE TABLE gene_expression (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_id INT NOT NULL,
    gene_symbol VARCHAR(255) NOT NULL,
    expression_value FLOAT NOT NULL,
    experiment_date DATE NOT NULL,
    UNIQUE KEY (sample_id, gene_symbol)
);

CREATE TABLE neuronal_activity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    neuron_id INT NOT NULL,
    activity_timestamp DATETIME NOT NULL,
    activity_value FLOAT NOT NULL,
    UNIQUE KEY (neuron_id, activity_timestamp)
);
