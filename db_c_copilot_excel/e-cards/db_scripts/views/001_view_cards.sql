CREATE VIEW vw_cards_detailed AS
SELECT 
    c.id,
    c.hp,
    c.name,
    c.informacoes,
    c.attack,
    c.damage,
    c.weak,
    c.ressis,
    c.retreat,
    c.cardNumberInCollection,
    col.collectionSetName AS collection_name,
    col.releaseDate AS collection_release_date,
    col.totalCardsInCollection AS collection_total_cards,
    t.typeName AS type_name,
    s.stageName AS stage_name
FROM tbl_cards c
JOIN tbl_collections col ON c.collection_id = col.id
JOIN tbl_types t ON c.type_id = t.id
JOIN tbl_stages s ON c.stage_id = s.id;


'''
A FORMA DE CÓDIGO ABAIXO É MAIS EFICIENTE:

SELECT 
    id,
    hp,
    name,
    informacoes,
    attack,
    damage,
    weak,
    ressis,
    retreat,
    cardNumberInCollection,
    collection_name,
    collection_release_date,
    collection_total_cards,
    type_name,
    stage_name
FROM vw_cards_detailed;



'''