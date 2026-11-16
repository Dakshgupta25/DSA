select s.requester_id as id ,count(distinct(s.accepter_id)) as num
from (
    (select requester_id as requester_id ,accepter_id as accepter_id from RequestAccepted)
    union
    (select accepter_id as requester_id,requester_id as accepter_id from RequestAccepted)
) s
group by s.requester_id
order by count(distinct(s.accepter_id)) desc 
limit 1