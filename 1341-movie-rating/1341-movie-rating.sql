# Write your MySQL query statement below
(select u.name as results from Users u 
left join MovieRating mr on u.user_id=mr.user_id
group by u.user_id 
order by count(mr.rating) desc,u.name
limit 1
)

union all
(
select m.title as results from movies m 
left join MovieRating mr on m.movie_id=mr.movie_id
WHERE mr.created_at >= '2020-02-01'AND mr.created_at < '2020-03-01'
group by m.movie_id 
order by avg(mr.rating) desc,m.title
limit 1
)