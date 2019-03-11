select * from pub
where pcity  = "GARDEN CITY"

select count(*)
from bib bb inner join 
pub pb on bb.pubid = pb.pubid
where pb.pcity = "NEW YORK"
