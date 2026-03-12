
INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection)
VALUES
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);


INSERT INTO tbl_types (typeName)
VALUES
('Grass'),
('Fire'),
('Water'),
('Lightning'),
('Psychic'),
('Fighting'),
('Colorless');


INSERT INTO tbl_stages (stageName)
VALUES
('Basic'),
('Stage 1'),
('Stage 2');


INSERT INTO tbl_cards (
    hp, name, informacoes, attack, damage, weak, ressis, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
)
VALUES
(40, 'Bulbasaur', 'Seed Pokémon', 'Leech Seed', '20', 'Fire', NULL, '1',
 1, 1, 1, 1),

(50, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', NULL, '1',
 4, 1, 2, 1),

(50, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '10', 'Lightning', NULL, '1',
 7, 1, 3, 1),

(60, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', NULL, '1',
 58, 1, 4, 1),

(60, 'Machop', 'Superpower Pokémon', 'Low Kick', '20', 'Psychic', NULL, '1',
 52, 1, 6, 1),

(60, 'Jigglypuff', 'Balloon Pokémon', 'Lullaby', '—', 'Fighting', 'Psychic', '1',
 54, 1, 7, 1),

(60, 'Haunter', 'Gas Pokémon', 'Hypnosis', '—', 'Psychic', NULL, '1',
 29, 1, 5, 2);
