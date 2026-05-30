SELECT
    date,
    produit,
    categorie,
    quantite,
    prix_unitaire,
    ville,
    quantite * prix_unitaire AS chiffre_affaires
FROM
    ventes_raw
WHERE
    quantite > 0 AND prix_unitaire > 0