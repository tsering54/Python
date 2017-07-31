-- 1
-- select customer.first_name, customer.last_name, address.address, address.address2, address.postal_code
-- from customer
-- 	join address on customer.address_id = address.address_id
--     where city_id=312
 
-- 2  comedy films
-- select film.title, film.description, film.release_year, film.rating, film.special_features, category.name
-- from film
-- 	join film_category on film.film_id = film_category.film_id
--  join category on film_category.category_id = category.category_id
-- where category.name = 'Comedy';

-- 3
-- select actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
-- from film
-- 	join film_actor on film.film_id=film_actor.film_id
--     join actor on actor.actor_id = film_actor.actor_id
-- where actor.actor_id = 5;

-- 4
-- select customer.first_name, customer.last_name, customer.email, address.address
-- from customer 
-- 	join address on customer.address_id = address.address_id
-- 	join city on address.city_id = city.city_id
-- where customer.store_id = 1 and city.city_id in (1, 42, 312, 459);

-- 5
-- select film.title, film.description, film.release_year, film.rating, film.special_features
-- from film
-- 	join film_actor on film.film_id = film_actor.film_id
-- where film.rating = 'G' and film.special_features like '%Behind the Scenes%' and film_actor.actor_id = 15;

-- 6
-- select film.film_id, film.title, actor.actor_id, concat(actor.first_name, ' ', actor.last_name)as actor_name
-- from film
-- 	join film_actor on film.film_id = film_actor.film_id
-- 	join actor on film_actor.actor_id = actor.actor_id
-- where film.film_id = 369;

-- 7
-- select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
-- from film
-- 	join film_category on film.film_id = film_category.film_id
--     join category on film_category.category_id = category.category_id
-- where category.name = 'Drama' and film.rental_rate='2.99';
 
-- 8
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, actor.first_name, actor.last_name
from actor
	join film_actor on actor.actor_id = film_actor.actor_id
    join film on film_actor.film_id = film.film_id
    join film_category on film.film_id = film_category.film_id
    join category on film_category.category_id = category.category_id
where actor.first_name = 'Sandra'
	and actor.last_name = 'Kilmer'
    and category.name='Action';













