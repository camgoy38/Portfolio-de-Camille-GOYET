CREATE TEMP TABLE USA_biscuit_cake AS
(SELECT distinct on (code) code,
product_name,
nutriscore_grade,
food_groups,
categories_tags,
countries_tags,
fat_100g,
saturated_fat_100g,
sugars_100g,
proteins_100g,
carbohydrates_100g,
energy_100g,
salt_100g,
sodium_100g,
CAST(((proteins_100g * 17) + (fat_100g * 37) + (carbohydrates_100g * 17)) AS numeric) AS computed_energy_100g,
Case when labels_tags like '%en:organic%' then true
when labels_tags like '%en:non-organic%'  then false
else null
END as organic,
CASE when ingredients_analysis_tags like '%en:vegan%' then TRUE
when ingredients_analysis_tags like '%en:non-vegan%' then FALSE
else NULL
END AS vegan,
CASE when ingredients_analysis_tags like '%en:vegetarian%' then TRUE
when ingredients_analysis_tags like '%en:non-vegetarian%' then FALSE
else NULL
END AS vegetarian,
CASE when ingredients_analysis_tags like '%en:palm-oil%' then TRUE
when ingredients_analysis_tags like '%en:palm-oil-free%' then FALSE
else NULL
END AS palm_oil,
CASE when nutrient_levels_tags like '%en:fat-in-high-quantity%' then 'h'
when nutrient_levels_tags like '%en:fat-in-low-quantity%' then 'l'
when nutrient_levels_tags like '%en:fat-in-moderate-quantity%' then 'm'
else NULL
END AS level_fat,
CASE when nutrient_levels_tags like '%en:salt-in-high-quantity%' then 'h'
when nutrient_levels_tags like '%en:salt-in-low-quantity%' then 'l'
when nutrient_levels_tags like '%en:salt-in-moderate-quantity%' then 'm'
else NULL
END AS level_salt,
CASE when nutrient_levels_tags like '%en:saturated-fat-in-high-quantity%' then 'h'
when nutrient_levels_tags like '%en:satured-fat-in-low-quantity%' then 'l'
when nutrient_levels_tags like '%en:satured-fat-in-moderate-quantity%' then 'm'
else NULL
END AS level_saturated_fat,
CASE when nutrient_levels_tags like '%en:sugars-in-high-quantity%' then 'h'
when nutrient_levels_tags like '%en:sugars-in-low-quantity%' then 'l'
when nutrient_levels_tags like '%en:sugars-in-moderate-quantity%' then 'm'
else NULL
END AS level_sugars
FROM openfoodfacts
WHERE countries_tags like '%en:united-states%'
AND food_groups='en:biscuits-and-cakes'
and length(code)=13
and nutriscore_grade!='unknown'
and LENGTH(nutriscore_grade)=1
and nutriscore_grade is not NULL
and data_quality_errors_tags is NULL
and fat_100g>=0 and fat_100g<100
and saturated_fat_100g>=0
and saturated_fat_100g<100 and
sugars_100g>=0 and sugars_100g<100 and
proteins_100g>=0 and proteins_100g<100 and
carbohydrates_100g>=0 and carbohydrates_100g<100 and
salt_100g>=0 and salt_100g<100 and
sodium_100g>=0 and sodium_100g<100
and energy_100g>=10 and energy_100g<3000
and fat_100g>saturated_fat_100g
and salt_100g>sodium_100g
and carbohydrates_100g>sugars_100g
and fat_100g+proteins_100g+carbohydrates_100G/3>salt_100G) ;


delete from USA_biscuit_cake
where code not in (
select min(code) from USA_biscuit_cake group by (
    product_name,nutriscore_grade,food_groups,categories_tags,countries_tags,fat_100g,
saturated_fat_100g,sugars_100g,proteins_100g,carbohydrates_100g,energy_100g,salt_100g,
sodium_100g));

\copy (select * from USA_biscuit_cake) to '/users/info/etu-1a/goyetcam/team_d01.csv' WITH (DELIMITER E'\t', format CSV, HEADER,NULL 'NA', ENCODING 'UTF8');

